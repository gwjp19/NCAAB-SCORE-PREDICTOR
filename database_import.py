import sqlite3
import requests
import pandas as pd

conn = sqlite3.connect("basketball.db")
cursor = conn.cursor()

cursor.execute("""
  SELECT 
    tgs.game_id,
    tgs.team_id,
    tgs.points,
    tgs.field_goals_attempted,
    tgs.offensive_rebounds,
    tgs.total_rebounds,
    tgs.turnovers,
    tgs.personal_fouls,
    tgs.field_goal_attempts_allowed,
    tgs.offensive_rebounds_allowed,
    tgs.total_rebounds_allowed,
    tgs.turnovers_forced,
    tgs.fouls_drawn,
    tgs.ppp,
    tgs.papp,
    t.team_name
  FROM team_game_stats tgs
  FROM teams t
    ON tgs.team_id = t.id
""")

games = pd.DataFrame(cursor.fetchall(), columns=[
  "game_id",
  "team_id",
  "points",
  "feild_goals_attempted",
  "offensive_rebounds",
  "total_renounds",
  "turnovers",
  "personal_fouls",
  "feild_goal_attempts_allowed",
  "offensive_rebound_allowed",
  "total_rebounds_allowed",
  "turnovers_forced",
  "fouls_drawn",
  "ppp",
  "papp"
  "team_name"
])
