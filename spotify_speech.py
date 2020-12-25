from gtts import gTTS
import speech_recognition as sr
import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Play_Music:
    def __init__(self, user, password):
        url = 'https://open.spotify.com/'

        self.browser = webdriver.Chrome()
        self.browser.get(url)

        self.browser.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[1]/header/div[5]/button[2]').click()

        time.sleep(3)
        self.browser.find_element_by_xpath('//*[@id="login-username"]').send_keys(user)
        self.browser.find_element_by_xpath('//*[@id="login-password"]').send_keys(password + Keys.ENTER)

        time.sleep(5)
        self.browser.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/nav/div[2]/div/div[2]').click()
        time.sleep(3)
    def play(self):
        # start
        self.browser.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[4]/main/div[2]/div[2]/div/div/div[2]/section/div[4]/div/div[2]/div[2]/div[1]/div/div[1]/div').click()
    def next(self):
        # next
        self.browser.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[3]/footer/div/div[2]/div/div[1]/button[4]').click()
    def pause(self):
        # pause
        self.browser.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[3]/footer/div/div[2]/div/div[1]/button[3]').click()
    def previous(self):
        # previous - back
        for _ in range(2):
            self.browser.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[3]/footer/div/div[2]/div/div[1]/button[2]').click()
    def kill(self):
        self.browser.close()

user = '***************@gmail.com'
password = '*************'

PM = Play_Music(user, password)
r = sr.Recognizer()

text = 'nothing'

while True:
    with sr.Microphone() as source:
        print('Speak Anything : ')
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print('You said: {}'.format(text))
        except:
            print('Sorry could not hear')
    try:
        text = text.lower()
    except NameError:
        text = 'nothing'

    if 'bye' in text:
        PM.kill()
    elif 'next' in text:
        PM.next()
    elif 'pause' in text:
        PM.pause()
    elif 'play' in text:
        PM.play()
    elif 'back' in text:
        PM.previous()
    else:
        continue
    text = 'nothing'
