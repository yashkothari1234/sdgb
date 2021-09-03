from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
import csv






rows = []

with open("main.csv", "r") as f:
  csvreader = csv.reader(f)
  for row in csvreader: 
    rows.append(row)

headers = rows[0]
star_data_rows = rows[1:]
print(headers)
print(star_data_rows[0])

star_masses = []
star_radiuses = []
star_names = []
for star_data in star_data_rows:
  star_masses.append(star_data[3])
  star_radiuses.append(star_data[4])
  star_names.append(star_data[1])
star_gravity = []
for index, name in enumerate(star_names):
  gravity = (float(star_masses[index])*6.674e-11) / (float(star_radiuses[index])*float(star_radiuses[index])) * 6.674e-11
  planet_gravity.append(gravity)

fig = px.scatter(x=star_radiuses, y=star_masses, size=star_gravity, hover_data=[star_names])
fig.show()

low_gravity_stars = []
for index, gravity in enumerate(star_gravity):
  if gravity < 10:
    low_gravity_stars.append(star_data_rows[index])

print(len(low_gravity_stars))

star_masses = []
star_radiuses = []
for star_data in low_gravity_stars:
  star_masses.append(star_data[3])
  star_radiuses.append(star_data[7])

fig = px.scatter(x=star_radiuses, y=star_masses)
fig.show()

X = []
for index, star_mass in enumerate(star_masses):
  temp_list = [
                  star_radiuses[index],
                  star_mass
              ]
  X.append(temp_list)

wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state = 42)
    kmeans.fit(X)
    # inertia method returns wcss for that model
    wcss.append(kmeans.inertia_)

plt.figure(figsize=(10,5))
sns.lineplot(range(1, 11), wcss, marker='o', color='red')
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

planet_masses = []
planet_radiuses = []
planet_types = []
for star_data in low_gravity_stars:
  star_masses.append(star_data[3])
  star_radiuses.append(star_data[7])
  star_types.append(star_data[6])

fig = px.scatter(x=star_radiuses, y=star_masses, color=star_types)
fig.show()