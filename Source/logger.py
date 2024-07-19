import logging
import os
from datetime import datetime

# Generate a folder name based on the current date
current_date = datetime.now().strftime('%d_%m_%Y')
logs_path = os.path.join(os.getcwd(), "logs", current_date)

# Create the logs directory for the current date if it doesn't exist
os.makedirs(logs_path, exist_ok=True)

# Generate a log file name with the current time
LOG_FILE = f"{datetime.now().strftime('%H_%M_%S_LOG')}.log"

# Define the full path for the log file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure the logging settings
logging.basicConfig(
    filename=LOG_FILE_PATH,  # Set the log file path
    format="Time: %(asctime)s\n Line No: %(lineno)d\n Logger Name: %(name)s - \n Level Name: %(levelname)s - \n Message: %(message)s",  # Define the log message format
    level=logging.INFO  # Set the logging level to INFO
)

# Example usage: logging an info message
logging.info("This is a log message.")