import json
import matplotlib.pyplot as plt

def load_data(file_path):
    """
    Load order book data from a JSON file.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        dict: Loaded data.
    """
    with open(file_path, "r") as f:
        return json.load(f)

def plot_combined_depth_and_distribution_with_annotations(data):
    """
    Combine depth chart and bar chart in one visualization with key levels annotated.

    Args:
        data (dict): The order book data containing 'bids' and 'asks'.
    """
    if not data or "bids" not in data or "asks" not in data:
        print("Invalid data format.")
        return

    # Convert price and quantity to float
    bids = [(float(price), float(quantity)) for price, quantity in data["bids"]]
    asks = [(float(price), float(quantity)) for price, quantity in data["asks"]]

    # Sort bids and asks
    bids.sort(key=lambda x: x[0], reverse=True)
    asks.sort(key=lambda x: x[0])

    # Cumulative quantities for depth chart
    bid_prices = [x[0] for x in bids]
    bid_quantities = [x[1] for x in bids]
    bid_cumulative = [sum(bid_quantities[:i+1]) for i in range(len(bid_quantities))]

    ask_prices = [x[0] for x in asks]
    ask_quantities = [x[1] for x in asks]
    ask_cumulative = [sum(ask_quantities[:i+1]) for i in range(len(ask_quantities))]

    # Identify key levels
    largest_buy_wall_price = bid_prices[0]
    largest_buy_wall_quantity = bid_quantities[0]
    largest_sell_wall_price = ask_prices[0]
    largest_sell_wall_quantity = ask_quantities[0]

    # Plot combined chart
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # Bar chart for liquidity distribution
    ax1.bar(bid_prices, bid_quantities, color="green", alpha=0.6, label="Bids (Buy Orders)")
    ax1.bar(ask_prices, ask_quantities, color="red", alpha=0.6, label="Asks (Sell Orders)")
    ax1.set_xlabel("Price")
    ax1.set_ylabel("Quantity")
    ax1.legend(loc="upper left")

    # Line chart for depth
    ax2 = ax1.twinx()
    ax2.plot(bid_prices, bid_cumulative, color="darkgreen", label="Bid Depth (Cumulative)")
    ax2.plot(ask_prices, ask_cumulative, color="darkred", label="Ask Depth (Cumulative)")
    ax2.set_ylabel("Cumulative Quantity")
    ax2.legend(loc="upper right")

    # Annotate key levels
    ax1.annotate(f"Largest Buy Wall\nQty: {largest_buy_wall_quantity}",
                 xy=(largest_buy_wall_price, largest_buy_wall_quantity),
                 xytext=(largest_buy_wall_price, largest_buy_wall_quantity * 1.2),
                 arrowprops=dict(facecolor='green', arrowstyle="->"),
                 fontsize=10, color="green")

    ax1.annotate(f"Largest Sell Wall\nQty: {largest_sell_wall_quantity}",
                 xy=(largest_sell_wall_price, largest_sell_wall_quantity),
                 xytext=(largest_sell_wall_price, largest_sell_wall_quantity * 1.2),
                 arrowprops=dict(facecolor='red', arrowstyle="->"),
                 fontsize=10, color="red")

    plt.title("Combined Order Book Visualization with Key Levels")
    plt.show()

if __name__ == "__main__":
    # Example file path (modify as needed)
    file_path = "data/raw/mexc/spot/BTCUSDT.json"

    print(f"Loading data from {file_path}...")
    data = load_data(file_path)

    print("Visualizing order book data with key levels annotated...")
    plot_combined_depth_and_distribution_with_annotations(data)
