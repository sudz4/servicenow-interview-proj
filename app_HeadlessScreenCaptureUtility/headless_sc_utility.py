import os
import time
import subprocess
from datetime import datetime
import pyfiglet

"""  
add a watermark here. could be a .svg 
might also be good to have some stats about the project, date, time, client, etc.
bottom right?
"""

# # Set CONSTANT vars
# CLIENT_NAME = 'ServiceNow'  # input the clients name or topic, i.e, ACME Solutions
# meeting_type = 'Training'  # input the meeting type, i.e., CAB (Change Advisory Board)
# CLIENT_NAME = CLIENT_NAME.upper()

"""
SET CONSTANTS
"""
# list of SC responsibilities / use cases for headless screen capture utility program
sc_job_list = ['DEMO', # 0
               'ROM',
               'BE',
               'SOW',
               'RFP',
               'POC',
               'Documentation',
               'Deliverable',
               'NA']
           
# constant set (1)
## select the first item in the SC job list
PURPOSE = sc_job_list[0]  # 'DEMO'
COMPANY = 'ServiceNow'  
WORKFLOW = 'IT' 
CAPABILITY = 'GenAI' 

# constant set (2)
INTERVAL = 5  # in seconds
COUNTDOWN_SECONDS = INTERVAL
RUNTIME_IN_MINUTES = 90  # in minutes

def create_screenshots_folder(company):
    """Send to functional technical specs master (all) folder"""
    top_folder_path = '/Users/sudz4/Desktop/SERVICENOW-INTERVIEW/servicenow-interview-proj/app_HeadlessScreenCaptureUtility/output_technical_functional_specs'
    
    if not os.path.exists(top_folder_path):
        os.makedirs(top_folder_path)

    client_folder_path = os.path.join(top_folder_path, company)
    if not os.path.exists(client_folder_path):
        os.makedirs(client_folder_path)
    
    # Debugging line to ensure the client_folder_path is correct
    print(f"Client folder path: {client_folder_path}")

    return client_folder_path

def interval_countdown(interval):
    for i in range(interval, 0, -1):
        os.system('clear')
        countdown_text = f"Screen Capture Incoming In: {i} seconds"
        large_countdown_text = pyfiglet.figlet_format(str(i), font="big")
        if i == COUNTDOWN_SECONDS:
            print(f"{countdown_text}\n{large_countdown_text}")
        else:
            print(f"{countdown_text}\n{large_countdown_text}")
        time.sleep(1)
    return interval

def take_screenshot(folder_path, workflow):
    # Debugging line to ensure folder_path is correct
    print(f"Saving screenshot to folder: {folder_path}")

    timestamp = time.strftime("%Y%m%d-%H%M%S")
    screenshot_file = os.path.join(folder_path, f"{PURPOSE}_{COMPANY}_{workflow}_{CAPABILITY}_{timestamp}.png")
    
    # Debugging line to ensure the screenshot_file path is correct
    print(f"Screenshot will be saved as: {screenshot_file}")
    
    subprocess.run(["screencapture", "-x", screenshot_file])
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{workflow} screen capture SAVED AS {screenshot_file} @ {current_time}")
    return True

def main():
    end_time = time.time() + RUNTIME_IN_MINUTES * 60
    folder_path = create_screenshots_folder(COMPANY)

    print(f"Machine screen capture in progress ({INTERVAL} second intervals) for {RUNTIME_IN_MINUTES} minutes...")
    print("Press control+c to quit or stop running program")

    while time.time() < end_time:
        remaining_time = interval_countdown(INTERVAL)
        take_screenshot(folder_path, WORKFLOW)
        time.sleep(remaining_time)

def ascii_art_signature():
    ascii_art_sudz4 = r""" # a program by,
███████ ██    ██ ██████  ███████ ██   ██ 
██      ██    ██ ██   ██    ███  ██   ██ 
███████ ██    ██ ██   ██   ███   ███████ 
     ██ ██    ██ ██   ██  ███         ██ 
███████  ██████  ██████  ███████      ██                               
    """
    print(ascii_art_sudz4)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
        print("\nScreen Captures SAVED!")
        print("Thanks for using sCrEeN cApTuRe!")
        ascii_art_signature()
        print()
