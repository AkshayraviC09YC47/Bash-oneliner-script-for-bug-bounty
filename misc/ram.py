import psutil
import time
import os
from prettytable import PrettyTable
from termcolor import colored

def clear_screen():
    """Clear the terminal screen based on the operating system."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_ram_usage():
    """Retrieve and format RAM usage information."""
    mem = psutil.virtual_memory()
    total_ram = mem.total / (1024 ** 3)  # Convert to GB
    used_ram = mem.used / (1024 ** 3)    # Convert to GB
    used_percentage = mem.percent        # Used RAM in percentage
    return total_ram, used_ram, used_percentage

def get_cpu_usage():
    """Retrieve and format CPU usage information."""
    cpu_usage = psutil.cpu_percent(interval=1)  # CPU usage over 1 second
    return cpu_usage

def get_status(usage):
    """Determine status and color based on usage percentage."""
    if usage < 30:
        return "LOW", "blue"
    elif 30 <= usage < 60:
        return "MEDIUM", "yellow"
    elif 60 <= usage < 90:
        return "HIGH", "red"
    else:
        return "CRITICAL", "on_red"  # "on_red" for dark red background

def display_system_status():
    """Display RAM and CPU usage in a formatted table with color-coded status."""
    try:
        while True:
            # Get RAM and CPU usage
            total_ram, used_ram, ram_percentage = get_ram_usage()
            cpu_usage = get_cpu_usage()

            # Determine status and color for RAM and CPU usage
            ram_status, ram_color = get_status(ram_percentage)
            cpu_status, cpu_color = get_status(cpu_usage)

            # Create a pretty table
            table = PrettyTable()
            table.field_names = ["Metric", "Value", "Status"]
            table.add_row([
                "RAM Usage",
                f"{used_ram:.2f} GB",
                colored(ram_status, ram_color, attrs=["bold"])
            ])
            table.add_row([
                "CPU Usage",
                f"{cpu_usage:.2f}%",
                colored(cpu_status, cpu_color, attrs=["bold"])
            ])

            # Clear the screen and print the table
            clear_screen()
            print("System Usage Monitor (Updated every 2 seconds)")
            print(f"Total System RAM: {total_ram:.2f} GB")
            print(table)

            time.sleep(2)
    except KeyboardInterrupt:
        print("\nExiting system monitor. Goodbye!")

if __name__ == "__main__":
    display_system_status()
