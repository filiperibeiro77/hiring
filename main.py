from block_io import BlockIo
import sys

version = 2
block_io = BlockIo('e61b-2513-431a-3906', 'shakurraph2', version)

def send_bitcoin():
        block_io.withdraw_from_labels(
        amounts='0.001',
        from_labels='default',
        to_addresses='2N23YsTMNSdgxcfebqekGcJjDEkqKk8eunm',
        pin='shakurraph2'
    )

if __name__ == "__main__":
    print(send_bitcoin())
