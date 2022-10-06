import hashlib
from os import system

'''
@LayeNdiaye
'''

class NeuralCoinBlock:

    def __init__(self, previous_block_hash, transaction_list):

        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list
        self.Block_data = "-".join(transaction_list)+ "-" +previous_block_hash
        self.block_hash = hashlib.sha256(self.Block_data.encode()).hexdigest()



trans_1 = "laye sends 2 NC to awa"
trans_2 = "joe sends 2.5 NC to awa"
trans_3 = "awa sends 4 NC to joe"
trans_4 = "Alice sends 10 NC to laye"
trans_5 = "awa sends 15 NC to taphe"
trans_6 = "awa sends 6 NC to Mike"

initial_block = NeuralCoinBlock("initial code",[trans_1,trans_2])

print(initial_block.Block_data)
print(initial_block.block_hash)

print()
second_block = NeuralCoinBlock(initial_block.block_hash,[trans_3,trans_5])

print(second_block.Block_data)
print(second_block.block_hash)

print()
third_block = NeuralCoinBlock(second_block.block_hash,[trans_4,trans_6])

print(third_block.Block_data)
print(third_block.block_hash)

# Sample Output!
# If any these block of data is modified, the others blocks will also modified (the hash code will be not same)
 #And that make this system very secure

'''

PS D:\BlockChain> & C:/Users/layen/AppData/Local/Programs/Python/Python310/python.exe d:/BlockChain/Block_Chain.py
laye sends 2 NC to awa-joe sends 2.5 NC to awa-initial code
ed25d71ae153b7828dfc3b7f6c1888c10935aeee44912fbfb13e173659eb8fd7

awa sends 4 NC to joe-awa sends 15 NC to taphe-ed25d71ae153b7828dfc3b7f6c1888c10935aeee44912fbfb13e173659eb8fd7  
e0c83f1ce1f27d526419d536fc32724fe72754f6dbcf8a0fb546270f5d7a9678

Alice sends 10 NC to laye-awa sends 6 NC to Mike-e0c83f1ce1f27d526419d536fc32724fe72754f6dbcf8a0fb546270f5d7a9678
5077090e1be9c93ba1960e1b121d44332dc890afc5174230f872dc6200bfd584
            
'''            