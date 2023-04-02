from main import Pokemon

class Normal(Pokemon): #Je créer une classe pour le type Normal qui hérite de la classe Pokémon
    def __init__(self, name, hp, level, attack, defense):
        Pokemon.__init__(self, name, hp, level, attack, defense)

    def set_name(self, name): #Modification de la valeur privée name
        self.__name = name
        return self.__name
    def get_name(self):       #Récupération de la valeur privée name
        return self.__name

    def set_hp(self, hp):   #Modification de la valeur hp
        self.__hp = hp
        return self.__hp        
    def get_hp(self):       #Récupération de la valeur hp 
        return self.__hp
        
    def set_attack(self, attack): #Modification de la puissance d'attaque
        self.attack = attack
        return self.attack    
    def get_attack(self): #Récupération de la valeur de la puissance d'attaque
        return self.attack
                
    def set_defense(self, defense): #Modification de la défense
        self.defense = defense
        return self.defense
                
    def get_defense(self):  #Récupération de la valeur de la défense
        return self.defense
    
    def show_stats(self):       #Méthode permettant d'afficher les stats du pokémon
        print("name :", self.__name)
        print("lvl ;", self.level)
        print("hp :", self.__hp)
        print("atq :", self.attack)
        print("def :", self.defense)