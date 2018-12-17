from block import *
from user import *
import random


def randomTransaction(users):

    rand1 = random.randint(0,4)
    rand2 = random.randint(5,9)
    sender = users[rand1]
    receiver = users[rand2]
    amount = random.randint(0,sender.wallet)
    sender.wallet-= amount
    receiver.wallet+= amount
    return {"sender":sender.name, "receiver": receiver.name, "amount": amount}



chain = [PyBlock(0, 364)]


# Random user list
Names = ['Ada','Ana','Thomas','Robert','Caroline', 'Joe','Lois','Ben','Amanda','John']
users = []

#
for i in range(10):
    wallet = random.randint(100, 20000)
    users.append(User(Names[i], wallet))
    print("Created {User} with {Wallet}".format(User=users[i].name, Wallet = users[i].wallet))

# print(len(users))

for i in range(100):
    activeBlock = chain[i]
    z = 0
    while(len(activeBlock.transactionData)<100):
        temp = randomTransaction(users)
        # print(str(z) + ". " + str(type(temp)))
        sender = temp["sender"]
        receiver = temp["receiver"]
        amount = temp["amount"]
        # print(str(z) + ". " + sender + " -> " + receiver + " ({amount})".format(amount = amount))
        activeBlock.__newTransaction__(sender, receiver, amount)
        z+=1



    newBlock = PyBlock(activeBlock.Hash, proofOfWork(chain[i].Hash, chain[i].proofOfWork))
    chain.append(newBlock)
    print("Previous Block was Hashed with {hash2}\nBlock: {index} | Hashed with SHA256: {hash} \n\n".format(index = i, hash=str(hex(chain[i].Hash)), hash2=str(hex(chain[i].prevHash))))


print("After transactions;")
for i in range(10):

    print("{User} with {Wallet}".format(User=users[i].name, Wallet = users[i].wallet))



print(chain[2].transactionData[8])
