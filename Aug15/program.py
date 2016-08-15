import requests

if __name__ == '__main__':
    docs = requests.get('http://docs.python-requests.org/en/master/')
    print(docs.status_code)
