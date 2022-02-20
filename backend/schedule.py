import structures


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

        if endTimes[i][5] == 'P' and endTimes[i][0:2] != 12:
            endTimes[i] = str(int(endTimes[i][0:2]) + 12) + endTimes[i][2:5]

        startTimes[i] = startTimes[i][0:5]
        endTimes[i] = endTimes[i][0:5]

    return day, startTimes, endTimes


def get_intervals_avgs(week, intervalsList):
    avgsList = []
    for i in range(len(intervalsList)):
        interval = intervalsList[i]
        for time in interval:
           avgsList.append(week[time][0] / week[time][1])


def get_best_times(timeString):
    intervalSize = 2 # defines the number of intervals which define time in gym (2x30min = 1 hr interval)
    day, level, startList, endList = parse_user_data(day, level, timeString)
    levels = {'Track' : structures.track_week, 'Level 3': structures.level3_week, 'Level 2': structures.level2_week, 'Level 1': structures.level1_week, 'Power House': structures.power_week}
    week = levels[level]
    intervalsList = get_week_intervals(week, startList, endList) # returns list of intervals
    avgsList = get_intervals_avgs(week, intervalsList) # returns list of averages for intervals
    optimalInterval = get_best_interval(intervalSize, avgsList) # returns the optimal interval from averages
    return optimalInterval

