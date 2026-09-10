from main.py import pfga1, sim_fga1, pfga2, sim_fga2, pfd1, sim_fd1, pfd2, sim_fd1, ptv1, sim_tv1, ptv2, sim_tv2, ptvf1, sim_tvf1, ptvf2, sim_tvf2
from main.py import pfc1, sim_pfc1, pfc2, sim_pfc2, porb1, sim_orb1, porb2, sim_orb2, pdrb1, sim_drb1, pdrb2, sim_drb2, porba1, sim_orba1, porba2, sim_orba2. pdrba1, sim_drba1, pdrba1, sim_drba2
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


