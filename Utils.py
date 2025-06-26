from itertools import product, combinations, islice
from functools import lru_cache
from typing import List, Union
from Hero import Hero

# Tune these constants
priority_order = [2, 3, 1, 4, 5, 6] # 1-based
POSITION_WEIGHT = 10
BLANK_SLOT_PENALTY = 1000

global_ranking = {}

def initialize():
    global global_ranking
    global_ranking = {}

@lru_cache(maxsize=None)
def cached_score_team(team_tuple):
    global global_ranking
    team = list(team_tuple)
    score = 0
    for hero in team:
        if hero == Hero.BLANK:
            score -= BLANK_SLOT_PENALTY
        else:
            score += global_ranking.get(hero, -BLANK_SLOT_PENALTY)
    return score

def rank_heroes(heroes: List[str]) -> dict:
    return {hero: len(heroes) - i for i, hero in enumerate(heroes)}

def generate_partial_blank_variants(team: List[str], max_blanks: int = 2) -> List[List[str]]:
    variants = [team[:]]
    for blanks_count in range(1, max_blanks + 1):
        for blank_positions in combinations(range(len(team)), blanks_count):
            variant = team[:]
            for pos in blank_positions:
                variant[pos] = Hero.BLANK
            variants.append(variant)
    return variants

def is_valid_combination(combo: List[List[str]]) -> bool:
    used = set()
    for team in combo:
        for hero in team:
            if hero == Hero.BLANK:
                continue
            if hero in used:
                return False
            used.add(hero)
    return True

def chunked_iterable(iterable, size):
    it = iter(iterable)
    while True:
        chunk = list(islice(it, size))
        if not chunk:
            break
        yield chunk

def evaluate_combinations(args):
    combo_indexes_chunk, filtered_comps_per_battle = args
    local_best_score = float("inf")
    local_best_combo = None
    local_best_indexes = None
    for combo_indexes in combo_indexes_chunk:
        combo = [filtered_comps_per_battle[b][idx] for b, idx in enumerate(combo_indexes)]
        if not is_valid_combination(combo):
            continue
        score = sum(
            cached_score_team(tuple(combo[b])) + combo_indexes[b] * POSITION_WEIGHT
            for b in range(len(combo))
        )
        if score < local_best_score:
            local_best_score = score
            local_best_combo = combo
            local_best_indexes = combo_indexes
    return local_best_score, local_best_combo, local_best_indexes

def find_best_team_set(my_heroes: List[Hero], recommended_comps_per_battle: List[List[List[Hero]]]) -> List[List[Hero]]:
    global global_ranking
    global_ranking = rank_heroes(my_heroes)

    print(f"Battle priorities: {priority_order}")
    num_battles = len(recommended_comps_per_battle)
    assigned_teams = [None] * num_battles
    used_heroes = set()

    for battle_num in priority_order:
        battle_idx = battle_num - 1
        battle_comps = recommended_comps_per_battle[battle_idx]
        filtered = [
            team for team in battle_comps
            if all(hero == Hero.BLANK or (hero in global_ranking and hero not in used_heroes) for hero in team)
            and len(set(hero for hero in team if hero != Hero.BLANK)) == len([hero for hero in team if hero != Hero.BLANK])
        ]

        if not filtered:
            print(f"Battle {battle_num} has no valid teams. Adding fallback (BLANK) teams.")
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
        for team in filtered:
            if any(h in used_heroes for h in team if h != Hero.BLANK):
                continue
            score = sum(global_ranking.get(hero, -BLANK_SLOT_PENALTY) if hero != Hero.BLANK else -BLANK_SLOT_PENALTY for hero in team)
            if score > best_score:
                best_score = score
                best_team = team

        assigned_teams[battle_idx] = best_team
        if best_team is not None:
            used_heroes.update(h for h in best_team if h != Hero.BLANK)

    print("\n=== Priority-Based Team Breakdown ===")
    for i, team in enumerate(assigned_teams, start=1):
        if team is None:
            print(f"Battle {i}: No team assigned.")
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
        print(f"Battle {i}: {', '.join(printable_team)} -> Score: {score}")

    return assigned_teams

def expand_team(template: List[Union[str, List[str]]]) -> List[List[str]]:
    expanded_slots = [
        [slot] if isinstance(slot, str) else slot
        for slot in template
    ]
    return [list(team) for team in product(*expanded_slots)]

def deduplicate_and_validate_battle_comps(battle_comps: List[List[str]]) -> List[List[str]]:
    seen = set()
    unique = []
    for team in battle_comps:
        if len(team) != 5:
            print("\n\n\n BAD TEAM " + str(team) + "\n\n")
        if len(team) != len(set(team)):
            continue  # Invalid: duplicate hero in team
        key = tuple(team)
        if key not in seen:
            seen.add(key)
            unique.append(team)
    return unique

def convert_nested_hero_lists_to_enum(data):
    if isinstance(data, str):
        return Hero[data.replace('-', '_').replace(' ', '_').replace('.', '')]
    elif isinstance(data, list):
        return [convert_nested_hero_lists_to_enum(x) for x in data]
    else:
        return data

def FindBest(comps, my_heroes):
    initialize()

    comps = convert_nested_hero_lists_to_enum(comps)

    expanded_recommended_comps_per_battle = []
    for battle_teams in comps:
        new_teams = []
        for team in battle_teams:
            partial_variants = generate_partial_blank_variants(team, max_blanks=5)
            new_teams.extend(partial_variants)
        filtered = deduplicate_and_validate_battle_comps(new_teams)
        expanded_recommended_comps_per_battle.append(filtered)

    best_set = find_best_team_set(my_heroes, expanded_recommended_comps_per_battle)
