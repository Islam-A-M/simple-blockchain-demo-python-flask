"""Provides verification helper methods. """

from utility.hash_util import hash_block,hash_string_256
from wallet import Wallet


class Verification:
    """
    A helper class which offer various static and class-bassed verification-
    and validation methods.
    """
    @staticmethod
    def valid_proof(transactions, last_hash, proof):
        """Valid a proof of work bumber and see if it silves the puzzle algorithm (two leading 0s).
        Arguments:
        :transactions: The transactions of the block for which the proof is created.
        :last_hash: The previous block's hash which will be stored in the current block.
        :proof: The proof number we're testing.
        """
        guess = (str([tx.to_ordered_dict() for tx in transactions]
                     ) +str(last_hash) + str(proof)).encode()
        guess_hash = hash_string_256(guess)
        print(guess_hash)
        return guess_hash[0:2]=='00'
    @classmethod
    def verify_chain(cls,blockchain):
        """ Verify the current blockchain and return True if it's valid, False otherwise."""
        for index,block in enumerate(blockchain):
            if index ==0:
                continue
            if block.previous_hash != hash_block(blockchain[index-1]):
                return False
            if not cls.valid_proof(block.transactions[:-1],
                                   block.previous_hash,
                                   block.proof):
                print('Proof of work is invalid')
                return False

        return True
    @staticmethod
    def verify_transaction(transaction,get_balance , check_funds = True):
        """
        Verify a transaction by checking whether the sender has sufficient credit.
        Arguments:
        :transaction: The transaction that should be verified.
        :get_balance: Get balance refrence to call this instance function.
        :check_funds: Boolean argument to check if it for check funds and-
        verify transaction or verify transaction only.
        """

        if check_funds:
            sender_balance=get_balance(transaction.sender)
            print('sender_balance')
            print(sender_balance)
            return (sender_balance>=transaction.amount and
                    Wallet.verify_transaction(transaction))
        return Wallet.verify_transaction(transaction)

    @classmethod
    def verify_transactions(cls,open_transactions,get_balance):
        """Verifies all open transactions."""
        # is_valid= True
        # for tx in open_transactions:
        #     if verify_transaction(tx):
        #         is_valid=True
        #     else:
        #         is_valid=False
        # return is_valid
        return all([cls.verify_transaction(tx,get_balance,False) for tx in open_transactions])
