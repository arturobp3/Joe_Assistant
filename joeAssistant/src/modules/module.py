# los modulos tienen que ser observados por "selfRecognition" para que este sepa en que estado estan

from abc import ABC, abstractmethod


class Module(ABC):

    @abstractmethod
    def start(self) -> str:
        pass

    @abstractmethod
    def stop(self) -> str:
        pass

    @abstractmethod
    def update(self) -> str:
        pass

    @abstractmethod
    def pause(self) -> str:
        pass

    @abstractmethod
    def activate_before_joe_speaks(self):
        pass

    @abstractmethod
    def activate_after_joe_speaks(self):
        pass
