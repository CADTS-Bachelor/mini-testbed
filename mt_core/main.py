# coding=UTF-8


# TODO 后台组: 解析指定XML文件
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
import sys

try:
    tree = ET.parse("TX2015.xml")  # 打开xml文档
    root = tree.getroot()  # 获得root节点
except Exception, e:
    print "Error:cannot parse file:TX2015.xml."
    sys.exit(1)

for node in root:
    node_templateId = node.get('templateId')
    node_name=node.get('name')
    node_category=node.get('category')
    node_emulation=node.get('emulation')
    node_os=node.get('os')
    node_image=node.get('image')
    node_x=node.get('x')
    node_y=node.get('y')
    for config in node.findall('config'):
        node_config_name=config.get('name')
        node_config_type=config.get('type')
        node_config_value=config.get('value')
        node_config_unit=config.get('unit')
        node_config_index=config.get('index')
        for config in config.findall('config'):
            node_config_config_name = config.get('name')
            node_config_config_type = config.get('type')
            node_config_config_value = config.get('value')
            node_config_config_unit = config.get('unit')
            node_config_config_index = config.get('index')
            for config in config.findall('config'):
                node_config_config_config_name = config.get('name')
                node_config_config_config_type = config.get('type')
                node_config_config_config_value = config.get('value')
                node_config_config_config_unit = config.get('unit')
                node_config_config_config_index = config.get('index')
    for interface in node.findall('interface'):
        node_interface_name=interface.get('name')
        node_interface_name = interface.get('index')
        node_interface_name = interface.get('toNode')
        node_interface_name = interface.get('toIndex')
        for config in interface.findall('config'):
           node_interface_config_name = config.get('name')
           node_interface_config_type = config.get('type')
           node_interface_config_value = config.get('value')
           node_interface_config_unit = config.get('unit')
    print

