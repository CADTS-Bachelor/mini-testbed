# coding=utf-8

#import os
from vboxapi import VirtualBoxManager     #引入
# TODO 后台组:启动VirtualBox虚拟机
def power_on():
    mgr = VirtualBoxManager(None, None)
    vbox = mgr.vbox
    name = "XP"
    mach = vbox.findMachine(name)
    session = mgr.mgr.getSessionObject(vbox)
    progress = mach.launchVMProcess(session, "gui", "")
    progress.waitForCompletion(-1)
    console = session.console
 #   os.system("cd C:/Program Files/Oracle/VirtualBox/ && dir")
 #   os.system("cd C:/Program Files/Oracle/VirtualBox/ && VirtualBox.exe")

power_on()


