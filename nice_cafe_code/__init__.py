from compiler import dung_compiler
from status import dung_status_change


# comparable tuple
VERSION = (0, 1, 0)
# generate __version__ via VERSION tuple
__version__ = ".".join(map(str, VERSION))
