# coding=utf-8

import os
import  virtualbox.library_ext.machine
from vboxapi import VirtualBoxManager     #引入

import logging

logger = logging.getLogger(__name__)

#  TODO 后台组:启动VirtualBox虚拟机
from mt_core.backends import Hypervisor


# TODO override all methods
class VirtualBox(Hypervisor):
    def __init__(self):
        self.mgr = VirtualBoxManager(None, None)
        self.vbox = self.mgr.vbox

    def power_on(self, vm):
        raise NotImplementedError()

    def add_nic(self, vm, index, vlan_name):
        raise NotImplementedError()


def power_on():
    mgr = VirtualBoxManager(None, None)
    vbox = mgr.vbox
    name = "XP"
    mach = vbox.findMachine(name)
    session = mgr.mgr.getSessionObject(vbox)
    print(session)
    progress = mach.launchVMProcess(session, "gui", "")
    print(progress)
    progress.waitForCompletion(-1)
    console = session.console
    os.system("cd C:/Program Files/Oracle/VirtualBox/ && dir")
    os.system("cd C:/Program Files/Oracle/VirtualBox/ && VirtualBox.exe")

def power_off(name):
    os.chdir('C:\\Program Files\\oracle\\virtualBox')
    os.system("VBoxManage control "+"name "+"poweroff")
    print("successful poweroff!")

def set_CPU(name,size):
    os.chdir('C:\\Program Files\\oracle\\virtualBox')
    os.system("VBoxManage modifyvm "+name+ " --memory "+size)
    print("successful!")

def set_VRAM(name,size):
    os.chdir('C:\\Program Files\\oracle\\virtualBox')
    os.system("VBoxManage modifyvm " + name + " --vram " + size)
    print("successful!")


def set_snapshot(name,n_name):
    os.chdir('C:\\Program Files\\oracle\\virtualBox')
    os.system("VBoxManage snapshot "+name+" take "+n_name)
    print("successful!")

def clone_machine():
    os.chdir('C:\\Program Files\\oracle\\virtualBox')
    os.system('VBoxManage clonehd "W:\\vbox\\XP_1\\XP.vmdk" "W:\\vbox\\XP_1\\XP2.vmdk"')

#power_on()
#power_off("zjf")
#clone_machine()
#set_CPU("XP_1","567")
#set_VRAM("XP_1","567")
#set_snapshot("XP","XPm")
