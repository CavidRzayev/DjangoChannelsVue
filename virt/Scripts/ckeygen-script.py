#!c:\users\xoxan\desktop\vv\virt\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'Twisted==18.9.0','console_scripts','ckeygen'
__requires__ = 'Twisted==18.9.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('Twisted==18.9.0', 'console_scripts', 'ckeygen')()
    )
