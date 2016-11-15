# coding=UTF-8

class NodeTemplate:
    def __init__(self, template_id, emulation, guest_info=None):
        self.template_id = template_id
        self.emulation = emulation
        self.guest_info = guest_info


class NodeTemplateRepository:
    def __init__(self):
        pass

    def load_template(self, template_id):
        """
        加载节点模板
        :param template_id: 节点模板ID
        :return: 节点模板对象(NodeTemplate)
        """
        pass


class FileNodeTemplateRepository(NodeTemplateRepository):
    def __init__(self, base_dir):
        NodeTemplateRepository.__init__(self)
        self.base_dir= base_dir
        self.cache = dict()

    def load_template(self, template_id):
        if template_id in self.cache:
            return self.cache[template_id]
        else:
            template = self._load_from_file(template_id)
            self.cache[template_id] = template
            return template

    def _load_from_file(self, template_id):
        # TODO 查询节点模板文件是否存在
        pass

