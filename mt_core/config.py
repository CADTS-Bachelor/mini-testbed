# coding=UTF-8

import six

ConfigParser = six.moves.configparser.ConfigParser


class SceneConfig:
    def __init__(self):
        self.clone_type = 'link'


class Config:
    def __init__(self):
        self.scene_config = SceneConfig()
        self.listen_port = None
        self.listen_address = None
        self.db_url = None
        self.instances_base_dir = None
        self.repository_base_dir = None
        self.hypervisor_type = None

    def load(self):
        # TODO load from config/mt.cfg use ConfigParser
        pass


if __name__ == '__main__':
    print(ConfigParser())
