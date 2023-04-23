from dataclasses import dataclass, field, fields
from app.player.modules import Abstract
from app.player.data_input import Input
from core.infrastructure.constants.data import PLAYER_DATA


@dataclass
class Player(Abstract):

    _list: list = field(default_factory=list)

    def __post_init__(self) -> None:
        self.data = self.read_json(PLAYER_DATA)
        self.player = Input(**self.data)

    @property
    def execute(self) -> list[str]:
        for each_field in fields(self.player):
            name, _type = each_field.name, each_field.type.__name__
            attribute = getattr(self.player, name)
            result = f'{name}: {_type} = {attribute!r}'
            self._list.append(result)

        return self._list
