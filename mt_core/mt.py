# coding=UTF-8
import time

from config import Config
from templates import FileNodeTemplateRepository
from db import Database
from server import Server
from scene import SceneInstanceManager
from backends import create_hypervisor


def main():
    config = Config()
    config.load()

    node_template_repository = FileNodeTemplateRepository(base_dir=config.repository_base_dir)
    db = Database(config.db_url)
    hypervisor = create_hypervisor(config.hypervisor_type)
    scene_instance_manager = SceneInstanceManager(config.instances_base_dir, node_template_repository, db, hypervisor, config.scene_config)
    server = Server(config.listen_address, config.listen_port, scene_instance_manager)

    server.start()

    # wait for Ctrl-C
    try:
        while 1:
            time.sleep(1)
    finally:
        server.stop()


if __name__ == '__main__':
    main()
