import os
global splitcap_path
data_set_path = "C:\Users\ehud\Desktop\dataset"
splitcap_path = "C:\Users\ehud\Desktop\SplitCap_2-1\Splitcap.exe"

#add sessions dir to directories
def add_sessions_dir(data_set_path):
    for dirs in os.listdir(data_set_path):
        for subdirs in os.listdir(os.path.join(data_set_path,dirs)):
            if os.path.isdir(os.path.join(os.path.join(data_set_path, dirs, subdirs))):
                if 'sessions' in os.listdir(os.path.join(data_set_path, dirs, subdirs)):
                    print os.path.join(data_set_path, dirs, subdirs)
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
