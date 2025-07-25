from itertools import product, combinations
from functools import lru_cache
from typing import List, Union
from Hero import Hero
from Comp import *
from MyHeroes import my_heroes

# Tune these constants
POSITION_WEIGHT = 1 # len(my_heroes) / 2
BLANK_SLOT_PENALTY = 10000


def initialize():
    pass

@lru_cache(maxsize=None)
def cached_score_team(team_tuple):
    team = list(team_tuple)
    score = 0
    for hero in team:
        if hero == Hero.BLANK:
            score -= BLANK_SLOT_PENALTY
        else:
            score += my_heroes.get(hero, -BLANK_SLOT_PENALTY)
    return score

def generate_partial_blank_variants(team: List[Hero], max_blanks: int = 2) -> List[List[Hero]]:
    variants = [team[:]]
    for blanks_count in range(1, max_blanks + 1):
        for blank_positions in combinations(range(len(team)), blanks_count):
            variant = team[:]
            for pos in blank_positions:
                variant[pos] = Hero.BLANK
            variants.append(variant)
    return variants

def find_best_team_set(recommended_comps_per_battle: List[List[List[Hero]]], priority_order: List[int]) -> List[List[Hero]]:
    num_battles = len(recommended_comps_per_battle)
    assigned_teams = [None] * num_battles
    used_heroes = set()

    for battle_num in priority_order:
        battle_idx = battle_num - 1
        battle_comps = recommended_comps_per_battle[battle_idx]

        filtered = [
            team for team in battle_comps
            if all(hero == Hero.BLANK or (hero in my_heroes and hero not in used_heroes) for hero in team)
            and len(set(hero for hero in team if hero != Hero.BLANK)) == len([hero for hero in team if hero != Hero.BLANK])
        ]

        if not filtered:
            blank_variants = []
            for team in battle_comps:
                try:
                    blank_variants.extend(generate_partial_blank_variants(team, max_blanks=0))
                except Exception as e:
                    print(f"Error processing team {team}: {e}")
            blank_variants = deduplicate_and_validate_battle_comps(blank_variants)
            if not blank_variants:
                blank_variants = [[Hero.BLANK] * 5]
            filtered = blank_variants

        best_team = None
        best_score = float('-inf')
        for idx, team in enumerate(filtered):
            if any(h in used_heroes for h in team if h != Hero.BLANK):
                continue


            hero_score = sum(my_heroes.get(hero, -BLANK_SLOT_PENALTY) if hero != Hero.BLANK else -BLANK_SLOT_PENALTY for hero in team)
            score = hero_score - idx * POSITION_WEIGHT
            if score > best_score:
                best_score = score
                best_team = team

        assigned_teams[battle_idx] = best_team
        if best_team is not None:
            used_heroes.update(h for h in best_team if h != Hero.BLANK)

    return assigned_teams

def print_result(assigned_teams: List[List[Hero]], battles: List[Comp], priority_order: List[int]):

    formatted_teams = []
    for i, team in enumerate(assigned_teams, start=1):
        if team is None:
            formatted_teams.append((battles[i-1].mode, battles[i-1].name, None, None))
            continue
        score = cached_score_team(tuple(team))
        printable_team = []
        names_seen = set()
        for hero in team:
            if hero == Hero.BLANK:
                printable_team.append("BLANK")
                continue
            name = hero.name
            if name in names_seen:
                name = f"{name}*"
            names_seen.add(name)
            if hero not in my_heroes:
                printable_team.append(f"BLANK({name})")
            else:
                printable_team.append(name)
        team_str = ', '.join(printable_team)
        score = cached_score_team(tuple(team))
        formatted_teams.append((battles[i-1].mode, battles[i-1].name, team_str, score))

    team_name_length = max(len(f"{name}") for mode, name, team, score in formatted_teams if team is not None)
    team_comp_length = max(len(team) for mode, name, team, score in formatted_teams if team is not None)

    print(f"\n=== {formatted_teams[0][0]} ===")
    print(f"Battle priorities: {priority_order}")
    for mode, name, team_str, score in formatted_teams:
        label = f"{name}"
        if team_str is None:
            print(f"{label:<{team_name_length}}: No team assigned.")
        else:
            print(f"{label:<{team_name_length}}: {team_str:<{team_comp_length}} -> Score: {score}")

def expand_team(template: List[Union[str, Hero, List[Union[str, Hero]]]]) -> List[List[Hero]]:
    expanded_slots = []
    for slot in template:
        if isinstance(slot, list):
            heroes = [Hero[s.name] for s in slot]
        else:
            heroes = [Hero[slot.name]]
        expanded_slots.append(heroes)
    return [list(team) for team in product(*expanded_slots)]

def deduplicate_and_validate_battle_comps(battle_comps: List[List[Hero]]) -> List[List[Hero]]:
    seen = set()
    unique = []
    for team in battle_comps:
        if not isinstance(team, list) or len(team) != 5:
            print("\n\n\n BAD TEAM " + ', '.join(h.name if isinstance(h, Hero) else str(h) for h in team) + "\n\n")
            continue
        try:
            names = [h.name if isinstance(h, Hero) else str(h) for h in team]
            if len(names) != len(set(names)):
                continue
            key = tuple(names)
            if key not in seen:
                seen.add(key)
                unique.append(team)
        except TypeError:
            continue
    return unique

def convert_nested_hero_lists_to_enum(data):
    if isinstance(data, str):
        return Hero[data.replace('-', '_').replace(' ', '_').replace('.', '')]
    elif isinstance(data, list):
        return [convert_nested_hero_lists_to_enum(x) for x in data]
    elif isinstance(data, Comp):
        return convert_nested_hero_lists_to_enum(data.comps)
    else:
        return data

def FindBest(comp_list: CompList):
    initialize()

    comps = convert_nested_hero_lists_to_enum(comp_list.battles)

    expanded_recommended_comps_per_battle = []
    for battle_teams in comps:
        new_teams = []
        for team in battle_teams:
            partial_variants = generate_partial_blank_variants(team, max_blanks=0)
            new_teams.extend(partial_variants)
        filtered = deduplicate_and_validate_battle_comps(new_teams)
        expanded_recommended_comps_per_battle.append(filtered)

    best_set = find_best_team_set(expanded_recommended_comps_per_battle, comp_list.priority_order)
    print_result(best_set, comp_list.battles, comp_list.priority_order)
