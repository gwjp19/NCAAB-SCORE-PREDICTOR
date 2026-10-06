from main.py import sim_fga_a, sim_fgaa_a, sim_orb_a, sim_orba_a, sim_tov_a, sim_tovf_a, sim_pf_a, sim_fd_a, sim_srb_a, sim_drba_a, sim_orbp_a
from main.py import sim_fga_b, sim_fgaa_b, sim_orb_b, sim_orba_b, sim_tov_b, sim_tovf_b, sim_pf_b, sim_fd_b, sim_srb_b, sim_drba_b, sim_orbp_a

def calculate_fga(team_values, opponent_values):
  fga_results = []
  
  for team_value, opponent_value in zip(team_values, opponent_values):
    fga = (team_value + 1.2 * opponent_value) / 2.2
    fga_results.append(fga)
    
  return fgs_results

def calculate_ft(team_values, opponent_values):
  ft_results = []
  
  for team_value, opponent_value in zip(team_values, opponent_values):
    ft = (team_value + 1.2 * opponenet_value) * 1.1
    ft_results.appened(ft)
    
  return ft_results

def calculate_rb(first_values, second_values, third_values):
  rb_results = []
  for first_value, second_value, third_value in zip(first_values, second_values, third_values):
    rb = third_value * (first_value + second_value)
    rb_results.append(rb)
  return rb_results

def calculate_tov(team_values, opponent_values):
  tov_results = []
  
  for team_value, opponenet_value in zip(team_values, opponent_values):
    tov = ((1.6 * team_value) + (1.4 * opponent_value)) / 3
    tov_results.append(tov)
  return tov_results

pred_tov_a = calculate_tov(sim_tov_a, sim_tovf_b)
pred_tov_b = calculate_tov(sim_tov_b, sim_tovf_a)

pred_fga_a = calculate_fga(sim_fga_a, sim_fgaa_b)
pred_fga_b = calculate_fga(sim_fga_b, sim_fgaa_a)

pred_ft_a = calculate_fga(sim_fd_a, sim_pf_b)
pred_ft_b = calculate_fga(sim_fd_b, sim_pf_a)

pred_orb_a = calculate_rb(sim_orb_a, sim_drba_a, sim_orbp_a)
pred_orb_b = calculate_rb(sim_orb_b, sim_drba_b, sim_orbp_b)

def calculate_poss(first_values, second_values, third_values, fourth_values):
  possesions = []
  for first_value, second_value, third_value, fourth_value in zip(first_values, second_values, third_values, fourth_values):
    possesion = (random.choice(first_value) + (0.475 * random.choice(second_value)) - random.choice(third_value) + random.choice(fourth_value))
    possesions.append(possesion)
  return possesions

pred_poss_a = calculate_poss(pred_fga_a, pred_ft_a, pred_orb_a, pred_tov_a)
pred_poss_b = calculate_poss(pred_fga_b, pred_ft_b, pred_orb_b, pred_tov_b)
