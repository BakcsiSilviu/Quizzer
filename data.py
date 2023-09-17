import requests

question_data = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean").json()['results']
