import time
import datetime
import wordclock_colors as wcc

# Word Clock Layout 12x12
layout = ["ITMISBALTENH", # 0-11
          "HALFXQUARTER", # 12-23
          "TWENTYJFIVEQ", # 24-35
          "HAPPYGPASTZY", # 36-47
          "TODLBIRTHDAY", # 48-59
          "VELEVENXONEU", # 60-71
          "FIVEKSEVENDE", # 72-83
          "TWELVEFCTENM", # 84-95
          "LFOURQEIGHTN", # 96-107
          "TWOSIXTHREEA", # 108-119
          "NINEMIDNIGHT", # 120-131
          "JOCLOCKRNOON"] # 132-143

class time_as_words():
    '''
    This class returns a given time as a range of LED-indices.
    Illuminating these LEDs represents the current time on an english WCA
    '''

    def __init__(self):
        self.prefix = range(0,2) +  range(3,5) # -> IT IS
        self.minutes=[[], \
            # -> FIVE PAST
            range(31,35) + range(42,46), \
            # -> TEN PAST
            range(8,11) + range(42,46), \
            # -> QUARTER PAST
            range(17,24) + range(42,46), \
            # -> TWENTY PAST
            range(24,30) + range(42,46), \
            # -> TWENTYFIVE PAST
            range(24,30) + range(31,35) + range(42,46), \
            # -> HALF PAST
            range(12,16) + range(42,46), \
            # -> TWENTYFIVE TO
            range(24,30) + range(31,35) + range(48,50), \
            # -> TWENTY TO
            range(24,30) + range(48,50), \
            # -> QUARTER TO
            range(17,24) + range(48,50), \
            # -> TEN TO
            range(8,11) + range(48,50), \
            # -> FIVE TO
            range(31,35) + range(48,50) ]
            # -> MIDNIGHT
        self.hours= [range(124,132), \
            # -> ONE
            range(68,71), \
            # -> TWO
            range(108,111), \
            # -> THREE
            range(114,119), \
            # -> FOUR
            range(97,101), \
            # -> FIVE
            range(72,76), \
            # -> SIX
            range(111,114), \
            # -> SEVEN
            range(77,82), \
            # -> EIGHT
            range(102,107), \
            # -> NINE
            range(120,124), \
            # -> TEN
            range(92,95),\
            # -> ELEVEN
            range(61,67), \
            # -> NOON
            range(140,144)]
        # -> OCLOCK
        self.full_hour= range(133,139)

        self.bg_color     = wcc.BLACK  # default background color
        self.word_color   = wcc.WWHITE # default word color
        self.minute_color = wcc.WWHITE # default minute color

        self.typewriter_speed = 5

    def get_time(self, time, withPrefix=True):
        hour = time.hour%12 + (1 if time.minute/5 >= 7 else 0)
        minute = time.minute/5
        # Assemble indices
        return  \
            (self.prefix if withPrefix else []) + \
            self.minutes[minute] + \
            self.hours[hour] + \
            (self.full_hour if (minute == 0) else [])

    def run(self, wcd):
        '''
        Displays time until aborted by user interaction on pin button_return
        '''
        # Some initializations of the "previous" minute
        prev_min = -1

        while True:
            # Get current time
            now = datetime.datetime.now()
            # Check, if a minute has passed (to render the new time)
            if prev_min < now.minute:
                # Set background color
                wcd.setColorToAll(self.bg_color, includeMinutes=True)
                # Returns indices, which represent the current time, when being illuminated
                taw_indices = self.get_time(now)
                if now.minute%5 == 0:
                    for i in range(len(taw_indices)):
                        wcd.setColorBy1DCoordinates(wcd.strip, taw_indices[0:i+1], self.word_color)
                        wcd.show()
                        time.sleep(1.0/self.typewriter_speed)
                    wcd.setMinutes(now, self.minute_color)
                    wcd.show()
                else:
                    wcd.setColorBy1DCoordinates(wcd.strip, taw_indices, self.word_color)
                    wcd.setMinutes(now, self.minute_color)
                    wcd.show()
                prev_min = -1 if now.minute == 59 else now.minute
