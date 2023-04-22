from tests.player.methods import Abstract
from tests.player.data_input import Input
from dataclasses import dataclass, field, fields


@dataclass
class Player(Abstract):

    _list: list = field(default_factory=list)

    def __post_init__(self) -> None:
        data = self.read_json('data.json')
        self.player_input = Input(**data)

    def execute(self) -> list[str]:
        for each_field in fields(self.player_input):
            name, _type = each_field.name, each_field.type.__name__
            attribute = getattr(self.player_input, name)
            result = f'{name}: {_type} = {attribute!r}'
            self._list.append(result)
        return self._list
