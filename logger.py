from datetime import datetime as dt
from time import time
import codecs

def number_logger(info):
    time = dt.now().strftime('%H:%M')
    with codecs.open('log.txt', 'a', 'utf-16') as file:
        file.write('{}: {}\n'
            .format(time, info))