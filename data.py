import requests

# parameters necessary for call to opentdb
parameters = {
    "amount": 10,
    "type": "boolean",
    "category": 18
}

# Uses api to grab information
response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
question_data = response.json()['results']
