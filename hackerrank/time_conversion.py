# problem: https://www.hackerrank.com/challenges/time-conversion/problem?isFullScreen=true

import time
from datetime import datetime
def time_conversion(s):
    print(datetime.strptime(str, "%I:%M:%S%p").strftime("%H:%M:%S"))

if __name__ == '__main__':
    print(datetime.strptime(str, "%I:%M:%S%p").strftime("%H:%M:%S"))