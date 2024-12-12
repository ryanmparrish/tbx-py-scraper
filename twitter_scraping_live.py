
# Import Dependencies
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()
driver.get("https://x.com/i/flow/login")

subject = "Chobani"

# Setup the log in
sleep(3)
username = driver.find_element(By.XPATH,"//input[@name='text']")
username.send_keys("churchofslidin@gmail.com")
next_button = driver.find_element(By.XPATH,"//span[contains(text(),'Next')]")
next_button.click()

# phone
sleep(3)
username = driver.find_element(By.XPATH,"//input[@name='text']")
username.send_keys("8017421743")
next_button = driver.find_element(By.XPATH,"//span[contains(text(),'Next')]")
next_button.click()

sleep(3)
password = driver.find_element(By.XPATH,"//input[@name='password']")
password.send_keys('Surf@ndSnow<3')
log_in = driver.find_element(By.XPATH,"//span[contains(text(),'Log in')]")
log_in.click()

# Search item and fetch it
sleep(3)
search_box = driver.find_element(By.XPATH,"//input[@data-testid='SearchBox_Search_Input']")
search_box.send_keys(subject)
search_box.send_keys(Keys.ENTER)

# sleep(3)
# people = driver.find_element(By.XPATH,"//span[contains(text(),'People')]")
# people.click()

sleep(3)
people = driver.find_element(By.XPATH,"//span[contains(text(),'Latest')]")
people.click()

# sleep(3)
# todo - Find selector for profile... etc. 
# profile = driver.find_element(By.XPATH,"//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[2]/div/section/div/div/div[1]/div/div/div/div/div[2]/div/div[1]/div/div[1]/a/div/div[1]/span/span")
# profile.click()


# UserTag = driver.find_element(By.XPATH,"//div[@data-testid='User-Names']").text
# TimeStamp = driver.find_element(By.XPATH,"//time").get_attribute('datetime')
# Tweet = driver.find_element(By.XPATH,"//div[@data-testid='tweetText']").text
# Reply = driver.find_element(By.XPATH,"//div[@data-testid='reply']").text
# reTweet = driver.find_element(By.XPATH,"//div[@data-testid='retweet']").text
# Like = driver.find_element(By.XPATH,"//div[@data-testid='like']").text


# UserTags=[]
# TimeStamps=[]
# Tweets=[]
# Replys=[]
# reTweets=[]
# Likes=[]

# New data-testids... ^ above are out of date
# data-testid = Tweet-User-Avatar, User-Name, tweetText, reply, rewtweet, like, bookmark

UserNames=[]
TweetTexts=[]
Replys=[]
Rewtweets=[]
Likes=[]

articles = driver.find_elements(By.XPATH,"//article[@data-testid='tweet']")
while True:
    for article in articles:
        UserName = driver.find_element(By.XPATH,".//div[@data-testid='User-Name']").text
        UserNames.append(UserName)
        
        # TimeStamp = driver.find_element(By.XPATH,".//time").get_attribute('datetime')
        # TimeStamps.append(TimeStamp)
        
        TweetText = driver.find_element(By.XPATH,".//div[@data-testid='tweetText']").text
        TweetTexts.append(TweetText)
        
        Reply = driver.find_element(By.XPATH,".//button[@data-testid='reply']").text
        Replys.append(Reply)
        
        ReTweet = driver.find_element(By.XPATH,".//button[@data-testid='retweet']").text
        Rewtweets.append(ReTweet)
        
        Like = driver.find_element(By.XPATH,".//button[@data-testid='like']").text
        Likes.append(Like)
        
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    sleep(3)
    articles = driver.find_elements(By.XPATH,"//article[@data-testid='tweet']")
    Tweets2 = list(set(TweetTexts))
    if len(Tweets2) > 5:
        break


print(
len(UserNames),
len(TweetTexts),
len(Replys),
len(Rewtweets),
len(Likes))


import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame(zip(UserNames,TweetTexts,Replys,Rewtweets,Likes),columns=['UserNames','TweetTexts','Replys','Rewtweets','Likes'])

# df = pd.DataFrame(zip(UserTags,TimeStamps,Tweets,Replys,reTweets,Likes),columns=['UserTags','TimeStamps','Tweets','Replys','reTweets','Likes'])

# Display the first 5 rows of the DataFrame
df.head()

# df.to_excel(r"D:\Learnerea\Tables\tweets_live.xlsx",index=False)

# import os
# os.system('start "excel" "D:\Learnerea\Tables\\tweets_live.xlsx"')

# Save the DataFrame to a CSV file
df.to_csv('chobani_tweets_data.csv', index=False, encoding='utf-8')
