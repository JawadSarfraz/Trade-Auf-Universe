import json
import os

def load_data(file_path):
    """
    Load order book data from a JSON file.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        dict: Loaded data.
    """
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return None
    with open(file_path, "r") as f:
        return json.load(f)

def analyze_order_book(data, depth=10):
    """
    Analyze the order book data to identify significant buy and sell walls.

    Args:
        data (dict): The order book data containing 'bids' and 'asks'.
        depth (int): Number of top levels to analyze.

    Returns:
        dict: Analysis results with top bids and asks.
    """
    if not data or "bids" not in data or "asks" not in data:
        print("Invalid data format.")
        return None

    # Convert price and quantity to float for numerical operations
    bids = [(float(price), float(quantity)) for price, quantity in data["bids"][:depth]]
    asks = [(float(price), float(quantity)) for price, quantity in data["asks"][:depth]]

    # Sort bids by price descending, asks by price ascending
    bids.sort(key=lambda x: x[0], reverse=True)
    asks.sort(key=lambda x: x[0])

    return {"top_bids": bids, "top_asks": asks}

def display_analysis(results):
    """
    Display the top bids and asks.

    Args:
        results (dict): Analysis results with 'top_bids' and 'top_asks'.
    """
    if not results:
        print("No results to display.")
        return

    print("\n--- Top Bids (Buy Orders) ---")
    for price, quantity in results["top_bids"]:
        print(f"Price: {price}, Quantity: {quantity}")

    print("\n--- Top Asks (Sell Orders) ---")
    for price, quantity in results["top_asks"]:
        print(f"Price: {price}, Quantity: {quantity}")

if __name__ == "__main__":
    # Example file path (modify as needed)
    file_path = "data/raw/mexc/spot/BTCUSDT.json"

    print(f"Loading data from {file_path}...")
    data = load_data(file_path)

    if data:
        print("Analyzing order book data...")
        results = analyze_order_book(data, depth=100)
        display_analysis(results)
