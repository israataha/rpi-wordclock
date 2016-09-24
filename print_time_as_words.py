from neopixel import *
import time
import datetime

bg_color    = BLACK = Color(  0,  0,  0)
word_color  = Color(255,255, 50) # Warm white

# LED strip configuration:
WCA_HEIGHT  = 12      # len(layout)             
WCA_WIDTH   = 12      # len(layout[0])
LED_COUNT   = self.WCA_HEIGHT*self.WCA_WIDTH    # Number of LED pixels.
LED_PIN     = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA     = 5       # DMA channel to use for generating signal (try 5)
LED_INVERT  = False   # True to invert the signal (when using NPN transistor level shift)
brightness  = 20

strip = Adafruit_NeoPixel(self.wcl.LED_COUNT, self.wcl.LED_PIN, self.wcl.LED_FREQ_HZ, self.wcl.LED_DMA, self.wcl.LED_INVERT, brightness)
strip.begin()

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

#Prefix
prefix = list(range(0,2)) + list(range(3,5)) # -> IT IS

#Minutes
minutes=[[], \
            # -> FIVE PAST
            list(range(31,35)) + list(range(42,46)), \
            # -> TEN PAST
            list(range(8,11)) + list(range(42,46)), \
            # -> QUARTER PAST
            list(range(17,24)) + list(range(42,46)), \
            # -> TWENTY PAST
            list(range(24,30)) + list(range(42,46)), \
            # -> TWENTYFIVE PAST
            list(range(24,30)) + list(range(31,35)) + list(range(42,46)), \
            # -> HALF PAST
            list(range(12,16)) + list(range(42,46)), \
            # -> TWENTYFIVE TO
            list(range(24,30)) + list(range(31,35)) + list(range(48,50)), \
            # -> TWENTY TO
            list(range(24,30)) + list(range(48,50)), \
            # -> QUARTER TO
            list(range(17,24)) + list(range(48,50)), \
            # -> TEN TO
            list(range(8,11)) + list(range(48,50)), \
            # -> FIVE TO
            list(range(31,35)) + list(range(48,50)) ]

#Hours
hours= [range(124,132), \
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

#OCLOCK
full_hour= range(133,139)

prev_min = -1

while True:
    # Get current time
    now = datetime.datetime.now()
    # Check, if a minute has passed (to render the new time)
    if prev_min < now.minute:
        hour = now.hour%12 + (1 if now.minute/5 >= 7 else 0)
        minute = round(now.minute/5)
        taw_indices = prefix + \
                minutes[minute] + \
                list(hours[hour]) + \
                (list(full_hour) if (minute == 0) else [])
        
        print(hour)
        print(minute)
        print(taw_indices)
        
        #Set all LEDs back to black
        for i in range(LED_COUNT):
                strip.setPixelColor(i, bg_color)

        for i in range(len(taw_indices)):
                strip.setPixelColor(taw_indices[i], word_color)
                strip.show()
                #time.sleep(1.0/self.typewriter_speed)

        prev_min = -1 if now.minute == 59 else now.minute