import csv
from configs import conf
"""
    Class CsvGenartor gets path and csv_data in format of a list and creates csv file containing that data.
    The class also holds function to manipulate csv data and make it ready to export.
"""


class CsvGenerator:

    def __init__(self, path, csv_data):
        self.path = path
        self.csv_data = csv_data

    """Function saves new file containing the data from csv_data in the path we get in the init function"""
    def create_file(self):
        with open(self.path, 'w', newline='') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerows(self.csv_data)
        csvFile.close()

    """Static function custom_headers gets a list of names(the headers) and a key word to make it uniq expression for 
    headers in the csv file, Function return each name from list_headers with the prefix word_custom"""
    @staticmethod
    def custom_headers(list_headers, word_custom):
        custom_list = []
        for string in list_headers:
            if string != "first_peak":
                custom_list.append(word_custom +"_" + string)
            else:
                for feature in conf.first_peak_features:
                    custom_list.append(word_custom+"_first_peak_"+feature)

        return custom_list

    """Static function custom_headers gets a array which each item is a list and simply combine them into one array with 
     the same order."""
    @staticmethod
    def combine_list(array_of_lists):
        combined_list = []
        for arr in array_of_lists:
            combined_list = combined_list + arr
        return combined_list

