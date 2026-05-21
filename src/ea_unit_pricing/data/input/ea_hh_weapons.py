from __future__ import annotations

from ea_unit_pricing.domain import Traits
from ea_unit_pricing.domain.weapons import RangedWeapon


class HeavyBolter(RangedWeapon):
    def __init__(
        self,
        aa: int = 0,
        traits: list[Traits] | None = None,
        stat_modifiers: dict[str, int] | None = None,
    ) -> None:
        super().__init__(
            30,
            ap=5,
            aa=aa,
            name="Heavy Bolter",
            traits=traits or [],
            stat_modifiers=stat_modifiers or {},
        )


class TwinHeavyBolter(RangedWeapon):
    def __init__(self, aa: int = 0, traits: list[Traits] | None = None) -> None:
        super().__init__(30, ap=4, aa=aa, name="Twin-linked Heavy Bolter", traits=traits or [])


class LasCannon(RangedWeapon):
    def __init__(self, aa: int = 0, traits: list[Traits] | None = None) -> None:
        super().__init__(45, at=5, aa=aa, name="Lascannon", traits=traits or [])


class TwinLinkedLasCannon(RangedWeapon):
    def __init__(self, aa: int = 0, traits: list[Traits] | None = None) -> None:
        super().__init__(45, at=4, aa=aa, name="Twin-linked Lascannon", traits=traits or [])


class QuadLasCannon(RangedWeapon):
    def __init__(self, aa: int = 0, traits: list[Traits] | None = None) -> None:
        super().__init__(45, at=3, aa=aa, name="Quad Lascannon", traits=traits or [])


class BattleCannon(RangedWeapon):
    def __init__(self, traits: list[Traits] | None = None) -> None:
        super().__init__(75, at=4, ap=4, name="Battle Cannon", traits=traits or [])


class VanquisherBattleCannon(RangedWeapon):
    def __init__(self, traits: list[Traits] | None = None) -> None:
        super().__init__(75, at=3, ap=6, name="Vanquisher Cannon", traits=traits or [])


class DemolisherCannon(RangedWeapon):
    def __init__(self, traits: list[Traits] | None = None) -> None:
        super().__init__(
            30,
            ap=3,
            at=4,
            traits=[Traits.IGNORE_COVER, *(traits or [])],
            name="Demolisher Cannon",
        )


class AutoCannon(RangedWeapon):
    def __init__(self, aa: int = 0, traits: list[Traits] | None = None) -> None:
        super().__init__(45, ap=5, at=6, aa=aa, name="Auto Cannon", traits=traits or [])


class TwinAutoCannon(RangedWeapon):
    def __init__(self, aa: int = 0, traits: list[Traits] | None = None) -> None:
        super().__init__(45, ap=4, at=5, aa=aa, name="Twin-linked Auto Cannon", traits=traits or [])
