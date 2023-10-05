from web3.middleware import construct_sign_and_send_raw_middleware
from web3 import Web3, AsyncWeb3
import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

# IPCProvider:
w3 = Web3(Web3.HTTPProvider('https://eth-goerli.g.alchemy.com/v2/LOxUiFd7inEC7y9S-rxGH-_FmJjLlYC1'))

# Note: Never commit your key in your code! Use env variables instead:
pk = os.environ.get('PRIVATE_KEY')

# Instantiate an Account object from your key:
acc = w3.eth.account.from_key(pk)

print("Sending transaction...")
# For the sake of this example, fund the new account:
tx_hash = w3.eth.send_transaction({
    "from": acc.address,
    "value": "1000",
    "to": "0xe98A6145acF43Fa2f159B28C70eB036A5Dc69409"
})

print("Transaction sent, wait for receipt...")

receipt = w3.eth.get_transaction_receipt(tx_hash)

if(receipt.status == 0):
    print("Success") else print("failed")
