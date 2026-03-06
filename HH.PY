import random
import time

def getRandomDate(startdate,enddate):
    print("Printing random date between",startdate,"and",enddate)
    randomGenerator = random.random()
    dateFormat = "%d/%m/%Y"
    

    starttime = time.mktime(time.strptime(startdate,dateFormat))
    endtime = time.mktime(time.strptime(enddate,dateFormat))

    randomtime = starttime + randomGenerator * (endtime - starttime)
    randomdate = time.strftime(dateFormat, time.localtime(randomtime))
    return randomdate

print(getRandomDate("13/5/2013","3/6/2026"))

