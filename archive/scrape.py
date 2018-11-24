import os,time,threading
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
get_Loaded_Fraction = "return document.getElementById('movie_player').getVideoLoadedFraction()"
get_Playback_quality = "return document.getElementById('movie_player').getPlaybackQuality()"
quality_144p = 10;
quality_244p = 9;
quality_360p = 8;
quality_480p = 7;
quality_720p = 6;
quality_1080p = 5;

def record( url, quality, copies ):
    quality_counter = 0
    video_quality = 0
    is_finished = 0

    option = webdriver.ChromeOptions()
    option.add_argument("--incognito" )
    option.add_argument("--enable-quic")
    option.add_argument('--no-sandbox')


    # Create new Instance of Chrome in incognito mode
    browser = webdriver.Chrome(executable_path='/home/ehud/chromedriver', chrome_options=option)
    browser.maximize_window()
    for i in range( 1,copies):
        try:
            browser.get("https://www.youtube.com/watch?v=Yy25p3gTMZw")
            #click setting button


            browser.find_element_by_class_name("ytp-settings-button").click()
            #click quality button
            browser.find_elements_by_class_name("ytp-menuitem-label")[4].click()
            #select desired qdriveruality
            print(browser.find_elements_by_class_name("ytp-menuitem-label")[quality])
            ActionChains(browser).click( browser.find_elements_by_class_name("ytp-menuitem-label")[quality]).perform()
            video_quality = browser.execute_script(get_Playback_quality)
            print(video_quality)
            time.sleep(4)
            if(video_quality != 'tiny'):
                raise Exception('quality isnt matching')
            else:
                quality_counter += 1
            while is_finished != 1:
                is_finished = browser.execute_script(get_Loaded_Fraction)

            browser.close()

        except Exception as e: print(e)
    print(quality_counter)

record('Yy25p3gTMZw',quality_144p,2)

