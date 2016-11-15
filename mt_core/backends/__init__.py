# coding=UTF-8


class GuestInfo:
    OS_WINDOWS = "windows"
    OS_LINUX = "linux"
    def __init__(self, username, password, os):
        self.username = username
        self.password = password
        self.os = os


class Hypervisor:
    # 完全克隆
    CLONE_FULL = "full"
    # 链接克隆
    CLONE_LINK = "link"

    def clone(self, src_vm, dst_vm, type=CLONE_LINK):
        """
        克隆虚拟机
        :param src_vm: 模板虚拟机路径
        :param dst_vm: 目标虚拟机路径
        :param type: 克隆类型
        :return:
        """
        pass

    def set_cpu_count(self, vm, cpu_count):
        """
        设置CPU个数
        :param vm: 虚拟机路径
        :param cpu_count: CPU个数
        """
        pass

    def set_ram(self, vm, ram):
        """
        设置内存大小
        :param vm: 虚拟机路径
        :param ram: 内存大小,以MB为单位
        """
        pass

    def wait_for_running(self, vm, timeout_seconds=-1):
        pass

    def power_on(self, vm):
        pass

    def power_off(self, vm):
        pass

    def reset(self, vm):
        pass

    def shutdown_guest(self, vm):
        pass

    def restart_guest(self, vm):
        pass

    def create_vlan(self, vlan_name):
        pass

    def delete_vlan(self, vlan_name):
        pass

    def add_nic(self, vm, index, vlan_name):
        pass

    def remove_nic(self, vm, index):
        pass

    def put_file(self, vm, local_path, guest_path, guest_info):
        """
        将本地文件放置到客户操作系统中
        :param vm: 虚拟机路径
        :param local_path: 本地文件路径
        :param guest_path: 客户操作系统路径
        :param guest_info: 客户操作系统类型
        """
        pass

    def get_file(self, vm, local_path, guest_path, guest_info):
        """
        将客户操作系统中的文件传输到本地
        :param vm: 虚拟机路径
        :param local_path: 本地文件路径
        :param guest_path: 客户操作系统路径
        :param guest_info: 客户操作系统类型
        """
        pass

    def exec_guest(self, vm, cmd, guest_info):
        """
        在虚拟机中执行指定命令
        :param vm: 虚拟机路径
        :param cmd: 命令行
        :param guest_info: 客户操作系统信息
        :return: 返回值
        """

    def create_snapshot(self, vm, name):
        """
        创建快照
        :param vm: 虚拟机路径
        :param name: 快照名称
        """

    def revert_snapshot(self, vm, name):
        """
        恢复快照
        :param vm: 虚拟机路径
        :param name: 快照名称
        """

import workstation
import virtualbox

HYPERVISOR_WORKSTATION = "workstation"
HYPERVISOR_VIRTUALBOX = "virtualbox"

def create_hypervisor(hypervisor_type, *args, **kwargs):
    if hypervisor_type == HYPERVISOR_WORKSTATION:
        workstation.Workstation(*args, **kwargs)
    elif hypervisor_type == HYPERVISOR_VIRTUALBOX:
        virtualbox.VirtualBox(*args, **kwargs)
    else:
        raise NotImplementedError("hypervisor {} not support".format(hypervisor_type))
