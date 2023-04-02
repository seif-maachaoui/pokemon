
class Combat():
    def __init__(self, pokemon1, pokemon2):
        self._pokemon1 = pokemon1
        self._pokemon2 = pokemon2
        

    def check_death(self):  # Vérification de la mort d'un des pokémon
            if self.get_hp() <= 0 :
                print(f"{self.get_name()} est K.O.")
                return True
            else:
                return False

    def check_victory(self, target): #Vérification de la victoire d'un pokémon
        if self.get_hp() <= 0:
            print(f"{target.get_name()} est K.O., {self.get_name()} a gagné le combat !")
            return self.get_name()
        else:
            return None


    def check_type(self, target): #Récupération du type et de son attaque
        from type1 import Normal
        from type2 import Feu
        from type3 import Eau
        from type4 import Terre

        if isinstance(target, Normal):
            if self.get_type() == 'Normal':
                self.attack *= 1
            elif self.get_type() == 'Eau':
                self.attack *= 0.75
            elif self.get_type() == 'Feu':
                self.attack *= 0.75
            elif self.get_type() == 'Terre':
                self.attack *= 0.75

        elif isinstance(target, Eau):
            if self.get_type() == 'Normal':
                self.attack *= 1
            elif self.get_type() == 'Eau':
                self.attack *= 1
            elif self.get_type() == 'Feu':
                self.attack *= 2
            elif self.get_type() == 'Terre':
                self.attack *= 0.5

        elif isinstance(target, Feu):
            if self.get_type() == 'Normal':
                self.attack *= 1
            elif self.get_type() == 'Eau':
                self.attack *= 0.5
            elif self.get_type() == 'Feu':
                self.attack *= 1
            elif self.get_type() == 'Terre':
                self.attack *= 2

        elif isinstance(target, Terre):
            if self.get_type() == 'Normal':
                self.attack *= 1
            elif self.get_type() == 'Eau':
                self.attack *= 2
            elif self.get_type() == 'Feu':
                self.attack *= 0.5
            elif self.get_type() == 'Terre':
                self.attack *= 1

        #Inflige les dégâts à la cible
        target.take_damage(self.attack, self.get_attack(), target.get_defense())

        # Vérifie si la cible est KO
        if target.check_death():
            print(f"{target.get_name()} a été mis KO !")
            return target.get_name()

        #Si la cible n'est pas KO, retourner None
        return None

    def take_damage(self, damage, target_attack, target_defense):
        # Enlever des points de vie en fonction de la défense 
        damage -= target_defense
        damage *= target_attack / self.get_defense()

        # On s'assure que les dégâts infligés ne sont pas négatifs
        if damage < 0:
            damage = 0

        # On applique les dégâts à la cible
        self.set_hp(self.get_hp() - damage)

    def check_loose(self, target): # Vérifie la défaite d'un pokémon
        if self.check_death():
            return f"{self.get_name()} a perdu !"
        elif target.check_death():
            return f"{target.get_name()} a perdu !"
        else:
            return "Le combat se poursuit !"

    def run_combat(self, pokemon2): #Déroulement du combat 
        
        # Je Demande à l'utilisateur s'il veut commencer une partie
        while True:
            play = input("Voulez-vous lancer une partie (y/n) ? ")
            if play.lower() == "y":
                print("Le combat commence !")
                break
            elif play.lower() == "n":
                print("Partie annulée.")
                return
            else:
                print("Entrée invalide, veuillez saisir 'y' ou 'n'.")

        #Ensuite je demande à l'utilisateur de choisir son pokémon
        while True:
            choice = input("Veuillez choisir votre pokémon (Salamèche ou Carapuce) : ")
            if choice.lower() == "salamèche":
                player_pokemon = self._pokemon1
                print("Vous avez choisi Salamèche !")
                break
            elif choice.lower() == "carapuce":
                player_pokemon = self._pokemon2
                print("Vous avez choisi Carapuce !")
                break
            else:
                print("Pokémon invalide, veuillez saisir 'Salamèche' ou 'Carapuce'.")

        # Je souhaite afficher les stats du pokémon choisi
        player_pokemon.show_stats()

        # Le menu d'attaque de Salamèche s'il a été choisi
        if isinstance(player_pokemon, self._pokemon1):
            print("Menu d'attaque :")
            print("1. Griffe")
            print("2. Flammèche")
        #Sinon si Carapuce est choisi, on affiche son menu d'attaque
        elif isinstance(player_pokemon, self._pokemon2):
            print("Menu d'attaque :")
            print("1. Charge")
            print("2. Pistolet")




                
            
                
                        
                    

                
                



                        

                    
                    

                
                
            



                    
                

                
                                
                                
                                