from flask import Flask
from app.webhook_handlers import voice_webhook

app = Flask(__name__)
app.add_url_rule('/voice/webhook', view_func=voice_webhook, methods=['POST'])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
