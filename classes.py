class Character:
    health = 100
    inventory = []
    current_room = str

    def damage(self, amount):
        self.health = self.health - amount


class Item:
    name = 'None'
    weight = 0
    damage = 0
    description = 'Enter a text based description here'

    def use_item(self, target):
        if target is None:
            print("No valid target")
            return
