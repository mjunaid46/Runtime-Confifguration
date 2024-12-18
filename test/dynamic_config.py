
import time
import logging
import configparser

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def read_and_print_config(file_path):
    """
    Reads a config.ini file and prints its content in a clear format.
    :param file_path: Path to the config.ini file
    """
    config = configparser.ConfigParser()
    try:
        # Read the config file
        config.read(file_path)
        # Check if the file was successfully read
        if not config.sections():
            print("The config file is empty or not found.")
            return
        # Print the sections and their key-value pairs
        for section in config.sections():
            print(f"[{section}]")
            for key, value in config.items(section):
                print(f"{key} = {value}")
            print()  # Add an empty line for better readability
    except Exception as e:
        print(f"Error reading config file: {e}")









while True:
    logging.info("Printt")
    # print("Hello")
    
    # Example usage
    file_path = "config2.ini"
    read_and_print_config(file_path)
    time.sleep(1)
