from math_stuff import pred_poss_a, pred_poss_b, pred_ppp_a, pred_ppp_b

def calculate_score(poss_values, score_values):
  score_results = []
  for poss_value, socre_value in zip(poss_values, score_values):
    score = poss_value * score_value
    score_results.append(score)
  return score_results

pred_score_a = calculate_score(pred_poss_a, pred_ppp_a)
pred_score_b = calculate_score(pred_poss_b, pred_ppp_b)

def win_percentage(a_values, b_values):
  a_wins = 0
  for a_value, b_value in zip(a_values, b_values):
    if a_value > b_value:
      a_wins += 1
  return a_wins / len(a_values)

pred_wins = win_percentage(pred_score_a, pred_score_b)

print(f"TEAM A: {team_a_name} ({team_a})")
print(f"TEAM B: {team_b_name} ({team_b})")
print(f"WIN PROBABILITY: {pred_wins:.1%}")
