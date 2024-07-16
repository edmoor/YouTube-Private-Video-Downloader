import json
import os
import subprocess

json_cookies_path = 'PATH/PATH/PATH'
video_url = 'YT_LINK'

with open(json_cookies_path, 'r') as json_file:
    cookies = json.load(json_file)

temp_cookies_path = 'temp_cookies.txt'

with open(temp_cookies_path, 'w') as netscape_file:
    netscape_file.write("# Netscape HTTP Cookie File\n")
    for cookie in cookies:
        if 'expirationDate' in cookie:
            expiration = int(cookie['expirationDate'])
        else:
            expiration = 0
        domain_specified = 'TRUE' if cookie['domain'].startswith('.') else 'FALSE'
        netscape_file.write("\t".join([
            cookie['domain'],
            domain_specified,
            cookie['path'],
            'TRUE' if cookie['secure'] else 'FALSE',
            str(expiration),
            cookie['name'],
            cookie['value']
        ]) + "\n")

command = [
    'yt-dlp',
    '-f', 'bestvideo+bestaudio/best',
    video_url,
    '--cookies', temp_cookies_path
]
subprocess.run(command)
os.remove(temp_cookies_path)
