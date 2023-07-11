import requests
import json

RUNNER_TOKEN="xxxxx"
ORG_NAME="yyyy"

headers = { "Accept":"application/vnd.github+json",
            "Authorization":"Bearer "+RUNNER_TOKEN,
            "X-GitHub-Api-Version":"2022-11-28"
           }

r = requests.get('https://api.github.com/orgs/'+ORG_NAME+'/actions/runners',headers=headers).json()['runners']
for runner in r:
    if runner['status'] == "offline":
        print("Removing "+str(runner['id']))
        d = requests.delete('https://api.github.com/orgs/'+ORG_NAME+'/actions/runners/'+str(runner['id']),headers=headers)
        if str(d.status_code) == "204":
            print("Runner successfully deleted.")
