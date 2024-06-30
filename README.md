
# YouTube Blocker for Kidz

## Description
This is a Python-based web application that blocks YouTube access on a Windows system. The application uses Flask as the web framework and provides a simple web interface to block and unblock YouTube. The blocking mechanism works by modifying the system's hosts file to redirect YouTube traffic to a local IP address.



## Features

- Blocks YouTube access on a Windows system
- Provides a simple web interface to block and unblock YouTube
- Allows two types of users: children and self (admin)
- Children can unblock YouTube for a limited duration (1 hour) by - entering a password
- Self (admin) can unblock YouTube permanently by entering a  password
- Displays remaining time for children's unblock duration
- Flushes DNS cache after blocking or unblocking YouTube


## Installation

### Requirements

- Python =>3.10.1
- Flask
- Windows OS (for hosts file manipulation)

### Install dependencies

```bash
  pip install flask
```
### Clone the repository:

```bash
  Open CMD as administrator
  git clone https://github.com/0x4a6f6a6f/Youtube-Blocker-For-Kids.git
  cd Youtube-Blocker-For-Kids
  python youtubeBlocker.py
```


    
## Run Using Executable File

### Set Application Administrator Privilege

- Download project as Zip
- Unzip the project
- Navigate to Release folder > youtubeBlocker folder.
- Locate the youtubeBlocker.exe file
- Right-click on the youtubeBlocker.exe file: Right-click on the executable file and select "Properties" from the context menu.
- Open the Properties window:
- In the Properties window, go to the "Compatibility" tab.
- Towards the bottom of the Compatibility tab, you should see a section titled "Privilege Level" with a checkbox that says "Run this program as an administrator".
- Check this box.
- Apply and Save: Click on "Apply" and then "OK" to save the changes.

### Set Application to run on startup
- Copy the youtubeBlocker.exe file
- Press Win + R on your keyboard to open the Run dialog boxType shell:startup and press Enter. This will open the Startup folder for the current user.
- Paste the youtubeBlocker.exe file.
- Restart your computer or log out and log back in to test if the .exe file runs automatically on startup.
## Usage

- Navigate to http://127.0.0.1:8000 in your web browser.
- Enter the children's password to unlock YouTube for a limited time (1 hour) after one hour it will automatically .
- Enter the self password to unlock YouTube indefinitely.

### Set password
- p1.txt used to store password for childrens
- p2.txt used to store password for others



## Notes

- Ensure proper permissions to modify the hosts file (C:\Windows\System32\drivers\etc\hosts).
- Use responsibly and respect intended usage scenarios.
