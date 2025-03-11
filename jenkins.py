#This script is used to update config file via script


import argparse
import requests
import maskpass
from requests.auth import HTTPBasicAuth

parser = argparse.ArgumentParser(
    prog="Jenkins Update Custom Config File script",
    description="Script will update Jenkins Config File Provider content."
)

parser.add_argument("--url", required=True)
parser.add_argument("--username", required=True)
parser.add_argument("--apitoken", required=True)
parser.add_argument("--config_id", required=True)
parser.add_argument("--new_content", required=True)
parser.add_argument("--crumb", required=True)

args = parser.parse_args()
password = args.apitoken
updated_content = args.new_content
update_url = f"{args.url}/job/folder/configfiles/saveConfig"

data = {
        "json": (
            f'{{"config": {{"stapler-class": "org.jenkinsci.plugins.configfiles.properties.PropertiesConfig",'
            f' "id": "{args.config_id}", "content": "{updated_content}"}}}}'
        )
    }

update_response = requests.post(
    update_url,
    headers = {"Jenkins-Crumb": args.crumb},
    auth=HTTPBasicAuth(args.username,password),
    data=data
)

if update_response.status_code == 200:
    print("Config file updated successfully!")
else:
    print(f"Failed to update config file.StatusCode: {update_response.status_code}")
    print(update_response.text)
