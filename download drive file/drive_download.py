import subprocess
import re
import sys

FILENAME = sys.argv[1]
link = sys.argv[2]

# First parameter is the ID, second parameter is the filename
FILEID = re.search(r"/d/([a-zA-Z0-9_-]+)", link).group(1)

# This script downloads the drive file with the given ID and saves it with the given name
COOKIE_FILE = "cookies.txt"

# First get the confirmation prompt because the file is too big
cmd1 = f'curl -s -c {COOKIE_FILE} "https://docs.google.com/uc?export=download&id={FILEID}" | sed -rn \'s/.*confirm=([0-9A-Za-z_]+).*/\\1\\n/p\''
confirm = subprocess.check_output(cmd1, shell=True).decode().strip()

# Then download the file using the confirmation prompt
cmd2 = f'curl -s -L -b {COOKIE_FILE} "https://docs.google.com/uc?export=download&confirm={confirm}&id={FILEID}" -o "{FILENAME}"'
subprocess.run(cmd2, shell=True)

# Finally, delete the cookie file
subprocess.run(f'rm {COOKIE_FILE}', shell=True);