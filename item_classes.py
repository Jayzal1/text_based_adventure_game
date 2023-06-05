from classes import Item, Character


class Rope(Item):
    name = "rope"
    weight = 100
    damage = 1
    description = "This rope can be used to climb things"

    def use_item(self, target):
        if isinstance(target, Character):
            target.damage(Sword.damage)
        else:
            print("sword does nothing")


class Sword(Item):
    name = "sword"
    weight = 100
    damage = 10
    description = "Poke them with the pointy end"

    def use_item(self, target):
        if isinstance(target, Character):
            target.damage(Sword.damage)
        else:
            print("sword does nothing")
