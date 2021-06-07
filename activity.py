from user_data import UsersData
import matplotlib.pyplot as plt

activity = UsersData()
total = activity.getUsersActivity()
total_items = total.items()
total_ordenado = sorted(total_items)
tiempo = []
jugadores = []
for to in total_ordenado:
    tiempo.append(to[0].days - 1)
    jugadores.append(to[1])
plt.plot(tiempo[0:7], jugadores[0:7])
plt.ylabel('players')
plt.xlabel('last time active(days)')
plt.savefig("activity.png") 