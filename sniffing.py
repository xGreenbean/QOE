
import os,time,threading
import time
from scapy.all import *
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
get_player_state = "return document.getElementById('movie_player').getPlayerState()"
get_Loaded_Fraction = "return document.getElementById('movie_player').getVideoLoadedFraction()"
get_Playback_quality = "return document.getElementById('movie_player').getPlaybackQuality()"
get_Playback_quality = "return document.getElementById('movie_player').getPlaybackQuality()"
quality_144p = 10;
quality_244p = 9;
quality_360p = 8;
quality_480p = 7;
quality_720p = 6;
quality_1080p = 5;
num_of_copies = 1
test = {}
event_e = threading.Event()

def set_quality(browser,quality):
	browser.find_element_by_class_name("ytp-settings-button").click()
	# click quality button
	browser.find_elements_by_class_name("ytp-menuitem-label")[4].click()
	# select desired quality
	ActionChains(browser).click(browser.find_elements_by_class_name("ytp-menuitem-label")[quality[0]]).perform()
	time.sleep(5)

def sniffing():
	global test
	time.sleep(0.4)
	test = sniff(count = 10000000, stop_filter = lambda p: event_e.is_set())




def record( vid_id, quality ):
	copies_counter = 0
	skipable = True
	option = webdriver.ChromeOptions()
	option.add_argument("--incognito" )
	option.add_argument("--enable-quic")
	option.add_argument('--no-sandbox')
	log_name = "sniffing_log_" + time.strftime("%c")
	browser = webdriver.Chrome(executable_path='/home/ehud/chromedriver', chrome_options=option)
	while copies_counter != num_of_copies:
		event_e.clear()
		try:
			browser.get("https://www.youtube.com/watch?v="+vid_id)

			while browser.execute_script(get_player_state) == -1:
				continue

			t = threading.Thread(target=sniffing)
			t.start()
			set_quality(browser,quality)
			video_quality = browser.execute_script(get_Playback_quality)
			print(video_quality)

			if(video_quality != quality[1]):
				raise Exception('quality isnt matching')
			else:
				copies_counter += 1

			while not event_e.is_set():
				if browser.execute_script(get_Loaded_Fraction) == 1:
					event_e.set()

			t.join()
			time.sleep(3)

			if not os.path.exists(video_quality):
				os.makedirs(video_quality)
			wrpcap(video_quality +"_"+ vid_id + ".cap", test)
		except Exception as e:
			with open("temp/"+log_name, "a+") as log:
				log.write(str(e))
			event_e.set()
			t.join()
	browser.close()

#randomFile should get the path of existing video_id's from the file
# rndfile = randomFile("test.txt")
# for line in rndfile:
#main
def main():
	with open("test.txt") as f:
		quality_list = [(quality_144p, 'tiny'), (quality_244p, 'small'), (quality_360p, 'medium'),
						(quality_480p, 'large'), (quality_720p, 'hd720'), (quality_1080p, 'hd1080')]
		for i in range(1, 20):
			vid_id = f.readline()
			for quality in quality_list:
				record(vid_id, quality)
if __name__ == "__main__":
	main()


	




