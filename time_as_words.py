import time
import datetime
import wordclock_colors as wcc

class time_as_words():
    '''
    This class returns a given time as a range of LED-indices.
    Illuminating these LEDs represents the current time on an english WCA
    '''

    def __init__(self):
        self.prefix = range(0,2) +  range(3,5) # -> IT IS
        self.minutes=[[], \
            # -> FIVE PAST
            range(28,32) + range(44,48), \
            # -> TEN PAST
            range(38,41) + range(44,48), \
            # -> QUARTER PAST
            range(13,20) + range(44,48), \
            # -> TWENTY PAST
            range(22,28) + range(44,48), \
            # -> TWENTYFIVE PAST
            range(22,32) + range(44,48), \
            # -> HALF PAST
            range(33,37) + range(44,48), \
            # -> TWENTYFIVE TO
            range(22,32) + range(42,44), \
            # -> TWENTY TO
            range(22,28) + range(42,44), \
            # -> QUARTER TO
            range(13,20) + range(42,44), \
            # -> TEN TO
            range(38,41) + range(42,44), \
            # -> FIVE TO
            range(28,32) + range(42,44) ]
            # -> TWELVE
        self.hours= [range(93,99), \
            # -> ONE
            range(55,58), \
            # -> TWO
            range(74,77), \
            # -> THREE
            range(61,66), \
            # -> FOUR
            range(66,70), \
            # -> FIVE
            range(70,74), \
            # -> SIX
            range(58,61), \
            # -> SEVEN
            range(88,93), \
            # -> EIGHT
            range(77,82), \
            # -> NINE
            range(51,55), \
            # -> TEN
            range(99,102),\
            # -> ELEVEN
            range(82,88), \
            # -> TWELVE
            range(93,99)]
        # -> OCLOCK
        self.full_hour= range(104,110)

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
                # Returns indices, which represent the current time, when beeing illuminated
                taw_indices = self.get_time(now)
                if self.typewriter and now.minute%5 == 0:
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
