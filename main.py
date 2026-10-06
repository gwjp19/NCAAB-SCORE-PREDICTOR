from team_selection.py import select_teams, selected_games, 

def simulated_stats(stat_data):
  values = []
  
  for _ in range(n):
    z = np.random.normal(0, 1)
    
    if -3 <= z <= 3:
      value = stat_data["mean"] + stat_data["sd"] * z
      values.append(value)
    
  return values

sim_fga_a = simulated_stats(team_a_stats["fga"])
sim_fgaa_a = simulated_stats(team_a_stats["fgaa"])
sim_orb_a = simulated_stats(team_a_stats["orb"])
sim_orba_a = simulated_stats(team_a_stats["orba"])
sim_tov_a = simulated_stats(team_a_stats["tov"])
sim_tovf_a = simulated_stats(team_a_stats["tovf"])
sim_pf_a = simulated_stats(team_a_stats["pf"])
sim_fd_a = simulated_stats(team_a_stats["fd"])
sim_drb_a = simulated_stats(team_a_stats["drb"])
sim_drba_a = simulated_stats(team_a_stats["drba"])


sim_fga_b = simulated_stats(team_b_stats["fga"])
sim_fgaa_b = simulated_stats(team_b_stats["fgaa"])
sim_orb_b = simulated_stats(team_b_stats["orb"])
sim_orba_b = simulated_stats(team_b_stats["orba"])
sim_tov_b = simulated_stats(team_b_stats["tov"])
sim_tovf_b = simulated_stats(team_b_stats["tovf"])
sim_pf_b = simulated_stats(team_b_stats["pf"])
sim_fd_b = simulated_stats(team_b_stats["fd"])
sim_drb_b = simulated_stats(team_b_stats["drb"])
sim_drba_b = simulated_stats(team_b_stats["drba"])
