from datetime import datetime, date, timedelta

def checkTime(teeTime, players, earlyTime, latestTime):
     thisTime = datetime.strptime(teeTime, "%I:%M%p")
     if thisTime <= latestTime and thisTime >= earlyTime:
          if "4" in players:
               print("Found")
               return True

calculateDate = date.today() + timedelta(days = 7)
DATE = calculateDate.strftime("%m/%d/%Y")

earlyTime='9:00AM'
latestTime='10:30AM'