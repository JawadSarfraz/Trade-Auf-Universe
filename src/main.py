import os
import json
from api.mexc_spot_api import fetch_spot_order_book

def save_data(exchange, market_type, symbol, data):
    """
    Saves scraped data to the appropriate directory.
    
    Args:
        exchange (str): The exchange name (e.g., mexc).
        market_type (str): Either 'spot'.
        symbol (str): The trading pair (e.g., BTCUSDT).
        data (dict): The scraped data.
    """
    base_path = f"data/raw/{exchange}/{market_type}/"
    os.makedirs(base_path, exist_ok=True)
    file_path = os.path.join(base_path, f"{symbol}.json")
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)
    print(f"Data saved to: {file_path}")

def main():
    print("Welcome to the Crypto Data Scraper!")
    
    # Step 1: Select exchange
    exchanges = ["mexc"]  # Add more exchanges here as you expand
    print("Available Exchanges:", ", ".join(exchanges))
    exchange = input("Enter the exchange you want to scrape (e.g., mexc): ").strip().lower()
    if exchange not in exchanges:
        print(f"Exchange '{exchange}' not supported. Exiting.")
        return
    
    # Step 2: Select coin
    symbol = input("Enter the trading pair you want to scrape (e.g., BTCUSDT): ").strip().upper()
    
    # Step 3: Fetch and save spot data
    if exchange == "mexc":
        print(f"Fetching spot order book for {symbol} from {exchange}...")
        spot_data = fetch_spot_order_book(symbol=symbol, limit=100)
        if spot_data:
            save_data(exchange, "spot", symbol, spot_data)
        else:
            print(f"Failed to fetch spot data for {symbol}.")
    
    print("Scraping complete. Data has been saved.")

if __name__ == "__main__":
    main()
