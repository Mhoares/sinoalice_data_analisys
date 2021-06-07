from user_data import UsersData
import matplotlib.pyplot as plt
activity = UsersData()
total_historico = activity.getUsersActivityHistory()
total_historico_items = total_historico.items()
total_historico_ordenado = sorted(total_historico_items)
day =[]
players =[]
for to in total_historico_ordenado[0:339]:
  day.append(to[0])
  players.append(to[1])
plt.plot(day, players)
plt.ylabel('Number of players')
plt.xlabel('Day')
plt.savefig("history.png") 