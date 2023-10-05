from web3 import Web3, AsyncWeb3
from abi import tokenAbi
from contractAddresses import usdcAddress
import os
from dotenv import load_dotenv
from web3.middleware import construct_sign_and_send_raw_middleware

load_dotenv()  # take environment variables from .env.

ALCHEMY_GOERLI_RPC = os.environ.get('ALCHEMY_GOERLI_RPC')

# IPCProvider:
w3 = Web3(Web3.HTTPProvider(ALCHEMY_GOERLI_RPC))


# Note: Never commit your key in your code! Use env variables instead:
pk = os.environ.get('PRIVATE_KEY')

# Instantiate an Account object from your key:
acc = w3.eth.account.from_key(pk)

print("is connected :", w3.is_connected())

#create contract
contract = w3.eth.contract(abi=tokenAbi, address=usdcAddress)

#read contract function
name = contract.functions.name().call()

print("name :", name)

w3.middleware_onion.add(construct_sign_and_send_raw_middleware(acc))

print("Sending transaction...")
tx_hash = contract.functions.transfer('0xe98A6145acF43Fa2f159B28C70eB036A5Dc69409', 1000).transact({
    "from": acc.address
})

print("Transaction sent, wait for receipt...")
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

if(tx_receipt.status == 1):
    print("Success")
else:
    print("failed")



