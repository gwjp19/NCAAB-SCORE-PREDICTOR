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
tv1mean = sum(tv1_list) / n
tv1_squared_diff = [(x-tv1mean) ** 2 for x in tv1_list]
tv1_variance_pop = sum(tv1_squared_diff) / tv1n
tv1_sd_pop = tv1_variance_pop ** 0.5
#////////////////
from Data_inputs import tvf1_list
tvf1n = len(tvf1_list)
tvf1mean = sum(tvf1_list) / n
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
