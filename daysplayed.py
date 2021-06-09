from userdata import UsersData
import matplotlib.pyplot as plt
import sys

daysPlayed = UsersData()
total = daysPlayed.getUsersDaysPlayed()
total_items = total.items()
total_sorted = sorted(total_items)
days = []
players = []

if len(sys.argv) > 1:
    total_sorted = total_sorted[:int(sys.argv[1])]

for to in total_sorted:
    days.append(to[0])
    players.append(to[1])

plt.plot(days, players)
plt.ylabel('Number of players')
plt.xlabel('days played')
plt.savefig("dayplayed.png") 