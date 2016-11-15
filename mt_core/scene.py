# coding=UTF-8

# TODO 完成场景生成功能
import os
import uuid


class SceneInstanceManager:
    def __init__(self, base_dir, node_template_repository, db, hypervisor, scene_config):
        self.base_dir = base_dir
        self.node_template_repository = node_template_repository
        self.db = db
        self.hypervisor = hypervisor
        self.scene_config = scene_config
        # id -> SceneInstance
        self.scene_dict = dict()

    def create_scene(self, topo, name):
        """
        创建场景
        :param topo: 拓扑
        :param name: 场景名称,显示在界面上
        :return: 场景实例
        """
        scene_id = self.generate_scene_id()
        instance = SceneInstance(scene_id, name, topo)
        self.scene_dict[scene_id] = instance
        self._do_create(instance)
        return scene_id

    def _do_create(self, instance):
        # create vlan
        vlan_created = dict()
        for link in instance.topo.iter_links():
            vlan_name = link.vlan_name
            if vlan_name not in vlan_created:
                vlan = self.hypervisor.create_vlan(vlan_name)
                vlan_created[vlan_name] = vlan
                # TODO save to db

        # create node
        for virtual_node in instance.topo.iter_nodes():
            node_template = self.node_template_repository.load_template(virtual_node.template_id)
            vm_path = self.format_vm_path(instance.id, virtual_node.name)
            node = SceneNode(virtual_node, vm_path)
            # TODO save to db
            self.hypervisor.clone(node_template.vm_path, node.vm_path, self.scene_config.clone_type)
            # TODO update scene state in db
            if 'cpuCount' in virtual_node.config:
                self.hypervisor.set_cpu_count(node.vm_path, int(virtual_node.config['cpuCount']))
            if 'ram' in virtual_node.config:
                self.hypervisor.set_ram(node.vm_path, int(virtual_node.config['ram']))

            for virtual_port in virtual_node.iter_ports:
                self.hypervisor.add_nic(node.vm_path, virtual_port.index, virtual_port.link.vlan_name)

            self.hypervisor.power_on(node.vm_path)
            self.hypervisor.wait_for_running(node.vm_path)

            # TODO more


    def destroy_scene(self, scene):
        """
        销毁场景
        :param scene: 场景
        """

    def query_scene(self, scene_id):
        """
        查找场景
        :param scene_id_or_name: 场景ID或名称
        :return: 场景实例
        """

    def restore(self):
        """
        从数据库中读取所有节点实例的数据,重建场景实例注册表
        """

    def generate_scene_id(self):
        return str(uuid.uuid4())

    def format_vm_path(self, scene_id, node_name):
        return os.path.join(self.base_dir, scene_id, node_name)


class SceneInstance:
    def __init__(self, scene_id, name, topo):
        self.id = scene_id
        self.name = name
        self.topo = topo
        # node_name -> SceneNode
        self.node_dict = dict()

    def to_info(self):
        return {}


class SceneNode:
    def __init__(self, virtual_node, vm_path):
        self.name = virtual_node.name
        self.virtual_node = virtual_node
        self.vm_path = vm_path
