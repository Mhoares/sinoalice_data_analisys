from userdata import UsersData
import matplotlib.pyplot as plt

activity = UsersData()
total_history = activity.getUsersActivityHistory()
total_history_items = total_history.items()
total_history_sorted = sorted(total_history_items)
day =[]
players =[]
for to in total_history_sorted[0:339]:
  day.append(to[0])
  players.append(to[1])
plt.plot(day, players)
plt.ylabel('Number of players')
plt.xlabel('Day')
plt.savefig("history.png") 