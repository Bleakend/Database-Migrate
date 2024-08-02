import logging

def config_logging(file_name="Logs", file_mode="w"):
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s: %(message)s",
        datefmt='%Y-%m-%d,%H:%M:%S',
        filename=f"{file_name}.txt",
        filemode=file_mode
    )