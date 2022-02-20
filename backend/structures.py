tupleCount = (2, 10, 18, 21, 25)


class sunday:
    def __init__(self):
        self.times = {'08:00': [0, 0], '08:30': [0, 0], '09:00': [0, 0],
                      '09:30': [0, 0], '10:00': [0, 0], '10:30': [0, 0],
                      '11:00': [0, 0], '11:30': [0, 0], '12:00': [0, 0],
                      '12:30': [0, 0], '13:00': [0, 0], '13:30': [0, 0],
                      '14:00': [0, 0], '14:30': [0, 0], '15:00': [0, 0],
                      '15:30': [0, 0], '16:00': [0, 0], '16:30': [0, 0],
                      '17:00': [0, 0], '17:30': [0, 0], '18:00': [0, 0],
                      '18:30': [0, 0], '19:00': [0, 0], '19:30': [0, 0],
                      '20:00': [0, 0], '20:30': [0, 0], '21:00': [0, 0],
                      '21:30': [0, 0], '22:00': [0, 0], '22:30': [0, 0],
                      '23:00': [0, 0], '23:30': [0, 0]}


class mon_thurs:
    def __init__(self):
        self.times = {'06:00': [0, 0], '06:30': [0, 0], '07:00': [0, 0],
                      '07:30': [0, 0], '08:00': [0, 0], '08:30': [0, 0],
                      '09:00': [0, 0], '09:30': [0, 0], '10:00': [0, 0],
                      '10:30': [0, 0], '11:00': [0, 0], '11:30': [0, 0],
                      '12:00': [0, 0], '12:30': [0, 0], '13:00': [0, 0],
                      '13:30': [0, 0], '14:00': [0, 0], '14:30': [0, 0],
                      '15:00': [0, 0], '15:30': [0, 0], '16:00': [0, 0],
                      '16:30': [0, 0], '17:00': [0, 0], '17:30': [0, 0],
                      '18:00': [0, 0], '18:30': [0, 0], '19:00': [0, 0],
                      '19:30': [0, 0], '20:00': [0, 0], '20:30': [0, 0],
                      '21:00': [0, 0], '21:30': [0, 0], '22:00': [0, 0],
                      '22:30': [0, 0], '23:00': [0, 0], '23:30': [0, 0]}


class friday:
    def __init__(self):
        self.times = {'06:00': [0, 0], '06:30': [0, 0], '07:00': [0, 0],
                      '07:30': [0, 0], '08:00': [0, 0], '08:30': [0, 0],
                      '09:00': [0, 0], '09:30': [0, 0], '10:00': [0, 0],
                      '10:30': [0, 0], '11:00': [0, 0], '11:30': [0, 0],
                      '12:00': [0, 0], '12:30': [0, 0], '13:00': [0, 0],
                      '13:30': [0, 0], '14:00': [0, 0], '14:30': [0, 0],
                      '15:00': [0, 0], '15:30': [0, 0], '16:00': [0, 0],
                      '16:30': [0, 0], '17:00': [0, 0], '17:30': [0, 0],
                      '18:00': [0, 0], '18:30': [0, 0], '19:00': [0, 0],
                      '19:30': [0, 0], '20:00': [0, 0], '20:30': [0, 0],
                      '21:00': [0, 0], '21:30': [0, 0]}


class saturday:
    def __init__(self):
        self.times = {'08:00': [0, 0], '08:30': [0, 0], '09:00': [0, 0],
                      '09:30': [0, 0], '10:00': [0, 0], '10:30': [0, 0],
                      '11:00': [0, 0], '11:30': [0, 0], '12:00': [0, 0],
                      '12:30': [0, 0], '13:00': [0, 0], '13:30': [0, 0],
                      '14:00': [0, 0], '14:30': [0, 0], '15:00': [0, 0],
                      '15:30': [0, 0], '16:00': [0, 0], '16:30': [0, 0],
                      '17:00': [0, 0], '17:30': [0, 0], '18:00': [0, 0],
                      '18:30': [0, 0], '19:00': [0, 0], '19:30': [0, 0],
                      '20:00': [0, 0], '20:30': [0, 0], '21:00': [0, 0],
                      '21:30': [0, 0]}


trackSun = sunday()
trackMon = mon_thurs()
trackTues = mon_thurs()
trackWed = mon_thurs()
trackThurs = mon_thurs()
trackFri = friday()
trackSat = saturday()
track_week = {'Sunday': trackSun, 'Monday': trackMon, 'Tuesday': trackTues, 'Wednesday': trackWed,
              'Thursday': trackThurs, 'Friday': trackFri, 'Saturday': trackSat}

lvl1Sun = sunday()
lvl1Mon = mon_thurs()
lvl1Tues = mon_thurs()
lvl1Wed = mon_thurs()
lvl1Thurs = mon_thurs()
lvl1Fri = friday()
lvl1Sat = saturday()
level1_week = {'Sunday': lvl1Sun, 'Monday': lvl1Mon, 'Tuesday': lvl1Tues, 'Wednesday': lvl1Wed,
               'Thursday': lvl1Thurs, 'Friday': lvl1Fri, 'Saturday': lvl1Sat}

lvl2Sun = sunday()
lvl2Mon = mon_thurs()
lvl2Tues = mon_thurs()
lvl2Wed = mon_thurs()
lvl2Thurs = mon_thurs()
lvl2Fri = friday()
lvl2Sat = saturday()
level2_week = {'Sunday': lvl2Sun, 'Monday': lvl2Mon, 'Tuesday': lvl2Tues, 'Wednesday': lvl2Wed,
               'Thursday': lvl2Thurs, 'Friday': lvl2Fri, 'Saturday': lvl2Sat}

lvl3Sun = sunday()
lvl3Mon = mon_thurs()
lvl3Tues = mon_thurs()
lvl3Wed = mon_thurs()
lvl3Thurs = mon_thurs()
lvl3Fri = friday()
lvl3Sat = saturday()
level3_week = {'Sunday': lvl3Sun, 'Monday': lvl3Mon, 'Tuesday': lvl3Tues, 'Wednesday': lvl3Wed,
               'Thursday': lvl3Thurs, 'Friday': lvl3Fri, 'Saturday': lvl3Sat}

powerSun = sunday()
powerMon = mon_thurs()
powerTues = mon_thurs()
powerWed = mon_thurs()
powerThurs = mon_thurs()
powerFri = friday()
powerSat = saturday()
power_week = {'Sunday': powerSun, 'Monday': powerMon, 'Tuesday': powerTues, 'Wednesday': powerWed,
              'Thursday': powerThurs, 'Friday': powerFri, 'Saturday': powerSat}