from business_object.pokemon.all_rounder_pokemon import AllRounderPokemon
from business_object.statistic import Statistic

class TestAllRounderPokemon:
    def test_get_coef_damage_type(self):
        # GIVEN
        poke_rounder = AllRounderPokemon(stat_current=Statistic(sp_atk=200, sp_df=200))

        # WHEN
        multiplier = poke_rounder.get_pokemon_attack_coef()

        # THEN
        assert multiplier == 3


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])