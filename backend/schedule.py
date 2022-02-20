

def parseUserData(timeString):
    userTimes = timeString

def get_best_times(timeString):
    day, startList, endList  = parseUserData(timeString)
    avgList = []
    for i in startList:
        startTime = startList[i]
        endTime = endList[i]
        while not startTime.equals(endTime):
            avgList = None # for now
            # access the time, pull average
            # add 30 to the time

