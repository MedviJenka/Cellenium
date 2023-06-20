from nessus import API
from dataclasses import dataclass


@dataclass
class NessusManager:

    base_url: str
    username: str
    password: str

    def __post_init__(self) -> None:
        self.nessus = API(base_url=self.base_url, username=self.username, password=self.password)

    def get_list(self) -> list[str]:
        return self.nessus.users.list()
