import requests


USERNAME_ID = 'id_username'
PASSWORD_ID = 'id_password'
USERNAME = '10002000'
PASSWORD = 'passwd1234'
SIGNUP_URL = 'http://localhost:8000/login'


def submit_form():
    """Submit a form"""

    resp_1 = requests.get(SIGNUP_URL)
    print(f"Response to GET request: {resp_1.content}")

    payload = {USERNAME_ID : USERNAME, PASSWORD_ID : PASSWORD,}
    resp_2 = requests.post(SIGNUP_URL, payload)
    
    print(f"Headers from a POST request response: {resp_2.headers}")
    print(f"HTML Response: {resp_2} {resp_2.text}")

    
if __name__ == '__main__':
    submit_form()
