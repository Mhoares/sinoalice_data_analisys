from userdata import UsersData
import matplotlib.pyplot as plt
import sys

userData = UsersData()
total_registration = userData.getUsersRegistrationMonthly()
total_registration_items = total_registration.items()
total_registration_sorted = sorted(total_registration_items)
month =[]
players =[]
for to in total_registration_sorted[int(sys.argv[1]):]:
  month.append(str(to[0][1]) +"-"+ str(to[0][0]))
  players.append(to[1])

plt.plot(month, players)
plt.ylabel('Number of players')
plt.xlabel('Month')

plt.xticks( ticks=None, labels=None,  rotation=90)

plt.tick_params(axis='both', which='major', labelsize=10)
plt.tick_params(axis='both', which='minor', labelsize=8)

plt.tight_layout()
plt.savefig("montly.png")