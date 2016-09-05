import wordclock_display as wcd
import time_as_words as taw

class wordclock
    def __init__(self):
        # Create object to display any content on the wordclock display
        # Its implementation depends on your (individual) wordclock layout/wiring
        self.wcd = wcd.wordclock_display(self.config)

    def run(self):
        # Run the wordclock forever
        while True:
            taw.run(self.wcd)

if __name__ == '__main__':
    word_clock = wordclock()
    word_clock.run()