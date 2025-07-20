from Utils import *
from Comp import *
from Hero import Hero as h

priority_order = [1, 2, 3, 4] # 1-based

# From https://afk.guide/temporal-rift/
recommended_comps_per_battle = [
    # All battles
    expand_team([h.Albedo, h.Merlin, [h.Joan_Arc, h.Mulan, h.ABrutus, h.AAthalia, h.ASafiya], [h.Emilia, h.Mulan, h.ABrutus, h.AAthalia, h.ASafiya], h.Rem]) +
    expand_team([[h.Albedo, h.Mulan, h.ABrutus, h.ATalene], [h.Merlin, h.ATalene, h.Robin_Hood, h.Geralt, h.ASolise, h.Haelus], [h.Joan_Arc, h.Mulan, h.ABrutus, h.AAthalia, h.ASafiya, h.Robin_Hood, h.Joker, h.Ezio, h.Yennefer, h.Geralt, h.ASolise, h.Haelus], [h.Emilia, h.Mulan, h.ABrutus, h.AAthalia, h.ASafiya, h.Robin_Hood, h.Joker, h.Ezio, h.Yennefer, h.Geralt, h.ASolise], h.Rem]) +
    expand_team([[h.Alna, h.Ivan], h.ABelinda, [h.Raine, h.Jerome], h.Palmer, [h.Rowan, h.Ivan, h.Jerome]]) +
    expand_team([[h.Alna, h.Ivan, h.Ezizh, h.Jerome], h.ABelinda, [h.Raine, h.Jerome, h.Haelus, h.Rosaline, h.Ezizh, h.Elijah_Lailah], [h.Palmer, h.Ivan, h.Haelus, h.Rosaline, h.Ezizh, h.Elijah_Lailah, h.Sonja], [h.Rowan, h.Ivan, h.Jerome, h.Haelus, h.Rosaline]]) +
    expand_team([h.ASolise, [h.Mishka, h.Astar, h.ABaden, h.Canisa_Ruke, h.AShemira, h.Veithael], h.Nevanthi, h.Scarlet, [h.ALyca, h.Astar, h.ABaden, h.Trishea]]) +
    expand_team([[h.ASolise, h.AShemira, h.Astar], [h.Mishka, h.Astar, h.ABaden, h.Canisa_Ruke, h.AShemira, h.Veithael, h.Grezhul, h.Eorin, h.Tamrus, h.Ivan, h.Sonja], [h.Nevanthi, h.Tamrus, h.Haelus, h.Desira, h.Silas, h.Mortas], h.Scarlet, [h.ALyca, h.Astar, h.ABaden, h.Trishea, h.Eorin, h.Tamrus, h.Haelus, h.Desira, h.Silas, h.Mortas, h.Ivan, h.Lavatune]]) +
    expand_team([[h.AShemira, h.Alna], [h.ABaden, h.Canisa_Ruke, h.Grezhul], [h.Oden, h.Lady_Simona, h.Olgath, h.AAthalia, h.Mulan], h.Silas, [h.Ivan, h.Desira, h.Mortas, h.Nevanthi, h.Lavatune]]) +
    expand_team([[h.AShemira, h.Alna, h.ABrutus, h.Canisa_Ruke, h.Grezhul, h.Edwin, h.Veithael, h.Maetria, h.Treznor], [h.ABaden, h.Canisa_Ruke, h.Grezhul, h.ABrutus], [h.Oden, h.Lady_Simona, h.Olgath, h.AAthalia, h.Mulan, h.Scarlet, h.Mortas, h.Robin_Hood, h.Lavatune, h.Edwin, h.Athalia, h.Maetria, h.Treznor], [h.Silas, h.Nevanthi, h.Hodgkin, h.Palmer, h.ASolise], [h.Ivan, h.Desira, h.Mortas, h.Nevanthi, h.Lavatune, h.Robin_Hood, h.Ferael, h.Hodgkin, h.Lady_Simona, h.Haelus, h.Palmer, h.Tamrus, h.Edwin, h.Astar, h.Mulan, h.Treznor]]) +
    expand_team([[h.ABrutus, h.Canisa_Ruke, h.Veithael], [h.Lucilla, h.Canisa_Ruke, h.Veithael, h.Merlin, h.ATalene], h.Liberta, [h.Daemia, h.Canisa_Ruke, h.Veithael, h.AAthalia, h.Mulan, h.Haelia, h.ATalene], [h.ASafiya, h.AAthalia, h.Haelia]]),
    expand_team([[h.ABrutus, h.Canisa_Ruke, h.Veithael, h.Joan_Arc], [h.Lucilla, h.Canisa_Ruke, h.Veithael, h.Merlin, h.ATalene, h.Joan_Arc, h.Skreg, h.Anasta, h.Talene], h.Liberta, [h.Daemia, h.Canisa_Ruke, h.Veithael, h.AAthalia, h.Mulan, h.Haelia, h.ATalene, h.Emilia, h.Astar, h.Joan_Arc, h.Anasta, h.Merlin, h.Crassio, h.Talene, h.Framton], [h.ASafiya, h.AAthalia, h.Haelia, h.Mulan, h.Emilia, h.Astar, h.Skreg, h.Anasta, h.Merlin]]),
    expand_team([h.Alna, [h.AThane, h.Eorin], [h.Athalia, h.Treznor, h.Mulan, h.Palmer, h.Ferael, h.Oden, h.Haelia, h.Tamrus, h.ALyca], [h.Silas, h.Mortas, h.ASolise, h.Merlin], [h.Desira, h.Edwin, h.Salaki, h.Astar, h.Palmer, h.Skreg, h.Hodgkin, h.Joan_Arc, h.ALyca]]),
    expand_team([[h.Sonja, h.Canisa_Ruke, h.Skreg, h.Rowan], h.AThane, [h.Haelia, h.Silas, h.Palmer, h.Tamrus, h.Joan_Arc], [h.Mulan, h.Rosaline, h.Tamrus, h.Athalia, h.Treznor, h.Joan_Arc], [h.Veithael, h.ALyca, h.Rosaline, h.Athalia, h.Edwin, h.Astar, h.Canisa_Ruke, h.Skreg, h.Joan_Arc]]),
    expand_team([h.ABrutus, [h.Anasta, h.Talene, h.ATalene, h.ABaden, h.Treznor, h.Merlin, h.Ezio, h.Mulan, h.Joan_Arc, h.Tamrus, h.Astar, h.Crassio], [h.Skreg, h.ASafiya, h.Merlin, h.Salaki, h.Palmer, h.Talene, h.ATalene, h.Tamrus], [h.Framton, h.ASafiya, h.Astar, h.Merlin, h.Salaki, h.Palmer, h.Ezio, h.Talene, h.ATalene, h.Crassio], [h.Haelia, h.ASafiya, h.Astar, h.Salaki, h.Joan_Arc, h.Palmer, h.Daemia]]),
    expand_team([h.Albedo, h.Merlin, [h.Joan_Arc, h.Ezio, h.Emilia, h.Yennefer, h.Geralt, h.ATalene, h.AAthalia], [h.Mulan, h.Ezio, h.Yennefer, h.Ainz, h.Daimon, h.Geralt, h.ATalene, h.ASolise, h.Joker, h.AAthalia], [h.Emilia, h.Yennefer, h.Ainz, h.Daimon, h.Joker]]),
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
            Comp(thisMode, "4", recommended_comps_per_battle[0]),
          ]

comp_list = CompList(battles, priority_order)
