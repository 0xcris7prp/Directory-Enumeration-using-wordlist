import requests
import sys
sub_list = open("wordlist.txt").read()
directories = sub_list.splitlines()

for x in directories:
    dir_enum = f"http://{sys.argv[1]}/{x}.html"
    r = requests.get(dir_enum)
    if r.status_code == 404:
        pass
    else:
        print("valid directory found", dir_enum)
