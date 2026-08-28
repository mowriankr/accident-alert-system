import requests


BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"


def send_telegram_alert(latitude, longitude):

    message = (
        "🚨 ACCIDENT DETECTED!\n\n"
        "📍 Location:\n"
        f"Latitude: {latitude}\n"
        f"Longitude: {longitude}\n\n"
        f"🗺️ Google Maps:\n"
        f"https://www.google.com/maps?q={latitude},{longitude}"
    )

    url = (
        f"https://api.telegram.org/bot"
        f"{BOT_TOKEN}/sendMessage"
    )

    data = {
        "chat_id": CHAT_ID,
        "text": message
    }

    response = requests.post(url, data=data)

    print("Telegram response:", response.text)
