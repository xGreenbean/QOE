tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/SVGUKBugoKo/tiny/SVGUKBugoKoVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/SVGUKBugoKo/tiny/SVGUKBugoKo.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/SVGUKBugoKo/small/SVGUKBugoKoVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/SVGUKBugoKo/small/SVGUKBugoKo.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/SVGUKBugoKo/medium/SVGUKBugoKoVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/SVGUKBugoKo/medium/SVGUKBugoKo.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/SVGUKBugoKo/large/SVGUKBugoKoVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/SVGUKBugoKo/large/SVGUKBugoKo.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/SVGUKBugoKo/hd720/SVGUKBugoKoVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/SVGUKBugoKo/hd720/SVGUKBugoKo.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/SVGUKBugoKo/hd1080/SVGUKBugoKoVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/SVGUKBugoKo/hd1080/SVGUKBugoKo.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/Myd33zH1NTc/tiny/Myd33zH1NTcVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/Myd33zH1NTc/tiny/Myd33zH1NTc.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/Myd33zH1NTc/small/Myd33zH1NTcVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/Myd33zH1NTc/small/Myd33zH1NTc.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/Myd33zH1NTc/medium/Myd33zH1NTcVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/Myd33zH1NTc/medium/Myd33zH1NTc.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/Myd33zH1NTc/large/Myd33zH1NTcVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/Myd33zH1NTc/large/Myd33zH1NTc.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/Myd33zH1NTc/hd720/Myd33zH1NTcVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/Myd33zH1NTc/hd720/Myd33zH1NTc.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/Myd33zH1NTc/hd1080/Myd33zH1NTcVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/Myd33zH1NTc/hd1080/Myd33zH1NTc.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/ADmRvOTFN_M/tiny/ADmRvOTFN_MVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/ADmRvOTFN_M/tiny/ADmRvOTFN_M.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/ADmRvOTFN_M/small/ADmRvOTFN_MVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/ADmRvOTFN_M/small/ADmRvOTFN_M.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/ADmRvOTFN_M/medium/ADmRvOTFN_MVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/ADmRvOTFN_M/medium/ADmRvOTFN_M.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/ADmRvOTFN_M/large/ADmRvOTFN_MVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/ADmRvOTFN_M/large/ADmRvOTFN_M.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/ADmRvOTFN_M/hd720/ADmRvOTFN_MVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/ADmRvOTFN_M/hd720/ADmRvOTFN_M.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/ADmRvOTFN_M/hd1080/ADmRvOTFN_MVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/ADmRvOTFN_M/hd1080/ADmRvOTFN_M.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/boB6qu5dcCw/tiny/boB6qu5dcCwVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/boB6qu5dcCw/tiny/boB6qu5dcCw.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/boB6qu5dcCw/small/boB6qu5dcCwVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/boB6qu5dcCw/small/boB6qu5dcCw.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/boB6qu5dcCw/medium/boB6qu5dcCwVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/boB6qu5dcCw/medium/boB6qu5dcCw.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/boB6qu5dcCw/large/boB6qu5dcCwVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/boB6qu5dcCw/large/boB6qu5dcCw.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/boB6qu5dcCw/hd720/boB6qu5dcCwVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/boB6qu5dcCw/hd720/boB6qu5dcCw.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/boB6qu5dcCw/hd1080/boB6qu5dcCwVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/boB6qu5dcCw/hd1080/boB6qu5dcCw.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/w7CtP73taJA/tiny/w7CtP73taJAVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/w7CtP73taJA/tiny/w7CtP73taJA.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/w7CtP73taJA/small/w7CtP73taJAVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/w7CtP73taJA/small/w7CtP73taJA.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/w7CtP73taJA/medium/w7CtP73taJAVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/w7CtP73taJA/medium/w7CtP73taJA.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/w7CtP73taJA/large/w7CtP73taJAVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/w7CtP73taJA/large/w7CtP73taJA.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/w7CtP73taJA/hd720/w7CtP73taJAVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/w7CtP73taJA/hd720/w7CtP73taJA.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/w7CtP73taJA/hd1080/w7CtP73taJAVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/w7CtP73taJA/hd1080/w7CtP73taJA.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/bxFoRCvEjUA/tiny/bxFoRCvEjUAVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/bxFoRCvEjUA/tiny/bxFoRCvEjUA.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/bxFoRCvEjUA/small/bxFoRCvEjUAVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/bxFoRCvEjUA/small/bxFoRCvEjUA.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/bxFoRCvEjUA/medium/bxFoRCvEjUAVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/bxFoRCvEjUA/medium/bxFoRCvEjUA.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/bxFoRCvEjUA/large/bxFoRCvEjUAVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/bxFoRCvEjUA/large/bxFoRCvEjUA.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/bxFoRCvEjUA/hd720/bxFoRCvEjUAVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/bxFoRCvEjUA/hd720/bxFoRCvEjUA.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/bxFoRCvEjUA/hd1080/bxFoRCvEjUAVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/bxFoRCvEjUA/hd1080/bxFoRCvEjUA.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/6EiI5_-7liQ/tiny/6EiI5_-7liQVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/6EiI5_-7liQ/tiny/6EiI5_-7liQ.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/6EiI5_-7liQ/small/6EiI5_-7liQVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/6EiI5_-7liQ/small/6EiI5_-7liQ.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/6EiI5_-7liQ/medium/6EiI5_-7liQVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/6EiI5_-7liQ/medium/6EiI5_-7liQ.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/6EiI5_-7liQ/large/6EiI5_-7liQVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/6EiI5_-7liQ/large/6EiI5_-7liQ.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/6EiI5_-7liQ/hd720/6EiI5_-7liQVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/6EiI5_-7liQ/hd720/6EiI5_-7liQ.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/6EiI5_-7liQ/hd1080/6EiI5_-7liQVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/6EiI5_-7liQ/hd1080/6EiI5_-7liQ.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/CdsfMfRKVNk/tiny/CdsfMfRKVNkVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/CdsfMfRKVNk/tiny/CdsfMfRKVNk.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/CdsfMfRKVNk/small/CdsfMfRKVNkVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/CdsfMfRKVNk/small/CdsfMfRKVNk.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/CdsfMfRKVNk/medium/CdsfMfRKVNkVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/CdsfMfRKVNk/medium/CdsfMfRKVNk.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/CdsfMfRKVNk/large/CdsfMfRKVNkVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/CdsfMfRKVNk/large/CdsfMfRKVNk.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/CdsfMfRKVNk/hd720/CdsfMfRKVNkVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/CdsfMfRKVNk/hd720/CdsfMfRKVNk.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/CdsfMfRKVNk/hd1080/CdsfMfRKVNkVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/CdsfMfRKVNk/hd1080/CdsfMfRKVNk.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/4faVkCbNRG8/tiny/4faVkCbNRG8Vudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/4faVkCbNRG8/tiny/4faVkCbNRG8.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/4faVkCbNRG8/small/4faVkCbNRG8Vudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/4faVkCbNRG8/small/4faVkCbNRG8.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/4faVkCbNRG8/medium/4faVkCbNRG8Vudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/4faVkCbNRG8/medium/4faVkCbNRG8.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/4faVkCbNRG8/large/4faVkCbNRG8Vudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/4faVkCbNRG8/large/4faVkCbNRG8.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/4faVkCbNRG8/hd720/4faVkCbNRG8Vudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/4faVkCbNRG8/hd720/4faVkCbNRG8.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/4faVkCbNRG8/hd1080/4faVkCbNRG8Vudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/4faVkCbNRG8/hd1080/4faVkCbNRG8.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/GhVLQBtmz6g/tiny/GhVLQBtmz6gVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/GhVLQBtmz6g/tiny/GhVLQBtmz6g.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/GhVLQBtmz6g/small/GhVLQBtmz6gVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/GhVLQBtmz6g/small/GhVLQBtmz6g.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/GhVLQBtmz6g/medium/GhVLQBtmz6gVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/GhVLQBtmz6g/medium/GhVLQBtmz6g.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/GhVLQBtmz6g/large/GhVLQBtmz6gVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/GhVLQBtmz6g/large/GhVLQBtmz6g.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/GhVLQBtmz6g/hd720/GhVLQBtmz6gVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/GhVLQBtmz6g/hd720/GhVLQBtmz6g.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/GhVLQBtmz6g/hd1080/GhVLQBtmz6gVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/GhVLQBtmz6g/hd1080/GhVLQBtmz6g.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/s5KNIWKjzS4/tiny/s5KNIWKjzS4Vudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/s5KNIWKjzS4/tiny/s5KNIWKjzS4.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/s5KNIWKjzS4/small/s5KNIWKjzS4Vudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/s5KNIWKjzS4/small/s5KNIWKjzS4.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/s5KNIWKjzS4/medium/s5KNIWKjzS4Vudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/s5KNIWKjzS4/medium/s5KNIWKjzS4.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/s5KNIWKjzS4/large/s5KNIWKjzS4Vudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/s5KNIWKjzS4/large/s5KNIWKjzS4.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/s5KNIWKjzS4/hd720/s5KNIWKjzS4Vudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/s5KNIWKjzS4/hd720/s5KNIWKjzS4.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/s5KNIWKjzS4/hd1080/s5KNIWKjzS4Vudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_1/s5KNIWKjzS4/hd1080/s5KNIWKjzS4.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/SVGUKBugoKo/tiny/SVGUKBugoKoVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/SVGUKBugoKo/tiny/SVGUKBugoKo.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/SVGUKBugoKo/small/SVGUKBugoKoVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/SVGUKBugoKo/small/SVGUKBugoKo.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/SVGUKBugoKo/medium/SVGUKBugoKoVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/SVGUKBugoKo/medium/SVGUKBugoKo.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/SVGUKBugoKo/large/SVGUKBugoKoVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/SVGUKBugoKo/large/SVGUKBugoKo.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/SVGUKBugoKo/hd720/SVGUKBugoKoVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/SVGUKBugoKo/hd720/SVGUKBugoKo.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/SVGUKBugoKo/hd1080/SVGUKBugoKoVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/SVGUKBugoKo/hd1080/SVGUKBugoKo.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/Myd33zH1NTc/tiny/Myd33zH1NTcVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/Myd33zH1NTc/tiny/Myd33zH1NTc.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/Myd33zH1NTc/small/Myd33zH1NTcVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/Myd33zH1NTc/small/Myd33zH1NTc.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/Myd33zH1NTc/medium/Myd33zH1NTcVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/Myd33zH1NTc/medium/Myd33zH1NTc.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/Myd33zH1NTc/large/Myd33zH1NTcVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/Myd33zH1NTc/large/Myd33zH1NTc.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/Myd33zH1NTc/hd720/Myd33zH1NTcVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/Myd33zH1NTc/hd720/Myd33zH1NTc.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/Myd33zH1NTc/hd1080/Myd33zH1NTcVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/Myd33zH1NTc/hd1080/Myd33zH1NTc.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/ADmRvOTFN_M/tiny/ADmRvOTFN_MVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/ADmRvOTFN_M/tiny/ADmRvOTFN_M.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/ADmRvOTFN_M/small/ADmRvOTFN_MVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/ADmRvOTFN_M/small/ADmRvOTFN_M.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/ADmRvOTFN_M/medium/ADmRvOTFN_MVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/ADmRvOTFN_M/medium/ADmRvOTFN_M.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/ADmRvOTFN_M/large/ADmRvOTFN_MVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/ADmRvOTFN_M/large/ADmRvOTFN_M.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/ADmRvOTFN_M/hd720/ADmRvOTFN_MVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/ADmRvOTFN_M/hd720/ADmRvOTFN_M.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/ADmRvOTFN_M/hd1080/ADmRvOTFN_MVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/ADmRvOTFN_M/hd1080/ADmRvOTFN_M.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/boB6qu5dcCw/tiny/boB6qu5dcCwVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/boB6qu5dcCw/tiny/boB6qu5dcCw.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/boB6qu5dcCw/small/boB6qu5dcCwVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/boB6qu5dcCw/small/boB6qu5dcCw.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/boB6qu5dcCw/medium/boB6qu5dcCwVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/boB6qu5dcCw/medium/boB6qu5dcCw.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/boB6qu5dcCw/large/boB6qu5dcCwVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/boB6qu5dcCw/large/boB6qu5dcCw.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/boB6qu5dcCw/hd720/boB6qu5dcCwVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/boB6qu5dcCw/hd720/boB6qu5dcCw.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/boB6qu5dcCw/hd1080/boB6qu5dcCwVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/boB6qu5dcCw/hd1080/boB6qu5dcCw.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/w7CtP73taJA/tiny/w7CtP73taJAVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/w7CtP73taJA/tiny/w7CtP73taJA.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/w7CtP73taJA/small/w7CtP73taJAVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/w7CtP73taJA/small/w7CtP73taJA.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/w7CtP73taJA/medium/w7CtP73taJAVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/w7CtP73taJA/medium/w7CtP73taJA.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/w7CtP73taJA/large/w7CtP73taJAVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/w7CtP73taJA/large/w7CtP73taJA.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/w7CtP73taJA/hd720/w7CtP73taJAVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/w7CtP73taJA/hd720/w7CtP73taJA.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/w7CtP73taJA/hd1080/w7CtP73taJAVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/w7CtP73taJA/hd1080/w7CtP73taJA.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/bxFoRCvEjUA/tiny/bxFoRCvEjUAVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/bxFoRCvEjUA/tiny/bxFoRCvEjUA.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/bxFoRCvEjUA/small/bxFoRCvEjUAVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/bxFoRCvEjUA/small/bxFoRCvEjUA.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/bxFoRCvEjUA/medium/bxFoRCvEjUAVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/bxFoRCvEjUA/medium/bxFoRCvEjUA.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/bxFoRCvEjUA/large/bxFoRCvEjUAVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/bxFoRCvEjUA/large/bxFoRCvEjUA.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/bxFoRCvEjUA/hd720/bxFoRCvEjUAVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/bxFoRCvEjUA/hd720/bxFoRCvEjUA.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/bxFoRCvEjUA/hd1080/bxFoRCvEjUAVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/bxFoRCvEjUA/hd1080/bxFoRCvEjUA.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/6EiI5_-7liQ/tiny/6EiI5_-7liQVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/6EiI5_-7liQ/tiny/6EiI5_-7liQ.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/6EiI5_-7liQ/small/6EiI5_-7liQVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/6EiI5_-7liQ/small/6EiI5_-7liQ.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/6EiI5_-7liQ/medium/6EiI5_-7liQVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/6EiI5_-7liQ/medium/6EiI5_-7liQ.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/6EiI5_-7liQ/large/6EiI5_-7liQVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/6EiI5_-7liQ/large/6EiI5_-7liQ.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/6EiI5_-7liQ/hd720/6EiI5_-7liQVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/6EiI5_-7liQ/hd720/6EiI5_-7liQ.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/6EiI5_-7liQ/hd1080/6EiI5_-7liQVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/6EiI5_-7liQ/hd1080/6EiI5_-7liQ.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/CdsfMfRKVNk/tiny/CdsfMfRKVNkVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/CdsfMfRKVNk/tiny/CdsfMfRKVNk.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/CdsfMfRKVNk/small/CdsfMfRKVNkVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/CdsfMfRKVNk/small/CdsfMfRKVNk.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/CdsfMfRKVNk/medium/CdsfMfRKVNkVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/CdsfMfRKVNk/medium/CdsfMfRKVNk.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/CdsfMfRKVNk/large/CdsfMfRKVNkVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/CdsfMfRKVNk/large/CdsfMfRKVNk.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/CdsfMfRKVNk/hd720/CdsfMfRKVNkVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/CdsfMfRKVNk/hd720/CdsfMfRKVNk.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/CdsfMfRKVNk/hd1080/CdsfMfRKVNkVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/CdsfMfRKVNk/hd1080/CdsfMfRKVNk.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/4faVkCbNRG8/tiny/4faVkCbNRG8Vudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/4faVkCbNRG8/tiny/4faVkCbNRG8.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/4faVkCbNRG8/small/4faVkCbNRG8Vudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/4faVkCbNRG8/small/4faVkCbNRG8.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/4faVkCbNRG8/medium/4faVkCbNRG8Vudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/4faVkCbNRG8/medium/4faVkCbNRG8.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/4faVkCbNRG8/large/4faVkCbNRG8Vudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/4faVkCbNRG8/large/4faVkCbNRG8.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/4faVkCbNRG8/hd720/4faVkCbNRG8Vudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/4faVkCbNRG8/hd720/4faVkCbNRG8.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/4faVkCbNRG8/hd1080/4faVkCbNRG8Vudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/4faVkCbNRG8/hd1080/4faVkCbNRG8.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/GhVLQBtmz6g/tiny/GhVLQBtmz6gVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/GhVLQBtmz6g/tiny/GhVLQBtmz6g.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/GhVLQBtmz6g/small/GhVLQBtmz6gVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/GhVLQBtmz6g/small/GhVLQBtmz6g.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/GhVLQBtmz6g/medium/GhVLQBtmz6gVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/GhVLQBtmz6g/medium/GhVLQBtmz6g.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/GhVLQBtmz6g/large/GhVLQBtmz6gVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/GhVLQBtmz6g/large/GhVLQBtmz6g.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/GhVLQBtmz6g/hd720/GhVLQBtmz6gVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/GhVLQBtmz6g/hd720/GhVLQBtmz6g.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/GhVLQBtmz6g/hd1080/GhVLQBtmz6gVudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/GhVLQBtmz6g/hd1080/GhVLQBtmz6g.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/s5KNIWKjzS4/tiny/s5KNIWKjzS4Vudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/s5KNIWKjzS4/tiny/s5KNIWKjzS4.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/s5KNIWKjzS4/small/s5KNIWKjzS4Vudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/s5KNIWKjzS4/small/s5KNIWKjzS4.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/s5KNIWKjzS4/medium/s5KNIWKjzS4Vudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/s5KNIWKjzS4/medium/s5KNIWKjzS4.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/s5KNIWKjzS4/large/s5KNIWKjzS4Vudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/s5KNIWKjzS4/large/s5KNIWKjzS4.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/s5KNIWKjzS4/hd720/s5KNIWKjzS4Vudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/s5KNIWKjzS4/hd720/s5KNIWKjzS4.csv
tshark -nr ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/s5KNIWKjzS4/hd1080/s5KNIWKjzS4Vudp.cap -q -z io,stat,1,BYTES | grep -P "\d+\s+<>\s+\d+\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ~/Desktop/QOE/Records/"Sat Dec 15 05_53_32 2018"/Copy_2/s5KNIWKjzS4/hd1080/s5KNIWKjzS4.csv