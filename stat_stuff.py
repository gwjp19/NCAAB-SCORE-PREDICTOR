from database_imports.py import games, team_data
games["drb"] = (
  games["total_rebounds"] - games["offensive_rebounds"]
)
games["drba"] = (
  games["total_rebounds_allowed"] - games["offensive_rebounds_allowed"]
)
game_stats = games.groupby(["team_id"]).agg(
  fga = ("feild_goals_attempted", list),
  orb = ("offensive_rebounds", list),
  tb = ("total_rebounds", list),
  tov = ("turnovers", list),
  pf = ("personal_fouls", list),
  fgaa = ("feild_goal_attempts_allowed", list),
  orba = ("offensive_rebounds_allowed", list),
  tba = ("total_rebounds_allowed", list),
  tovf = ("turnovers_forced", list),
  fd = ("fouls_drawn", list)
  drb = ("drb", list),
  drba = ("drba", list)
).reset_index()

def get_stats(data):
  n = len(data)
  mean = sum(data)/ n 
  squared_diff = [(x-mean) ** 2 for x in data]
  variance = sum(squared_diff) / n
  sd = variance ** 0.5

  return mean, variance, sd
