from main.py import sim_fga_a, sim_fgaa_a, sim_orb_a, sim_orba_a, sim_tov_a, sim_tovf_a, sim_pf_a, sim_fd_a, sim_srb_a, sim_drba_a
from main.py import sim_fga_b, sim_fgaa_b, sim_orb_b, sim_orba_b, sim_tov_b, sim_tovf_b, sim_pf_b, sim_fd_b, sim_srb_b, sim_drba_b

from stat_stuff.py import orb1_percent, orb2_percent
porb1_results = []
for porb1 in sim_orb1:
  porb1_result = (orb1_percent * ( porb1 + pdrba2)
  porb1_results.append(porb1_result)
#////////////
porb2_results = []
for porb2 in sim_orb2:
  porb2_result = (orb2_percent * ( porb2 + pdrba1)
  porb2_results.append(porb2_result)
#////////////
ptv1_results = []
for ptv1 in sim_tv1:
  ptv1_result = ((1.6 * ptv1)+(1.4 * ptvf2)) / 3
  ptv1_results.append(ptv1_result)
#////////////
ptv2_results = []
for ptv2 in sim_tv2:
  ptv2_result = ((1.6 * ptv2)+(1.4 * ptvf1)) / 3
  ptv2_results.append(ptv2_result)
#////////////
def calculate_fga(team_values, opponent_values):
  fga_results = []
  
  for team_value, opponent_value in zip(team_values, opponent_values):
    fga = (team_value + 1.2 * opponent_value) / 2.2
    fga_results.append(fga)
    
  return fgs_results

pred_fga_a = calculate_fga(sin_fga_a, sim_fgaa_b)
pred_fga_b = calculate_fga(sin_fga_b, sim_fgaa_a)

def calculate_ft(team_values, opponent_values):
  ft_results = []
  
  for team_value, opponent_value in zip(team_values, opponent_values):
    ft = (team_value + 1.2 * opponenet_value) * 0.475
    ft_results.appened(ft)
    
  return ft_results
   
pred_ft_a = calculate_fga(sim_fd_a, sim_pf_b)
pred_ft_b = calculate_fga(sim_fd_b, sim_pf_a)

def calculate_orbp(team_values, opponenet_values):
  orbp_results = []
  for team_value, opponent_value in zip(team_values, opponent_values):
    orba = 


p_possesions1 =[]

for pfg1, pft1, porb1, ptv1 in zip(
  pfg1_results,
  pft1_results,
  porb1_results,
  ptv1_results
):
  p_possesion1 = (random.choice(pfga1_results) + (1.5 * random.choice(pft1_results)) - random.choice(porb1_results) + random.choice(ptv1_results))
  p_possesions1.append(p_possesion1)
#////////////
p_possesions2 =[]

for pfg2, pft2, porb2, ptv2 in zip(
  pfg2_results,
  pft2_results,
  porb2_results,
  ptv2_results
):
  p_possesion2 = (random.choice(pfga2_results) + (1.5 * random.choice(pft2_results)) - random.choice(porb2_results) + random.choice(ptv2_results))
  p_possesions2.append(p_possesion2)


