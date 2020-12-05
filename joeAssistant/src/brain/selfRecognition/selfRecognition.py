

class SelfRecognition:

    def __init__(self):
        self.modules_running = dict()

    def is_module_running(self, name) -> bool:
        return name in self.modules_running

    def get_module(self, name):
        return self.modules_running[name]

    def add_module_running(self, name, module):
        self.modules_running[name] = module

    def stop_running_module(self, name) -> bool:
        try:
            del self.modules_running[name]
            return True
        except KeyError:
            return False

    def notify_joe_is_speaking(self):
        for module in self.modules_running.keys():
            self.modules_running[module].activate_before_joe_speaks()

    def notify_joe_stop_speaking(self):
        for module in self.modules_running.keys():
            self.modules_running[module].activate_after_joe_speaks()







