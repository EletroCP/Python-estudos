from abc import ABC, abstractmethod


class CharacterInterface(ABC):

    @abstractmethod
    def speak(self):
        raise NotImplementedError
