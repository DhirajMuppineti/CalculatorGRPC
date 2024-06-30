# CalculatorGRPC

A simple calculator that can add and subtract two numbers in the client via gRPC.

## Features
- Addition of two numbers
- Subtraction of two numbers

## Requirements
- Python 3.8+
- `grpcio` and `grpcio-tools` Python packages

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/DhirajMuppineti/CalculatorGRPC.git
   cd CalculatorGRPC
   
2. **Create a virtual environment (optional but recommended):**

    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`

3. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    Running the Server

4. **Generate gRPC code from the .proto file:**

    ```sh
    python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. calculator.proto

5. **Run the server:**

    ```sh
    python server.py

6. **Running the Client**

    ```sh
    python client.py
