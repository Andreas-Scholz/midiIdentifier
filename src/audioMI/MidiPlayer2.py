import time
from telnetlib import Telnet
import subprocess

class MidiPlayer2():

    def __init__(self):
        self.p = None

    def play(self, file):
        self.p = subprocess.Popen(["aplaymidi", "-p128:0", file])

    def stop(self):
        fluid = Telnet("localhost","9988")
        self.p.terminate()
        fluid.write("reset\n".encode('ascii'))
        fluid.write("quit\n".encode('ascii'))

def main():
    player = MidiPlayer2()
    player.play("../../files/midi/StarWarsMainTheme.mid")
    time.sleep(2)
    player.stop()

if __name__ == "__main__":
    main()
