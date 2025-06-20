import requests

BOT_TOKEN = "7738392758:AAFsMfvVcA1xingWTYmwdBjkR2DO6ozP8Ek"
CHAT_ID = "7943883784"

def enviar_mensaje(texto):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": texto}
    requests.post(url, data=data)

mensaje = "📊 Nuevo Pick EV+

🏟️ Partido: Team A vs Team B
✅ Probabilidad: 72%\n💸 Cuota: 1.80\n📈 EV+: 0.15"
enviar_mensaje(mensaje)