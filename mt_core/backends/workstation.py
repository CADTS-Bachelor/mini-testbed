import os

from mt_core.backends import Hypervisor

os.system('g: && cd g:/vmware && vmrun.exe -T ws start "virtual machine/win7/Windows 7 x64.vmx"')


# TODO override all methods
class Workstation(Hypervisor):
    pass