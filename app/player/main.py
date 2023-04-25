from dataclasses import dataclass, field, fields
from app import Abstract
from app import Input
from core.infrastructure.constants.data import PLAYER_DATA


@dataclass
class Player(Abstract):

    _list: list = field(default_factory=list)

    def __post_init__(self) -> None:
        self.json = self.read_json(PLAYER_DATA)['player_1']
        self.data = Input(**self.json)

    def execute(self) -> list[str]:
        for each_field in fields(self.data):
            name = each_field.name
            _type = each_field.type.__name__
            attributes = getattr(self.data, name)
            result = f'{name}: {_type} = {attributes!r}'
            self._list.append(result)

        return self._list
