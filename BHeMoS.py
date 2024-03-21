import os, webbrowser,subprocess
subprocess.run(['powercfg','/batteryreport'])
username= os.environ.get("USERNAME")
filepath = f'C:\\Users\\{username}\\battery-report.html'
a = input("Would You Like To Open a tips page for improving your battery(y/n)?")
if a.lower()=='y':
    webbrowser.open(r'https://www.pcmag.com/how-to/how-to-increase-laptop-battery-life')

webbrowser.open(filepath)
