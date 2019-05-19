import csv


class CsvGenerator:

    def __init__(self, path, csv_data):
        self.path = path
        self.csv_data = csv_data

    def create_file(self):
        with open(self.path, 'w', newline='') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerows(self.csv_data)
        csvFile.close()

    @staticmethod
    def custom_headers(list_headers, word_custom):
        custom_list = []
        for string in list_headers:
            custom_list.append(word_custom + "_" + string)
        return custom_list

    @staticmethod
    def combine_list(array_of_lists):
        combined_list = []
        for arr in array_of_lists:
            combined_list = combined_list + arr
        return combined_list

