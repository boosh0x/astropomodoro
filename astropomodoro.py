import time
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def countdown_timer(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        time_format = '{:02d}:{:02d}'.format(mins, secs)
        print("Time remaining: " + time_format, end='\r')
        time.sleep(1)
        seconds -= 1
    clear_console()

def pomodoro(work_duration=25, short_break_duration=5, long_break_duration=15, cycles=4):
    cycle_count = 0

    while cycle_count < cycles:
        print(f"Starting work session {cycle_count + 1} of {cycles}.")
        countdown_timer(work_duration * 60)

        if cycle_count < cycles - 1:
            print(f"Short break time! Relax for {short_break_duration} minutes.")
            countdown_timer(short_break_duration * 60)
        else:
            print(f"Long break time! Relax for {long_break_duration} minutes.")
            countdown_timer(long_break_duration * 60)

        cycle_count += 1

    print("Congratulations! You've completed all your Pomodoro cycles.")

if __name__ == "__main__":
    pomodoro()
