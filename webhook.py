import requests

def send_webhook(new_jobs):
    webhook_url = "http://webhook.net"

    data = {f"content": "Wake up! there is {new_jobs} new job posts!"}

    try:
        response = requests.post(webhook_url, json=data)
        print(f"Status code: {response.status_code}")
        print(f"Response body: {response.text}")
    except Exception as e:
        print(f"An error occurred: {e}")