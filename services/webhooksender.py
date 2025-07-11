import requests

def send_webhook():
    webhook_url = input("Enter the Discord Webhook URL: ").strip()
    username = input("Enter a username for the message (optional): ").strip()
    message = input("Enter the message to send: ").strip()

    data = {
        "content": message
    }

    if username:
        data["username"] = username

    response = requests.post(webhook_url, json=data)

    if response.status_code == 204:
        print("✅ Message sent successfully!")
    else:
        print(f"❌ Failed to send message. Status Code: {response.status_code}")
        print(response.text)