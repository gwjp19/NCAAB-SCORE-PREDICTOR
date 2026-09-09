from Data_inputs import fga1_list
n = len(fga1_list)
mean = sum(fga1_list) / n
squared_diff = [(x-mean) ** 2 for x in fga1_list]
variance_pop = sum(squared_diff) / n
sd_pop = variance_pop ** 0.5
#////////////////
from Data_inputs import fgaa1_list
fgaa1n = len(fgaa1_list)
fgaa1mean = sum(fgaa1_list) / fgaa1n
fgaa1_squared_diff = [(x-fgaa1mean) ** 2 for x in fgaa1_list]
fgaa1_variance_pop = sum(fgaa1_squared_diff) / fgaa1n
fgaa1_sd_pop = fgaa1_variance_pop ** 0.5
#////////////////
from Data_inputs import fd1_list
fd1n = len(fd1_list)
fd1mean = sum(fd1_list) / fd1n
fd1_squared_diff = [(x-fd1mean) ** 2 for x in fd1_list]
fd1_variance_pop = sum(fd1_squared_diff) / fd1n
fd1_sd_pop = fd1_variance_pop ** 0.5
#////////////////
from Data_inputs import fc1_list
fc1n = len(fc1_list)
fc1mean = sum(fc1_list) / fc1n
fc1_squared_diff = [(x-fc1mean) ** 2 for x in fc1_list]
fc1_variance_pop = sum(fc1_squared_diff) / fc1n
fc1_sd_pop = fc1_variance_pop ** 0.5
#////////////////
from Data_inputs import tv1_list
tv1n = len(tv1_list)
tv1mean = sum(tv1_list) / tv1n
tv1_squared_diff = [(x-tv1mean) ** 2 for x in tv1_list]
tv1_variance_pop = sum(tv1_squared_diff) / tv1n
tv1_sd_pop = tv1_variance_pop ** 0.5
#////////////////
from Data_inputs import tvf1_list
tvf1n = len(tvf1_list)
tvf1mean = sum(tvf1_list) / tvf1n
tvf1_squared_diff = [(x-tvf1mean) ** 2 for x in tvf1_list]
tvf1_variance_pop = sum(tvf1_squared_diff) / tvf1n
tvf1_sd_pop = tvf1_variance_pop ** 0.5
#////////////////
from Data_inputs import orb1_list
orb1n = len(orb1_list)
orb1mean = sum(orb1_list) / orb1n
orb1_squared_diff = [(x-orb1mean) ** 2 for x in orb1_list]
orb1_variance_pop = sum(orb1_squared_diff) / orb1n
orb1_sd_pop = orb1_variance_pop ** 0.5
#////////////////
from Data_inputs import drb1_list
drb1n = len(drb1_list)
drb1mean = sum(drb1_list) / drb1n
drb1_squared_diff = [(x-drb1mean) ** 2 for x in drb1_list]
drb1_variance_pop = sum(drb1_squared_diff) / drb1n
drb1_sd_pop = drb1_variance_pop ** 0.5
#////////////////
from Data_inputs import drba1_list
drba1n = len(drba1_list)
drba1mean = sum(drba1_list) / drba1n
drba1_squared_diff = [(x-drba1mean) ** 2 for x in drba1_list]
drba1_variance_pop = sum(drba1_squared_diff) / drba1n
drba1_sd_pop = drba1_variance_pop ** 0.5
#////////////////
from Data_inputs import orba1_list
orba1n = len(orba1_list)
orba1mean = sum(orba1_list) / orba1n
orba1_squared_diff = [(x-orba1mean) ** 2 for x in orba1_list]
orba1_variance_pop = sum(orba1_squared_diff) / orba1n
orba1_sd_pop = orba1_variance_pop ** 0.5
#////////////////
orb1_percent = orb1mean / (orb1mean + drba1mean)
#////////////////
drb1_percent = drb1mean / (drb1mean + orba1mean)
#////////////////

from Data_inputs import fga2_list
n2 = len(fga1_list)
mean2 = sum(fga1_list) / n2
squared_diff2 = [(x-mean2) ** 2 for x in fga2_list]
variance_pop2 = sum(squared_diff2) / n2
sd_pop2 = variance_pop2 ** 0.5
#////////////////
from Data_inputs import fgaa2_list
fgaa2n = len(fgaa2_list)
fgaa2mean = sum(fgaa2_list) / fgaa2n
fgaa2_squared_diff = [(x-fgaa2mean) ** 2 for x in fgaa2_list]
fgaa2_variance_pop = sum(fgaa2_squared_diff) / fgaa2n
fgaa2_sd_pop = fgaa2_variance_pop ** 0.5
#////////////////
from Data_inputs import fd2_list
fd2n = len(fd2_list)
fd2mean = sum(fd2_list) / fd2n
fd2_squared_diff = [(x-fd2mean) ** 2 for x in fd2_list]
fd2_variance_pop = sum(fd2_squared_diff) / fd2n
fd2_sd_pop = fd2_variance_pop ** 0.5
#////////////////
from Data_inputs import fc2_list
fc2n = len(fc2_list)
fc2mean = sum(fc2_list) / fc2n
fc2_squared_diff = [(x-fc2mean) ** 2 for x in fc2_list]
fc2_variance_pop = sum(fc2_squared_diff) / fc2n
fc2_sd_pop = fc2_variance_pop ** 0.5
#////////////////
from Data_inputs import tv2_list
tv2n = len(tv2_list)
tv2mean = sum(tv2_list) / tv2n
tv2_squared_diff = [(x-tv2mean) ** 2 for x in tv2_list]
tv2_variance_pop = sum(tv2_squared_diff) / tv2n
tv2_sd_pop = tv2_variance_pop ** 0.5
#////////////////
from Data_inputs import tvf2_list
tvf2n = len(tvf2_list)
tvf2mean = sum(tvf2_list) / tvf2n
tvf2_squared_diff = [(x-tvf2mean) ** 2 for x in tvf2_list]
tvf2_variance_pop = sum(tvf2_squared_diff) / tvf2n
tvf2_sd_pop = tvf2_variance_pop ** 0.5
#////////////////
from Data_inputs import orb2_list
orb2n = len(orb2_list)
orb2mean = sum(orb2_list) / orb2n
orb2_squared_diff = [(x-orb2mean) ** 2 for x in orb2_list]
orb2_variance_pop = sum(orb2_squared_diff) / orb2n
orb2_sd_pop = orb2_variance_pop ** 0.5
#////////////////
from Data_inputs import drb2_list
drb2n = len(drb2_list)
drb2mean = sum(drb2_list) / drb2n
drb2_squared_diff = [(x-drb2mean) ** 2 for x in drb2_list]
drb2_variance_pop = sum(drb2_squared_diff) / drb2n
drb2_sd_pop = drb2_variance_pop ** 0.5
#////////////////
from Data_inputs import drba2_list
drba2n = len(drba2_list)
drba2mean = sum(drba2_list) / drba2n
drba2_squared_diff = [(x-drba2mean) ** 2 for x in drba2_list]
drba2_variance_pop = sum(drba2_squared_diff) / drba2n
drba2_sd_pop = drba2_variance_pop ** 0.5
#////////////////
from Data_inputs import orba2_list
orba2n = len(orba2_list)
orba2mean = sum(orba2_list) / orba2n
orba2_squared_diff = [(x-orba2mean) ** 2 for x in orba2_list]
orba2_variance_pop = sum(orba2_squared_diff) / orba2n
orba2_sd_pop = orba2_variance_pop ** 0.5
#////////////////
orb2_percent = orb2mean / (orb2mean + drba2mean)
#////////////////
drb2_percent = drb2mean / (drb2mean + orba2mean)
#////////////////
