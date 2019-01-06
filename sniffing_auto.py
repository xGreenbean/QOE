import os, time, threading, math
from datetime import datetime
from scapy.all import *
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

get_player_state = "return document.getElementById('movie_player').getPlayerState()"
get_Loaded_Fraction = "return document.getElementById('movie_player').getVideoLoadedFraction()"
get_Playback_quality = "return document.getElementById('movie_player').getPlaybackQuality()"
get_Playback_quality = "return document.getElementById('movie_player').getPlaybackQuality()"
get_duration = "return document.getElementById('movie_player').getDuration()"
get_current_time = "return document.getElementById('movie_player').getCurrentTime()"
play_video = "return document.getElementById('movie_player').playVideo()"
quality_144p = 10
quality_244p = 9
quality_360p = 8
quality_480p = 7
quality_720p = 6
quality_1080p = 5
num_of_copies = 0
num_of_videos = 0
tresh_hold = 70
start_capture_time = datetime.now()
finish_capture_time = datetime.now()
test = {}
freeze_text = ""
event_e = threading.Event()
event_freeze = threading.Event()
date_today = time.strftime("%c")


def formatTime(time):
    time = round(time)
    minutes = math.floor(time / 60)
    seconds = time - minutes * 60
    if seconds < 10:
        seconds = '0' + seconds
    return str(minutes) + ":" + str(seconds)





def sniffing(browser):
    global test
    global start_capture_time
    time.sleep(0.4)
    start_capture_time = datetime.now()
    thread_freeze = threading.Thread(target=isfreezed, args=[browser])
    thread_freeze.start()
    test = sniff(count=10000000, stop_filter=lambda p: event_e.is_set())
    event_freeze.set()
    thread_freeze.join()
    event_freeze.clear()


def isfreezed(browser):
    global freeze_text
    was_freezed = False
    start_freeze_time = datetime.now()
    current_time = browser.execute_script(get_current_time)
    while not event_freeze.is_set():

        while browser.execute_script(get_player_state) == 3:
            if was_freezed == False:
                start_freeze_time = datetime.now()
                was_freezed = True
                current_time = browser.execute_script(get_current_time)
            print("FREEZE")

        if was_freezed == True:
            was_freezed = False
            no_freeze = browser.execute_script(get_current_time)
            finish_freeze_time = datetime.now()
            freeze_text += "there was a freeze for " + str(
                finish_freeze_time - start_freeze_time) + " ,Freeze started in time: " + str(
                current_time) + " and finished in time: " + str(no_freeze) + "\n"


def record(vid_id, quality, is_auto):
    copies_counter = 0
    trsh_counter = 0
    global finish_capture_time
    global date_today
    option = webdriver.ChromeOptions()
    option.add_argument("--incognito")
    option.add_argument("--enable-quic")
    option.add_argument('--no-sandbox')
    browser = webdriver.Chrome(executable_path='/home/cyberlab/Desktop/QOE/chromedriver', chrome_options=option)
    global freeze_text
    video_length = ""
    video_quality = ""
    if not os.path.exists("Records/" + date_today):
        os.mkdir("Records/" + date_today, 0o777)
    log_file = open("Records/" + date_today + "/LogFile", 'a+')

    while copies_counter != num_of_copies:
        is_running = False
        event_e.clear()
        try:
            browser.get("https://www.youtube.com/watch?v=" + vid_id)
            time.sleep(2)

            while browser.execute_script(get_player_state) == -1:
                continue

            t = threading.Thread(target=sniffing, args=[browser])
            t.start()
            is_running = True

            while not event_e.is_set():
                if browser.execute_script(get_Loaded_Fraction) == 1:
                    event_e.set()
                    finish_capture_time = datetime.now()
                    video_length = formatTime(browser.execute_script(get_duration))
            t.join()
            time.sleep(3)
            total_capture_time = finish_capture_time - start_capture_time
            copies_counter += 1
            if not os.path.exists("Records/" + date_today + "/Copy_" + str(copies_counter)):
                os.makedirs("Records/" + date_today + "/Copy_" + str(copies_counter))
            if not os.path.exists("Records/" + date_today + "/Copy_" + str(copies_counter) + "/" + vid_id):
                os.makedirs("Records/" + date_today + "/Copy_" + str(copies_counter) + "/" + vid_id)
            if not os.path.exists(
                    "Records/" + date_today + "/Copy_" + str(copies_counter) + "/" + vid_id + "/" + video_quality):
                os.makedirs(
                    "Records/" + date_today + "/Copy_" + str(copies_counter) + "/" + vid_id + "/" + video_quality)
            print(freeze_text)
            wrpcap("Records/" + date_today + "/Copy_" + str(
                copies_counter) + "/" + vid_id + "/" + video_quality + "/" + vid_id + ".cap", test)
            f = open("Records/" + date_today + "/Copy_" + str(
                copies_counter) + "/" + vid_id + "/" + video_quality + "/" + "feature_List", 'a+')
            f.write("Capture time: " + str(
                total_capture_time) + "\n" + "Video Length: " + video_length + "\n" + freeze_text + "\n")
            freeze_text = ""
            f.close()
            if is_auto == 1:
                f.write("RECORDED IN AUTO MODE")
            print("Video id: " + vid_id + "was succesfully captured in quality:" + video_quality)
        except Exception as e:
            log_file.write(str(e) + "\n")

            if is_running == True:
                event_e.set()
                t.join()
            else:
                trsh_counter += 1

    browser.close()
    log_file.close()


# randomFile should get the path of existing video_id's from the file
# rndfile = randomFile("test.txt")
# for line in rndfile:
# main
def main():
    try:
        global num_of_videos
        global num_of_copies
        if not os.path.exists("Records"):
            os.mkdir("Records")
        user_vid = ""
        is_auto = int(input("Press 1 to record in auto quality,otherwise press any other number:"))
        what_vid = int(input("Press 2 to enter specific video id(press any other number to use videos id file):"))
        if what_vid == 2:
            user_vid = input("Plese enter video id:")
            num_of_videos = 1
        else:
            num_of_videos = int(input("Enter numbers of videos to check from the file:"))

        num_of_copies = int(input("How many copies would you like to do to each video id:"))
        with open("test.txt") as f:
            quality_list = [(quality_144p, 'tiny'), (quality_244p, 'small'), (quality_360p, 'medium'),
                            (quality_480p, 'large'), (quality_720p, 'hd720'), (quality_1080p, 'hd1080')]

            for i in range(1, num_of_videos + 1):

                vid_id = f.readline().split('\n')[0]
                if what_vid == 2:
                    vid_id = user_vid
                for quality in quality_list:
                    record(vid_id, quality, is_auto)

    except KeyboardInterrupt:
        sys.exit(1)


if __name__ == "__main__":
    main()







