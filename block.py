import hashlib
import datetime, time
import random

def proofOfWork(Hash ,lastProof):
    """
    Naive proofOfWork function for closing old block
    """
    iterator = lastProof + 1
    while not(int(Hash/(2^128)) % iterator == 0 and iterator%23 == 0):
        iterator+=1

    return iterator

class PyBlock:

    def __init__(self,prevHash, proofOfWork):

        self.prevHash = prevHash

        self.timeStamp = str(datetime.datetime.now())
        self.transactionData = []
        self.proofOfWork =  proofOfWork
        self.__hashBlock__()



    def __getTranscationDataBytes__(self):
        """
        Each transaction is a tuple. Each record is added as: '| sender  -> receiver (amount) |' string
        This method reads all transactions in current block saves it to 'tmp' string and returns encoded bytes to '__hashBlock__' method
        """
        tmp = '|'
        for transaction in self.transactionData:
            tmp += transaction[0] + "->" + transaction[1] + "({amount})|".format(amount = transaction[2])

        return tmp.encode('utf=8')


    def __hashBlock__(self):
        """
        This method hashes current block with transaction:
            data
            timestamp
            previous hash
        Every element is byte object (Big Endian)
        """
        hash = hashlib.sha256()

        timeStampBytes = self.timeStamp.encode('utf-8')
        prevHashBytes = (str(hex(self.prevHash))).encode('utf-8')
        transactionDataBytes = self.__getTranscationDataBytes__()

        hash.update(timeStampBytes + transactionDataBytes + prevHashBytes)
        self.Hash = int.from_bytes(hash.digest(), "big")


    def __newTransaction__(self, sender, receiver, amount):
        """
        This method records new transaction through two users (sender, receiver) with 'amount' value
        Every record is immutable tuple type saved in 'transactionData' list## IDEA: vector
        If size of list reached 100 new block is created (post transaction checking)
        """
        tuple = (sender, receiver, amount)
        self.transactionData.append(tuple)
        size = len(self.transactionData)
        if size == 100:
            self.__hashBlock__()
