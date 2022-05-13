from os.path import basename, dirname
from glob import glob

__all__ = [basename(f)[:-3] for f in glob(dirname(__file__) + "/*.py")]
