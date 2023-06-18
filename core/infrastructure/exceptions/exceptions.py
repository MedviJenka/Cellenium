from abc import ABC, abstractmethod


class AbstractMessage(ABC):
    @abstractmethod
    def message(self, *args: str, **kw: str) -> str:
        raise Exception


class NoSuchTypeException(AbstractMessage, BaseException):
    @staticmethod
    def message() -> str:
        raise Exception("no such type in the page base file")


class GlobalError(Exception, AbstractMessage):
    @staticmethod
    def message() -> str:
        raise 'an error has been made'
