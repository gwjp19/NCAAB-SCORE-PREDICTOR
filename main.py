from math_stuff import pred_poss_a, pred_poss_b, pred_ppp_a, pred_ppp_b
from sim import team_a_name, team_a, team_b_name, team_b

points_a = []
for pred_poss in pred_poss_a:
  score = pred_poss * pred_ppp_a
  points_a.append(score)

points_b = []
for pred_poss in pred_poss_b:
  score = pred_poss * pred_ppp_b
  points_b.append(score)

def win_percentage(a_values, b_values):
  a_wins = 0
  for a_value, b_value in zip(a_values, b_values):
    if a_value > b_value:
      a_wins += 1
  return a_wins / len(a_values)

pred_wins = win_percentage(points_a, points_b)

print(f"TEAM A: {team_a_name} ({team_a})")
print(f"TEAM B: {team_b_name} ({team_b})")
print(f"WIN PROBABILITY: {pred_wins:.1%}")
