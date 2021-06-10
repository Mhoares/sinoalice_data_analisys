import json
import math
from datetime import  date
class UsersData:
  def __init__(self, path ="users.json"):
    self.path = path
    self.usersData =self.load()

  def load(self):
     users =[]
     for data in json.load(open(self.path, encoding="utf8")):
       users.append(User(data))
     return users
    
  def getUsersActivity(self):
      usersActivity = dict()  
      for user in self.usersData:
          if user.timeAgo() not in usersActivity.keys():         
             usersActivity[user.timeAgo()] =  0
          usersActivity[user.timeAgo()] +=1     
      return usersActivity

  def getUsersActivityHistory(self):
    usersActivityHistory = dict()  
    for user in self.usersData:
         for day in range(user.timeAgo().days, user.timeAgo("createdTime").days):
           if day not in usersActivityHistory:
             usersActivityHistory[day]= 0
           usersActivityHistory[day]+=1
    return usersActivityHistory

  def getUsersRegistrationDaily(self):
    usersRegistration = dict()  
    for user in self.usersData:
        day = user.timeAgo("createdTime").days
        if day not in usersRegistration:
          usersRegistration[day]= 0
        usersRegistration[day]+=1
    return usersRegistration

  def getUsersRegistrationMonthly(self):
    usersRegistration = dict()  
    for user in self.usersData:
        month , year= user.monthCreated()
        key =(year, month)
        if key not in usersRegistration:
          usersRegistration[key]= 0
        usersRegistration[key]+=1
    return usersRegistration

  def getUsersDaysPlayed(self):
    usersDayPlayed = dict()  
    for user in self.usersData:
        day = user.getDaysPlayed()
        if day not in usersDayPlayed:
          usersDayPlayed[day]= 0
        usersDayPlayed[day]+=1
    return usersDayPlayed

  def getUsersPowerGvG(self, interval = 10000):
    usersPowerGvG = dict() 
    powers =[]
   
    for user in self.usersData:
        powers.append(user.getPowerGvG())
    
    powers = sorted(powers)
    index = iter(powers)
    intervals = math.ceil( powers[-1]/interval)
    power =powers[0]
    usersPowerGvG[interval] = 0
    for i in range(interval,interval*intervals,interval):    
      while power and power < i:        
        power = next(index, False)   
        usersPowerGvG[i]+=1    
      if power:      
        usersPowerGvG[i+interval] = 1
      

    return usersPowerGvG
   
class User:
  def __init__(self, user, key = "userData"):
   self.user = user[key]

  def timeAgo(self, key ="lastAccessTime"):
   return date.today() - date.fromtimestamp(self.user[key])

  def monthCreated(self, key = "createdTime") :
    return date.fromtimestamp(self.user[key]).month , date.fromtimestamp(self.user[key]).year

  def getDaysPlayed(self, created = "createdTime", last = "lastAccessTime"):
    return (date.fromtimestamp(self.user[last] ) - date.fromtimestamp(self.user[created] )).days

  def getPowerGvG(self, key ="gvgTotalPower"):
    return self.user[key]




  