import os
import subprocess
from datetime import datetime, timedelta
from flask import Flask, render_template, request, redirect, url_for, jsonify

# Function to read passwords from files
def read_password(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()

app = Flask(__name__)
# Read passwords from p1.txt and p2.txt
password_children = read_password('p1.txt')
password_self = read_password('p2.txt')
unblock_duration = timedelta(hours=1)  # Duration for which YouTube remains unblocked

unblock_time_children = None  # Store unblock time for children

redirect_ip = "127.0.0.1"
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"

def block_youtube():
    try:
        with open(hosts_path, "r") as file:
            lines = file.readlines()
        
        youtube_blocked = False
        for line in lines:
            if redirect_ip in line and ("youtube.com" in line or "www.youtube.com" in line):
                youtube_blocked = True
                break
        
        if not youtube_blocked:
            with open(hosts_path, "a") as file:
                file.write(f"{redirect_ip} youtube.com\n")
                file.write(f"{redirect_ip} www.youtube.com\n")
            
            print("YouTube successfully blocked.")
            subprocess.run(["ipconfig", "/flushdns"], check=True)
            print("DNS cache flushed.")
        else:
            print("YouTube is already blocked.")
        
    except Exception as e:
        print(f"Failed to block YouTube: {e}")


def unblock_youtube():
    try:
        with open(hosts_path, "r") as file:
            lines = file.readlines()
        
        with open(hosts_path, "w") as file:
            for line in lines:
                if not (redirect_ip in line and ("youtube.com" in line or "www.youtube.com" in line)):
                    file.write(line)
        
        print("YouTube successfully unblocked.")
        subprocess.run(["ipconfig", "/flushdns"], check=True)
        print("DNS cache flushed.")
    except Exception as e:
        print(f"Failed to unblock YouTube: {e}")


def is_children_access_valid():
    global unblock_time_children
    if unblock_time_children is None:
        return False
    elif datetime.now() < unblock_time_children + unblock_duration:
        return True
    else:
        unblock_time_children = None
        block_youtube()
        return False

@app.route('/')
def home():
    if is_children_access_valid():
        # Calculate remaining time
        remaining_time = (unblock_time_children + unblock_duration - datetime.now()).seconds // 60
        return render_template('children_unlocked.html', remaining_time=remaining_time)
    else:
        return render_template('restricted.html')

from flask import redirect

@app.route('/unlock', methods=['POST', 'GET'])
def unlock():
    if request.method == 'GET':
        return redirect(url_for('home'))

    entered_password = request.form['password']
    if entered_password == password_children:
        global unblock_time_children
        unblock_time_children = datetime.now()
        unblock_youtube()
        return redirect(url_for('home'))
    elif entered_password == password_self:
        unblock_youtube()
        return render_template('self_unlocked.html')
    else:
        # Password is incorrect, show alert on restricted page
        return render_template('restricted.html', show_alert=True)


@app.route('/lock-youtube', methods=['POST'])
def lock_youtube_route():
    data = request.get_json()
    action = data.get('action')
    
    if action == 'lock':
        block_youtube()
        return 'YouTube locked', 200
    else:
        return jsonify({'error': 'Invalid action'}), 400



if __name__ == '__main__':
    block_youtube()
    app.run(host='127.0.0.1', port=8000)
