from userdata import UsersData
import matplotlib.pyplot as plt
import sys

powerGvG = UsersData()

if len(sys.argv) > 2:
    u = powerGvG.filterUsersByActivity(int(sys.argv[2]))
    u = powerGvG.filterUsersByJob(sys.argv[1],u)
    total = powerGvG.getUsersPowerGvG(u)
    subjects = sys.argv[1] +"s" +" online in last "+sys.argv[2]+" Days"
elif len(sys.argv) > 1:
    total = powerGvG.getUsersPowerGvG(powerGvG.filterUsersByJob(sys.argv[1]))
    subjects = sys.argv[1] +"s"    
else:    
    total = powerGvG.getUsersPowerGvG()
    subjects = "players"

total_items = total.items()
total_sorted = sorted(total_items)
power= []
players = []


for to in total_sorted:
    power.append(to[0])
    players.append(to[1])
    print(to)

plt.plot(power, players)
plt.ylabel('Number of '+subjects)
plt.xlabel('Power')
plt.xticks( ticks=None, labels=None,  rotation=90)

plt.tick_params(axis='both', which='major', labelsize=10)
plt.tick_params(axis='both', which='minor', labelsize=8)
plt.tight_layout()
plt.savefig("powergvg.png") 