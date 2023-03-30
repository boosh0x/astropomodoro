import time
import curses

def pomodoro(stdscr, work_duration=25, short_break_duration=5, long_break_duration=15, cycles=4):
    timer_active = True
    timer_paused = True
    reset_timer = False

    stdscr.nodelay(True)
    stdscr.timeout(100)

    instructions = "Commands: (s)tart, (p)ause, (r)eset, (q)uit"
    while True:
        cycle_count = 0
        while cycle_count < cycles:
            timer_active = True
            reset_timer = False
            stdscr.addstr(2, 0, f"Starting work session {cycle_count + 1} of {cycles}.")
            stdscr.addstr(3, 0, instructions)
            stdscr.refresh()

            work_seconds = work_duration * 60
            while work_seconds > 0 and timer_active and not reset_timer:
                user_input = stdscr.getch()

                if user_input == ord('s'):
                    timer_paused = False
                elif user_input == ord('p'):
                    timer_paused = not timer_paused
                elif user_input == ord('r'):
                    reset_timer = True
                    timer_active = False
                    timer_paused = True
                elif user_input == ord('q'):
                    timer_active = False
                    stdscr.clear()
                    stdscr.refresh()
                    curses.endwin()
                    exit(0)

                mins, secs = divmod(work_seconds, 60)
                time_format = '{:02d}:{:02d}'.format(mins, secs)
                stdscr.addstr(0, 0, "Time remaining: " + time_format)
                stdscr.refresh()

                if not timer_paused:
                    time.sleep(1)
                    work_seconds -= 1

            if reset_timer:
                stdscr.clear()
                continue

            if cycle_count < cycles - 1:
                break_duration = short_break_duration
            else:
                break_duration = long_break_duration

            timer_active = True
            stdscr.addstr(1, 0, f"Break time! Relax for {break_duration} minutes.")
            stdscr.refresh()

            break_seconds = break_duration * 60
            while break_seconds > 0 and timer_active and not reset_timer:
                user_input = stdscr.getch()

                if user_input == ord('p'):
                    timer_paused = not timer_paused
                elif user_input == ord('r'):
                    reset_timer = True
                    timer_active = False
                elif user_input == ord('q'):
                    timer_active = False
                    stdscr.clear()
                    stdscr.refresh()
                    curses.endwin()
                    exit(0)

                if not timer_paused:
                    mins, secs = divmod(break_seconds, 60)
                    time_format = '{:02d}:{:02d}'.format(mins, secs)
                    stdscr.addstr(0, 0, "Time remaining: " + time_format)
                    stdscr.refresh()
                    time.sleep(1)
                    break_seconds -= 1

            if reset_timer:
                stdscr.clear()
                break

            cycle_count += 1

        if not reset_timer:
            stdscr.addstr(1, 0, "Congratulations! You've completed all your Pomodoro cycles.")
            stdscr.refresh()
            time.sleep(5)
            break

if __name__ == "__main__":
    curses.wrapper(pomodoro)
