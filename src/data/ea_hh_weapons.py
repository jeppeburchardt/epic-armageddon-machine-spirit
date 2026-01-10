from data.models import RangedWeapon, Traits


class HeavyBolter(RangedWeapon):
    def __init__(self):
        super().__init__(30, ap=5, name="Heavy Bolter")


class TwinHeavyBolter(RangedWeapon):
    def __init__(self, aa=0):
        super().__init__(30, ap=4, aa=aa, name="Twin-linked Heavy Bolter")


class LasCannon(RangedWeapon):
    def __init__(self, aa=0):
        super().__init__(45, at=5, aa=aa, name="Lascannon")


class TwinLinkedLasCannon(RangedWeapon):
    def __init__(self, aa=0):
        super().__init__(45, at=4, aa=aa, name="Twin-linked Lascannon")


class QuadLasCannon(RangedWeapon):
    def __init__(self, aa=0):
        super().__init__(45, at=3, aa=aa, name="Quad Lascannon")


class BattleCannon(RangedWeapon):
    def __init__(self):
        super().__init__(75, at=4, ap=4, name="Battle Cannon")


class VanquisherBattleCannon(RangedWeapon):
    def __init__(self):
        super().__init__(75, at=3, ap=6, name="Vanquisher Cannon")


class DemolisherCannon(RangedWeapon):
    def __init__(self):
        super().__init__(
            30, ap=3, at=4, traits=[Traits.IGNORE_COVER], name="Demolisher Cannon"
        )


class AutoCannon(RangedWeapon):
    def __init__(self, aa=0):
        super().__init__(45, ap=5, at=6, aa=aa, name="Auto Cannon")


class TwinAutoCannon(RangedWeapon):
    def __init__(self, aa=0):
        super().__init__(45, ap=4, at=5, aa=aa, name="Twin-linked Auto Cannon")
