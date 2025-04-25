#!/usr/bin/env python3
import os
import time
from datetime import datetime

FILENAME = "LustUpdate"
INTERVAL = 300  # 5 минут в секундах

while True:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w") as f:
            f.write(now)
    else:
        with open(FILENAME, "w") as f:
            f.write(now)
    time.sleep(INTERVAL)
