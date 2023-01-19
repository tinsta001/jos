import sqlite3
import smtplib
import time
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import ElementNotSelectableException
from selenium.common.exceptions import InvalidElementStateException
from selenium.common.exceptions import InvalidSelectorException
from selenium.common.exceptions import NoSuchAttributeException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

ignored_exceptions=(ElementClickInterceptedException,WebDriverException,ElementNotInteractableException,ElementNotSelectableException,ElementNotVisibleException,InvalidElementStateException,InvalidSelectorException,NoSuchAttributeException,StaleElementReferenceException,TimeoutException,)

start=0
while (start < 1):
    try:
        driver = webdriver.Chrome(executable_path='C:\webdrivers\chromedriver.exe')
        driver.get('https://virtual-games.virtustec.com/desktop-v4/default/?checkScroll=true&containerId=golden-race-desktop-app&profile=sportybet-dark&hwId=c738da5f-d2c7-409e-9886-3af263af244c&showHeader=true#/scheduled/league/playlist/13163')
        driver.maximize_window()
        wait = WebDriverWait(driver, 2)
        time.sleep(20)
        print("Lets see")
        conn = sqlite3.connect('sporty.db')
        c = conn.cursor()
        ht1=WebDriverWait(driver, 200).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[1]/div[2]/div[2]/app-participant-name[1]/span"))).text
        ms1=WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[1]/div[2]/div[2]/span/span/span[1]"))).text
        ms11=WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[1]/div[2]/div[2]/span/span/span[3]"))).text
        aw1=WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[1]/div[2]/div[2]/app-participant-name[2]/span"))).text
        score1=int(ms1)+int(ms11)
        if score1 >= 3:
            c.execute("UPDATE sporty1 SET OV = OV * 0 WHERE TEAM = ?", ([ht1]))
            c.execute("UPDATE sporty1 SET OV = OV * 0 WHERE TEAM = ?", ([aw1]))
        else:
            c.execute("UPDATE sporty1 SET OV = OV * 0 WHERE TEAM = ?", ([ht1]))
            c.execute("UPDATE sporty1 SET OV = OV * 0 WHERE TEAM = ?", ([aw1]))
        conn.commit()
        print(ht1+" & "+ aw1+ "=" + str(score1))
        print("--------------------------------")
        ht2=WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[2]/div[2]/div[2]/app-participant-name[1]/span"))).text
        ms2=WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[2]/div[2]/div[2]/span/span/span[1]"))).text
        ms22=WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[2]/div[2]/div[2]/span/span/span[3]"))).text
        aw2=WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[2]/div[2]/div[2]/app-participant-name[2]/span"))).text
        score2=int(ms2)+int(ms22)
        if score2 >= 3:
            c.execute("UPDATE sporty1 SET OV = OV * 0 WHERE TEAM = ?", ([ht2]))
            c.execute("UPDATE sporty1 SET OV = OV * 0 WHERE TEAM = ?", ([aw2]))
        else:
            c.execute("UPDATE sporty1 SET OV = OV * 0 WHERE TEAM = ?", ([ht2]))
            c.execute("UPDATE sporty1 SET OV = OV * 0 WHERE TEAM = ?", ([aw2]))
        conn.commit()
        print(ht2+" & "+ aw2+ "=" + str(score2))
        print("--------------------------------")
        ht3=WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[3]/div[2]/div[2]/app-participant-name[1]/span"))).text
        ms3=WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[3]/div[2]/div[2]/span/span/span[1]"))).text
        ms33=WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[3]/div[2]/div[2]/span/span/span[3]"))).text
        aw3=WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[3]/div[2]/div[2]/app-participant-name[2]/span"))).text
        score3=int(ms3)+int(ms33)
        if score3 >= 3:
            c.execute("UPDATE sporty1 SET OV = OV * 0 WHERE TEAM = ?", ([ht3]))
            c.execute("UPDATE sporty1 SET OV = OV * 0 WHERE TEAM = ?", ([aw3]))
        else:
            c.execute("UPDATE sporty1 SET OV = OV * 0 WHERE TEAM = ?", ([ht3]))
            c.execute("UPDATE sporty1 SET OV = OV * 0 WHERE TEAM = ?", ([aw3]))
        conn.commit()
        print(ht3+" & "+ aw3+ "=" + str(score3))
        print("--------------------------------")
        ht4=WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[4]/div[2]/div[2]/app-participant-name[1]/span"))).text
        ms4=WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[4]/div[2]/div[2]/span/span/span[1]"))).text
        ms44=WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[4]/div[2]/div[2]/span/span/span[3]"))).text
        aw4=WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[4]/div[2]/div[2]/app-participant-name[2]/span"))).text
        score4=int(ms4)+int(ms44)
        if score4 >= 3:
            c.execute("UPDATE sporty1 SET OV = OV * 0 WHERE TEAM = ?", ([ht4]))
            c.execute("UPDATE sporty1 SET OV = OV * 0 WHERE TEAM = ?", ([aw4]))
        else:
            c.execute("UPDATE sporty1 SET OV = OV * 0 WHERE TEAM = ?", ([ht4]))
            c.execute("UPDATE sporty1 SET OV = OV * 0 WHERE TEAM = ?", ([aw4]))
        conn.commit()
        print(ht4+" & "+ aw4+ "=" + str(score4))
        print("--------------------------------")
        ht5=WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[5]/div[2]/div[2]/app-participant-name[1]/span"))).text
        ms5=WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[5]/div[2]/div[2]/span/span/span[1]"))).text
        ms55=WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[5]/div[2]/div[2]/span/span/span[3]"))).text
        aw5=WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[5]/div[2]/div[2]/app-participant-name[2]/span"))).text
        score5=int(ms5)+int(ms55)
        if score5 >= 3:
            c.execute("UPDATE sporty1 SET OV = OV * 0 WHERE TEAM = ?", ([ht5]))
            c.execute("UPDATE sporty1 SET OV = OV * 0 WHERE TEAM = ?", ([aw5]))
        else:
            c.execute("UPDATE sporty1 SET OV = OV * 0 WHERE TEAM = ?", ([ht5]))
            c.execute("UPDATE sporty1 SET OV = OV * 0 WHERE TEAM = ?", ([aw5]))
        conn.commit()
        print(ht5+" & "+ aw5+ "=" + str(score5))
        print("--------------------------------")
        ht6=WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[6]/div[2]/div[2]/app-participant-name[1]/span"))).text
        ms6=WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[6]/div[2]/div[2]/span/span/span[1]"))).text
        ms66=WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[6]/div[2]/div[2]/span/span/span[3]"))).text
        aw6=WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[6]/div[2]/div[2]/app-participant-name[2]/span"))).text
        score6=int(ms6)+int(ms66)
        if score6 >= 3:
            c.execute("UPDATE sporty1 SET OV = OV * 0 WHERE TEAM = ?", ([ht6]))
            c.execute("UPDATE sporty1 SET OV = OV * 0 WHERE TEAM = ?", ([aw6]))
        else:
            c.execute("UPDATE sporty1 SET OV = OV * 0 WHERE TEAM = ?", ([ht6]))
            c.execute("UPDATE sporty1 SET OV = OV * 0 WHERE TEAM = ?", ([aw6]))
        conn.commit()
        print(ht6+" & "+ aw6+ "=" + str(score6))
        print("--------------------------------")
        ht7=WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[7]/div[2]/div[2]/app-participant-name[1]/span"))).text
        ms7=WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[7]/div[2]/div[2]/span/span/span[1]"))).text
        ms77=WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[7]/div[2]/div[2]/span/span/span[3]"))).text
        aw7=WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[7]/div[2]/div[2]/app-participant-name[2]/span"))).text
        score7=int(ms7)+int(ms77)
        if score7 >= 3:
            c.execute("UPDATE sporty1 SET OV = OV * 0 WHERE TEAM = ?", ([ht7]))
            c.execute("UPDATE sporty1 SET OV = OV * 0 WHERE TEAM = ?", ([aw7]))
        else:
            c.execute("UPDATE sporty1 SET OV = OV * 0 WHERE TEAM = ?", ([ht7]))
            c.execute("UPDATE sporty1 SET OV = OV * 0 WHERE TEAM = ?", ([aw7]))
        conn.commit()
        print(ht7+" & "+ aw7+ "=" + str(score7))
        print("--------------------------------")
        ht8=WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[8]/div[2]/div[2]/app-participant-name[1]/span"))).text
        ms8=WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[8]/div[2]/div[2]/span/span/span[1]"))).text
        ms88=WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[8]/div[2]/div[2]/span/span/span[3]"))).text
        aw8=WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[8]/div[2]/div[2]/app-participant-name[2]/span"))).text
        score8=int(ms8)+int(ms88)
        if score8 >= 3:
            c.execute("UPDATE sporty1 SET OV = OV * 0 WHERE TEAM = ?", ([ht8]))
            c.execute("UPDATE sporty1 SET OV = OV * 0 WHERE TEAM = ?", ([aw8]))
        else:
            c.execute("UPDATE sporty1 SET OV = OV * 0 WHERE TEAM = ?", ([ht8]))
            c.execute("UPDATE sporty1 SET OV = OV * 0 WHERE TEAM = ?", ([aw8]))
        conn.commit()
        print(ht8+" & "+ aw8+ "=" + str(score8))
        print("--------------------------------")
        ht9=WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[9]/div[2]/div[2]/app-participant-name[1]/span"))).text
        ms9=WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[9]/div[2]/div[2]/span/span/span[1]"))).text
        ms99=WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[9]/div[2]/div[2]/span/span/span[3]"))).text
        aw9=WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[9]/div[2]/div[2]/app-participant-name[2]/span"))).text
        score9=int(ms9)+int(ms99)
        if score9 >= 3:
            c.execute("UPDATE sporty1 SET OV = OV * 0 WHERE TEAM = ?", ([ht9]))
            c.execute("UPDATE sporty1 SET OV = OV * 0 WHERE TEAM = ?", ([aw9]))
        else:
            c.execute("UPDATE sporty1 SET OV = OV * 0 WHERE TEAM = ?", ([ht9]))
            c.execute("UPDATE sporty1 SET OV = OV * 0 WHERE TEAM = ?", ([aw9]))
        conn.commit()
        print(ht9+" & "+ aw9+ "=" + str(score9))
        print("--------------------------------")
        ht10=WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[10]/div[2]/div[2]/app-participant-name[1]/span"))).text
        ms10=WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[10]/div[2]/div[2]/span/span/span[1]"))).text
        ms1010=WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[10]/div[2]/div[2]/span/span/span[3]"))).text
        aw10=WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[10]/div[2]/div[2]/app-participant-name[2]/span"))).text
        score10=int(ms10)+int(ms1010)
        if score10 >= 3:
            c.execute("UPDATE sporty1 SET OV = OV * 0 WHERE TEAM = ?", ([ht10]))
            c.execute("UPDATE sporty1 SET OV = OV * 0 WHERE TEAM = ?", ([aw10]))
        else:
            c.execute("UPDATE sporty1 SET OV = OV * 0 WHERE TEAM = ?", ([ht10]))
            c.execute("UPDATE sporty1 SET OV = OV * 0 WHERE TEAM = ?", ([aw10]))
        #conn.commit()
        print(ht10+" & "+ aw10+ "=" + str(score10))
        print("--------------------------------")
        conn.commit()
        c.close()
        conn.close()
        start +=1
    except (ElementClickInterceptedException,WebDriverException,ElementNotInteractableException,ElementNotSelectableException,ElementNotVisibleException,InvalidElementStateException,InvalidSelectorException,NoSuchAttributeException,StaleElementReferenceException,TimeoutException) as e:
        print("Got stale element")
        pass

    
while True:
    try:
        weeks="Week 38"
        day=WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[2]/app-market-panel[1]/div/app-market-header/div/div[2]/app-event-ID/span"))).text    
        print(day)
        if day != weeks:
            print("it is week 1 to 37")
            conn = sqlite3.connect('sporty.db')
            c = conn.cursor() 
            #timer=WebDriverWait(driver, 180).until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-player/div[1]/div/div/div[2]/app-waiting/app-waiting-football/div/div/app-countdown/span"),"00:00"))
            print("True")
            time.sleep(10)
            #text1=WebDriverWait(driver, 500).until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[2]/app-live-event-selector/div/div[2]/div"),"No LIVE events available at this time."))            
            #print (text1)
            text2=WebDriverWait(driver, 500).until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-player/div[1]/div/div/div[2]/app-finished/app-finished-football/div[2]/div/span"),"FINISHED"))            
            print (text2)
            time.sleep(3)
            ht1=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[1]/div[2]/div[2]/app-participant-name[1]/span"))).text
            ms1=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[1]/div[2]/div[2]/span/span/span[1]"))).text
            ms11=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[1]/div[2]/div[2]/span/span/span[3]"))).text
            aw1=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[1]/div[2]/div[2]/app-participant-name[2]/span"))).text
            score1=int(ms1)+int(ms11)
            if score1 >= 3:
                c.execute("UPDATE sporty1 SET OV = OV * 0 WHERE TEAM = ?", ([ht1]))
                c.execute("UPDATE sporty1 SET OV = OV * 0 WHERE TEAM = ?", ([aw1]))    
            else:    
                c.execute("UPDATE sporty1 SET OV = OV + 1 WHERE TEAM = ?", ([ht1]))
                c.execute("UPDATE sporty1 SET OV = OV + 1 WHERE TEAM = ?", ([aw1]))
            if score1 == 2:
                c.execute("UPDATE sporty2 SET COUNT = COUNT + 1 WHERE TEAMS = ?", ([ht1]))
                c.execute("UPDATE sporty2 SET COUNT = COUNT + 1 WHERE TEAMS = ?", ([aw1]))
            else:
                c.execute("UPDATE sporty2 SET COUNT = COUNT * 0 WHERE TEAMS = ?", ([ht1]))
                c.execute("UPDATE sporty2 SET COUNT = COUNT * 0 WHERE TEAMS = ?", ([aw1]))
            conn.commit()
            print(ht1+" & "+ aw1+ "=" + str(score1))
            print("--------------------------------")
            ht2=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[2]/div[2]/div[2]/app-participant-name[1]/span"))).text
            ms2=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[2]/div[2]/div[2]/span/span/span[1]"))).text
            ms22=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[2]/div[2]/div[2]/span/span/span[3]"))).text
            aw2=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[2]/div[2]/div[2]/app-participant-name[2]/span"))).text
            score2=int(ms2)+int(ms22)
            if score2 >= 3:
                c.execute("UPDATE sporty1 SET OV = OV * 0 WHERE TEAM = ?", ([ht2]))
                c.execute("UPDATE sporty1 SET OV = OV * 0 WHERE TEAM = ?", ([aw2]))    
            else:    
                c.execute("UPDATE sporty1 SET OV = OV + 1 WHERE TEAM = ?", ([ht2]))
                c.execute("UPDATE sporty1 SET OV = OV + 1 WHERE TEAM = ?", ([aw2]))
            if score2 == 2:
                c.execute("UPDATE sporty2 SET COUNT = COUNT + 1 WHERE TEAMS = ?", ([ht2]))
                c.execute("UPDATE sporty2 SET COUNT = COUNT + 1 WHERE TEAMS = ?", ([aw2]))
            else:
                c.execute("UPDATE sporty2 SET COUNT = COUNT * 0 WHERE TEAMS = ?", ([ht2]))
                c.execute("UPDATE sporty2 SET COUNT = COUNT * 0 WHERE TEAMS = ?", ([aw2]))
            conn.commit()
            print(ht2+" & "+ aw2+ "=" + str(score2))
            print("--------------------------------")
            ht3=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[3]/div[2]/div[2]/app-participant-name[1]/span"))).text
            ms3=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[3]/div[2]/div[2]/span/span/span[1]"))).text
            ms33=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[3]/div[2]/div[2]/span/span/span[3]"))).text
            aw3=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[3]/div[2]/div[2]/app-participant-name[2]/span"))).text
            score3=int(ms3)+int(ms33)
            if score3 >= 3:
                c.execute("UPDATE sporty1 SET OV = OV * 0 WHERE TEAM = ?", ([ht3]))
                c.execute("UPDATE sporty1 SET OV = OV * 0 WHERE TEAM = ?", ([aw3]))    
            else:    
                c.execute("UPDATE sporty1 SET OV = OV + 1 WHERE TEAM = ?", ([ht3]))
                c.execute("UPDATE sporty1 SET OV = OV + 1 WHERE TEAM = ?", ([aw3]))
            if score3 == 2:
                c.execute("UPDATE sporty2 SET COUNT = COUNT + 1 WHERE TEAMS = ?", ([ht3]))
                c.execute("UPDATE sporty2 SET COUNT = COUNT + 1 WHERE TEAMS = ?", ([aw3]))
            else:
                c.execute("UPDATE sporty2 SET COUNT = COUNT * 0 WHERE TEAMS = ?", ([ht3]))
                c.execute("UPDATE sporty2 SET COUNT = COUNT * 0 WHERE TEAMS = ?", ([aw3]))
            conn.commit()
            print(ht3+" & "+ aw3+ "=" + str(score3))
            print("--------------------------------")
            ht4=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[4]/div[2]/div[2]/app-participant-name[1]/span"))).text
            ms4=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[4]/div[2]/div[2]/span/span/span[1]"))).text
            ms44=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[4]/div[2]/div[2]/span/span/span[3]"))).text
            aw4=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[4]/div[2]/div[2]/app-participant-name[2]/span"))).text
            score4=int(ms4)+int(ms44)
            if score4 >= 3:
                c.execute("UPDATE sporty1 SET OV = OV * 0 WHERE TEAM = ?", ([ht4]))
                c.execute("UPDATE sporty1 SET OV = OV * 0 WHERE TEAM = ?", ([aw4]))    
            else:    
                c.execute("UPDATE sporty1 SET OV = OV + 1 WHERE TEAM = ?", ([ht4]))
                c.execute("UPDATE sporty1 SET OV = OV + 1 WHERE TEAM = ?", ([aw4]))
            if score4 == 2:
                c.execute("UPDATE sporty2 SET COUNT = COUNT + 1 WHERE TEAMS = ?", ([ht4]))
                c.execute("UPDATE sporty2 SET COUNT = COUNT + 1 WHERE TEAMS = ?", ([aw4]))
            else:
                c.execute("UPDATE sporty2 SET COUNT = COUNT * 0 WHERE TEAMS = ?", ([ht4]))
                c.execute("UPDATE sporty2 SET COUNT = COUNT * 0 WHERE TEAMS = ?", ([aw4]))
            conn.commit()
            print(ht4+" & "+ aw4+ "=" + str(score4))
            print("--------------------------------")
            ht5=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[5]/div[2]/div[2]/app-participant-name[1]/span"))).text
            ms5=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[5]/div[2]/div[2]/span/span/span[1]"))).text
            ms55=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[5]/div[2]/div[2]/span/span/span[3]"))).text
            aw5=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[5]/div[2]/div[2]/app-participant-name[2]/span"))).text
            score5=int(ms5)+int(ms55)
            if score5 >= 3:
                c.execute("UPDATE sporty1 SET OV = OV * 0 WHERE TEAM = ?", ([ht5]))
                c.execute("UPDATE sporty1 SET OV = OV * 0 WHERE TEAM = ?", ([aw5]))    
            else:    
                c.execute("UPDATE sporty1 SET OV = OV + 1 WHERE TEAM = ?", ([ht5]))
                c.execute("UPDATE sporty1 SET OV = OV + 1 WHERE TEAM = ?", ([aw5]))
            if score5 == 2:
                c.execute("UPDATE sporty2 SET COUNT = COUNT + 1 WHERE TEAMS = ?", ([ht5]))
                c.execute("UPDATE sporty2 SET COUNT = COUNT + 1 WHERE TEAMS = ?", ([aw5]))
            else:
                c.execute("UPDATE sporty2 SET COUNT = COUNT * 0 WHERE TEAMS = ?", ([ht5]))
                c.execute("UPDATE sporty2 SET COUNT = COUNT * 0 WHERE TEAMS = ?", ([aw5]))
            conn.commit()
            print(ht5+" & "+ aw5+ "=" + str(score5))
            print("--------------------------------")
            ht6=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[6]/div[2]/div[2]/app-participant-name[1]/span"))).text
            ms6=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[6]/div[2]/div[2]/span/span/span[1]"))).text
            ms66=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[6]/div[2]/div[2]/span/span/span[3]"))).text
            aw6=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[6]/div[2]/div[2]/app-participant-name[2]/span"))).text
            score6=int(ms6)+int(ms66)
            if score6 >= 3:
                c.execute("UPDATE sporty1 SET OV = OV * 0 WHERE TEAM = ?", ([ht6]))
                c.execute("UPDATE sporty1 SET OV = OV * 0 WHERE TEAM = ?", ([aw6]))    
            else:    
                c.execute("UPDATE sporty1 SET OV = OV + 1 WHERE TEAM = ?", ([ht6]))
                c.execute("UPDATE sporty1 SET OV = OV + 1 WHERE TEAM = ?", ([aw6]))
            if score6 == 2:
                c.execute("UPDATE sporty2 SET COUNT = COUNT + 1 WHERE TEAMS = ?", ([ht6]))
                c.execute("UPDATE sporty2 SET COUNT = COUNT + 1 WHERE TEAMS = ?", ([aw6]))
            else:
                c.execute("UPDATE sporty2 SET COUNT = COUNT * 0 WHERE TEAMS = ?", ([ht6]))
                c.execute("UPDATE sporty2 SET COUNT = COUNT * 0 WHERE TEAMS = ?", ([aw6]))
            conn.commit()
            print(ht6+" & "+ aw6+ "=" + str(score6))
            print("--------------------------------")
            ht7=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[7]/div[2]/div[2]/app-participant-name[1]/span"))).text
            ms7=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[7]/div[2]/div[2]/span/span/span[1]"))).text
            ms77=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[7]/div[2]/div[2]/span/span/span[3]"))).text
            aw7=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[7]/div[2]/div[2]/app-participant-name[2]/span"))).text
            score7=int(ms7)+int(ms77)
            if score7 >= 3:
                c.execute("UPDATE sporty1 SET OV = OV * 0 WHERE TEAM = ?", ([ht7]))
                c.execute("UPDATE sporty1 SET OV = OV * 0 WHERE TEAM = ?", ([aw7]))    
            else:    
                c.execute("UPDATE sporty1 SET OV = OV + 1 WHERE TEAM = ?", ([ht7]))
                c.execute("UPDATE sporty1 SET OV = OV + 1 WHERE TEAM = ?", ([aw7]))
            if score7 == 2:
                c.execute("UPDATE sporty2 SET COUNT = COUNT + 1 WHERE TEAMS = ?", ([ht7]))
                c.execute("UPDATE sporty2 SET COUNT = COUNT + 1 WHERE TEAMS = ?", ([aw7]))
            else:
                c.execute("UPDATE sporty2 SET COUNT = COUNT * 0 WHERE TEAMS = ?", ([ht7]))
                c.execute("UPDATE sporty2 SET COUNT = COUNT * 0 WHERE TEAMS = ?", ([aw7]))
            conn.commit()
            print(ht7+" & "+ aw7+ "=" + str(score7))
            print("--------------------------------")
            ht8=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[8]/div[2]/div[2]/app-participant-name[1]/span"))).text
            ms8=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[8]/div[2]/div[2]/span/span/span[1]"))).text
            ms88=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[8]/div[2]/div[2]/span/span/span[3]"))).text
            aw8=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[8]/div[2]/div[2]/app-participant-name[2]/span"))).text
            score8=int(ms8)+int(ms88)
            if score8 >= 3:
                c.execute("UPDATE sporty1 SET OV = OV * 0 WHERE TEAM = ?", ([ht8]))
                c.execute("UPDATE sporty1 SET OV = OV * 0 WHERE TEAM = ?", ([aw8]))    
            else:    
                c.execute("UPDATE sporty1 SET OV = OV + 1 WHERE TEAM = ?", ([ht8]))
                c.execute("UPDATE sporty1 SET OV = OV + 1 WHERE TEAM = ?", ([aw8]))
            if score8 == 2:
                c.execute("UPDATE sporty2 SET COUNT = COUNT + 1 WHERE TEAMS = ?", ([ht8]))
                c.execute("UPDATE sporty2 SET COUNT = COUNT + 1 WHERE TEAMS = ?", ([aw8]))
            else:
                c.execute("UPDATE sporty2 SET COUNT = COUNT * 0 WHERE TEAMS = ?", ([ht8]))
                c.execute("UPDATE sporty2 SET COUNT = COUNT * 0 WHERE TEAMS = ?", ([aw8]))
            conn.commit()
            print(ht8+" & "+ aw8+ "=" + str(score8))
            print("--------------------------------")
            ht9=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[9]/div[2]/div[2]/app-participant-name[1]/span"))).text
            ms9=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[9]/div[2]/div[2]/span/span/span[1]"))).text
            ms99=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[9]/div[2]/div[2]/span/span/span[3]"))).text
            aw9=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[9]/div[2]/div[2]/app-participant-name[2]/span"))).text
            score9=int(ms9)+int(ms99)
            if score9 >= 3:
                c.execute("UPDATE sporty1 SET OV = OV * 0 WHERE TEAM = ?", ([ht9]))
                c.execute("UPDATE sporty1 SET OV = OV * 0 WHERE TEAM = ?", ([aw9]))    
            else:    
                c.execute("UPDATE sporty1 SET OV = OV + 1 WHERE TEAM = ?", ([ht9]))
                c.execute("UPDATE sporty1 SET OV = OV + 1 WHERE TEAM = ?", ([aw9]))
            if score9 == 2:
                c.execute("UPDATE sporty2 SET COUNT = COUNT + 1 WHERE TEAMS = ?", ([ht9]))
                c.execute("UPDATE sporty2 SET COUNT = COUNT + 1 WHERE TEAMS = ?", ([aw9]))
            else:
                c.execute("UPDATE sporty2 SET COUNT = COUNT * 0 WHERE TEAMS = ?", ([ht9]))
                c.execute("UPDATE sporty2 SET COUNT = COUNT * 0 WHERE TEAMS = ?", ([aw9]))
            conn.commit()
            print(ht9+" & "+ aw9+ "=" + str(score9))
            print("--------------------------------")
            ht1o=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[10]/div[2]/div[2]/app-participant-name[1]/span"))).text
            ms1o=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[10]/div[2]/div[2]/span/span/span[1]"))).text
            ms1o1o=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[10]/div[2]/div[2]/span/span/span[3]"))).text
            aw1o=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[10]/div[2]/div[2]/app-participant-name[2]/span"))).text
            score1o=int(ms1o)+int(ms1o1o)
            if score1o >= 3:
                c.execute("UPDATE sporty1 SET OV = OV * 0 WHERE TEAM = ?", ([ht1o]))
                c.execute("UPDATE sporty1 SET OV = OV * 0 WHERE TEAM = ?", ([aw1o]))    
            else:    
                c.execute("UPDATE sporty1 SET OV = OV + 1 WHERE TEAM = ?", ([ht1o]))
                c.execute("UPDATE sporty1 SET OV = OV + 1 WHERE TEAM = ?", ([aw1o]))
            if score1o == 2:
                c.execute("UPDATE sporty2 SET COUNT = COUNT + 1 WHERE TEAMS = ?", ([ht1o]))
                c.execute("UPDATE sporty2 SET COUNT = COUNT + 1 WHERE TEAMS = ?", ([aw1o]))
            else:
                c.execute("UPDATE sporty2 SET COUNT = COUNT * 0 WHERE TEAMS = ?", ([ht1o]))
                c.execute("UPDATE sporty2 SET COUNT = COUNT * 0 WHERE TEAMS = ?", ([aw1o]))
                
            conn.commit()
            print(ht1o+" & "+ aw1o+ "=" + str(score1o))
            print("--------------------------------")
            c.close()
            conn.close()
            time.sleep(1)
            timer=WebDriverWait(driver, 300).until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-player/div[1]/div/div/div[2]/app-waiting/app-waiting-football/div/div/app-countdown/span"),"00:50"))
            print(timer)
            conn = sqlite3.connect('sporty.db')
            c = conn.cursor()
            mn1=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/app-ranking/div/div[2]/div/table/tbody/tr[1]/td[1]"))).text
            te1=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/app-ranking/div/div[2]/div/table/tbody/tr[1]/td[2]/app-participant-name/span"))).text
            c.execute("UPDATE sporty1 SET POSITION = ? WHERE TEAM = ?",(mn1, te1,))
            conn.commit()
            print(mn1+":"+te1)
            print("----------------")
            
            mn2=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/app-ranking/div/div[2]/div/table/tbody/tr[2]/td[1]"))).text
            te2=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/app-ranking/div/div[2]/div/table/tbody/tr[2]/td[2]/app-participant-name/span"))).text
            c.execute("UPDATE sporty1 SET POSITION = ? WHERE TEAM = ?",(mn2, te2,))
            conn.commit()
            print(mn2+":"+te2)
            print("----------------")
            mn3=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/app-ranking/div/div[2]/div/table/tbody/tr[3]/td[1]"))).text
            te3=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/app-ranking/div/div[2]/div/table/tbody/tr[3]/td[2]/app-participant-name/span"))).text
            c.execute("UPDATE sporty1 SET POSITION = ? WHERE TEAM = ?",(mn3, te3,))
            conn.commit()
            print(mn3+":"+te3)
            print("----------------")
            mn4=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/app-ranking/div/div[2]/div/table/tbody/tr[4]/td[1]"))).text
            te4=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/app-ranking/div/div[2]/div/table/tbody/tr[4]/td[2]/app-participant-name/span"))).text
            c.execute("UPDATE sporty1 SET POSITION = ? WHERE TEAM = ?",(mn4, te4,))
            conn.commit()
            print(mn4+":"+te4)
            print("----------------")
            mn5=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/app-ranking/div/div[2]/div/table/tbody/tr[5]/td[1]"))).text
            te5=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/app-ranking/div/div[2]/div/table/tbody/tr[5]/td[2]/app-participant-name/span"))).text
            c.execute("UPDATE sporty1 SET POSITION = ? WHERE TEAM = ?",(mn5, te5,))
            conn.commit()
            print(mn5+":"+te5)
            print("----------------")
            mn6=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/app-ranking/div/div[2]/div/table/tbody/tr[6]/td[1]"))).text
            te6=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/app-ranking/div/div[2]/div/table/tbody/tr[6]/td[2]/app-participant-name/span"))).text
            c.execute("UPDATE sporty1 SET POSITION = ? WHERE TEAM = ?",(mn6, te6,))
            conn.commit()
            print(mn6+":"+te6)
            print("----------------")
            mn7=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/app-ranking/div/div[2]/div/table/tbody/tr[7]/td[1]"))).text
            te7=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/app-ranking/div/div[2]/div/table/tbody/tr[7]/td[2]/app-participant-name/span"))).text
            c.execute("UPDATE sporty1 SET POSITION = ? WHERE TEAM = ?",(mn7, te7,))
            conn.commit()
            print(mn7+":"+te7)
            print("----------------")
            mn8=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/app-ranking/div/div[2]/div/table/tbody/tr[8]/td[1]"))).text
            te8=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/app-ranking/div/div[2]/div/table/tbody/tr[8]/td[2]/app-participant-name/span"))).text
            c.execute("UPDATE sporty1 SET POSITION = ? WHERE TEAM = ?",(mn8, te8,))
            conn.commit()
            print(mn8+":"+te8)
            print("----------------")
            mn9=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/app-ranking/div/div[2]/div/table/tbody/tr[9]/td[1]"))).text
            te9=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/app-ranking/div/div[2]/div/table/tbody/tr[9]/td[2]/app-participant-name/span"))).text
            c.execute("UPDATE sporty1 SET POSITION = ? WHERE TEAM = ?",(mn9, te9,))
            conn.commit()
            print(mn9+":"+te9)
            print("----------------")
            mn10=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/app-ranking/div/div[2]/div/table/tbody/tr[10]/td[1]"))).text
            te10=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/app-ranking/div/div[2]/div/table/tbody/tr[10]/td[2]/app-participant-name/span"))).text
            c.execute("UPDATE sporty1 SET POSITION = ? WHERE TEAM = ?",(mn10, te10,))
            conn.commit()
            print(mn10+":"+te10)
            print("----------------")
            mn11=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/app-ranking/div/div[2]/div/table/tbody/tr[11]/td[1]"))).text
            te11=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/app-ranking/div/div[2]/div/table/tbody/tr[11]/td[2]/app-participant-name/span"))).text
            c.execute("UPDATE sporty1 SET POSITION = ? WHERE TEAM = ?",(mn11, te11,))
            conn.commit()
            print(mn11+":"+te11)
            print("----------------")
            mn12=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/app-ranking/div/div[2]/div/table/tbody/tr[12]/td[1]"))).text
            te12=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/app-ranking/div/div[2]/div/table/tbody/tr[12]/td[2]/app-participant-name/span"))).text
            c.execute("UPDATE sporty1 SET POSITION = ? WHERE TEAM = ?",(mn12, te12,))
            conn.commit()
            print(mn12+":"+te12)
            print("----------------")
            mn13=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/app-ranking/div/div[2]/div/table/tbody/tr[13]/td[1]"))).text
            te13=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/app-ranking/div/div[2]/div/table/tbody/tr[13]/td[2]/app-participant-name/span"))).text
            c.execute("UPDATE sporty1 SET POSITION = ? WHERE TEAM = ?",(mn13, te13,))
            conn.commit()
            print(mn13+":"+te13)
            print("----------------")
            mn14=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/app-ranking/div/div[2]/div/table/tbody/tr[14]/td[1]"))).text
            te14=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/app-ranking/div/div[2]/div/table/tbody/tr[14]/td[2]/app-participant-name/span"))).text
            c.execute("UPDATE sporty1 SET POSITION = ? WHERE TEAM = ?",(mn14, te14,))
            conn.commit()
            print(mn14+":"+te14)
            print("----------------")
            mn15=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/app-ranking/div/div[2]/div/table/tbody/tr[15]/td[1]"))).text
            te15=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/app-ranking/div/div[2]/div/table/tbody/tr[15]/td[2]/app-participant-name/span"))).text
            c.execute("UPDATE sporty1 SET POSITION = ? WHERE TEAM = ?",(mn15, te15,))
            conn.commit()
            print(mn15+":"+te15)
            print("----------------")
            mn16=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/app-ranking/div/div[2]/div/table/tbody/tr[16]/td[1]"))).text
            te16=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/app-ranking/div/div[2]/div/table/tbody/tr[16]/td[2]/app-participant-name/span"))).text
            c.execute("UPDATE sporty1 SET POSITION = ? WHERE TEAM = ?",(mn16, te16,))
            conn.commit()
            print(mn16+":"+te16)
            print("----------------")
            mn17=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/app-ranking/div/div[2]/div/table/tbody/tr[17]/td[1]"))).text
            te17=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/app-ranking/div/div[2]/div/table/tbody/tr[17]/td[2]/app-participant-name/span"))).text
            c.execute("UPDATE sporty1 SET POSITION = ? WHERE TEAM = ?",(mn17, te17,))
            conn.commit()
            print(mn17+":"+te17)
            print("----------------")
            mn18=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/app-ranking/div/div[2]/div/table/tbody/tr[18]/td[1]"))).text
            te18=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/app-ranking/div/div[2]/div/table/tbody/tr[18]/td[2]/app-participant-name/span"))).text
            c.execute("UPDATE sporty1 SET POSITION = ? WHERE TEAM = ?",(mn18, te18,))
            conn.commit()
            print(mn18+":"+te18)
            print("----------------")
            mn19=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/app-ranking/div/div[2]/div/table/tbody/tr[19]/td[1]"))).text
            te19=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/app-ranking/div/div[2]/div/table/tbody/tr[19]/td[2]/app-participant-name/span"))).text
            c.execute("UPDATE sporty1 SET POSITION = ? WHERE TEAM = ?",(mn19, te19,))
            conn.commit()
            print(mn19+":"+te19)
            print("----------------")
            mn20=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/app-ranking/div/div[2]/div/table/tbody/tr[20]/td[1]"))).text
            te20=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/app-ranking/div/div[2]/div/table/tbody/tr[20]/td[2]/app-participant-name/span"))).text
            c.execute("UPDATE sporty1 SET POSITION = ? WHERE TEAM = ?",(mn20, te20,))
            conn.commit()
            print(mn20+":"+te20)
            print("----------------")
            c.close()
            conn.close()
              
            print("Italy league now")
            italy = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div[1]/app-scheduled/div/asIDe[1]/app-menu/nav/app-menu-item/ul/li[2]/div/app-menu-item/ul/li[3]/a"))).click()
            print("England League Now")
            time.sleep(10)
            england = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div[1]/app-scheduled/div/asIDe[1]/app-menu/nav/app-menu-item/ul/li[2]/div/app-menu-item/ul/li[2]/a"))).click()
            time.sleep(10)
        else:
            print("It is week 38")

            timer=WebDriverWait(driver, 180).until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-player/div[1]/div/div/div[2]/app-waiting/app-waiting-football/div/div/app-countdown/span"),"00:00"))
            print(timer)
            time.sleep(10)
            el=WebDriverWait(driver, 90).until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[2]/app-live-event-selector/div/div[2]/div"),"No LIVE events available at this time."))
            time.sleep(5)
            conn = sqlite3.connect('sporty.db')
            c = conn.cursor()
            ht1=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[1]/div[2]/div[2]/app-participant-name[1]/span"))).text
            ms1=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[1]/div[2]/div[2]/span/span/span[1]"))).text
            ms11=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[1]/div[2]/div[2]/span/span/span[3]"))).text
            aw1=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[1]/div[2]/div[2]/app-participant-name[2]/span"))).text
            score1=int(ms1)+int(ms11)
            if score1 >= 3:
                c.execute("UPDATE sporty1 SET OV = OV + 1  WHERE TEAM = ?", ([ht1]))
                c.execute("UPDATE sporty1 SET OV = OV + 1 WHERE TEAM = ?", ([aw1]))
            else:
                c.execute("UPDATE sporty1 SET OV = OV + 1 WHERE TEAM = ?", ([ht1]))
                c.execute("UPDATE sporty1 SET OV = OV + 1 WHERE TEAM = ?", ([aw1]))
            conn.commit()
            print(ht1+" & "+ aw1+ "=" + str(score1))
            print("--------------------------------")
            ht2=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[2]/div[2]/div[2]/app-participant-name[1]/span"))).text
            ms2=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[2]/div[2]/div[2]/span/span/span[1]"))).text
            ms22=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[2]/div[2]/div[2]/span/span/span[3]"))).text
            aw2=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[2]/div[2]/div[2]/app-participant-name[2]/span"))).text
            score2=int(ms2)+int(ms22)
            if score2 >= 3:
                c.execute("UPDATE sporty1 SET OV = OV + 1 WHERE TEAM = ?", ([ht2]))
                c.execute("UPDATE sporty1 SET OV = OV + 1 WHERE TEAM = ?", ([aw2]))
            else:
                c.execute("UPDATE sporty1 SET OV = OV + 1 WHERE TEAM = ?", ([ht2]))
                c.execute("UPDATE sporty1 SET OV = OV + 1 WHERE TEAM = ?", ([aw2]))
            conn.commit()
            print(ht2+" & "+ aw2+ "=" + str(score2))
            print("--------------------------------")
            ht3=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[3]/div[2]/div[2]/app-participant-name[1]/span"))).text
            ms3=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[3]/div[2]/div[2]/span/span/span[1]"))).text
            ms33=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[3]/div[2]/div[2]/span/span/span[3]"))).text
            aw3=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[3]/div[2]/div[2]/app-participant-name[2]/span"))).text
            score3=int(ms3)+int(ms33)
            if score3 >= 3:
                c.execute("UPDATE sporty1 SET OV = OV + 1 WHERE TEAM = ?", ([ht3]))
                c.execute("UPDATE sporty1 SET OV = OV + 1 WHERE TEAM = ?", ([aw3]))
            else:
                c.execute("UPDATE sporty1 SET OV = OV + 1 WHERE TEAM = ?", ([ht3]))
                c.execute("UPDATE sporty1 SET OV = OV + 1 WHERE TEAM = ?", ([aw3]))
            conn.commit()
            print(ht3+" & "+ aw3+ "=" + str(score3))
            print("--------------------------------")
            ht4=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[4]/div[2]/div[2]/app-participant-name[1]/span"))).text
            ms4=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[4]/div[2]/div[2]/span/span/span[1]"))).text
            ms44=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[4]/div[2]/div[2]/span/span/span[3]"))).text
            aw4=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[4]/div[2]/div[2]/app-participant-name[2]/span"))).text
            score4=int(ms4)+int(ms44)
            if score4 >= 3:
                c.execute("UPDATE sporty1 SET OV = OV + 1 WHERE TEAM = ?", ([ht4]))
                c.execute("UPDATE sporty1 SET OV = OV + 1 WHERE TEAM = ?", ([aw4]))
            else:
                c.execute("UPDATE sporty1 SET OV = OV + 1 WHERE TEAM = ?", ([ht4]))
                c.execute("UPDATE sporty1 SET OV = OV + 1 WHERE TEAM = ?", ([aw4]))
            conn.commit()
            print(ht4+" & "+ aw4+ "=" + str(score4))
            print("--------------------------------")
            ht5=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[5]/div[2]/div[2]/app-participant-name[1]/span"))).text
            ms5=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[5]/div[2]/div[2]/span/span/span[1]"))).text
            ms55=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[5]/div[2]/div[2]/span/span/span[3]"))).text
            aw5=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[5]/div[2]/div[2]/app-participant-name[2]/span"))).text
            score5=int(ms5)+int(ms55)
            if score5 >= 3:
                c.execute("UPDATE sporty1 SET OV = OV + 1 WHERE TEAM = ?", ([ht5]))
                c.execute("UPDATE sporty1 SET OV = OV + 1 WHERE TEAM = ?", ([aw5]))
            else:
                c.execute("UPDATE sporty1 SET OV = OV + 1 WHERE TEAM = ?", ([ht5]))
                c.execute("UPDATE sporty1 SET OV = OV + 1 WHERE TEAM = ?", ([aw5]))
            conn.commit()
            print(ht5+" & "+ aw5+ "=" + str(score5))
            print("--------------------------------")
            ht6=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[6]/div[2]/div[2]/app-participant-name[1]/span"))).text
            ms6=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[6]/div[2]/div[2]/span/span/span[1]"))).text
            ms66=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[6]/div[2]/div[2]/span/span/span[3]"))).text
            aw6=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[6]/div[2]/div[2]/app-participant-name[2]/span"))).text
            score6=int(ms6)+int(ms66)
            if score6 >= 3:
                c.execute("UPDATE sporty1 SET OV = OV + 1 WHERE TEAM = ?", ([ht6]))
                c.execute("UPDATE sporty1 SET OV = OV + 1 WHERE TEAM = ?", ([aw6]))
            else:
                c.execute("UPDATE sporty1 SET OV = OV + 1 WHERE TEAM = ?", ([ht6]))
                c.execute("UPDATE sporty1 SET OV = OV + 1 WHERE TEAM = ?", ([aw6]))
            conn.commit()
            print(ht6+" & "+ aw6+ "=" + str(score6))
            print("--------------------------------")
            ht7=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[7]/div[2]/div[2]/app-participant-name[1]/span"))).text
            ms7=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[7]/div[2]/div[2]/span/span/span[1]"))).text
            ms77=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[7]/div[2]/div[2]/span/span/span[3]"))).text
            aw7=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[7]/div[2]/div[2]/app-participant-name[2]/span"))).text
            score7=int(ms7)+int(ms77)
            if score7 >= 3:
                c.execute("UPDATE sporty1 SET OV = OV + 1 WHERE TEAM = ?", ([ht7]))
                c.execute("UPDATE sporty1 SET OV = OV + 1 WHERE TEAM = ?", ([aw7]))
            else:
                c.execute("UPDATE sporty1 SET OV = OV + 1 WHERE TEAM = ?", ([ht7]))
                c.execute("UPDATE sporty1 SET OV = OV + 1 WHERE TEAM = ?", ([aw7]))
            conn.commit()
            print(ht7+" & "+ aw7+ "=" + str(score7))
            print("--------------------------------")
            ht8=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[8]/div[2]/div[2]/app-participant-name[1]/span"))).text
            ms8=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[8]/div[2]/div[2]/span/span/span[1]"))).text
            ms88=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[8]/div[2]/div[2]/span/span/span[3]"))).text
            aw8=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[8]/div[2]/div[2]/app-participant-name[2]/span"))).text
            score8=int(ms8)+int(ms88)
            if score8 >= 3:
                c.execute("UPDATE sporty1 SET OV = OV + 1 WHERE TEAM = ?", ([ht8]))
                c.execute("UPDATE sporty1 SET OV = OV + 1 WHERE TEAM = ?", ([aw8]))
            else:
                c.execute("UPDATE sporty1 SET OV = OV + 1 WHERE TEAM = ?", ([ht8]))
                c.execute("UPDATE sporty1 SET OV = OV + 1 WHERE TEAM = ?", ([aw8]))
            conn.commit()
            print(ht8+" & "+ aw8+ "=" + str(score8))
            print("--------------------------------")
            ht9=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[9]/div[2]/div[2]/app-participant-name[1]/span"))).text
            ms9=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[9]/div[2]/div[2]/span/span/span[1]"))).text
            ms99=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[9]/div[2]/div[2]/span/span/span[3]"))).text
            aw9=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[9]/div[2]/div[2]/app-participant-name[2]/span"))).text
            score9=int(ms9)+int(ms99)
            if score9 >= 3:
                c.execute("UPDATE sporty1 SET OV = OV + 1 WHERE TEAM = ?", ([ht9]))
                c.execute("UPDATE sporty1 SET OV = OV + 1 WHERE TEAM = ?", ([aw9]))
            else:
                c.execute("UPDATE sporty1 SET OV = OV + 1 WHERE TEAM = ?", ([ht9]))
                c.execute("UPDATE sporty1 SET OV = OV + 1 WHERE TEAM = ?", ([aw9]))
            conn.commit()
            print(ht9+" & "+ aw9+ "=" + str(score9))
            print("--------------------------------")
            ht10=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[10]/div[2]/div[2]/app-participant-name[1]/span"))).text
            ms10=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[10]/div[2]/div[2]/span/span/span[1]"))).text
            ms1010=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[10]/div[2]/div[2]/span/span/span[3]"))).text
            aw10=WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[1]/app-live-event-panel/div/div/app-live-event-result/app-result-football/div[2]/div[10]/div[2]/div[2]/app-participant-name[2]/span"))).text
            score10=int(ms10)+int(ms1010)
            if score10 >= 3:
                c.execute("UPDATE sporty1 SET OV = OV + 1 WHERE TEAM = ?", ([ht10]))
                c.execute("UPDATE sporty1 SET OV = OV + 1 WHERE TEAM = ?", ([aw10]))
            else:
                c.execute("UPDATE sporty1 SET OV = OV + 1 WHERE TEAM = ?", ([ht10]))
                c.execute("UPDATE sporty1 SET OV = OV + 1 WHERE TEAM = ?", ([aw10]))
            conn.commit()
            print(ht10+" & "+ aw10+ "=" + str(score10))
            print("--------------------------------")
            c.close()            
            conn.close()
            time.sleep(120)
            print("Italy league now")
            italy = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div[1]/app-scheduled/div/asIDe[1]/app-menu/nav/app-menu-item/ul/li[2]/div/app-menu-item/ul/li[3]/a"))).click()
            print("England League Now")
            time.sleep(10)
            england = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div[1]/app-scheduled/div/asIDe[1]/app-menu/nav/app-menu-item/ul/li[2]/div/app-menu-item/ul/li[2]/a"))).click()
            time.sleep(10)          
        
    except (ElementClickInterceptedException,ElementNotInteractableException,ElementNotSelectableException,ElementNotVisibleException,InvalidElementStateException,InvalidSelectorException,NoSuchAttributeException,StaleElementReferenceException,TimeoutException,) as e:
            print("An error occured 1")
            continue
        



