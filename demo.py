import asyncio
from web3 import Web3
from web3.middleware import pythonic_middleware

async def web3_basics():
    # Set your WebSocket provider URL
    websocket_url = 'wss://eth-sepolia.g.alchemy.com/v2/KmKrflP4v6rPMPmhLl-zP44PzIJV1t8i'

    # Create a web3 instance with the WebSocketProvider and add middleware
    w3 = Web3(Web3.WebsocketProvider(websocket_url))
    w3.middleware_onion.add(pythonic_middleware)

    # Example: Print the latest block number
    block_number = w3.eth.get_block_number()
    print("Block Number:", block_number)

# Run the event loop
asyncio.get_event_loop().run_until_complete(web3_basics())
