import pathlib
import datetime
file = "/home/santosh/java_error_in_PYCHARM_3061.log"
filepath= pathlib.Path(file)
mtime = datetime.datetime.fromtimestamp(filepath.stat().st_mtime)
print(mtime)