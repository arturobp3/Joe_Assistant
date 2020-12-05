from typing import Union

from joeAssistant.src.modules.module import Module
from joeAssistant.src.modules.spotify.spotify import Spotify


class ModuleFactory:

    def switch(self, module_name: str) -> Union[Module, None]:
        switcher = {
            "spotify": Spotify(),
        }
        return switcher.get(module_name, None)

    def create_module(self, module_name: str) -> Module:
        return self.switch(module_name)
