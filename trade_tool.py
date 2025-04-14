import sys 
import os
from dotenv import load_dotenv

import ccxt



def main():
    # Load environment variables from .env file
    load_dotenv()
    #btc
    symbol = sys.argv[1:][0].upper()
    #currency
    currency = sys.argv[1:][1].upper()
    #maker or taker
    trade_type = sys.argv[1:][2]
    #buy or sell
    direction = sys.argv[1:][3].capitalize()
    total_amount = float(sys.argv[1:][4])
    ice_amount = float(sys.argv[1:][5])
    # Get the API keys from environment variables
    binance_api_key = os.getenv('BN_API_KEY')
    binance_secret_key = os.getenv('BN_SECRET_KEY')

    if not binance_api_key or not binance_secret_key:
        print("API keys are not set in the environment variables.")
        sys.exit(1)

    # Initialize the Binance exchange
    exchange = ccxt.binance({
        'apiKey': binance_api_key,
        'secret': binance_secret_key,
        'options': { 'defaultType': 'spot' }
    })

    # order_type = "limit" if trade_type == "maker" else "market"
    post_only = True if trade_type == "maker" else False    
    # Example: Fetch balance
    try:
        # Create a post-only limit order
        # Fetch the order book to get the latest bid and ask prices
        order_book = exchange.fetch_order_book(f"{symbol}/{currency}")
        bid_price = order_book['bids'][0][0] if order_book['bids'] else None
        ask_price = order_book['asks'][0][0] if order_book['asks'] else None

        if direction == "Buy":
            price = ask_price  # Use the ask price for buy orders
        elif direction == "Sell":
            price = bid_price  # Use the bid price for sell orders
        else:
            raise ValueError("Invalid direction. Must be 'Buy' or 'Sell'.")
        print("Price:", price)
        if price is None:
            raise ValueError("Could not fetch a valid price from the order book.")
        order = exchange.create_order(
            symbol=f"{symbol}/{currency}",
            type="limit",
            side=direction,
            amount=ice_amount,
            price=price,  # Specify the price for the limit order
            params={'postOnly': post_only}
        )
        print("Order placed:", order)
    except Exception as e:
        print("Error placing order:", str(e))
    
if __name__ == "__main__":
    main()