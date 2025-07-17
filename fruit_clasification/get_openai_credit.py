import os
import requests
import datetime

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

headers = {
    "Authorization": f"Bearer {OPENAI_API_KEY}"
}

# Fechas para el rango de uso
today = datetime.datetime.now()
start_date = today.replace(day=1).strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")

# Endpoint 1: Uso actual
usage_url = f"https://api.openai.com/v1/dashboard/billing/usage?start_date={start_date}&end_date={end_date}"
usage_response = requests.get(usage_url, headers=headers).json()
used = usage_response.get("total_usage", 0) / 100.0  # se devuelve en centavos

# Endpoint 2: Límite de suscripción (cuota total)
subscription_url = "https://api.openai.com/v1/dashboard/billing/subscription"
subscription_response = requests.get(subscription_url, headers=headers).json()
limit = subscription_response.get("hard_limit_usd", 0)

print(f"🔄 Has usado: ${used:.2f} USD")
print(f"💰 Tu límite total: ${limit:.2f} USD")
print(f"📉 Te queda: ${limit - used:.2f} USD")