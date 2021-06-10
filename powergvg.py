from userdata import UsersData
import matplotlib.pyplot as plt

powerGvG = UsersData()
total = powerGvG.getUsersPowerGvG()
total_items = total.items()
total_sorted = sorted(total_items)
power= []
players = []


for to in total_sorted:
    power.append(to[0])
    players.append(to[1])


plt.plot(power, players)
plt.ylabel('Number of players')
plt.xlabel('Power')
plt.xticks( ticks=None, labels=None,  rotation=90)

plt.tick_params(axis='both', which='major', labelsize=10)
plt.tick_params(axis='both', which='minor', labelsize=8)
plt.tight_layout()
plt.savefig("powergvg.png") 