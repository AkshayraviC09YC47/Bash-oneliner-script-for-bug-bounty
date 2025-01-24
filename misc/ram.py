import psutil
import time
from prettytable import PrettyTable
from termcolor import colored

def display_ram_usage():
    try:
        while True:
            # Get memory stats
            mem = psutil.virtual_memory()
            total_ram = mem.total / (1024 ** 3)  # Convert to GB
            used_ram = mem.used / (1024 ** 3)   # Convert to GB
            used_percentage = mem.percent       # Used RAM in percentage
            
            # Determine color based on RAM usage
            if used_percentage < 50:
                color = "green"
            elif 50 <= used_percentage < 75:
                color = "yellow"
            else:
                color = "red"

            # Create a pretty table
            table = PrettyTable()
            table.field_names = ["Metric", "Value"]
            table.add_row(["Total RAM", f"{total_ram:.2f} GB"])
            table.add_row(["Used RAM", f"{used_ram:.2f} GB"])
            
            # Clear the screen and print the table
            print("\033c", end="")  # Clear terminal
            print("RAM Usage Monitor (Updated every 2 seconds)")
            print(table)
            
            # Display RAM usage percentage in color
            print(f"Total Used RAM: {colored(f'{used_percentage:.2f}%', color, attrs=['bold'])}")
            
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nExiting RAM monitor. Goodbye!")

if __name__ == "__main__":
    display_ram_usage()
