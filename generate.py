from solders.keypair import Keypair
from solders.pubkey import Pubkey
from solders.system_program import TransferParams, transfer
from solana.transaction import Transaction
from solana.rpc.api import Client

def generate_solana_address(suffix_list, num_threads=12):
    from concurrent.futures import ThreadPoolExecutor, as_completed
    
    def generate_keypair_and_check_suffix():
        while True:
            keypair = Keypair()
            address = str(keypair.pubkey())
            print(address)
            if any(address.lower().endswith(suffix.lower()) for suffix in suffix_list):
                return keypair, address

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = [executor.submit(generate_keypair_and_check_suffix) for _ in range(num_threads)]
        for future in as_completed(futures):
            keypair, address = future.result()
            print(f"Address: {address}")
            print(f"Private Key: {keypair}")

suffix_list = []
generate_solana_address(suffix_list)
