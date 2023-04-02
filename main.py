from fight import Combat

class Pokemon():
    def __init__(self, name, hp, level, attack, defense, type):
        self.__name = name 
        self.__hp = hp
        self.level = level
        self.attack = attack
        self.defense = defense
        self.type = type

    def set_name(self, name): #Modification de la valeur privée name
        self.__name = name
    def get_name(self):       #Récupération de la valeur privée name
        return self.__name

    def set_hp(self, hp):   #Modification de la valeur hp
        self.__hp = hp       
    def get_hp(self):       #Récupération de la valeur hp 
        return self.__hp
        
    def set_attack(self, attack): #Modification de la puissance d'attaque
        self.attack = attack 
    def get_attack(self): #Récupération de la valeur de la puissance d'attaque
        return self.attack
                
    def set_defense(self, defense): #Modification de la défense
        self.defense = defense
                
    def get_defense(self):  #Récupération de la valeur de la défense
        return self.defense
    
    def get_type(self):  #Récupération de la valeur de self.type
        return self.type

#Création de deux objets Pokémon
pokemon1 = Pokemon('Salamèche', 39, 5, 52, 43, 'Feu')
pokemon2 = Pokemon('Carapuce', 44, 5, 48, 65, 'Eau')

#Création d'un objet Combat
fight = Combat(pokemon1, pokemon2)

#Appel de la méthode run_combat au sein de la classe Combat
fight.run_combat(pokemon2)


        
        
                    
                    

            


            

                
