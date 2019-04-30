import os
my_dir = os.listdir("cuttings")
for pcap_dirs in my_dir:
    my_dir_streams = os.listdir(os.getcwd() + "\\cuttings\\" + pcap_dirs)
    if len(my_dir_streams) == 1:
        for pcap_files in my_dir_streams:
            pcap_file_path = os.getcwd() + "\\cuttings\\" + pcap_dirs + "\\" + pcap_files
            pcap_dir_path = os.getcwd() + "\\cuttings\\" + pcap_dirs + "\\out.pcap"
            os.system('"C:\Program Files\Wireshark\editcap.exe" -i 5 ' + pcap_file_path +
              " " + pcap_dir_path)
