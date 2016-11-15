# coding=UTF-8
from topo import parse_xml_string


# TODO RPC
class Server:
    def __init__(self, listen_address, listen_port, scene_instance_manager):
        self.listen_address = listen_address
        self.listen_port = listen_port
        self.scene_instance_manager = scene_instance_manager

    def start(self):
        """
        开始监听
        """

    def stop(self):
        """
        停止监听
        """

    def on_create(self, name, topo_content):
        topo = parse_xml_string(topo_content)
        return self.scene_instance_manager.create_scene(topo_content, name)

    def on_info(self, scene_id):
        return self.scene_instance_manager.query_scene(scene_id).to_info()

    def on_destroy(self, scene_id):
        self.scene_instance_manager.destroy_scene(scene_id)
