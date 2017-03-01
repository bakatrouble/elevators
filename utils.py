import traceback
import sys


def excepthook(etype, value, tb):
    traceback.print_exception(etype, value, tb)
    sys.exit(1)
