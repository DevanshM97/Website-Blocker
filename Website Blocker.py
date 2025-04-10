import time
from datetime import datetime as dt

# Use appropriate hosts path based on OS
HOSTS_PATH = "/etc/hosts"  # Linux/macOS
# HOSTS_PATH = r"C:\\Windows\\System32\\drivers\\etc\\hosts"  # Uncomment for Windows
REDIRECT = "127.0.0.1"
WEBSITES = [
    "www.facebook.com",
    "facebook.com",
    "www.youtube.com",
    "youtube.com"
]

START_HOUR = 9
END_HOUR = 17

while True:
    now = dt.now()
    if START_HOUR <= now.hour < END_HOUR:
        print("Working hours: Blocking websites...")
        with open(HOSTS_PATH, 'r+') as file:
            content = file.read()
            for site in WEBSITES:
                if site not in content:
                    file.write(f"{REDIRECT} {site}\n")
    else:
        print("Non-working hours: Unblocking websites...")
        with open(HOSTS_PATH, 'r+') as file:
            lines = file.readlines()
            file.seek(0)
            for line in lines:
                if not any(site in line for site in WEBSITES):
                    file.write(line)
            file.truncate()
    time.sleep(300)  # Check every 5 minutes
