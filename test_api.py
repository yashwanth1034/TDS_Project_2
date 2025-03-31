import requests

url = "http://localhost:8000/api/"
files = {
    'file': ('abcd.zip', open('abcd.zip', 'rb')),
    'question': (None, 'Download and unzip file abcd.zip which has a single extract.csv file inside. What is the value in the answer column of the CSV file?')
}

response = requests.post(url, files=files)
print(response.json()) 