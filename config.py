import os

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    print("python-dotenv не установлен. Используйте переменные окружения системы или установите зависимости: pip install -r requirements.txt")

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))  # ID администратора для рассылки

# Ссылки и данные
REVIEWS_CHANNEL = "https://t.me/estasiacars"
COURSE_POST_LINK = "https://t.me/cnchange/185"
YANDEX_MAPS_LINK = "https://yandex.ru/maps/-/CHx3IY9h"

# Социальные сети
SOCIAL_LINKS = {
    "telegram": "https://t.me/cnbridgeru",
    "instagram": "https://www.instagram.com/cn.bridge?igsh=NDRtanJ0YWN5eGs2",
    "vk": "https://vk.com/cnbridge",
    "zen": "https://dzen.ru/id/67485ea7f18c29468e3620c4?share_to=link"
}
