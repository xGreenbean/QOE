import sqlite3
import pandas as pd
from sqlite3 import Error
global MessageData
global Timestamp
global netflix_start_end
global youtube_start_end
global netflix_qualities
global youtube_qualities
global time_first_picture

MessageData = 4
Timestamp = 5
netflix_start_end = ["Netflix,App,Loaded", "Netflix,App,Displaying ended"]
youtube_start_end = ["Start YouTube Service,A", "Youtube Service,Player,Video display duration reached"]
netflix_qualities = "Netflix,App,New resolution"
youtube_qualities = "Youtube Service,Player,New resolution"
time_first_picture = "Time to 1st picture"


class DataParser:

    def __init__(self, sql_file, csv_path):
        self.sql_file = DataParser.create_connection(sql_file)
        self.df = pd.read_csv(csv_path)

    def get_rows_by_query(self, query):
        cur = self.sql_file.cursor()
        cur.execute(query)
        return cur.fetchall()

    @staticmethod
    def create_connection(db_file):
        """ create a database connection to the SQLite database
            specified by the db_file
        :param db_file: database file
        :return: Connection object or None
        """
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(e)

        return None

    @staticmethod
    def timestamp_to_epoch(time_stamp):
        return (float(time_stamp) - 25569) * 86400

    @staticmethod
    def filter_rows_by_time(selected_rows, start_time, end_time):
        filtered_rows = []
        for row in selected_rows:
            epoch_row = DataParser.timestamp_to_epoch(row[Timestamp])
            if epoch_row > start_time and epoch_row <= end_time:
                filtered_rows.append(row)
        return filtered_rows

    @staticmethod
    def extract_qoe_string(quality_string_list):
        qualities = []
        for quality_string in quality_string_list:
            qualities.append(quality_string[MessageData].split(':')[1].split('x')[1])
        return qualities

    @staticmethod
    def extract_delay_string(delays_string_list):
        return delays_string_list[0][MessageData].split(':')[1].split('s')[0]

    def divide_playbacks(self):
        divided_metrics = []
        start_video_msgs = self.get_rows_by_query("SELECT * FROM Message Where MessageData Like '%{0}%' "
                                                  "OR MessageData LIKE '%{1}%'".format(youtube_start_end[0],
                                                                                       netflix_start_end[0]))
        ended_video_msgs = self.get_rows_by_query("SELECT * FROM Message Where MessageData Like '%{0}%' "
                                                  "OR MessageData LIKE '%{1}%'".format(youtube_start_end[1],
                                                                                       netflix_start_end[1]))
        qualities_rows = self.get_rows_by_query("SELECT * FROM Message Where MessageData Like '%{0}%' "
                                                "OR MessageData LIKE '%{1}%'".
                                                format(netflix_qualities, youtube_qualities))
        start_delay_rows = self.get_rows_by_query("SELECT * FROM Message Where "
                                                  "MessageData Like '%{0}%'".format(time_first_picture))
        for i in range(len(start_video_msgs)):

            df_interval = self.df[(self.df['frame.time_epoch'] <
                                   DataParser.timestamp_to_epoch(ended_video_msgs[i][Timestamp])) &
                                  (self.df['frame.time_epoch'] >=
                                   DataParser.timestamp_to_epoch(start_video_msgs[i][Timestamp]))]
            filtered_qualities = DataParser.filter_rows_by_time(
                qualities_rows, DataParser.timestamp_to_epoch(start_video_msgs[i][Timestamp]),
                DataParser.timestamp_to_epoch(ended_video_msgs[i][Timestamp]))
            filtered_delay_time = DataParser.filter_rows_by_time(
                start_delay_rows, DataParser.timestamp_to_epoch(start_video_msgs[i][Timestamp]),
                DataParser.timestamp_to_epoch(ended_video_msgs[i][Timestamp]))
            print(filtered_qualities)
            print(filtered_delay_time)
            divided_metrics.append([df_interval, DataParser.extract_qoe_string(filtered_qualities),
                                    DataParser.extract_delay_string(filtered_delay_time)])

        return divided_metrics


if __name__ == '__main__':
    data_files = DataParser(sql_file="C:\\Users\\Saimon\\Desktop\\faf\\youtube_cycles\\x.mf",
                            csv_path="C:\\Users\\Saimon\\Desktop\\faf\\youtube_cycles\\YT_4k_OPT.csv")
    playbacks = data_files.divide_playbacks()
    print(playbacks[0][2])
    print(playbacks[0][1])
