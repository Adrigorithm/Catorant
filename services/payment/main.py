import logging


def main():
    logging.info("Starting payment service...")
    pass

if __name__ == "__main__":
    # Setup logging
    logging.basicConfig(format="[%(levelname)s] - %(message)s", level=logging.DEBUG)

    main()