
from selenium import webdriver
import selenium
from selenium.webdriver.common.by import By  
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 

def to_eng_string(s):
    s=s.replace("ı","i")
    s=s.replace("ö","o")
    s=s.replace("ü","u")
    s=s.replace("ş","s")
    s=s.replace("ğ","g")
    s=s.replace("ç","c")
    s=s.replace("İ","I")
    s=s.replace("Ö","O")
    s=s.replace("Ü","U")
    s=s.replace("Ş","S")
    s=s.replace("Ğ","G")
    s=s.replace("Ç","C")
    return s

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
print("Scan QR Code, And then Enter")
input()
print("Logged In")

#STRING PARSING
persons_str="+90 551 588 06 33, +90 531 817 62 41, +90 554 240 43 30, +90 532 207 27 80, +90 543 299 56 89, +90 555 397 92 07, +90 553 089 76 19, +90 531 332 63 49, +90 551 121 43 01, +90 533 823 53 29, +90 543 893 84 53, +90 507 895 55 87, +90 533 409 15 34, +90 551 598 51 23, +90 505 466 74 09, +90 553 200 94 63, +90 552 608 77 82, +90 534 986 98 63, +90 536 665 70 48, +90 552 923 30 76, +90 539 406 98 87, +90 539 237 79 87, +90 535 484 61 94, +90 536 782 61 04, +90 501 057 97 22, +90 505 016 55 14, +90 505 060 15 32, +90 505 131 96 30, +90 505 135 29 85, +90 505 321 10 44, +90 505 367 78 09, +90 506 130 70 19, +90 506 190 66 32, +90 506 208 87 16, +90 506 356 53 46, +90 506 385 08 73, +90 506 586 95 16, +90 506 793 11 42, +90 507 002 38 51, +90 507 014 45 78, +90 507 036 78 61, +90 507 097 16 35, +90 507 140 19 70, +90 507 280 77 16, +90 507 593 94 05, +90 507 854 52 18, +90 507 902 69 95, +90 507 905 79 69, +90 530 135 78 71, +90 530 484 04 53, +90 530 648 60 05, +90 530 735 40 77, +90 531 402 38 16, +90 531 610 22 64, +90 531 930 07 03, +90 532 067 53 06, +90 532 134 43 93, +90 533 213 74 27, +90 533 397 68 27, +90 533 560 23 40, +90 533 704 60 19, +90 533 967 90 04, +90 534 320 65 04, +90 534 450 09 98, +90 534 529 42 24, +90 534 545 81 85, +90 534 550 05 23, +90 534 787 91 99, +90 534 953 00 08, +90 534 971 05 02, +90 535 221 25 76, +90 535 238 61 44, +90 535 439 70 34, +90 535 598 07 39, +90 535 663 30 04, +90 535 899 97 04, +90 536 051 13 52, +90 536 249 02 08, +90 536 463 23 52, +90 536 466 57 10, +90 536 572 42 01, +90 536 574 43 64, +90 536 653 02 80, +90 536 833 62 93, +90 536 860 69 40, +90 536 975 73 77, +90 537 214 38 82, +90 537 237 69 02, +90 537 272 90 35, +90 537 611 56 66, +90 537 630 38 05, +90 537 652 66 78, +90 537 663 37 19, +90 537 767 21 51, +90 537 791 70 17, +90 537 868 18 44, +90 538 351 86 03, +90 538 374 98 45, +90 538 383 65 55, +90 538 384 98 22, +90 538 410 57 03, +90 538 500 31 16, +90 538 748 60 19, +90 538 768 81 99, +90 538 825 31 44, +90 539 200 81 67, +90 539 266 18 40, +90 539 291 21 24, +90 539 349 74 28, +90 539 409 58 78, +90 539 501 51 56, +90 539 657 37 81, +90 539 834 45 93, +90 541 188 37 54, +90 541 372 13 69, +90 541 391 63 48, +90 541 460 23 28, +90 541 510 92 69, +90 541 522 38 77, +90 541 642 93 31, +90 541 696 57 80, +90 542 122 33 05, +90 542 250 34 49, +90 542 366 62 33, +90 542 470 17 25, +90 542 657 07 58, +90 542 717 99 56, +90 542 788 96 01, +90 542 894 85 72, +90 543 569 38 83, +90 543 594 85 83, +90 543 606 55 18, +90 543 670 18 28, +90 543 698 35 25, +90 543 710 83 14, +90 543 772 82 06, +90 543 866 31 82, +90 544 216 03 55, +90 544 513 48 32, +90 544 684 11 97, +90 545 243 27 20, +90 545 256 13 23, +90 545 401 02 32, +90 545 497 06 01, +90 545 522 75 10, +90 545 633 49 95, +90 545 647 95 38, +90 545 820 47 17, +90 546 218 59 14, +90 546 278 96 57, +90 546 294 68 25, +90 546 426 49 99, +90 546 451 12 46, +90 546 461 49 01, +90 546 498 30 82, +90 546 518 45 24, +90 546 572 44 94, +90 546 586 41 95, +90 546 656 13 76, +90 546 695 89 72, +90 546 855 59 12, +90 546 932 86 14, +90 551 085 55 66, +90 551 161 95 77, +90 551 196 89 53, +90 551 239 00 33, +90 551 612 01 61, +90 551 631 49 66, +90 551 657 39 03, +90 551 858 60 23, +90 551 947 73 97, +90 552 001 86 88, +90 552 171 88 73, +90 552 218 34 52, +90 552 238 80 29, +90 552 264 43 80, +90 552 272 01 85, +90 552 295 67 00, +90 552 298 18 28, +90 552 433 01 52, +90 552 455 27 06, +90 552 480 20 58, +90 552 489 49 71, +90 552 567 60 03, +90 552 602 28 29, +90 553 006 72 77, +90 553 012 55 12, +90 553 073 41 59, +90 553 171 34 29, +90 553 327 87 49, +90 553 379 87 15, +90 553 491 28 28, +90 553 545 87 75, +90 553 663 40 53, +90 553 678 90 44, +90 553 688 61 19, +90 553 696 37 05, +90 553 718 64 02, +90 553 749 12 42, +90 553 860 10 27, +90 553 907 48 50, +90 553 919 79 38, +90 553 920 66 98, +90 555 046 33 90, +90 555 072 52 55, +90 555 106 64 88, +90 555 196 68 67, +90 555 260 26 48, +90 555 883 07 35"
persons_str=to_eng_string(persons_str)
persons=persons_str.split(", ")

#We define wait object to wait for the elements to load
wait = WebDriverWait(driver,10)

search_box = wait.until(EC.presence_of_element_located((By.XPATH,"""//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p""")))
#Alternative code block for finding the search box
#search_box = driver.find_element(By.XPATH,"""//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p""")
search_box.click()
#Searching in the whatsapp search box
search_box.send_keys("HUAI EĞİTİM/PROJE’23")
search_box.send_keys(Keys.ENTER)
time.sleep(0.4)

person_box = wait.until(EC.presence_of_element_located((By.CLASS_NAME,"_21S-L")))
#person_box=driver.find_element(By.XPATH,"""//*[@id="pane-side"]/div[1]/div/div/div[5]/div/div/div/div[2]/div[1]/div[1]""")
person_box.click()
time.sleep(0.4)

print("asdkasjdk")
input()
print("bekle")
try:
    chat_box = wait.until(EC.presence_of_element_located((By.XPATH,"""//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p""")))
    #chat_box=driver.find_element(By.XPATH,"""//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p""")
    chat_box.click()  

    for i in range(len(persons)):
        try:                    
            time.sleep(0.5)
            print(persons[i])
            chat_box.send_keys(f"@%s"%persons[i])
            chat_box.send_keys(Keys.ENTER)
            chat_box.send_keys(Keys.END)
            time.sleep(0.4)
        except:
            print("bir hata oldu ama ne bilmiyorum..")
            

    chat_box.send_keys("\n(Mesaj python ile otomatik atılmıştır)")
    
    time.sleep(0.2)
    
except:
    print("bir hata oldu..")

print("Scan QR Code, And then Enter")
input()
print("Logged In")
driver.quit()





