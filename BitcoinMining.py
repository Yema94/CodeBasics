from hashlib import sha256
import time

max_nonce = 10000000

def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()

def mine(block_number, transactions, previous_hash, prefix_zeros):
    prefix_str = '0'*prefix_zeros
    for nonce in range(1000000, max_nonce):
        text = str(block_number) \
               + transactions \
               + previous_hash \
               + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            print(f"Yay! Successfully mind bitcoins with nonce value:"
                  f"{nonce}")
            return new_hash
    raise BaseException(f"Couldn't find correct hash after trying "
                        f"{max_nonce} times")


if __name__=='__main__':

    transactions = '''
    yesh -> Kiran -> 20,
    Kodimala -> Vamshi -> 25
    '''

    difficulty = 7

    print("Mining Started..")
    start = time.time()

    new_hash = mine(1,
                    transactions,
                    '00000000839a8e6886ab5951d76f411475428afc90947ee320161bbf18eb6048',
                    difficulty)

    total_time = str(time.time() - start)
    print(f"Mining finished...\n Total time taken is {total_time} secs!")

    print(new_hash)
