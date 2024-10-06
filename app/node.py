from uuid import uuid4
from flask import Flask, jsonify, request

from blockchain import Blockchain

# initiate our node
app = Flask(__name__)

# generate a globally unique address for this node
node_identifier = str(uuid4()).replace("-", "")

# initiate the blockchain
blockchain = Blockchain()

# API endpoints


@app.route("/mine", methods=["GET"])
def mine():
    # run the Proof of Work algorithm to get the next proof
    last_block = blockchain.last_block
    last_proof = last_block["proof"]
    proof = blockchain.proof_of_work(last_proof)

    # reward the miner by adding a transaction
    blockchain.new_transaction(sender="0", recipient=node_identifier, amount=1)

    # create the new block
    previous_hash = blockchain.hash(last_block)
    block = blockchain.new_block(proof, previous_hash)

    response = {
        "message": "New Block Forged",
        "index": block["index"],
        "transactions": block["transactions"],
        "proof": block["proof"],
        "previous_hash": block["previous_hash"],
    }

    return jsonify(response), 200


@app.route("/transactions/new", methods=["POST"])
def new_transaction():
    values = request.get_json()

    # chech that the required fields are in the POSTed data
    required = ["sender", "recipient", "amount"]
    if not all(k in values for k in required):
        return "Missing values", 400

    # create a new transaction
    index = blockchain.new_transaction(
        values["sender"], values["recipient"], values["amount"]
    )

    response = {"message": f"Transaction will be added to Block {index}"}
    return jsonify(response), 201


@app.route("/chain", methods=["GET"])
def full_chain():
    response = {"chain": blockchain.chain, "length": len(blockchain.chain)}

    return jsonify(response), 200
