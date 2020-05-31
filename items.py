class Weapon:  
    def __init__(self):
        raise NotImplementedError("Do not create raw Weapon Objects.")
        
    def __str__(self):
        return "{}+{} STR ".format(self.name, self.damage)
      
#class Pizza(Weapon):
#    def __init__(self):
#        self.name="Rock hard slice of pizza"
#        self.description= "A large slice of pizza, petrified by the elements."\
#                          "Not very sharp, but perfect for bludgeoning."
#        self.damage=5
#        self.value= 1
        
class CatEffigy(Weapon):
    def __init__(self):
        self.name="Cat Effigy"
        self.description="A small wooden cat carved from rotting wood. "\
                         "You can see specks of white paint clinging to 'weapon.' "\
                         "Show this to your foes and watch as they cower in fear."
        self.damage=10
        self.value= 20

class GoldCrossofMormoon(Weapon):
    def __init__(self):
        self.name="Gold Cross of Mormoon"
        self.description= "An odd sword with a shungite gem fashioned into the hilt. "\
                          "Whoever made it has extremely bad taste."
        self.damage=15
        self.value= 100

class EELLSpear(Weapon):
    def __init__(self):
        self.name="EELL Spear"
        self.description= "A spear used by the elite guard of Lord Jeremiah. "\
                          "It doubles as a fishing rod."
        self.damage=20
        self.value= 250
        
class CoomHammer(Weapon):
    def __init__(self):
        self.name="Coom Hammer"
        self.description= "The hammer used by the Hell-walker. "\
                          "Ghast tears are carved into the metal mass, "\
                          "signifying rebirth."
        self.damage=30
        self.value= 150
        
class GauntletoftheChamp(Weapon):
    def __init__(self):
        self.name="Gauntlet of the Champ"
        self.description= "The people bow to the gods. "\
                          "The gods bow to... THE CHAMP."
        self.damage=40
        self.value= 250        

class Consumable:
    def __init__ (self):
        raise NotImplementedError ("Do not creat raw Consumable Objects")
    
    def __str__(self):
        return "{}+{}HP".format(self.name, self.healing_value)
        
class HardTack(Consumable):
    def __init__ (self):
        self.name = "Hard Tack from 1863"
        self.healing_value = 15 
        self.value= 15

class Cum(Consumable):
    def __init__(self):
        self.name = "Small flask of cum"
        self.healing_value = 50
        self.value = 60 

class Jug(Consumable):
    def __init__(self):
        self.name = "Fortnite chug jug"
        self.healing_value = 100
        self.value = 150    

class bug: 
    def __init__(self):
        raise NotImplementedError("Do not create raw bug Objects.")
        
    def __str__(self):
        return "{} ".format(self.name)






#need better names

        
class BoneDoll(bug):
    def __init__(self):
        self.name = " Bone Doll"
        self.value = 7700    
        
class BoneFlute(bug):
    def __init__(self):
        self.name = " Bone Flute "
        self.value = 5600  
        
class BoneCrown(bug):        
     def __init__(self):
        self.name = " Bone Crown "   
        self.value = 6300  

class BoneHarp(bug):        
     def __init__(self):
        self.name = " Bone Harp "   
        self.value = 3000         