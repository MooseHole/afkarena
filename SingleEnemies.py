from Utils import *
from Comp import *
from Hero import Hero as h

SingleEnemyComps = {
    "Astral Devourer": deduplicate_and_validate_battle_comps(
        expand_team([h.Zohra, [h.Melion, h.Atheus, h.Randle, h.Lucilla, h.Raine, h.Mortas], h.Ivan, h.Envydiel, [h.Daemia, h.ASafiya]]) +
        expand_team([[h.Zohra, h.Lucilla, h.Rimuru, h.Skylan, h.Melion, h.Knox], h.Sion, h.Daemia, h.Palmer, h.Ivan]) +
        expand_team([h.Zohra, h.Envydiel, h.Ivan, [h.Mortas, h.Palmer, h.Elijah_Lailah], h.Daemia]) +
        expand_team([h.Knox, h.Rimuru, h.Daemia, [h.Palmer, h.Liberta], h.ALyca]) +
        [[h.Liberta, h.ALyca, h.Elijah_Lailah, h.Rimuru, h.Daemia]] +
        expand_team([[h.ALyca, h.ALucius], h.Knox, h.Daemia, h.Palmer, h.Ivan]) +
        expand_team([h.Daemia, [h.Lucilla, h.Knox], [h.Liberta, h.Palmer, h.Lavatune], h.AAthalia, h.Rimuru]) +
        expand_team([[h.Palmer, h.Lucilla], h.Zohra, [h.Liberta, h.Jerome, h.Lucilla, h.Ivan], h.Daemia, [h.Knox, h.AThoran]]) +
        [   [h.Lucilla, h.Liberta, h.Daemia, h.Zohra, h.Lady_Simona],
            [h.Daemia, h.Skylan, h.Liberta, h.Lucilla, h.Rimuru],
            [h.Skylan, h.Lucilla, h.Daemia, h.Zohra, h.ALyca],
            [h.Crassio, h.Palmer, h.Daemia, h.Rimuru, h.Lucilla],
            [h.Knox, h.Lavatune, h.Daemia, h.Palmer, h.Haelia],
            [h.AThoran, h.Rimuru, h.Liberta, h.Daemia, h.AShemira],
        ],
    ),
    "Fractured Fool": deduplicate_and_validate_battle_comps(
        expand_team([h.Orthros, h.Liberta, h.Lucilla, h.Knox, [h.Haelia, h.Shuna, h.Rosaline, h.Gavus, h.Veithael]]) +
        [   [h.Orthros, h.Jerome, h.Knox, h.Liberta, h.Lucilla],
            [h.Shuna, h.Knox, h.Liberta, h.Lysander, h.Orthros],
            [h.AAthalia, h.AThoran, h.ASafiya, h.Lucilla, h.Lysander],
            [h.AThane, h.Lan, h.Haelia, h.Veithael, h.Aurelia],
            [h.Warek, h.Lan, h.AThane, h.Veithael, h.Aurelia],] +
        expand_team([[h.Lan, h.Lavatune], h.Jerome, [h.Raine, h.Lorsan, h.AThoran, h.Veithael], [h.Vika, h.AThane], h.Rosaline]) +
        [   [h.Lavatune, h.Rosaline, h.Lorsan, h.Vika, h.Lady_Simona],
            [h.Vika, h.Lucilla, h.Rimuru, h.Lavatune, h.Liberta],
            [h.Vika, h.Lavatune, h.Rosaline, h.Anasta, h.Raoul],] +
        expand_team([h.Rem, h.ASolise, h.Randle, [h.Misha, h.AThoran], [h.Naroko, h.Numisu, h.AThoran]]) +
        expand_team([h.Trishea, h.Baden, h.Elijah_Lailah, [h.Villanelle, h.Hodgkin], h.Aurelia]) +
        [   [h.Jerome, h.Lavatune, h.Raine, h.ABelinda, h.Rosaline],
            [h.ABelinda, h.Liberta, h.Raine, h.Lavatune, h.Knox],
            [h.Naroko, h.Lucilla, h.Knox, h.Liberta, h.Ivan],
            [h.Sion, h.Lyca, h.ASafiya, h.Villanelle, h.Naroko], ]
    ),
    "Abyssal Murmur": deduplicate_and_validate_battle_comps(
        expand_team([[h.Randle, h.Adrian_Elyse, h.Lan], [h.Hodgkin, h.Melion, h.Lavatune], h.Rimuru, h.Sion, h.Misha]) +
        expand_team([[h.Envydiel, h.Zohra], [h.Randle, h.AThoran, h.Raine], [h.Hodgkin, h.Palmer, h.Velufira], [h.Misha, h.Saurus, h.Lavatune, h.Knox], [h.Rimuru, h.Raine, h.Jerome, h.Estrilda, h.Saurus, h.Silas]]) +
        [   [h.Melion, h.Lavatune, h.Rosaline, h.Haelia, h.Rimuru],
            [h.Lan, h.AThane, h.AEstrilda, h.Jerome, h.Raine],] +
        expand_team([h.Trishea, h.Baden, h.Elijah_Lailah, [h.Knox, h.Nevanthi, h.Naroko, h.Lavatune, h.AThoran], [h.Aurelia, h.Nevanthi]]) +
        expand_team([h.Rem, h.ASolise, [h.Naroko, h.Numisu, h.AThoran], h.Misha, h.Randle]) +
        expand_team([h.AEironn, h.Randle, h.Misha, [h.Knox, h.Rimuru], h.Hodgkin]),
    ),
    "Clawlossus": deduplicate_and_validate_battle_comps(
        expand_team([h.Jerome, [h.Lavatune, h.Lan], h.Raine, [h.Marcille, h.DGwyneth], h.Rosaline]) +
        expand_team([h.Marcille, [h.Aurelia, h.Velufira], [h.Silas, h.Elijah_Lailah], h.Lavatune, [h.Laios, h.Randle, h.Velufira]]) +
        expand_team([h.Aurelia, h.Lavatune, [h.Rosaline, h.Raine], h.Marcille, h.Velufira]) +
        [   [h.Randle, h.AThoran, h.Velufira, h.Lysander, h.DGwyneth],
            [h.AThoran, h.AAthalia, h.Randle, h.Lysander, h.Velufira],
            [h.Sion, h.Velufira, h.Rimuru, h.Misha, h.Randle],
            [h.Randle, h.ABelinda, h.Jerome, h.Lavatune, h.Rosaline],
            [h.Envydiel, h.Jerome, h.Raine, h.Velufira, h.Lan],] +
        expand_team([h.Envydiel, h.Raine, h.Velufira, [h.Atheus, h.Lan], [h.Rimuru, h.Silas]]) +
        [   [h.Envydiel, h.Randle, h.Rimuru, h.Misha, h.Hodgkin],] +
        expand_team([h.Trishea, h.Baden, h.Aurelia, [h.Lavatune, h.Knox, h.Liberta, h.Hodgkin], h.Elijah_Lailah]),
    ),
    "Sky Serpent": deduplicate_and_validate_battle_comps(
        expand_team([h.Orthros, [h.Laios, h.Velufira, h.Lucilla, h.ASolise, h.Leviathan, h.Kregor], [h.Knox, h.Velufira], h.Palmer, h.Liberta]) +
        [   [h.Randle, h.Misha, h.Silas, h.ASolise, h.Hodgkin],] +
        expand_team([[h.ALyca, h.Rimuru, h.Envydiel], h.Randle, [h.Silas, h.Rimuru, h.Ivan], h.Misha, h.Hodgkin]) +
        [   [h.Jerome, h.Randle, h.ALyca, h.Misha, h.ASolise],
            [h.Jerome, h.Sion, h.Villanelle, h.Shuna, h.Knox],],
    ),
    "Nightmare Weaver": deduplicate_and_validate_battle_comps(
        expand_team([[h.Leviathan, h.Adrian_Elyse, h.AEstrilda, h.Lan], [h.Misha, h.Lan], h.Rimuru, h.Sion, [h.Melion, h.Lan]]) +
        [   [h.ALyca, h.Melion, h.Misha, h.Sion, h.Rimuru],] +
        expand_team([h.Envydiel, h.AThoran, h.Lan, [h.Melion, h.Velufira], h.Laios]) +
        [   [h.AThoran, h.Sion, h.Lan, h.Laios, h.Shuna],
            [h.Lan, h.Bronn, h.Sion, h.Palmer, h.Melion],
            [h.Envydiel, h.Laios, h.Raine, h.Lysander, h.Lan],],
    ),
    "Marsha": deduplicate_and_validate_battle_comps(
        expand_team([h.Aurelia, h.Misha, [h.Rimuru, h.Elijah_Lailah], h.Randle, [h.Elijah_Lailah, h.ALyca, h.Velufira]]),
    ),
    "Kane": deduplicate_and_validate_battle_comps(
        [[h.Envydiel, h.Grezhul, h.Elijah_Lailah, h.Lysander, h.Queen],
        expand_team([h.Grezhul, h.Envydiel, [h.Kalene, h.Queen, h.Oden], [h.Elijah_Lailah, h.Queen], [h.Queen, h.Tamrus, h.Elijah_Lailah]]),
        expand_team([[h.Oden, h.Envydiel, h.AShemira, h.Hildwin, h.Oden, h.Naroko], [h.Envydiel, h.Naroko, h.Tamrus, h.AShemira, h.ABaden], [h.Mortas, h.Adrian_Elyse, h.Sion, h.Daemia], [h.Kren, h.Oden, h.Lavatune, h.Elijah_Lailah], [h.Elijah_Lailah, h.Daemia, h.Sion, h.Oden]]),
        expand_team([[h.Palmer, h.Envydiel], [h.AShemira, h.Melion], [h.Lavatune, h.Queen], [h.Envydiel, h.DGwyneth, h.Palmer, h.Sion, h.ABelinda], [h.Daemia, h.Elijah_Lailah]]),
        expand_team([[h.Lysander, h.Skylan, h.Velufira, h.Envydiel, h.Ivan, h.Melion, h.Rem], [h.Velufira, h.Zolrath, h.AThoran, h.Adrian_Elyse, h.Skylan, h.ASolise, h.Lan], [h.Haelia, h.Skylan, h.ASolise, h.DGwyneth, h.Ivan, h.Lan], [h.Rimuru, h.Velufira, h.AThoran, h.Ivan, h.ASolise, h.Zolrath], [h.Zolrath, h.Lan, h.Rimuru, h.Ivan]]),
        expand_team([h.ALucius, [h.Jerome, h.Aurelia], [h.Melion, h.Tamrus, h.Randle], [h.Aurelia, h.Naroko], [h.Randle, h.Queen, h.Tamrus]]),
        expand_team([h.Atheus, [h.AEironn, h.Hildwin, h.ABrutus], h.Nyla, [h.Misha, h.Ivan, h.Emilia, h.Kren], h.Knox]),
        expand_team([h.AAthalia, h.Rosaline, [h.Shuna, h.Lysander, h.AThoran], [h.Gavus, h.Shuna, h.Rimuru], h.Liberta])],
    ),
}
