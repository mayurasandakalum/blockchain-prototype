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

    @staticmethod
    def hash(block):
        # creates a SHA-256 hash of a Block
        block_string = json.dumps(block, sort_keys=True).encode()

        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        return self.chain[-1]

    def proof_of_work(self, last_proof):
        # Simple Proof of Work Algorithm:
        #     - Find a number p' such that hash(pp') contains leading 4 zeros
        #     - p is the previous proof, and p' is the new proof

        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1

        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        # validates the proof: does hash(last_proof, proof) contains 4 leading zeros?
        guess = f"{last_proof}{proof}".encode()
        guess_hash = hashlib.sha256(guess).hexdigest()

        return guess_hash[:4] == "000"
