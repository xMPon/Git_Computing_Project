from env.BackEnd.chain import Chain


b = Chain()
print("GET READY MINING ABOUT TO START")
print(b.chain)

last_block = b.latest_block
last_proof = last_block.proof_number
proof_number = b.proof(last_proof)
b.get_data(
    sender="business",  # this means that this node has constructed another block
    receiver="manufacturer",
    amount=1,  # building a new block (or figuring out the proof number) is awarded with 1
)
last_hash = last_block.compute_hash
block = b.build_block(proof_number, last_hash)
print("WOW, MINING HAS BEEN SUCCESSFUL!")
print(b.chain)
