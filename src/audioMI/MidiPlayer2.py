import time
from telnetlib import Telnet
import subprocess

class MidiPlayer2():

    def __init__(self):
        self.p = None
        self.fluid = Telnet("192.168.0.21","9988")

    def play(self, file):
        self.p = subprocess.Popen(["aplaymidi", "-p128:0", file])

    def stop(self):
        self.p.terminate()
        self.fluid.write("reset")
        self.fluid.write("quit")

def main():
    player = MidiPlayer2()
    player.play("../../files/midi/StarWarsMainTheme.mid")
    time.sleep(2)
    player.stop()

if __name__ == "__main__":
    main()
