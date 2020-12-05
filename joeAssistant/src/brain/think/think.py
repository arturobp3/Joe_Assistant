from joeAssistant.src.modules.moduleFactory import ModuleFactory
from joeAssistant.src.brain.selfRecognition.selfRecognition import SelfRecognition


class Think:

    def __init__(self):
        self._module_factory = ModuleFactory()

    def execute_action(self, intent_request: dict, self_recognition: SelfRecognition) -> str:
        '''if self._self_recognition.is_anything_running():
            # parar o bajar volumen de la musica por ejemplo
            # poner flag a true
            pass'''

        intent_name = intent_request["outcomes"][0]["entities"]["intent"][0]["value"]
        splitted_intent_name = intent_name.split("_")
        module_name = splitted_intent_name[0]
        function_to_invoke = "_".join(splitted_intent_name[1:])
        if self_recognition.is_module_running(module_name):
            module = self_recognition.get_module(module_name)
        else:
            module = self._module_factory.create_module(module_name)
        method_to_call = getattr(module, function_to_invoke)
        success, response = method_to_call()
        if success:
            self_recognition.add_module_running(module_name, module)
        return response


        # TODO: hacer algo si la tarea no se ha hecho bien

        # TODO: Como se podria hacer para pasarle por argumento los datos de la peticion? Args?
