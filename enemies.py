import random


class Enemy:
    def __init__ (self):
        raise NotImplementedError("Do not create raw Enemy objects")
    
    def __str__(self):
        return self.name
    
    def is_alive(self):
        return self.hp > 0
        
        
class boss (Enemy):
    def __init__(self):
        self.name = "Grand EELLer of Mormoon, Lord Jeremiah"
        self.hp = 550
        self.damage= 40
        self.gold=random.randint(20,40)
        self.exp =100

class BaldMan (Enemy):
    def __init__(self):
        self.name = "Bald man"
        self.hp = 10
        self.damage= 10
        self.gold=random.randint(20,40)
        self.exp =15
        
class GumSpider (Enemy):
    def __init__(self):
        self.name = "Spider of gum"
        self.hp = 30
        self.damage = 15
        self.gold=random.randint(40,60)
        self.exp =20
        
class CorruptedGnome (Enemy):
    def __init__(self) :
        self.name = "Corrupted gnome"
        self.hp = 80
        self.damage = 15
        self.gold=random.randint(60,80)
        self.exp =30
        
class CumColossus(Enemy):
    def __init__ (self):
        self.name ="Cum Colossus"
        self.hp =70
        self.damage=20 
        self.gold=random.randint(80,100)
        self.exp =40
