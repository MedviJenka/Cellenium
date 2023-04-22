from dataclasses import dataclass, field, fields
from tests.player.data_input import Data
from tests.player.methods import Abstract


@dataclass
class Player(Abstract):

    _list: list = field(default_factory=list)

    def __post_init__(self) -> None:
        player_data = self.read_json('data.json')
        self.data = Data(**player_data)

    def execute(self) -> list[str]:
        for each_field in fields(self.data):
            name, _type = each_field.name, each_field.type.__name__
            attribute = getattr(self.data, name)
            result = f'{name}: {_type} = {attribute!r}'
            self._list.append(result)
        return self._list


player = Player()
if __name__ == '__main__':
    for each in player.execute():
        print(each)
