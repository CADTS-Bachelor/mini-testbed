# coding=UTF-8


# TODO 界面组:显示文本列表程序
def show_list():
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
    print node.get('templateId'),node.get('name'),node.get('category'),node.get('emulation'),node.get('os'),node.get('image'),node.get('x'),node.get('y'),
    for config in node.findall('config'):
        print config.get('name'), config.get('type'), config.get('value'), config.get('unit'),config.get('index'),
        for config in config.findall('config'):
            print config.get('name'),config.get('type'),config.get('value'),config.get('unit'),config.get('index'),
            for config in config.findall('config'):
               print config.get('name'),config.get('type'),config.get('value'),config.get('unit'),
    for interface in node.findall('interface'):
        print interface.get('name'), interface.get('index'), interface.get('toNode'), interface.get('toIndex'),
        for config in interface.findall('config'):
           print config.get('name'), config.get('type'), config.get('value'), config.get('unit'),
    print

show_list()


