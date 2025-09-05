from business_object.pokemon.abstract_pokemon import AbstractPokemon

class AttackerPokemon(AbstractPokemon):
    def __init__(self, stat_max=None, stat_current=None, level=0, name=None): # enleve type car tjs le mm
        super.__init__(
            self, 
            stat_max=stat_max, 
            stat_current=stat_current, 
            level=level, 
            name=name, 
            type_pk="Attacker") # tjs Attacker comme type

    def get_pokemon_attack_coef(self) -> float:
        """
        Compute a damage multiplier related to the pokemon type.

        Returns :
            float : the multiplier
        """
        multiplier = 1 + (self.speed_current + self.attack_current) / 200
        return multiplier