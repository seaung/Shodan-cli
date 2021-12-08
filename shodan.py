import sys
from app.options import options
from app import Runner


runner = Runner()
options = options()


if __name__ == '__main__':
    try:
        runner.start(options)
    except KeyboardInterrupt:
        sys.exit(0)
