# coding=UTF-8

import networkx as nx
import six
# for security reason, use defusedxml package instead
try:
    import defusedxml.cElementTree as ET
except ImportError:
    import defusedxml.ElementTree as ET
import json


@six.python_2_unicode_compatible
class VirtualTopo:
    def __init__(self, name):
        self.name = name
        self.nodes = dict()
        self.links = dict()
        self.graph = nx.Graph()

    def add_node(self, node):
        self.nodes[node.name] = node
        self.graph.add_node(node)

    def add_link(self, link):
        self.links[link.name] = link
        # not support multi-links between nodes
        self.graph.add_edge(link.port1.node, link.port2.node)

    def check_node(self, name):
        return self.nodes[name]

    def check_link(self, name):
        return self.links[name]

    def iter_nodes(self):
        return six.itervalues(self.nodes)

    def iter_links(self):
        return six.itervalues(self.links)

    def __str__(self):
        return u'topo{{name={}}}'.format(self.name)


@six.python_2_unicode_compatible
class VirtualNode:
    CATEGORY_HOST = "Host"
    CATEGORY_SWITCH = "Switch"

    EMULATION_AUTO = ""
    EMULATION_VSPHERE = "vsphere"

    OS_WINDOWS = "windows"
    OS_LINUX = "linux"

    def __init__(self, name, template_id, category, emulation, os, image_path, x=-1, y=-1, config=None, ports=None):
        self.name = name
        self.template_id = template_id
        self.category = category
        self.emulation = emulation
        self.os = os
        self.image_path = image_path
        self.x = x
        self.y = y
        self.config = config if config else dict()
        self.ports = ports if ports else dict()

    def add_port(self, port):
        if port.index in self.ports:
            raise IndexError(port.index)
        else:
            self.ports[port.index] = port
            port.node = self

    def check_port(self, index):
        return self.ports[index]

    def add_config(self, config):
        self.config.update(config)

    def iter_ports(self):
        return six.itervalues(self.ports)

    def __str__(self):
        return u"node{{name={}, templateId={}, config={{{}}}}}".format(self.name,
                                                                   self.template_id,
                                                                   ', '.join([u'{}={}'.format(name, value) for name, value in self.config.items()]))


class VirtualPort:
    def __init__(self, index, to_node_name, to_port_index):
        self.index = index
        self.to_node_name = to_node_name
        self.to_port_index = to_port_index
        self.node = None
        self.to_port = None
        self.link = None
        self.config = dict()

    def add_config(self, config):
        self.config.update(config)

    def id(self):
        return u"{}.{}".format(self.node.name, self.index)


@six.python_2_unicode_compatible
class VirtualLink:
    def __init__(self, port1, port2):
        # ensure order for find
        if port1.id() <= port2.id():
            self.port1 = port1
            self.port2 = port2
        else:
            self.port1 = port2
            self.port2 = port1
        self.port1.to_port = port2
        self.port2.to_port = port1

        if port1.node.category == VirtualNode.CATEGORY_SWITCH:
            self.is_to_switch = True
            self.switch_node = port1.node
        elif port2.node.category == VirtualNode.CATEGORY_SWITCH:
            self.is_to_switch = True
            self.switch_node = port2.node
        else:
            self.is_to_switch = False
            self.switch_node = None

        self.name = u"{}--{}".format(self.port1.id(), self.port2.id())
        self.vlan_name = self.switch_node.name if self.is_to_switch else self.name

        self.port1.link = self
        self.port2.link = self

    def __str__(self):
        return u'link{{name={}}}'.format(self.name)


def load_config(parent_element):
    return _load_config(dict(), parent_element)

def _value(config_element):
    type = config_element.attrib['type']
    return config_element.attrib['value']

def _load_config(config, parent_element):
    for config_element in parent_element.findall('./config'):
        name = config_element.attrib['name']
        type = config_element.get('type')
        if type:
            # prime
            config[name] = _value(config_element)
        else:
            # table
            index = int(config_element.attrib['index'])
            table = config.get(name)
            if not table:
                table = []
                config[name] = table

            table.insert(index, _load_config(dict(), config_element))

    return config


def load_2_0(topo, topo_element):
    for node_element in topo_element.findall('./node'):
        node = VirtualNode(name=node_element.attrib["name"],
                           template_id=node_element.attrib['templateId'],
                           emulation=node_element.attrib['emulation'],
                           category=node_element.attrib['category'],
                           image_path=node_element.attrib['image'],
                           os=node_element.attrib['os'],
                           x=node_element.get('x', -1),
                           y=node_element.get('y', -1))
        topo.add_node(node)

        # parse node config
        node.add_config(load_config(node_element))

        # parse nic
        for interface_element in node_element.findall('./interface'):
            port = VirtualPort(index=interface_element.attrib['index'],
                               to_node_name=interface_element.attrib['toNode'],
                               to_port_index=interface_element.attrib['toIndex'])
            node.add_port(port)

            # parse port config
            port.add_config(load_config(interface_element))

    # construct link
    for node in topo.iter_nodes():
        for port in node.iter_ports():
            if not port.to_port:
                other_port = topo.check_node(port.to_node_name).check_port(port.to_port_index)
                link = VirtualLink(port, other_port)
                topo.add_link(link)


def parse_xml_string(xml_content):
    return _parse_xml(ET.fromstring(xml_content))


def parse_xml_file(filename):
    return _parse_xml(ET.parse(filename))


def _parse_xml(xml_tree):
    topo_element = xml_tree.getroot()
    topo = VirtualTopo(json.loads(topo_element.get('name')))
    version = topo_element.get('_v')
    if version == '2.0':
        load_2_0(topo, topo_element)
    else:
        raise NotImplementedError("version {} not support".format(version))
    return topo


if __name__ == '__main__':
    topo = parse_xml_file("../data/TX2015.xml")
    print(topo)
    for node in topo.iter_nodes():
        print(node)

    for link in topo.iter_links():
        print(link)
