from block import *
from user import *
import random





chain = [PyBlock(0, 364)]


# Random user list
Names = ['Ada','Ana','Thomas','Robert','Caroline', 'Joe','Lois','Ben','Amanda','John']
users = []
print(len(users))

#
for i in range(10):
    wallet = random.randint(100, 20000)
    users.append(User(Names[i], wallet))
    print("Created {User} with {Wallet}".format(User=users[i].name, Wallet = users[i].wallet))

for i in range(3):

    newBlock = PyBlock(chain[i].Hash, proofOfWork(chain[i].Hash, chain[i].proofOfWork))
    chain.append(newBlock)
    print("Previous Block was Hashed with {hash2}\nBlock: {index} | Hashed with SHA256: {hash} \n\n".format(index = i, hash=str(hex(chain[i].Hash)), hash2=str(hex(chain[i].prevHash))))
