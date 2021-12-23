#!/usr/bin/env python
import sys
from plico_motor.gui.camera_control_gui import Runner


def main():
    runner = Runner()
    print("%s" % sys.argv)
    sys.exit(runner.run(sys.argv[1:]))


if __name__ == '__main__':
    main()
