import structures

def parse_user_data(day, level, timeString):
    userTimes = timeString.split(',')
    startTimes = []
    endTimes = []
    
    for i in range(len(userTimes)):
        start, end = userTimes[i].split("-", 1)
        startTimes.append(start)
        endTimes.append(end)

        if startTimes[i][5] == 'P' and startTimes[i][0:2] != "12":
            startTimes[i] = str(int(startTimes[i][0:2]) + 12) + startTimes[i][2:5]

        if endTimes[i][5] == 'P'and endTimes[i][0:2] != "12":
            endTimes[i] = str(int(endTimes[i][0:2]) + 12) + endTimes[i][2:5]

        startTimes[i] = startTimes[i][0:5]
        endTimes[i] = endTimes[i][0:5]

    return day, level, startTimes, endTimes


def increment_time(currTime):
    if currTime[3] == "3":
        if len(str(int(currTime[0:2]) + 1)) == 1:
            currTime = "0" + str(int(currTime[0:2]) + 1) + ":00"
        else:
            currTime = str(int(currTime[0:2]) + 1) + ":00"
    else:
        currTime = currTime[0:2] + ":30"

    return currTime

def get_week_intervals(startList, endList):
    timeList = []

    for i in range(len(startList)):
        startTime = startList[i]
        endTime = endList[i]
        currTime = startTime
        intList = []
        
        while not currTime == endTime:
            intList.append(currTime)

            currTime = increment_time(currTime)
        
        timeList.append(intList)

    return timeList
            
  
def get_best_times(timeString):
    day, startList, endList  = parse_user_data(timeString)
    
