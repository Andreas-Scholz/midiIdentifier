import time
import threading
import subprocess

class MidiPlayer2():

    def __init__(self):
        self.p = None

    def play(self, file):
        self.p = subprocess.Popen(["aplaymidi", "-p128:0", file])

    def stop(self):
        self.p.terminate()


def main():
    player = MidiPlayer2()
    player.play("../../files/midi/StarWarsMainTheme.mid")
    time.sleep(2)
    player.stop()

if __name__ == "__main__":
    main()
