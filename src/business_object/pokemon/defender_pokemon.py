from business_object.pokemon.abstract_pokemon import AbstractPokemon

class DefenderPokemone(AbstractPokemon):
    def __init__(self, stat_max=None, stat_current=None, level=0, name=None): # enleve type car tjs le mm/ permet d'avoir le controle sur les arguments
        super.__init__(
            self, 
            stat_max=stat_max, 
            stat_current=stat_current, 
            level=level, 
            name=name, 
            type_pk="Defender") # tjs Defender comme type/ remets le init car veut preciser le type

    def get_pokemon_attack_coef(self) -> float:
        """
        Compute a damage multiplier related to the pokemon type.

        Returns :
            float : the multiplier
        """
        multiplier = 1 + (self.attack_current + self.defense_current) / 200
        return multiplier
