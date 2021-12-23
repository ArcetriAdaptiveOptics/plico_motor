import sys

import plico_motor
from guietta import Gui, _


class Runner(object):

    def __init__(self):
        self._motor = plico_motor.motor(host, port)

    def _setUp(self, argv):

        def moveby(gui):
            self._motor.moveby(int(gui.nsteps))

        def getpos(gui):
            try:
                gui.pos = self._motor.pos()
            except pico.PicomotorException:
                gui.pos = 'unreachable'

        self.gui = Gui(
             [  'Pos:'  , 'pos'       , _ ],
             [ ['Move by'] , '__nsteps__', 'steps' ]
        )
        self.gui.Move = moveby
        self.gui.timer_start(getpos, 0.1)

    def run(self, argv):
        self.gui.run()

    def terminate(self, signal, frame):
        pass


if __name__ == '__main__':
    runner = Runner()
    sys.exit(runner.run(sys.argv[1:]))

