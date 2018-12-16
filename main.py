from block import *







chain = [PyBlock(0)]
x = input("How many blocks to create?")
x = int(x)


for i in range(x):
    chain.append(PyBlock(chain[i].Hash))
    if i > 0:
        print("Previous Block was Hashed with {hash2}\nBlock: {index} | Hashed with SHA256: {hash} \n\n".format(index = i, hash=str(hex(chain[i].Hash)), hash2=str(hex(chain[i].prevHash))))
