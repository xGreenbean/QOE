
import os,time,threading
from scapy.all import *
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

get_Loaded_Fraction = "return document.getElementById('movie_player').getVideoLoadedFraction()"
get_Playback_quality = "return document.getElementById('movie_player').getPlaybackQuality()"
get_player_state = "return document.getElementById('movie_player').getPlayerState()"



def check_buffering_occcured():


	option = webdriver.ChromeOptions()
	option.add_argument("--incognito" )
	option.add_argument("--enable-quic")
	option.add_argument('--no-sandbox')
	while True:		
		# Create new Instance of Chrome in incognito mode
		browser = webdriver.Chrome(executable_path='/home/ehud/chromedriver', chrome_options=option)
		browser.maximize_window()
		is_finished = 0
		try:
			browser.get("https://www.youtube.com/watch?v=jajnYvh9Stk")
			#click setting button

			player_state = browser.execute_script(get_player_state)
			print(player_state)
		


			is_finished = browser.execute_script(get_Loaded_Fraction)

			while is_finished != 1:
				time.sleep(3)
				fraction = browser.execute_script(get_Loaded_Fraction)
				print("loaded fraction is: ", fraction *100 )
				player_state = browser.execute_script(get_player_state)
				print("player state is: ", player_state)
				if fraction == 1 and player_state == 1 :
					is_finished = 1

		except Exception as e:
			print(e)
			is_finished = 1
			
		browser.close()
check_buffering_occcured()


	




