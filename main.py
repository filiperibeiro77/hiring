from block_io import BlockIo
version = 2
block_io = BlockIo('e61b-2513-431a-3906', 'shakurraph2', version)

block_io.withdraw_from_labels(amounts='0.00001000', from_labels='default', to_addresses='2N23YsTMNSdgxcfebqekGcJjDEkqKk8eunm', pin='shakurraph2')

print(block_io.status)
