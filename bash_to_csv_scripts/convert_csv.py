import os

quality_list = ['tiny','small','medium','large','hd720','hd1080']




copies_counter = 1
record_name = str(input("Enter name of records:"))
copies = int(input("Enter number of copies:"))


if not os.path.exists("bash_to_csv_files"):
		os.mkdir("bash_to_csv_files",0o777)
if not os.path.exists("bash_to_csv_files/" + str(record_name)):
		os.mkdir("bash_to_csv_files/" + str(record_name),0o777)

f = open("bash_to_csv_files/" + str(record_name) + "/csv_bash.sh",'w+')
os.chmod("bash_to_csv_files/" + str(record_name) + "/csv_bash.sh",0o777)

while copies_counter != copies+1:
	
	pcap_path = "Records/"+ record_name + "/Copy_" + str(copies_counter)
	pcap_path2 = "Records/"+ '"' + record_name + '"' + "/Copy_" + str(copies_counter)
	video_list = os.listdir(pcap_path + "/.")
	for vid_id in video_list:
		for quality in quality_list:
			 f.write("tshark -nr ~/Desktop/QOE/"+ pcap_path2 + "/" + vid_id + "/" + quality + "/" + vid_id +"Vudp.cap -q -z io,stat,0.5,BYTES | grep -P "'"\d{1,2}\.{1}\d{1,2}\s+<>\s+\d{1,2}\.{1}\d{1,2}\s*\|\s+\d+"'"| awk -F '[ |]+' '{print $2"','"($5*8)}' > ~/Desktop/QOE/" + pcap_path2 + "/" + vid_id + "/" + quality + "/" +vid_id+ ".csv\n")

	copies_counter += 1
	

f.close()


