

def parseUserData(timeString):

    day = timeString[0].upper() + timeString[1:timeString.index(" ")]
    timeString = timeString[timeString.index(" ") + 1:]
    userTimes = timeString.split(',')
    startTimes = []
    endTimes = []
    
    for i in range(len(userTimes)):
        start, end = userTimes[i].split("-", 1)
        startTimes.append(start)
        endTimes.append(end)

        if startTimes[i][5] == 'P' and startTimes[i][0:2] != "12":
            startTimes[i] = str(int(startTimes[i][0:2]) + 12) + startTimes[i][2:5]

        if endTimes[i][5] == 'P'and endTimes[i][0:2] != 12:
            endTimes[i] = str(int(endTimes[i][0:2]) + 12) + endTimes[i][2:5]

        startTimes[i] = startTimes[i][0:5]
        endTimes[i] = endTimes[i][0:5]

    return day, startTimes, endTimes