# 任务列表

## 2017年03月14日

### 后端

实现下述功能，具体方法定义见[Hypervisor](mt_core/backends/__init__.py)里的Hypervisor类，下面两个类继承了这个类。

- [VirtualBox](mt_core/backends/virtualbox.py)，实现`VirtualBox`类的`clone`、`power_on`、`power_off`方法；
- [Workstation](mt_core/backends/workstation.py)，实现`Workstation`类的`clone`、`power_on`、`power_off`方法；

### 前端

实现下面这个界面：

![界面](docs/source/_static/topo_list.png)