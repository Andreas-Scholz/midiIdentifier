import time
import threading
import pygame

pygame.init()
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)

paused = False
do_pause = False
do_unpause = False

class MidiPlayer():

    stop_playback = False

    def __init__(self):
        pass

    def load(self, midi_file):
        pygame.mixer.music.load(midi_file)

    def play(self):
        playThread = threading.Thread(target=self._play)
        playThread.start()

    def _play(self):
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            if self.stop_playback:
                pygame.mixer.music.stop()
            pygame.time.wait(100)

    def stop(self):
        self.stop_playback = True


def main():
    player = MidiPlayer()
    player.load("../../files/midi/StarWarsMainTheme.mid")
    player.play()
    time.sleep(2)
    player.stop()

if __name__ == "__main__":
    main()
