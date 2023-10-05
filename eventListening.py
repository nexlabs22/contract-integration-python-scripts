from web3 import Web3, AsyncWeb3
from abi import tokenAbi
from contractAddresses import usdcAddress
import os
from dotenv import load_dotenv
from web3.middleware import construct_sign_and_send_raw_middleware
import time

load_dotenv()  # take environment variables from .env.

ALCHEMY_GOERLI_RPC = os.environ.get('ALCHEMY_GOERLI_RPC')

# IPCProvider:
w3 = Web3(Web3.HTTPProvider(ALCHEMY_GOERLI_RPC))


print("is connected :", w3.is_connected())

#create contract
contract = w3.eth.contract(abi=tokenAbi, address=usdcAddress)

#read contract function
name = contract.functions.name().call()

print("name :", name)


def handle_event(event):
    print(event)

def log_loop(event_filter, poll_interval):
    while True:
        for event in event_filter.get_new_entries():
            handle_event(event)
        time.sleep(poll_interval)

def main():
    # block_filter = w3.eth.filter('latest')
    event_filter = contract.events.Transfer.create_filter(fromBlock="latest")
    # log_loop(block_filter, 2)
    log_loop(event_filter, 2)

if __name__ == '__main__':
    main()



