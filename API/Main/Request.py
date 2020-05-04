import requests;          # library of requesting data from the web or server

def main():
    res = requests.get('https://renter-server.herokuapp.com/api/user')
    print(res.json())

if __name__ == '__main__':
    main();