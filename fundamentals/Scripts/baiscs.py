
import time
import sys

def countdown(minutes, label):
    """Core timer logic with a dynamic terminal display."""
    seconds = minutes * 60
    print(f"\n--- {label} ---")

    while seconds:
        mins, secs = divmod(seconds, 60)

        timer_format = f"{mins:02d}:{secs:02d}"
        print(f"Time Remaining: {timer_format}", end="\r")
        time.sleep(1)
        seconds -= 1

    print(f"{label} Complete!                ")

def start_pomodoro(work_mins=25, break_mins=5):
    """Main loop to alternate between work and rest."""
    try:
        print("Pomodoro Timer Started. Press Ctrl+C to stop.")
        while True:
            countdown(work_mins, "WORK TIME")
            print("\a")

            countdown(break_mins, "BREAK TIME")
            print("\a")

            cont = input("\nStart next session? (y/n): ").lower()
            if cont != 'y':
                break
    except KeyboardInterrupt:
        print("\n\nTimer stopped. Great work today!")

if __name__ == "__main__":
    start_pomodoro(work_mins=25, break_mins=5)