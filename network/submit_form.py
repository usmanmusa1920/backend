import requests


def submit_form():
    """Submit a form using python code"""
    
    client = requests.session()
    url="http://127.0.0.1:7000/login/"

    # retrieve the csrf token
    csrf = client.get(url).cookies["csrftoken"]

    login_data = dict(
        username = "Usman",
        password = "passwd123",
        csrfmiddlewaretoken = csrf,
        next = "/"
    )

    resp = client.post(
        url,
        data = login_data,
        headers = dict(Referer = url)
    )
    
    print(f"Headers from a POST request response: {resp.headers}")
    # print(f"\nHTML Response: {resp} {resp.text}")

    if resp.status_code == 200:
        print("\nSuccessfully logged in!", resp)

    
if __name__ == "__main__":
    submit_form()