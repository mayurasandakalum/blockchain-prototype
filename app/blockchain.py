import hashlib
import json
from time import time
from uuid import uuid4
from flask import Flask, jsonify, request


class Blockchain:
    def __init__(self) -> None:
        self.chain = []
        self.current_transaction = []

        # create the genesis block (first block)
        self.new_block(previous_hash="1", proof=100)

    def new_block(self, proof, previous_hash=None):

        # create a new Block in the Blockchain

        block = {
            "index": len(self.chain) + 1,
            "timestamp": time(),
            "transactions": self.current_transaction,
            "proof": proof,
            "previous_hash": previous_hash or self.hash(self.chain[-1]),
        }

        # reset the current list of transactions
        self.current_transaction = []

        self.chain_append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        # creates a new transaction to go into the next mined block
        self.current_transaction.append(
            {"sender": sender, "recipient": recipient, "amount": amount}
        )

        return self.last_block["index"] + 1
