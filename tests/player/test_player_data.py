from app.player.main import Player


class TestPlayer:

    player: object = Player()

    def test_name(self) -> None:
        assert self.player.execute[0] == "name: str = 'SmellMyGun'"
        print(type(self.player))

    def test_class(self) -> None:
        assert self.player.execute[1] == "player_class: str = 'corsair'"
        print(type(self.player))

    def test_level(self) -> None:
        assert self.player.execute[2] == "level: int = 175"
        print(type(self.player))

    def test_attack_range(self) -> None:
        assert self.player.execute[3] == "attack_range: int = 90000"
        print(type(self.player))

    def test_exp(self) -> None:
        assert self.player.execute[4] == "exp: str = '97.0%'"
        print(type(self.player))
