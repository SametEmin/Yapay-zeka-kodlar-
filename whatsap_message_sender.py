
from selenium import webdriver
import selenium
from selenium.webdriver.common.by import By  
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
print("Scan QR Code, And then Enter")
input()
print("Logged In")


wait = WebDriverWait(driver,10)
search_box = wait.until(EC.presence_of_element_located((By.XPATH,"""//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p""")))
#search_box = driver.find_element(By.XPATH,"""//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p""")
search_box.click()
search_box.send_keys("Alperen Aİ")
search_box.send_keys(Keys.ENTER)
time.sleep(0.4)

person_box = wait.until(EC.presence_of_element_located((By.CLASS_NAME,"_21S-L")))
#person_box=driver.find_element(By.XPATH,"""//*[@id="pane-side"]/div[1]/div/div/div[5]/div/div/div/div[2]/div[1]/div[1]""")
person_box.click()
time.sleep(0.4)



i=0
while(i<40):
    try:
        chat_box = wait.until(EC.presence_of_element_located((By.XPATH,"""//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p""")))
        #chat_box=driver.find_element(By.XPATH,"""//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p""")
        chat_box.click()                        
        time.sleep(0.2)
        chat_box.send_keys("(Mesaj python botu ile atılmıştır)")
        chat_box.send_keys(Keys.ENTER)
        time.sleep(0.2)
        
    except:
        print("bir hata oldu..")
    finally:
        i+=1




print("Scan QR Code, And then Enter")
input()
print("Logged In")
driver.quit()




