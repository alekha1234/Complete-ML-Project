import logging
import sys
import os
from datetime import datetime

# Generate a folder name based on the current date
current_date = datetime.now().strftime('%d_%m_%Y')
logs_path = os.path.join(os.getcwd(), "logs", current_date)

# Create the logs directory for the current date if it doesn't exist
os.makedirs(logs_path, exist_ok=True)

# Generate a log file name with the current date and time
LOG_FILE = f"{datetime.now().strftime('%H_%M_%S_Exception')}.log"

# Define the full path for the log file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure the logging settings
logging.basicConfig(
    filename=LOG_FILE_PATH,  # Set the log file path
    format="Time: %(asctime)s\n Line No: %(lineno)d\n Logger Name: %(name)s - \n Level Name: %(levelname)s - \n Message: %(message)s",  # Define the log message format,  # Define the log message format
    level=logging.INFO  # Set the logging level to INFO
)

def error_message_details(error, error_detail: sys):
    """
    Function to extract and format the error message details.

    Parameters:
    error (Exception): The exception object that was raised.
    error_detail (sys): The sys module to get exception info.

    Returns:
    str: A formatted string containing the filename, line number, and error message.
    """
    # Extracts the traceback object (exc_tb) from the exception info
    _, _, exc_tb = error_detail.exc_info()
    
    # Retrieves the filename where the error occurred
    file_name = exc_tb.tb_frame.f_code.co_filename
    
    # Formats the error message to include the filename, line number, and error message
    error_message = "\n Error occurred in : [{0}] \n Line number : [{1}] \n Error message : [{2}]".format(
        file_name, 
        exc_tb.tb_lineno, 
        str(error)
    )

    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        """
        Custom Exception class to handle and format exception messages.

        Parameters:
        error_message (str): The error message string.
        error_detail (sys): The sys module to get exception info.
        """
        # Initialize the base Exception class with the error message
        super().__init__(error_message)
        
        # Generate the detailed error message using the error_message_details function
        self.error_message = error_message_details(error_message, error_detail=error_detail)

        # Log the error message
        logging.error(self.error_message)

    def __str__(self):
        """
        Override the __str__ method to return the formatted error message.

        Returns:
        str: The detailed error message.
        """
        return self.error_message
