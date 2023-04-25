import ressyy
import random
from web3 import Web3

def generate_random_mnemonic(words):
    return ' '.join([random.choice(words).replace("\n", "") for i in range(12)]).strip(" ")


words = open("words.txt", "r", encoding="utf-8").readlines()

w3  = Web3(Web3.HTTPProvider("https://eth.llamarpc.com"))
w32 = Web3(Web3.HTTPProvider("https://bsc-dataseed1.ninicoin.io"))

while True:
    try:

        wallet = generate_random_mnemonic(words)
        w3.eth.account.enable_unaudited_hdwallet_features()
        account = w3.eth.account.from_mnemonic(wallet, account_path="m/44'/60'/0'/0/0")
        nonce = w3.eth.get_transaction_count(account.address)
        nonce += w32.eth.get_transaction_count(account.address)
        if nonce > 0:
            print(wallet)
    except:
        pass
