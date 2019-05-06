import os
global splitcap_path

# data_set_path = "C:\Users\ehud\Desktop\dataset"
data_set_path = "/home/cyberlab/Desktop/dataset"
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
def fill_sessions_dir(data_set_path):
    for dirs in os.listdir(data_set_path):
        for subdirs in os.listdir(os.path.join(data_set_path,dirs)):

            if os.path.isdir(os.path.join(os.path.join(data_set_path, dirs, subdirs))):
                curr_dir = os.path.join(data_set_path, dirs, subdirs)
                if 'sessions' in os.listdir(curr_dir):
                    curr_path_sessions = os.path.join(data_set_path, dirs, subdirs,'sessions')
                    if len(os.listdir(curr_path_sessions)) == 0:
                        print(curr_dir)
                        for pcap_file in os.listdir(curr_dir):
                            if pcap_file.endswith('pcap'):
                                curr_pcap_path = os.path.join(curr_dir,pcap_file)
                                os.system(splitcap_path + ' -r ' + '"' + curr_pcap_path +
                                          '"' + ' -o ' + '"' + curr_path_sessions + '"')

# create directory for every session and move it there
def create_dirs_for_sessions(data_set_path):
    for dirName, subdirList, fileList in os.walk(data_set_path):
        if dirName.find('sessions') != -1:
            # print('Found directory: %s' % dirName)
            for fname in fileList:
                if not os.path.exists(os.path.join(dirName, fname.split('.')[0])):
                    os.mkdir(os.path.join(dirName, fname.split('.')[2]))
                    os.rename(os.path.join(dirName, fname), os.path.join(dirName, fname.split('.')[2], fname))


def split_sessions_by_time(data_set_path):
    for dirName, subdirList, fileList in os.walk(data_set_path):
        if dirName.find('TCP') != -1 or dirName.find('UDP') != -1:
            for fname in fileList:
                print(fname)

split_sessions_by_time(data_set_path)