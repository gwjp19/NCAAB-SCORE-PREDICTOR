#messy_rn_but_im_working 
n = len(data)
mean = sum(data) / n
squared_diff = [(x - mean) ** 2 for x in data]
variance_pop = sum(squared_dif) / n
sd_pop = variance_pop ** 0.5
