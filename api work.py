import requests
import json

username = 'aws'
repo_name = 'aws-sdk-java-v2'
token = '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'

state = 'closed'
labels= 'bug'

#url --
url = f'https://api.github.com/repos/{username}/{repo_name}/issues'

params = {
    'state': state,
    'labels': labels
}

headers = {
    'Authorization' : f'token {token}',
    'Accept': 'application/vnd.github.v3+json'
} if token else {
    'Accept': 'application/vnd.github.v3+json'
}

response = requests.get(url, headers = headers, params=params)

if response.status_code == 200:
    issues = response.json()
    
    with open('issues.json', 'w') as file:
        json.dump(issues, file, indent=4)
    print("Issues saved")
else:
    print(f"Failed to fetch issues: {response.status_code} - {response.text}")