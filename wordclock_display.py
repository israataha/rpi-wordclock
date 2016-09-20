from neopixel import *
import time
import wiring
import wordclock_colors as wcc

class wordclock_display:
    '''
    Class to display content on the wordclock display
    '''

    def __init__(self):
        # Get the wordclocks wiring-layout
        self.wcl = wiring.wiring()

        brightness = 20
        
        try:
            self.strip = Adafruit_NeoPixel(self.wcl.LED_COUNT, self.wcl.LED_PIN, self.wcl.LED_FREQ_HZ, self.wcl.LED_DMA, self.wcl.LED_INVERT, brightness)
        except:
            print('WARNING: Your NeoPixel dependency is too old to accept customized brightness values')
            self.strip = Adafruit_NeoPixel(self.wcl.LED_COUNT, self.wcl.LED_PIN, self.wcl.LED_FREQ_HZ, self.wcl.LED_DMA, self.wcl.LED_INVERT)

        # Initialize the NeoPixel object
        self.strip.begin()

    def setPixelColor(self, pixel, color):
        '''
        Sets the color for a pixel, while considering the brightness, set within the config file
        '''
        self.strip.setPixelColor(pixel, color)

    def setBrightness(self, brightness):
        '''
        Sets the color for a pixel, while considering the brightness, set within the config file
        '''
        self.strip.setBrightness(brightness)

    def setColorBy1DCoordinates(self, *args, **kwargs):
        '''
        Sets a pixel at given 1D coordinates
        '''
        return self.wcl.setColorBy1DCoordinates(*args, **kwargs)

    def setColorBy2DCoordinates(self, *args, **kwargs):
        '''
        Sets a pixel at given 2D coordinates
        '''
        return self.wcl.setColorBy2DCoordinates(*args, **kwargs)

    def get_wca_height(self):
        '''
        Returns the height of the WCA
        '''
        return self.wcl.WCA_HEIGHT

    def get_wca_width(self):
        '''
        Returns the height of the WCA
        '''
        return self.wcl.WCA_WIDTH

    def setColorToAll(self, color, includeMinutes=True):
        '''
        Sets a given color to all leds
        If includeMinutes is set to True, color will also be applied to the minute-leds.
        '''
        if includeMinutes:
            for i in range(self.wcl.LED_COUNT):
                self.setPixelColor(i, color)
        else:
            for i in self.wcl.getWcaIndices():
                self.setPixelColor(i, color)

    def resetDisplay(self):
        '''
        Reset display
        '''
        self.setColorToAll(wcc.BLACK, True)

    def setMinutes(self, time, color):
        if time.minute%5 != 0:
            for i in range (1,time.minute%5+1):
                self.setPixelColor(self.wcl.mapMinutes(i), color)

    def show(self):
        '''
        This function provides the current color settings to the LEDs
        '''
        self.strip.show()
