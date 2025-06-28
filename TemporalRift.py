from Utils import *
from Comp import *
from Hero import Hero as h

priority_order = [1, 2, 3] # 1-based

# From https://afk.guide/temporal-rift/
recommended_comps_per_battle = [
    # All battles
    expand_team([h.Albedo, h.Merlin, [h.Joan_Arc, h.Mulan, h.ABrutus, h.AAthalia, h.ASafiya], [h.Emilia, h.Mulan, h.ABrutus, h.AAthalia, h.ASafiya], h.Rem]) +
    expand_team([[h.Albedo, h.Mulan, h.ABrutus, h.ATalene], [h.Merlin, h.ATalene, h.Robin_Hood, h.Geralt, h.ASolise, h.Haelus], [h.Joan_Arc, h.Mulan, h.ABrutus, h.AAthalia, h.ASafiya, h.Robin_Hood, h.Joker, h.Ezio, h.Yennefer, h.Geralt, h.ASolise, h.Haelus], [h.Emilia, h.Mulan, h.ABrutus, h.AAthalia, h.ASafiya, h.Robin_Hood, h.Joker, h.Ezio, h.Yennefer, h.Geralt, h.ASolise], h.Rem]) +
]

# Deduplicate and validate
recommended_comps_per_battle = [
    deduplicate_and_validate_battle_comps(battle)
    for battle in recommended_comps_per_battle
]

thisMode = "Temporal Rift"
battles = [ Comp(thisMode, "1", recommended_comps_per_battle[0]),
            Comp(thisMode, "2", recommended_comps_per_battle[0]),
            Comp(thisMode, "3", recommended_comps_per_battle[0]),
          ]
