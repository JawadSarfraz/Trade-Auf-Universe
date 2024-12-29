import requests

BASE_URL = "https://contract.mexc.com/api/v1"

def fetch_futures_order_book(symbol="BTC_USDT", limit=100):
    endpoint = f"{BASE_URL}/depth/symbol"
    params = {"symbol": symbol, "limit": limit}
    try:
        response = requests.get(endpoint, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching futures order book: {e}")
        return None
