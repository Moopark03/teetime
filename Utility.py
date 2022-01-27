from datetime import datetime
def checkTime(teeTime, players, earlyTime, latestTime):
     thisTime = datetime.strptime(teeTime, "%I:%M%p")
     if thisTime <= latestTime and thisTime >= earlyTime:
          if "4" in players:
               print("Found")
               return True