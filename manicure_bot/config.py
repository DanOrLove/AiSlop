import os
from dotenv import load_dotenv

load_dotenv()

# Токен бота
BOT_TOKEN = os.getenv("BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")

# ID администратора (можно несколько через запятую)
ADMIN_IDS = list(map(int, os.getenv("ADMIN_IDS", "123456789").split(",")))

# Канал для уведомлений
CHANNEL_ID = os.getenv("CHANNEL_ID", "@your_channel")
CHANNEL_LINK = os.getenv("CHANNEL_LINK", "https://t.me/your_channel  ")

# База данных
DB_PATH = os.getenv("DB_PATH", "bot_database.db")

# Часовой пояс для планировщика
TIMEZONE = os.getenv("TIMEZONE", "Europe/Moscow")