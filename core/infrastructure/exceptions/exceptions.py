class NoSuchTypeException(Exception):

    def __init__(self, current_type) -> None:
        raise super().__init__(f"no such type in the page base file, current type is: {current_type}")
