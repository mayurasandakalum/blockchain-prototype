# Simple Blockchain Implementation

This project is a basic implementation of a blockchain using Python and Flask. It includes functionalities such as creating blocks, adding transactions, mining new blocks, and maintaining consensus across multiple nodes.

## Features

- **Create Blocks:** Generate new blocks with a proof of work.
- **Add Transactions:** Record transactions to be added to the blockchain.
- **Mine Blocks:** Implement Proof of Work to mine new blocks.
- **Register Nodes:** Connect multiple nodes to form a decentralized network.
- **Consensus Algorithm:** Ensure all nodes agree on the blockchain state.

## Getting Started

### Prerequisites

- Python 3.x
- `pip` package manager

### Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/mayurasandakalum/blockchain-prototype.git
    cd blockchain-prototype
    ```

2. **Create a Virtual Environment (Optional but Recommended)**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

```bash
python run.py
