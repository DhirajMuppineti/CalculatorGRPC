import grpc
import calculator_pb2
import calculator_pb2_grpc


def add(num1, num2):
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = calculator_pb2_grpc.CalculatorStub(channel)
        response = stub.Add(calculator_pb2.AddRequest(num1=num1, num2=num2))
    print(f"Result: {response.result}")


def sub(num1, num2):
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = calculator_pb2_grpc.CalculatorStub(channel)
        response = stub.Sub(calculator_pb2.SubRequest(num1=num1, num2=num2))
    print(f"Result: {response.result}")


if __name__ == "__main__":
    # Get user Input
    num1 = int(input("Please input num1: "))
    num2 = int(input("Please input num2: "))
    
    print("Choose your operation:")
    print("1. Add")
    print("2. Sub")
    
    inp = input()
    if "1" in inp.lower() or "add" in inp.lower():
        add(num1, num2)
    elif "2" in inp.lower() or "sub" in inp.lower():
        sub(num1, num2)
        
