import requests

BASE_URL = "https://api.mexc.com/api/v3"

def fetch_spot_order_book(symbol="BTCUSDT", limit=100):
    endpoint = f"{BASE_URL}/depth"
    params = {"symbol": symbol, "limit": limit}
    try:
        response = requests.get(endpoint, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching spot order book: {e}")
        return None
