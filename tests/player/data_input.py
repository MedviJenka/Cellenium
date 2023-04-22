from dataclasses import dataclass


@dataclass
class Data:

    name: str
    player_class: str
    level: int
    attack_range: int
    exp: str

    def __post_init__(self) -> None:
        self.exp = f'{self.exp * 100}%'

