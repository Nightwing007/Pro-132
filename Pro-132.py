import csv
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

rows = []

with open("Pro-131.csv","r") as f :
  csvR = csv.reader(f)
  for row in csvR :
    rows.append(row)

header = rows[0]
planetData = rows[1:]

header[0] = "Index"

temp_list = list(planetData)

for data in planetData :
  planetMass = data[3]
  if planetMass.lower() == "unknown":
    planetData.remove(data)
    continue
  planetRadius = data[4]
  if planetRadius.lower() == "unknown":
    planetData.remove(data)
    continue

for data in planetData :
    mass = float(data[3]) * 1.989e+30
    data[3] = mass
    radius = float(data[4]) * 6.957e+8
    radius[4] = radius

plM = []
plG = []
plR = []


for data in planetData :
  plM.append(data[3])
  plG.append(data[5])
  plR.append(data[4])

plt.figure(figsize=(10,10))
sb.scatterplot(plR,plM)
plt.title('Radius Vs Mass')
plt.xlabel('Mass')
plt.ylabel('Radius')
plt.show()

plt.figure(figsize=(10,10))
sb.scatterplot(plG,plM)
plt.title('Gravity Vs Mass')
plt.xlabel('Mass')
plt.ylabel('Gravity')
plt.show()

