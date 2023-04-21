# ROUTINES TO CREATE, WRITE AND READ ATHLETE DATA FILE
# ====================================================

# LIBRARIES AND MODULES

import json

# CLASS DEFINITIONS

class ProcessJsonFile():

    def __init__(self):
        pass

    

    def saveData(self, file, data):
        """Saves all athelete data to disk

        Args:
            file (str): Name of the file
            data (list): List of dictionaries 
        Returns:
            tuple: Error code, Error message, detailed error message 
        """
        status = (0, 'Tallennus onnistui', 'All data saved successfully')
        return status
    
    def readData(self, file):
        """Reads athlete data from file

        Args:
            file (str): Name of the file

        Returns:
            tuple: Error code, Error message, detailed error message, data
        """
        data = (0, message, detailedMessage, readinfo)
        return data

    def appendData(self, file, data):
        """Adds a new json object to the file

        Args:
            file (str): Name of the file
            data (dict): python dictionary containing data

        Returns:
            tuple: Error code, Error message, detailed error message
        """

        status = (0, 'Tallennus onnistui', 'Data saved successfully')
        return status

# PRELIMINARY TESTS

if __name__ == "__main__":
    pass