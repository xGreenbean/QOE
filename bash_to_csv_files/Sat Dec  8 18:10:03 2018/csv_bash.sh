tshark -nr ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_1/3dJCroCMBPM/tiny/3dJCroCMBPM.cap -q -z io,stat,0.1,BYTES | grep -P "\d{1,2}\.{1}\d{1,2}\s+<>\s+\d{1,2}\.{1}\d{1,2}\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_1/3dJCroCMBPM/tiny/3dJCroCMBPM.csv
tshark -nr ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_1/3dJCroCMBPM/small/3dJCroCMBPM.cap -q -z io,stat,0.1,BYTES | grep -P "\d{1,2}\.{1}\d{1,2}\s+<>\s+\d{1,2}\.{1}\d{1,2}\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_1/3dJCroCMBPM/small/3dJCroCMBPM.csv
tshark -nr ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_1/3dJCroCMBPM/medium/3dJCroCMBPM.cap -q -z io,stat,0.1,BYTES | grep -P "\d{1,2}\.{1}\d{1,2}\s+<>\s+\d{1,2}\.{1}\d{1,2}\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_1/3dJCroCMBPM/medium/3dJCroCMBPM.csv
tshark -nr ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_1/3dJCroCMBPM/large/3dJCroCMBPM.cap -q -z io,stat,0.1,BYTES | grep -P "\d{1,2}\.{1}\d{1,2}\s+<>\s+\d{1,2}\.{1}\d{1,2}\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_1/3dJCroCMBPM/large/3dJCroCMBPM.csv
tshark -nr ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_1/3dJCroCMBPM/hd720/3dJCroCMBPM.cap -q -z io,stat,0.1,BYTES | grep -P "\d{1,2}\.{1}\d{1,2}\s+<>\s+\d{1,2}\.{1}\d{1,2}\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_1/3dJCroCMBPM/hd720/3dJCroCMBPM.csv
tshark -nr ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_1/3dJCroCMBPM/hd1080/3dJCroCMBPM.cap -q -z io,stat,0.1,BYTES | grep -P "\d{1,2}\.{1}\d{1,2}\s+<>\s+\d{1,2}\.{1}\d{1,2}\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_1/3dJCroCMBPM/hd1080/3dJCroCMBPM.csv
tshark -nr ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_1/-kETYvHON_I/tiny/-kETYvHON_I.cap -q -z io,stat,0.1,BYTES | grep -P "\d{1,2}\.{1}\d{1,2}\s+<>\s+\d{1,2}\.{1}\d{1,2}\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_1/-kETYvHON_I/tiny/-kETYvHON_I.csv
tshark -nr ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_1/-kETYvHON_I/small/-kETYvHON_I.cap -q -z io,stat,0.1,BYTES | grep -P "\d{1,2}\.{1}\d{1,2}\s+<>\s+\d{1,2}\.{1}\d{1,2}\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_1/-kETYvHON_I/small/-kETYvHON_I.csv
tshark -nr ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_1/-kETYvHON_I/medium/-kETYvHON_I.cap -q -z io,stat,0.1,BYTES | grep -P "\d{1,2}\.{1}\d{1,2}\s+<>\s+\d{1,2}\.{1}\d{1,2}\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_1/-kETYvHON_I/medium/-kETYvHON_I.csv
tshark -nr ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_1/-kETYvHON_I/large/-kETYvHON_I.cap -q -z io,stat,0.1,BYTES | grep -P "\d{1,2}\.{1}\d{1,2}\s+<>\s+\d{1,2}\.{1}\d{1,2}\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_1/-kETYvHON_I/large/-kETYvHON_I.csv
tshark -nr ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_1/-kETYvHON_I/hd720/-kETYvHON_I.cap -q -z io,stat,0.1,BYTES | grep -P "\d{1,2}\.{1}\d{1,2}\s+<>\s+\d{1,2}\.{1}\d{1,2}\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_1/-kETYvHON_I/hd720/-kETYvHON_I.csv
tshark -nr ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_1/-kETYvHON_I/hd1080/-kETYvHON_I.cap -q -z io,stat,0.1,BYTES | grep -P "\d{1,2}\.{1}\d{1,2}\s+<>\s+\d{1,2}\.{1}\d{1,2}\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_1/-kETYvHON_I/hd1080/-kETYvHON_I.csv
tshark -nr ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_1/_g8aLVGXyc0/tiny/_g8aLVGXyc0.cap -q -z io,stat,0.1,BYTES | grep -P "\d{1,2}\.{1}\d{1,2}\s+<>\s+\d{1,2}\.{1}\d{1,2}\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_1/_g8aLVGXyc0/tiny/_g8aLVGXyc0.csv
tshark -nr ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_1/_g8aLVGXyc0/small/_g8aLVGXyc0.cap -q -z io,stat,0.1,BYTES | grep -P "\d{1,2}\.{1}\d{1,2}\s+<>\s+\d{1,2}\.{1}\d{1,2}\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_1/_g8aLVGXyc0/small/_g8aLVGXyc0.csv
tshark -nr ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_1/_g8aLVGXyc0/medium/_g8aLVGXyc0.cap -q -z io,stat,0.1,BYTES | grep -P "\d{1,2}\.{1}\d{1,2}\s+<>\s+\d{1,2}\.{1}\d{1,2}\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_1/_g8aLVGXyc0/medium/_g8aLVGXyc0.csv
tshark -nr ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_1/_g8aLVGXyc0/large/_g8aLVGXyc0.cap -q -z io,stat,0.1,BYTES | grep -P "\d{1,2}\.{1}\d{1,2}\s+<>\s+\d{1,2}\.{1}\d{1,2}\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_1/_g8aLVGXyc0/large/_g8aLVGXyc0.csv
tshark -nr ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_1/_g8aLVGXyc0/hd720/_g8aLVGXyc0.cap -q -z io,stat,0.1,BYTES | grep -P "\d{1,2}\.{1}\d{1,2}\s+<>\s+\d{1,2}\.{1}\d{1,2}\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_1/_g8aLVGXyc0/hd720/_g8aLVGXyc0.csv
tshark -nr ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_1/_g8aLVGXyc0/hd1080/_g8aLVGXyc0.cap -q -z io,stat,0.1,BYTES | grep -P "\d{1,2}\.{1}\d{1,2}\s+<>\s+\d{1,2}\.{1}\d{1,2}\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_1/_g8aLVGXyc0/hd1080/_g8aLVGXyc0.csv
tshark -nr ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_1/YJ5q8Wrkbdw/tiny/YJ5q8Wrkbdw.cap -q -z io,stat,0.1,BYTES | grep -P "\d{1,2}\.{1}\d{1,2}\s+<>\s+\d{1,2}\.{1}\d{1,2}\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_1/YJ5q8Wrkbdw/tiny/YJ5q8Wrkbdw.csv
tshark -nr ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_1/YJ5q8Wrkbdw/small/YJ5q8Wrkbdw.cap -q -z io,stat,0.1,BYTES | grep -P "\d{1,2}\.{1}\d{1,2}\s+<>\s+\d{1,2}\.{1}\d{1,2}\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_1/YJ5q8Wrkbdw/small/YJ5q8Wrkbdw.csv
tshark -nr ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_1/YJ5q8Wrkbdw/medium/YJ5q8Wrkbdw.cap -q -z io,stat,0.1,BYTES | grep -P "\d{1,2}\.{1}\d{1,2}\s+<>\s+\d{1,2}\.{1}\d{1,2}\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_1/YJ5q8Wrkbdw/medium/YJ5q8Wrkbdw.csv
tshark -nr ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_1/YJ5q8Wrkbdw/large/YJ5q8Wrkbdw.cap -q -z io,stat,0.1,BYTES | grep -P "\d{1,2}\.{1}\d{1,2}\s+<>\s+\d{1,2}\.{1}\d{1,2}\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_1/YJ5q8Wrkbdw/large/YJ5q8Wrkbdw.csv
tshark -nr ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_1/YJ5q8Wrkbdw/hd720/YJ5q8Wrkbdw.cap -q -z io,stat,0.1,BYTES | grep -P "\d{1,2}\.{1}\d{1,2}\s+<>\s+\d{1,2}\.{1}\d{1,2}\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_1/YJ5q8Wrkbdw/hd720/YJ5q8Wrkbdw.csv
tshark -nr ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_1/YJ5q8Wrkbdw/hd1080/YJ5q8Wrkbdw.cap -q -z io,stat,0.1,BYTES | grep -P "\d{1,2}\.{1}\d{1,2}\s+<>\s+\d{1,2}\.{1}\d{1,2}\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_1/YJ5q8Wrkbdw/hd1080/YJ5q8Wrkbdw.csv
tshark -nr ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_2/3dJCroCMBPM/tiny/3dJCroCMBPM.cap -q -z io,stat,0.1,BYTES | grep -P "\d{1,2}\.{1}\d{1,2}\s+<>\s+\d{1,2}\.{1}\d{1,2}\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_2/3dJCroCMBPM/tiny/3dJCroCMBPM.csv
tshark -nr ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_2/3dJCroCMBPM/small/3dJCroCMBPM.cap -q -z io,stat,0.1,BYTES | grep -P "\d{1,2}\.{1}\d{1,2}\s+<>\s+\d{1,2}\.{1}\d{1,2}\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_2/3dJCroCMBPM/small/3dJCroCMBPM.csv
tshark -nr ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_2/3dJCroCMBPM/medium/3dJCroCMBPM.cap -q -z io,stat,0.1,BYTES | grep -P "\d{1,2}\.{1}\d{1,2}\s+<>\s+\d{1,2}\.{1}\d{1,2}\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_2/3dJCroCMBPM/medium/3dJCroCMBPM.csv
tshark -nr ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_2/3dJCroCMBPM/large/3dJCroCMBPM.cap -q -z io,stat,0.1,BYTES | grep -P "\d{1,2}\.{1}\d{1,2}\s+<>\s+\d{1,2}\.{1}\d{1,2}\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_2/3dJCroCMBPM/large/3dJCroCMBPM.csv
tshark -nr ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_2/3dJCroCMBPM/hd720/3dJCroCMBPM.cap -q -z io,stat,0.1,BYTES | grep -P "\d{1,2}\.{1}\d{1,2}\s+<>\s+\d{1,2}\.{1}\d{1,2}\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_2/3dJCroCMBPM/hd720/3dJCroCMBPM.csv
tshark -nr ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_2/3dJCroCMBPM/hd1080/3dJCroCMBPM.cap -q -z io,stat,0.1,BYTES | grep -P "\d{1,2}\.{1}\d{1,2}\s+<>\s+\d{1,2}\.{1}\d{1,2}\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_2/3dJCroCMBPM/hd1080/3dJCroCMBPM.csv
tshark -nr ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_2/-kETYvHON_I/tiny/-kETYvHON_I.cap -q -z io,stat,0.1,BYTES | grep -P "\d{1,2}\.{1}\d{1,2}\s+<>\s+\d{1,2}\.{1}\d{1,2}\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_2/-kETYvHON_I/tiny/-kETYvHON_I.csv
tshark -nr ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_2/-kETYvHON_I/small/-kETYvHON_I.cap -q -z io,stat,0.1,BYTES | grep -P "\d{1,2}\.{1}\d{1,2}\s+<>\s+\d{1,2}\.{1}\d{1,2}\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_2/-kETYvHON_I/small/-kETYvHON_I.csv
tshark -nr ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_2/-kETYvHON_I/medium/-kETYvHON_I.cap -q -z io,stat,0.1,BYTES | grep -P "\d{1,2}\.{1}\d{1,2}\s+<>\s+\d{1,2}\.{1}\d{1,2}\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_2/-kETYvHON_I/medium/-kETYvHON_I.csv
tshark -nr ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_2/-kETYvHON_I/large/-kETYvHON_I.cap -q -z io,stat,0.1,BYTES | grep -P "\d{1,2}\.{1}\d{1,2}\s+<>\s+\d{1,2}\.{1}\d{1,2}\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_2/-kETYvHON_I/large/-kETYvHON_I.csv
tshark -nr ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_2/-kETYvHON_I/hd720/-kETYvHON_I.cap -q -z io,stat,0.1,BYTES | grep -P "\d{1,2}\.{1}\d{1,2}\s+<>\s+\d{1,2}\.{1}\d{1,2}\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_2/-kETYvHON_I/hd720/-kETYvHON_I.csv
tshark -nr ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_2/-kETYvHON_I/hd1080/-kETYvHON_I.cap -q -z io,stat,0.1,BYTES | grep -P "\d{1,2}\.{1}\d{1,2}\s+<>\s+\d{1,2}\.{1}\d{1,2}\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_2/-kETYvHON_I/hd1080/-kETYvHON_I.csv
tshark -nr ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_2/_g8aLVGXyc0/tiny/_g8aLVGXyc0.cap -q -z io,stat,0.1,BYTES | grep -P "\d{1,2}\.{1}\d{1,2}\s+<>\s+\d{1,2}\.{1}\d{1,2}\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_2/_g8aLVGXyc0/tiny/_g8aLVGXyc0.csv
tshark -nr ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_2/_g8aLVGXyc0/small/_g8aLVGXyc0.cap -q -z io,stat,0.1,BYTES | grep -P "\d{1,2}\.{1}\d{1,2}\s+<>\s+\d{1,2}\.{1}\d{1,2}\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_2/_g8aLVGXyc0/small/_g8aLVGXyc0.csv
tshark -nr ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_2/_g8aLVGXyc0/medium/_g8aLVGXyc0.cap -q -z io,stat,0.1,BYTES | grep -P "\d{1,2}\.{1}\d{1,2}\s+<>\s+\d{1,2}\.{1}\d{1,2}\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_2/_g8aLVGXyc0/medium/_g8aLVGXyc0.csv
tshark -nr ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_2/_g8aLVGXyc0/large/_g8aLVGXyc0.cap -q -z io,stat,0.1,BYTES | grep -P "\d{1,2}\.{1}\d{1,2}\s+<>\s+\d{1,2}\.{1}\d{1,2}\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_2/_g8aLVGXyc0/large/_g8aLVGXyc0.csv
tshark -nr ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_2/_g8aLVGXyc0/hd720/_g8aLVGXyc0.cap -q -z io,stat,0.1,BYTES | grep -P "\d{1,2}\.{1}\d{1,2}\s+<>\s+\d{1,2}\.{1}\d{1,2}\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_2/_g8aLVGXyc0/hd720/_g8aLVGXyc0.csv
tshark -nr ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_2/_g8aLVGXyc0/hd1080/_g8aLVGXyc0.cap -q -z io,stat,0.1,BYTES | grep -P "\d{1,2}\.{1}\d{1,2}\s+<>\s+\d{1,2}\.{1}\d{1,2}\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_2/_g8aLVGXyc0/hd1080/_g8aLVGXyc0.csv
tshark -nr ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_2/YJ5q8Wrkbdw/tiny/YJ5q8Wrkbdw.cap -q -z io,stat,0.1,BYTES | grep -P "\d{1,2}\.{1}\d{1,2}\s+<>\s+\d{1,2}\.{1}\d{1,2}\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_2/YJ5q8Wrkbdw/tiny/YJ5q8Wrkbdw.csv
tshark -nr ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_2/YJ5q8Wrkbdw/small/YJ5q8Wrkbdw.cap -q -z io,stat,0.1,BYTES | grep -P "\d{1,2}\.{1}\d{1,2}\s+<>\s+\d{1,2}\.{1}\d{1,2}\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_2/YJ5q8Wrkbdw/small/YJ5q8Wrkbdw.csv
tshark -nr ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_2/YJ5q8Wrkbdw/medium/YJ5q8Wrkbdw.cap -q -z io,stat,0.1,BYTES | grep -P "\d{1,2}\.{1}\d{1,2}\s+<>\s+\d{1,2}\.{1}\d{1,2}\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_2/YJ5q8Wrkbdw/medium/YJ5q8Wrkbdw.csv
tshark -nr ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_2/YJ5q8Wrkbdw/large/YJ5q8Wrkbdw.cap -q -z io,stat,0.1,BYTES | grep -P "\d{1,2}\.{1}\d{1,2}\s+<>\s+\d{1,2}\.{1}\d{1,2}\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_2/YJ5q8Wrkbdw/large/YJ5q8Wrkbdw.csv
tshark -nr ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_2/YJ5q8Wrkbdw/hd720/YJ5q8Wrkbdw.cap -q -z io,stat,0.1,BYTES | grep -P "\d{1,2}\.{1}\d{1,2}\s+<>\s+\d{1,2}\.{1}\d{1,2}\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_2/YJ5q8Wrkbdw/hd720/YJ5q8Wrkbdw.csv
tshark -nr ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_2/YJ5q8Wrkbdw/hd1080/YJ5q8Wrkbdw.cap -q -z io,stat,0.1,BYTES | grep -P "\d{1,2}\.{1}\d{1,2}\s+<>\s+\d{1,2}\.{1}\d{1,2}\s*\|\s+\d+"| awk -F '[ |]+' '{print $2,($5*8)}' > ../../Records/"Sat Dec  8 18:10:03 2018"/Copy_2/YJ5q8Wrkbdw/hd1080/YJ5q8Wrkbdw.csv
