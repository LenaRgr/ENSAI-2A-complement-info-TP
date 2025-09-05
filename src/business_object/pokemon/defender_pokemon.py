from business_object.statistic import Statistic
from abc import ABC, abstractmethod
from business_object.pokemon.abstract_pokemon import AbstractPokemon

class DefenderPokemone(AbstractPokemon):

    def get_pokemon_attack_coef(self) -> float:
    """
    Compute a damage multiplier related to the pokemon type.

    Returns :
        float : the multiplier
    """
    multiplier = 1 + (self.attack_current + self.defense_current) / 200
