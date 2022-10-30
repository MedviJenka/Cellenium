class NoSuchTypeException(Exception):

    @staticmethod
    def message() -> str:
        return "no such type in the page base file"

