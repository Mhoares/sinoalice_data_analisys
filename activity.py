from userdata import UsersData
import matplotlib.pyplot as plt

activity = UsersData()
total = activity.getUsersActivity()
total_items = total.items()
total_sorted = sorted(total_items)
timeAgo = []
players = []
for to in total_sorted:
    timeAgo.append(to[0].days - 1)
    players.append(to[1])
plt.plot(timeAgo[0:7], players[0:7])
plt.ylabel('players')
plt.xlabel('last time active(days)')
plt.savefig("activity.png") 