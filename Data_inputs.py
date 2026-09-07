name1 = input("Team Name:")
fga1_list = []
for i in range(5):
  fga1 = float(input(name1+" Fga for the last five games:"))
  fga1_list.append(fga1)
#/////////              
fgaa1_list = []
for i in range(5):
  fgaa1 = float(input(name1+" Fga Allowed for the last five games:"))
  fgaa1_list.append(fgaa1)
#/////////
fd1_list = []
for i in range(5):
  fd1 = float(input(name1+" Fouls drawn for the last five games:"))
  fd1_list.append(fd1)
#/////////
fc1_list = []
for i in range(5):
  fc1 = float(input(name1+" Fouls commited for the last five games:"))
  fc1_list.append(fc1)
#//////////         
tv1_list = []
for i in range(5):
  tv1 = float(input(name1+" Turnovers for the last five games:"))
  tv1_list.append(tv1)
#//////////  
tvf1_list = []
for i in range(5):
  tvf1 = float(input(name1+" Turnovers forced for the last five games:"))
  tvf1_list.append(tvf1)
#////////// 
orb1_list = []
for i in range(5):
  orb1 = float(input("Offensive rebounds for the last five games:"))
  orb1_list.append(orb1)
#//////////     
drb1_list = []
for i in range(5):
  drb1 = float(input("Defensive rebounds for the last five games:"))
  drb1_list.append(drb1)
#//////////
drba1_list = []
for i in range(5):
  drba1 = float(input("Defensive rebounds allowed for the last five games:"))
  drba1_list.append(drba1)
#//////////
orba1_list = []
for i in range(5):
  orba1 = float(input("Offensive rebounds allowed for the last five games:"))
  orba1_list.append(orba1)
#//////////

print(fga1_list)

