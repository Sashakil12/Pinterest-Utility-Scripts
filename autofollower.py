import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import time
from random import randint

#Setup
def get_follows(url):
	#Make sure you have singed into this profile with your account, or add functionality to sign in.
	profile = FirefoxProfile("/home/winterfell/.mozilla/firefox/nrw5axxu.default")
	driver = webdriver.Firefox(profile)
	print "Loaded Profile"

	for i in range(0,2):
		start = 0
		#Avoid ICS & Sign into pintrest..
		print "Getting Google.com"
		driver.get("http://www.google.com")
		time.sleep(5)
		driver.get("http://www.pintrest.com")
		time.sleep(5) 

		#Url to Follow
		driver.get(url[i])

		driver.execute_script("window.scrollTo(0, 400)")
		elem = []
		while start == 0:
			
			elem = driver.find_elements_by_xpath('//span[@class=\"buttonText\"]')
			for each in elem:
				if each.text == "Follow":
					each.click()
					i=i+1
					print str(each) + ':' + str(i) 
					time.sleep(randint(3,10))
				if i == 250:
					start = 1
					break
				if i >= 255:
					start = 1
					break
		if i >= 260:
			print "Aborted!"
			break

get_follows(['https://www.pinterest.com/wholefoods/followers/','https://www.pinterest.com/fooddotcom/followers/','https://www.pinterest.com/foodnetwork/followers/'])
