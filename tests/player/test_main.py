from tests.player.main import Player


class TestMain(Player):

    def test_name(self) -> None:
        assert self.execute()[0] == "name: str = 'geralt'"

    def test_class(self) -> None:
        assert self.execute()[0] == 'name: str = "geralt"'

    def test_attack(self) -> None:
        assert self.execute()[0] == 'name: str = "geralt"'

    def test_level(self) -> None:
        assert self.execute()[0] == 'name: str = "geralt"'


