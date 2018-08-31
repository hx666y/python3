from callback import ResultCallback
from collections import namedtuple
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.vars.manager import VariableManager
from ansible.parsing.dataloader import DataLoader
from ansible.inventory.manager import InventoryManager
from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.playbook.play import Play
import ansible.constants as C
from ansible.utils.display import Display
from exceptions import AnsibleError
import json

Options = namedtuple('Options', [
    'listtags', 'listtasks', 'listhosts', 'syntax', 'connection',
    'module_path', 'forks', 'remote_user', 'private_key_file', 'timeout',
    'ssh_common_args', 'ssh_extra_args', 'sftp_extra_args',
    'scp_extra_args', 'become', 'become_method', 'become_user',
    'verbosity', 'check', 'extra_vars', 'playbook_path', 'passwords',
    'diff', 'gathering', 'remote_tmp',
])

def get_default_options():
    options = Options(
        listtags=False,
        listtasks=False,
        listhosts=False,
        syntax=False,
        timeout=60,
        connection='ssh',
        module_path='',
        forks=10,
        remote_user='root',
        private_key_file=None,
        ssh_common_args="",
        ssh_extra_args="",
        sftp_extra_args="",
        scp_extra_args="",
        become=None,
        become_method=None,
        become_user=None,
        verbosity=None,
        extra_vars=['host=localhost'],
        check=False,
        playbook_path=None,
        passwords=None,
        diff=False,
        gathering='implicit',
        remote_tmp='/tmp/.ansible'
    )

    return options

class AdHocRunner:
    results_callback_class = ResultCallback
    # results_callback = None
    # loader_class = DataLoader
    # variable_manager_class = VariableManager
    # default_options = get_default_options()

    def __init__(self, inventory):
        self.options = get_default_options()
        self.loader = DataLoader()
        self.inventory = InventoryManager(loader=self.loader, sources=['/etc/ansible/hosts'])
        self.variable_manager = VariableManager(loader=self.loader, inventory=self.inventory)

    def get_result_callback(self, file_obj=None):
        return self.__class__.results_callback_class(file_obj=file_obj)

    def run(self, tasks, pattern, play_name='Ansible Ad-hoc', gather_facts='no', file_obj=None):
        self.results_callback = self.get_result_callback(file_obj)
        play_source = dict(
            name=play_name,
            hosts=pattern,
            gather_facts=gather_facts,
            tasks=tasks
        )

        play = Play().load(
            play_source,
            variable_manager=self.variable_manager,
            loader=self.loader,
        )

        tqm = TaskQueueManager(
            inventory=self.inventory,
            variable_manager=self.variable_manager,
            loader=self.loader,
            options=self.options,
            stdout_callback=self.results_callback,
            passwords=self.options.passwords,
        )

        try:
            result = tqm.run(play)
            # return self.results_callback
        except Exception as e:
            raise AnsibleError(e)
        finally:
            tqm.cleanup()
            self.loader.cleanup_all_tmp_files()

        results_raw = {}
        results_raw['success'] = {}
        results_raw['failed'] = {}
        results_raw['unreachable'] = {}

        for host, result in self.results_callback.host_ok.items():
            results_raw['success'][host] = json.dumps(result._result)

        for host, result in self.results_callback.host_failed.items():
            results_raw['failed'][host] = result._result['msg']

        for host, result in self.results_callback.host_unreachable.items():
            results_raw['unreachable'][host] = result._result['msg']

        print(results_raw)


class PlayBookRunner:
    """
    用于执行AnsiblePlaybook的接口.简化Playbook对象的使用.
    """

    # Default results callback
    results_callback_class = ResultCallback
    loader_class = DataLoader
    variable_manager_class = VariableManager
    options = get_default_options()

    def __init__(self, options=None):
        if options:
            self.options = options
        C.RETRY_FILES_ENABLED = False
        self.loader = self.loader_class()
        self.inventory = InventoryManager(loader=self.loader, sources=['/etc/ansible/hosts'])
        self.results_callback = self.results_callback_class()
        #self.playbook_path = self.options.playbook_path
        self.variable_manager = self.variable_manager_class(
            loader=self.loader, inventory=self.inventory
        )
        self.passwords = self.options.passwords

    def run(self, playbook_path):
        executor = PlaybookExecutor(
            playbooks=[playbook_path],
            inventory=self.inventory,
            variable_manager=self.variable_manager,
            loader=self.loader,
            options=self.options,
            passwords=self.passwords
        )

        result = executor.run()
        return result


if __name__ == '__main__':
    # a = AdHocRunner()
    # host = ['10.10.1.105']
    # tasks = [
    #     dict(action=dict(module='shell', args='ps -ef | grep nginx')),
    #     # dict(action=dict(module='shell', args='python sleep.py')),
    #     # dict(action=dict(module='synchronize', args='src=/home/op/test dest=/home/op/ delete=yes')),
    # ]
    # #a.run(tasks,host)
    a = PlayBookRunner()
    a.run('/root/linux/ansible/config_release/update.yml')
