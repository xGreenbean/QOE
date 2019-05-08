import os
global splitcap_path
import shutil
from scapy.all import *
import pandas as pd
#data set format
# dataset/OTT/id/sessions/[TCP/UDP]/splits/

# data_set_path = "C:\Users\ehud\Desktop\dataset"
data_set_path = "/home/ehud/Desktop/dataset"
splitcap_path = "C:\\Users\\ehud\\Desktop\\SplitCap_2-1\\Splitcap.exe"


#add sessions dir to directories
def add_sessions_dir(data_set_path):
    for dirs in os.listdir(data_set_path):
        for subdirs in os.listdir(os.path.join(data_set_path,dirs)):
            if os.path.isdir(os.path.join(os.path.join(data_set_path, dirs, subdirs))):
                if 'sessions' in os.listdir(os.path.join(data_set_path, dirs, subdirs)):
                    print (os.path.join(data_set_path, dirs, subdirs))
                else:
                    os.mkdir(os.path.join(data_set_path, dirs, subdirs,'sessions'))


#fill sessions directories with split cap
#this only works in windows!!
def fill_sessions_dir(data_set_path):
    for dirs in os.listdir(data_set_path):
        for subdirs in os.listdir(os.path.join(data_set_path,dirs)):

            if os.path.isdir(os.path.join(os.path.join(data_set_path, dirs, subdirs))):
                curr_dir = os.path.join(data_set_path, dirs, subdirs)
                if 'sessions' in os.listdir(curr_dir):
                    curr_path_sessions = os.path.join(data_set_path, dirs, subdirs,'sessions')
                    if len(os.listdir(curr_path_sessions)) == 0:
                        print(curr_dir)
                        # for pcap_file in os.listdir(curr_dir):
                        #     if pcap_file.endswith('pcap'):
                        #         curr_pcap_path = os.path.join(curr_dir,pcap_file)
                        #         os.system(splitcap_path + ' -r ' + '"' + curr_pcap_path +
                        #                   '"' + ' -o ' + '"' + curr_path_sessions + '"')

# create directory for every session and move it there
def create_dirs_for_sessions(data_set_path):
    for dirName, subdirList, fileList in os.walk(data_set_path):
        #if there is no session directory
        if os.path.split(dirName)[-1] == ('sessions') != -1:
            # print('Found directory: %s' % dirName)
            for fname in fileList:
                if not os.path.exists(os.path.join(dirName, fname.split('.')[0])):
                    os.mkdir(os.path.join(dirName, fname.split('.')[2]))
                    os.rename(os.path.join(dirName, fname), os.path.join(dirName, fname.split('.')[2], fname))


#split each sessions by time, into the 'splits' directory
def split_sessions_by_time(data_set_path, split_interval):
    for dirName, subdirList, fileList in os.walk(data_set_path):
        if dirName.split(os.sep)[-1].find('TCP') != -1 or dirName.split(os.sep)[-1].find('UDP') != -1:
            for fname in fileList:
                if not os.path.exists(os.path.join(dirName, 'splits')):
                    os.mkdir(os.path.join(dirName, 'splits'))
                #check for exact path
                pcap_file_path = os.path.join(dirName, fname)
                out_path = os.path.join(dirName, 'splits', 'out.pcap')
                if len(os.listdir(os.path.join(dirName, 'splits'))) == 0:
                      os.system('editcap -i ' + str(split_interval) + ' ' + '"' + pcap_file_path + '"'
                               ' "' + out_path + '"')


#deletes the splits directory. we use it if we want to use diffrent time interval
def clean_splits(data_set_path):
    for dirName, subdirList, fileList in os.walk(data_set_path):
        if dirName.find('splits') != -1:
            shutil.rmtree(dirName)
        for fname in fileList:
            if fname.find('splits') != -1:
                os.remove(os.path.join(dirName, fname))


#deletes empty pcaps in the splits directories
def delete_empty_pcaps(data_set_path):
    for dirName, subdirList, fileList in os.walk(data_set_path):
        if dirName.split(os.sep)[-1].find('splits') != -1:
            for fname in fileList:
                if len(rdpcap(os.path.join(dirName,fname))) == 0:
                    os.remove(os.path.join(dirName,fname))

def remove_duplicates_csv(data_set_path):
    for dirName, subdirList, fileList in os.walk(data_set_path):
        if dirName.split(os.sep)[-1].startswith('id_'):
            for fname in fileList:
                if fname.endswith('csv'):
                    df = pd.read_csv(os.path.join(dirName,fname), sep=',')
                    df = df.filter(['Address A', 'Port A', 'Address B', 'Port B'])
                    df.drop_duplicates(subset=None, inplace=True)
                    df.to_csv(os.path.join(dirName,fname))

