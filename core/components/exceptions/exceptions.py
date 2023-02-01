class NoSuchTypeException(Exception):

    @staticmethod
    def message() -> str:
        raise "no such type in the page base file"
