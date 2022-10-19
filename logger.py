from datetime import datetime as dt
from time import time

def number_logger(book):
    time = dt.now().strftime('%H:%M')
    with open('log.txt', 'a') as file:
        file.write('{}; book: {}\n'
            .format(time, book))
