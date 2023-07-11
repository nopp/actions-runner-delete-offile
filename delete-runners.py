import requests
import json
import os

GHUB_PAT = os.environ['GHUB_PAT']
ORG_NAME = os.environ['ORG_NAME']

headers = { "Accept":"application/vnd.github+json",
            "Authorization":"Bearer "+GHUB_PAT,
            "X-GitHub-Api-Version":"2022-11-28"
           }

r = requests.get('https://api.github.com/orgs/'+ORG_NAME+'/actions/runners',headers=headers).json()['runners']
for runner in r:
    if runner['status'] == "offline":
        print("Removing "+str(runner['id']))
        d = requests.delete('https://api.github.com/orgs/'+ORG_NAME+'/actions/runners/'+str(runner['id']),headers=headers)
        if d.status_code == 204:
            print("Runner successfully deleted.")
