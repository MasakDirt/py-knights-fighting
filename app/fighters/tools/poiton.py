from __future__ import annotations


class Potion:
    def __init__(self, name: str, effect: dict) -> None:
        self.name = name
        self.effect = effect

    @classmethod
    def get_instance(cls, potion: dict) -> None | Potion:
        if not potion:
            return None
        return cls(name=potion["name"], effect=potion["effect"])

    def if_effect_exist_return_value(self, effect_name: str) -> int:
        if effect_name in self.effect:
            return self.effect[effect_name]

        return 0
