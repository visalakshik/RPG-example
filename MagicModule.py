class Magic:
    """
    This Magic has name,mp cost, damage, type
    """
    def __init(self,name,mp_cost,damage,type):
        self.name = name
        self.mp_cost = mp_cost
        self.damage = damage
        self.magic_type = magic_type
        self.high_damage = damage + 15
        self.low_damage = damage - 15

    def generate_magic_damage(self):
        dmg = random.randrange(self.low_damage,self.high_damage)
        return dmg
