
"""
FIX:
"""

"""
Class fields:
sess - Session DataFrame
"""

class Session:

    def __init__(self, srcPort, dstPort, srcIp, dstIp, csvFile):
        self.srcPort = srcPort
        self.srcIp = srcIp
        self.dstIp = dstIp
        self.dstPort = dstPort
        self.protocol = ""
        self.all_packets = self.get_rows_session(csvFile)
        self.uploads, self.downloads = self.find_uploads_downloads()

    def get_rows_session(self, csv_file):
        row_list = []
        for i in range(csv_file['ip.src'].count()):
            src_ip = csv_file['ip.src'][i]
            dst_ip = csv_file['ip.dst'][i]
            tcp_src_port = csv_file['tcp.srcport'][i]
            tcp_dst_port = csv_file['tcp.dstport'][i]
            udp_src_port = csv_file['udp.srcport'][i]
            udp_dst_port = csv_file['udp.dstport'][i]
            if True:
                if (src_ip == self.srcIp and dst_ip == self.dstIp) or (src_ip == self.dstIp and dst_ip == self.srcIp):
                    print(str(udp_src_port)[:-2] + " " + self.srcPort)
                    if (str(tcp_src_port)[:-2] == self.srcPort and str(tcp_dst_port)[:-2] == self.dstPort)\
                                              or (str(tcp_src_port)[:-2] == self.dstPort and str(tcp_dst_port)[:-2] == self.srcPort):
                        self.protocol = "TCP"
                        row_list.append(csv_file.loc[i])
                    elif (str(udp_src_port)[:-2] == self.srcPort and str(udp_dst_port)[:-2] == self.dstPort) or \
                            (str(udp_src_port)[:-2] == self.dstPort and str(udp_dst_port)[:-2] == self.srcPort):
                        self.protocol = "UDP"
                        row_list.append(csv_file.loc[i])
        # print(numUploads)
        return row_list


    def find_uploads_downloads(self):
        uploads = []
        downloads = []
        for i in range(len(self.all_packets)):
            if str(self.all_packets[i]['ip.src']) == self.srcIp:
                uploads.append(self.all_packets[i])
            else:
                downloads.append(self.all_packets[i])
        return uploads, downloads





