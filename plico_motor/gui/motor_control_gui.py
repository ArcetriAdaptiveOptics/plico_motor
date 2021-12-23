import sys

import plico_motor


class Runner(object):

    def __init__(self):
        pass

    def _setUp(self, argv):
        pass

    def run(self, argv):
        # show gui
        pass

    def terminate(self, signal, frame):
        # QApplication.quit()
        pass


if __name__ == '__main__':
    runner = Runner()
    sys.exit(runner.run(sys.argv[1:]))

