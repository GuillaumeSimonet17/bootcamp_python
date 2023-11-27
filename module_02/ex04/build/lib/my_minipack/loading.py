import time 
import sys

def calculate_color(progress):
    # Calculate color based on progress percentage
    r = int(255 * (1 - progress))
    g = int(255)
    b = int(0)

    # Return ANSI escape code for RGB color
    return "\033[38;2;{};{};{}m".format(r, g, b)

def ft_progress(lst):
    nb_el = len(lst)
    started_time = time.time()
    elapsed_time = 0
    progress_width = 40

    def format_bar(progress):
        bar_width = int(progress_width * progress)
        color_code = calculate_color(progress)
        return "{}[{}>] {:.2%}\033[0m".format(color_code, '=' * bar_width, progress)

    for i, el in enumerate(lst):
        yield el
        elapsed_time = time.time() - started_time
        progress = (i + 1) / nb_el
        eta = elapsed_time / progress - elapsed_time
        elapsed_str = "{:.2f}".format(elapsed_time)  
        eta_str =  "{:.2f}".format(eta)
        print(f"\033[38;2;20;20;255mETA: {eta_str}s \033[0m[{int(progress * 100)}%] {format_bar(progress)}] {i + 1}/{nb_el} | elapsed time {elapsed_str}s", end='\r')



def main():
    listy = range(3333)
    ret = 0
    print()
    for elem in ft_progress(listy):
        ret += elem
        time.sleep(0.005)
    print()
    print(ret)


if __name__ == "__main__":
    main()