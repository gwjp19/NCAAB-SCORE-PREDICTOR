from stat_stuff import game_stats, stats
from database_import import team_data, games

def select_teams():
  team_a = int(input("Team A ID:"))
  team_b = int(input("Team B ID:"))

  team_a_name = team_data.loc[
    team_data["team_id"] == team_a, "team_name"
  ].iloc[0]

  team_b_name = team_data.loc[
    team_data["team_id"] == team_b, "team_name"
  ].iloc[0]

  return team_a, team_b, stats[team_a], stats[team_b], team_a_name, team_b_name




