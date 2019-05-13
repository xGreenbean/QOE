
data_set_path = "/home/ehud/Desktop/dataset"
import pandas as pd

def compare(csv_path, stream_strings):
    PP = 0
    df = pd.read_csv(csv_path, sep=',')
    for index, row in df.iterrows():
        for stream_string in stream_strings:
            to_eval = stream_string.split(' ')
            if to_eval[0] == row['Address A'] and\
                to_eval[1] == str(row['Port A']) and\
                to_eval[2] == row['Address B'] and\
                to_eval[3] == str(row['Port B']):
                print(stream_string)
                PP+=1
    print('accuracy = %',PP/df.shape[0])
    if len(stream_strings) > 0:
        print('precision = %',PP/len(stream_strings))
    return PP, df.shape[0], len(stream_strings)