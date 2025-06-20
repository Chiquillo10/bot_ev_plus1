import requests
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def enviar_mensaje(texto):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": texto}
    requests.post(url, data=data)

mensaje = (
    "📊 Nuevo Pick EV+\n\n"
    "🏟️ Partido: Team A vs Team B\n"
    "✅ Probabilidad: 72%\n"
    "💸 Cuota: 1.80\n"
    "📈 EV+: 0.15"
)

enviar_mensaje(mensaje)
