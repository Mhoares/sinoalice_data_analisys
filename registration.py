from userdata import UsersData
import matplotlib.pyplot as plt

userData = UsersData()
total_registration = userData.getUsersRegistrationDaily()
total_registration_items = total_registration.items()
total_registration_sorted = sorted(total_registration_items)
day =[]
players =[]
for to in total_registration_sorted[0:339]:
  day.append(to[0])
  players.append(to[1])
plt.plot(day, players)
plt.ylabel('Number of players')
plt.xlabel('Day')
plt.savefig("registration.png") 