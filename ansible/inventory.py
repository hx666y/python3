from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager


class BaseInventory(InventoryManager):
    """
    提供生成Ansible inventory对象的方法
    """
    loader_class = DataLoader
    variable_manager_class = VariableManager

    def __init__(self, host_list=None, group_list=None):
        self.host_list = host_list or []
        self.group_list = group_list or []
        # assert isinstance(host_list, list)
        self.loader = self.loader_class()
        self.variable_manager = self.variable_manager_class()
        super().__init__(self.loader)

    def get_groups(self):
        return self._inventory.groups

    def get_groups(self, name):
        return self._inventory.groups.get(name, None)

