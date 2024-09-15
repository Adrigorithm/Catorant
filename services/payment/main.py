from concurrent import futures


import logging
import grpc

from generated import payment_pb2_grpc
from src import Payment


def main() -> None:
    logging.info("Starting payment service...")
    pass

def serve(port: int = 20001, max_instances: int = 20) -> None:
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=max_instances))
    payment_pb2_grpc.add_PaymentServicer_to_server(Payment(), server)
    server.add_insecure_port(f"[::]:{port}")
    
    server.start()
    logging.info(f"Payment service listening on port {port}.")
    server.wait_for_termination()


if __name__ == "__main__":
    # Setup logging
    logging.basicConfig(format="[%(levelname)s] - %(message)s", level=logging.DEBUG)

    main()