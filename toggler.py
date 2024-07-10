#!/usr/bin/env python3
import subprocess

# Define the commands
cmd_on = "/home/js/src/bin/openhue set light 8b2382bd-8878-4765-836a-717e7c300bd8 --on"
cmd_off = "/home/js/src/bin/openhue set light 8b2382bd-8878-4765-836a-717e7c300bd8 --off"
get_cmd = "/home/js/src/bin/openhue get light 8b2382bd-8878-4765-836a-717e7c300bd8"

# Function to get the current status of the light
def get_light_status():
    result = subprocess.run(get_cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception("Failed to get light status")
    output = result.stdout
    if "[on]" in output:
        return "on"
    elif "[  ]" in output:
        return "off"
    else:
        raise Exception("Unknown light status")

# Main function to toggle the command
def toggle_command():
    current_status = get_light_status()
    if current_status == "on":
        command = cmd_off
    else:
        command = cmd_on

    # Execute the command
    subprocess.run(command, shell=True)

# Run the toggle command function
if __name__ == "__main__":
    toggle_command()
