import psutil
import time

def display_usage(cpu_usage: float, mem_usage: float, bars = 50) -> None:
    cpu_percent = cpu_usage / 100.0
    mem_percent = mem_usage / 100.0
    
    cpu_bar = '•' * int(cpu_percent * bars) + '-' * (bars - int(cpu_percent * bars))
    mem_bar = '•' * int(mem_percent * bars) + '-' * (bars - int(mem_percent * bars))
    
    print(f'\r CPU Usage: |{cpu_bar}| {cpu_usage:.2f}%  ', end = '')
    print(f'MEM Usage: |{mem_bar}| {mem_usage:.2f}%  ', end = '\r')

while True:
    display_usage(cpu_usage = psutil.cpu_percent(), mem_usage = psutil.virtual_memory().percent, bars = 50)
    time.sleep(0.5)