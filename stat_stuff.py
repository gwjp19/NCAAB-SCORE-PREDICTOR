from Data_inputs import fga1_list
n = len(fga1_list)
mean = sum(fga1_list) / n
squared_diff = [(x-mean) ** 2 for x in fga1_list]
variance_pop = sum(squared_diff) / n
sd_pop = variance_pop ** 0.5
#////////////////
from Data_inputs import fgaa1_list
n2 = len(fgaa1_list)
mean2 = sum(fgaa1_list) / n2
squared_diff2 = [(x-mean2) ** 2 for x in fgaa1_list]
variance_pop2 = sum(squared_diff2) / n2
sd_pop2 = variance_pop2 ** 0.5
#////////////////
