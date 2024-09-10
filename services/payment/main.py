import logging

class PaymentService:
    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)

    def run(self) -> None:
        self.logger.info("Starting payment service...")
        # Payment stuff

if __name__ == "__main__":
    logging.basicConfig(format="[%(levelname)s] - %(message)s", level=logging.DEBUG)

    payment_service = PaymentService()
    payment_service.run()