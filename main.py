from team_selection.py import select_teams, selected_games
  z=np.random.normal(0,1)
  if -3 <= z <= 3:
    z_values.append(z)
#///////////
sim_fga1 =[]
for z in z_values:
  pfga1 = team_a_stats["fga"]["mean"] + (team_a_stats["fga"]["sd"] * z)
  sim_fga1.append(pfga1)
n=len(sim_fga1)
#//////////
sim_fgaa1 =[]
for z in z_values:
  pfgaa1 = fgaa1mean + (fgaa1_sd_pop * z)
  sim_fgaa1.append(pfgaa1)
fgaa1n=len(sim_fgaa1)
#///////////
sim_fd1 =[]
for z in z_values:
  pfd1 = fd1mean + (fd1_sd_pop * z)
  sim_fd1.append(pfd1)
fd1n=len(sim_fd1)
#///////////
sim_fc1 =[]
for z in z_values:
  pfc1 = fc1mean + (fc1_sd_pop * z)
  sim_fc1.append(pfc1)
fc1n=len(sim_fc1)
#///////////
sim_tv1 =[]
for z in z_values:
  ptv1 = tv1mean + (tv1_sd_pop * z)
  sim_tv1.append(ptv1)
tv1n=len(sim_tv1)
#///////////
sim_tvf1 =[]
for z in z_values:
  ptvf1 = tvf1mean + (tvf1_sd_pop * z)
  sim_tvf1.append(ptvf1)
tvf1n=len(sim_tvf1)
#///////////
sim_orb1 =[]
for z in z_values:
  porb1 = orb1mean + (orb1_sd_pop * z)
  sim_orb1.append(porb1)
orb1n=len(sim_orb1)
#///////////
sim_orba1 =[]
for z in z_values:
  porba1 = orba1mean + (orba1_sd_pop * z)
  sim_orba1.append(porba1)
orba1n=len(sim_orba1)
#///////////
sim_drb1 =[]
for z in z_values:
  pdrb1 = drb1mean + (drb1_sd_pop * z)
  sim_drb1.append(drb1)
drb1n=len(sim_drb1)
#///////////
sim_drba1 =[]
for z in z_values:
  pdrba1 = drba1mean + (drba1_sd_pop * z)
  sim_drba1.append(drba1)
drba1n=len(sim_drba1)
#///////////
#TEAM 2 //////////////
#///////////
sim_fga2 =[]
for z in z_values:
  pfga2 = mean + (sd_pop2 * z)
  sim_fga2.append(pfga2)
n2=len(sim_fga2)
#//////////
sim_fgaa2 =[]
for z in z_values:
  pfgaa2 = fgaa2mean + (fgaa2_sd_pop * z)
  sim_fgaa2.append(pfgaa2)
fgaa2n=len(sim_fgaa2)
#///////////
sim_fd2 =[]
for z in z_values:
  pfd2 = fd2mean + (fd2_sd_pop * z)
  sim_fd2.append(pfd2)
fd2n=len(sim_fd2)
#///////////
sim_fc2 =[]
for z in z_values:
  pfc2 = fc2mean + (fc2_sd_pop * z)
  sim_fc2.append(pfc2)
fc2n=len(sim_fc2)
#///////////
sim_tv2 =[]
for z in z_values:
  ptv2 = tv2mean + (tv2_sd_pop * z)
  sim_tv2.append(ptv2)
tv2n=len(sim_tv2)
#///////////
sim_tvf2 =[]
for z in z_values:
  ptvf2 = tvf2mean + (tvf2_sd_pop * z)
  sim_tvf2.append(ptvf2)
tvf2n=len(sim_tvf2)
#///////////
sim_orb2 =[]
for z in z_values:
  porb2 = orb2mean + (orb2_sd_pop * z)
  sim_orb2.append(porb2)
orb2n=len(sim_orb2)
#///////////
sim_orba2 =[]
for z in z_values:
  porba2 = orba2mean + (orba2_sd_pop * z)
  sim_orba2.append(porba2)
orba2n=len(sim_orba2)
#///////////
sim_drb2 =[]
for z in z_values:
  pdrb2 = drb2mean + (drb2_sd_pop * z)
  sim_drb2.append(drb2)
drb2n=len(sim_drb2)
#///////////
sim_drba2 =[]
for z in z_values:
  pdrba2 = drba2mean + (drba2_sd_pop * z)
  sim_drba2.append(drba2)
drba2n=len(sim_drba2)
#///////////





