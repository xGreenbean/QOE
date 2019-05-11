#here will be proof of concept code for breaking a network session into Request-Response.
#
from scapy.all import *
import matplotlib.pyplot as plt

video_pcap = rdpcap('/home/ehud/Desktop/exp1.pcap')
flag = True

ip_src = video_pcap[0][IP].src
request_start_time = 0
number_of_requests = 0
requests = []
responses = []
request = []
response = []
for pkt in video_pcap:
        if pkt[IP].src == ip_src and len(pkt) > 300 and\
            (request_start_time == 0 or pkt.time - request_start_time > 0.5):
                if len(request) > 0:
                    requests.append(list(request))
                if len(response) > 0:
                    responses.append(list(response))
                response = []
                request = []
                request_start_time = pkt.time
                #start new session.
                number_of_requests += 1
        else:
            if pkt[IP].src == ip_src and len(pkt) > 300:
                request.append(pkt)
            else:
                response.append(pkt)

if len(request) > 0:
    requests.append(list(request))
if len(response) > 0:
    responses.append(list(response))

req_lens = [len(pkt) for pkt in requests[1]]
res_lens = [len(pkt) for pkt in responses[1]]
times_req = [pkt.time for pkt in requests[1]]
times_res = [pkt.time for pkt in responses[1]]
plt.plot(times_req,req_lens,'rs',times_res,res_lens,'b--')
plt.show()
print(number_of_requests, len(responses),len(requests))
