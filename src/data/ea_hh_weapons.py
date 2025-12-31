from data.models import RangedWeapon, SmallArms, Traits, UnitType, Unit, AssaultWeapon

class HeavyBolter(RangedWeapon):
    def __init__(self):
        super().__init__(30, ap=5)

class LasCannon(RangedWeapon):
    def __init__(self):
        super().__init__(45, at=5)

class TwinLinkedLasCannon(RangedWeapon):
    def __init__(self):
        super().__init__(45, at=4)

class BattleCannon(RangedWeapon):
    def __init__(self):
        super().__init__(75, at=4, ap=4)

class VanquisherBattleCannon(RangedWeapon):
    def __init__(self):
        super().__init__(75, at=3, ap=6)

class DemolisherCannon(RangedWeapon):
    def __init__(self):
        super().__init__(30, ap=3, at=4, traits=[Traits.IGNORE_COVER])