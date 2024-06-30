#YouTube Blocker Tool
YouTube Blocker Tool is a Python-based Flask application designed to manage access to YouTube with password protection. This tool allows you to block and unblock YouTube on a Windows machine based on different password levels. It's an effective solution for parents who want to control their children's access to YouTube or for anyone who wants to restrict their own access to enhance productivity.

#Key Features
Password-Protected Access:
  Children's Password: Allows temporary access to YouTube for one hour.
  Self Password: Unlocks YouTube indefinitely.
Automated Blocking and Unblocking:

#Modifies the Windows hosts file to block or unblock YouTube.
Ensures YouTube remains blocked even after restarting the application.
#User-Friendly Interface:
Simple and intuitive HTML templates for different states (restricted, unlocked for children, unlocked for self).
Alerts for incorrect password entries.
#DNS Cache Management:
Automatically flushes the DNS cache to immediately apply changes to the hosts file.
