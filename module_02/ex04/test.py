import my_minipack
from my_minipack import log 
import time

lst = range(434)

@log
def iter():
    for elem in my_minipack.ft_progress(lst):
        time.sleep(0.005)

def main():
    iter()

if __name__ == "__main__":
    main()