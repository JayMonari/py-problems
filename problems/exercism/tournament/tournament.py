from typing import Dict, List


WIDTH = 30
ROW_WIDTH = 3
TeamResult = Dict[str, Dict[str, int]]


def map_scores(rows: List[str]) -> TeamResult:
    teams: TeamResult = {}
    for row in rows:
        [team1, team2, result] = row.split(';')
        teams.setdefault(team1, {'W': 0, 'D': 0, 'L': 0})
        teams.setdefault(team2, {'W': 0, 'D': 0, 'L': 0})
        if result == 'win':
            teams[team1]['W'] += 1
            teams[team2]['L'] += 1
        elif result == 'loss':
            teams[team2]['W'] += 1
            teams[team1]['L'] += 1
        else:
            teams[team2]['D'] += 1
            teams[team1]['D'] += 1
    return teams


def format_table_row(team: str, results: List[str]) -> str:
    row = [f"{team.ljust(WIDTH, ' ')}"]
    row.extend([f"|{res.rjust(ROW_WIDTH, ' ')}" for res in results])
    return ' '.join(row)


def create_results(teams: TeamResult) -> List[str]:
    result_rows: List[str] = []
    for team, results in teams.items():
        [(_, w_cnt), (_, d_cnt), (_, l_cnt)] = results.items()
        matches = sum(results.values())
        points = (w_cnt * 3) + d_cnt
        result_rows.append(format_table_row(
            team, list(map(lambda x: str(x), [matches, w_cnt, d_cnt, l_cnt, points]))))
    return sorted(result_rows, key=lambda s: (-int(s[-1]), s[0]))


def tally(rows: List[str]) -> List[str]:
    table = [format_table_row("Team", ["MP", "W", "D", "L", "P"])]
    teams: TeamResult = map_scores(rows)
    result_rows = create_results(teams)
    table.extend(result_rows)
    return table
