from main.py import pfga1, sim_fga1, pfga2, sim_fga2, pfd1, sim_fd1, pfd2, sim_fd1, pfc1, sim_pfc1, pfc2, sim_pfc2, porb1, sim_orb1, porb2, sim_orb2, 
fga1_results = []
for pfga1 in sim_fga1:
  fga1_result = ( pfga1 + (1.2 * pfgaa2) / 2.2)
  fga1_results.append(fga1_result)
#////////////
fga2_results = []
for pfga2 in sim_fga2:
  fga2_result = ( pfga2 + (1.2 * pfgaa1) / 2.2)
  fga2_results.append(fga2_result)
#////////////
pft1_results = []
for pfd1 in sim_fd1:
  pft1_result = ((( pfd1 + (1.2 * pfc2)) / 2) * .44)
  pft1_results.append(pft1_result)
#////////////
pft2_results = []
for pfd2 in sim_fd2:
  pft2_result = ((( pfd2 + (1.2 * pfc1)) / 2) * .44)
  pft2_results.append(pft2_result)
#////////////
from stat_stuff.py import 
porb1_results = []
for porb1 in sim_orb1:
  porb1_result = 
