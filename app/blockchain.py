class Blockchain:
    def __init__(self) -> None:
        self.chain = []
        self.current_transaction = []

        # create the genesis block (first block)
        self.new_block(previous_hash="1", proof=100)

    def new_block(self, proof, previous_hash=None):
        pass
