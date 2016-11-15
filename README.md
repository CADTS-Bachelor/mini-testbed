# mini-testbed
A mini network security testbed based on VirtualBox/VMware Workstation.


## 代码说明

### 后台服务器

- config.py: 加载配置文件内容
- db.py: 数据库操作, 使用SQLAlchemy操作Sqlite3数据库
- mt.py: 主程序, 加载配置文件并启动服务器
- scene.py: 场景实例管理, 提供场景生成、查询、销毁功能。
- server.py: 服务器类, 响应前端的请求, 执行对应的操作
- templates.py: 节点模板管理
- topo.py: 网络拓扑描述文件解析

- backends.__init__.py: 后端Hypervisor父类, VirtualBox、Workstation等后端必须实现该类的所有方法