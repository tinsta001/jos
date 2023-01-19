import sqlite3
import smtplib
import time
import itertools
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
ignored_exceptions=(ElementClickInterceptedException,ElementNotInteractableException,ElementNotSelectableException,ElementNotVisibleException,InvalidElementStateException,InvalidSelectorException,NoSuchAttributeException,StaleElementReferenceException,TimeoutException,)
driver = webdriver.Chrome(executable_path='C:\webdrivers\chromedriver.exe')
driver.get('https://www.mozzartbet.co.ke/en#/golden-race')
driver.maximize_window()
wait = WebDriverWait(driver, 500)

hover=wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[4]/div/div/div[2]/button[2]"))).click()
phoneNumber=wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='pageWrapper']/div/header/section[1]/article[3]/section/article/div[1]/form/input[1]")))
phoneNumber.clear()
phoneNumber.send_keys("0702551503")
pswd=wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='pageWrapper']/div/header/section[1]/article[3]/section/article/div[1]/form/input[2]")))
pswd.send_keys("6670")
time.sleep(1)

#log=driver.find_element_by_link_text("OK").click()
sub=wait.until(EC.element_to_be_clickable((By.XPATH, ".//button[contains(@class,'login-btn') and @type='submit']"))).click()
time.sleep(5)

iframe = wait.until(EC.element_to_be_clickable((By.ID, "xrpess-iframe")))
driver.switch_to.frame(iframe)
print("switched to frame1")
time.sleep(5)
iframe1 = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/iframe")))
driver.switch_to.frame(iframe1)
print("switched to frame2")
time.sleep(5)
football = WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/aside[1]/app-menu/nav/app-menu-item/ul/li[2]/a"))).click()
time.sleep(1)
print("switched to football")
element = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div[1]/app-scheduled/div/aside[1]/app-menu/nav/app-menu-item/ul/li[2]/div/app-menu-item/ul/li[2]/a"))).click()
print("This is England")
def coun():
    x=[]
    conn = sqlite3.connect('sporty.db')
    c= conn.cursor()
    def fat():
        c.execute("SELECT TEAMS FROM sporty2 WHERE COUNT>0 ")
        rows = c.fetchall()
        for row in rows:
            x.append(row)
    fat()
    coun.ti=x
    print(coun.ti)
    return coun.ti
    
def com(list1,list2): 
    result=0
    for x in list1:
        for y in list2:
            if x==y:
                result=1
    com.john=result
    b=com.john
    return b
        
def cow():
    l=[]
    conn = sqlite3.connect('sporty.db')
    c = conn.cursor()
    def fet():
        c.execute("SELECT TEAM FROM sporty1 WHERE OV=0 AND POSITION BETWEEN 1 and 20 ORDER BY POSITION ASC LIMIT 1")
        rows = c.fetchall()
        for row in rows:
            l.append(row)
        c.execute("SELECT TEAM FROM sporty1 WHERE OV=2 AND POSITION BETWEEN 1 and 20 ORDER BY POSITION ASC LIMIT 1")
        rows = c.fetchall()
        for row in rows:
            l.append(row)

    fet()
    cow.li=l
    leno=len(cow.li)
    cow.lenoo=str(leno)
    c.close()
    conn.close()
    print(cow.li)
    time.sleep(1)
final=[]
win=0
while True:
    try:
        timer1=WebDriverWait(driver, 800).until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[2]/app-market-panel[1]/div/app-market-header/div/div[1]/app-countdown/span"),"00:30"))
        print(timer1)
        cow()
        if cow.li!=[]:
            for row in cow.li:
                row9=str(row)
                if row9!="":
                    row1=row9.strip("('',)")
                    mt1=wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='main-content']/app-event-list/div/div/div[2]/app-market-panel[1]/div/app-market/div/app-match-result/div[2]/app-match-cell/div/a[1]/span[2]")))
                    mt2=wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='main-content']/app-event-list/div/div/div[2]/app-market-panel[1]/div/app-market/div/app-match-result/div[3]/app-match-cell/div/a[1]/span[2]")))
                    mt3=wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='main-content']/app-event-list/div/div/div[2]/app-market-panel[1]/div/app-market/div/app-match-result/div[4]/app-match-cell/div/a[1]/span[2]")))
                    mt4=wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='main-content']/app-event-list/div/div/div[2]/app-market-panel[1]/div/app-market/div/app-match-result/div[5]/app-match-cell/div/a[1]/span[2]")))
                    mt5=wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='main-content']/app-event-list/div/div/div[2]/app-market-panel[1]/div/app-market/div/app-match-result/div[6]/app-match-cell/div/a[1]/span[2]")))
                    mt6=wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='main-content']/app-event-list/div/div/div[2]/app-market-panel[1]/div/app-market/div/app-match-result/div[7]/app-match-cell/div/a[1]/span[2]")))
                    mt7=wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='main-content']/app-event-list/div/div/div[2]/app-market-panel[1]/div/app-market/div/app-match-result/div[8]/app-match-cell/div/a[1]/span[2]")))
                    mt8=wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='main-content']/app-event-list/div/div/div[2]/app-market-panel[1]/div/app-market/div/app-match-result/div[9]/app-match-cell/div/a[1]/span[2]")))
                    mt9=wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='main-content']/app-event-list/div/div/div[2]/app-market-panel[1]/div/app-market/div/app-match-result/div[10]/app-match-cell/div/a[1]/span[2]")))
                    mt10=wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='main-content']/app-event-list/div/div/div[2]/app-market-panel[1]/div/app-market/div/app-match-result/div[11]/app-match-cell/div/a[1]/span[2]")))
                    how=[mt1.text,mt2.text,mt3.text,mt4.text,mt5.text,mt6.text,mt7.text,mt8.text,mt9.text,mt10.text]
                    why=[mt1,mt2,mt3,mt4,mt5,mt6,mt7,mt8,mt9,mt10]
                    def find_indices(search_list, search_item):
                        for (index, item) in enumerate(search_list):
                          if search_item in item:
                              return index 
                    cl=find_indices(how,row1)
                    final.append(cl)
                else:
                    continue
            result = []
            for i in final: 
                if i not in result: 
                    result.append(i)
            leno=[]
            c=[]
            for p in itertools.islice(result,0,2):
                mt1=wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='main-content']/app-event-list/div/div/div[2]/app-market-panel[1]/div/app-market/div/app-match-result/div[2]/app-match-cell/div/a[1]/span[2]")))
                mt2=wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='main-content']/app-event-list/div/div/div[2]/app-market-panel[1]/div/app-market/div/app-match-result/div[3]/app-match-cell/div/a[1]/span[2]")))
                mt3=wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='main-content']/app-event-list/div/div/div[2]/app-market-panel[1]/div/app-market/div/app-match-result/div[4]/app-match-cell/div/a[1]/span[2]")))
                mt4=wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='main-content']/app-event-list/div/div/div[2]/app-market-panel[1]/div/app-market/div/app-match-result/div[5]/app-match-cell/div/a[1]/span[2]")))
                mt5=wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='main-content']/app-event-list/div/div/div[2]/app-market-panel[1]/div/app-market/div/app-match-result/div[6]/app-match-cell/div/a[1]/span[2]")))
                mt6=wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='main-content']/app-event-list/div/div/div[2]/app-market-panel[1]/div/app-market/div/app-match-result/div[7]/app-match-cell/div/a[1]/span[2]")))
                mt7=wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='main-content']/app-event-list/div/div/div[2]/app-market-panel[1]/div/app-market/div/app-match-result/div[8]/app-match-cell/div/a[1]/span[2]")))
                mt8=wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='main-content']/app-event-list/div/div/div[2]/app-market-panel[1]/div/app-market/div/app-match-result/div[9]/app-match-cell/div/a[1]/span[2]")))
                mt9=wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='main-content']/app-event-list/div/div/div[2]/app-market-panel[1]/div/app-market/div/app-match-result/div[10]/app-match-cell/div/a[1]/span[2]")))
                mt10=wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='main-content']/app-event-list/div/div/div[2]/app-market-panel[1]/div/app-market/div/app-match-result/div[11]/app-match-cell/div/a[1]/span[2]")))
                how=[mt1.text,mt2.text,mt3.text,mt4.text,mt5.text,mt6.text,mt7.text,mt8.text,mt9.text,mt10.text]
                why=[mt1,mt2,mt3,mt4,mt5,mt6,mt7,mt8,mt9,mt10]
                mn=how[p]
                dl=why[p]
                c.append(mn)
                driver.execute_script("arguments[0].click();", dl)
                time.sleep(1)
                #OVER2.5
                                                                             
                matchunder1=wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-detail/div/div/div[2]/app-event-detail-content/div[3]/app-market/div/app-over-under-football/div/div[2]/div/app-odd[1]/div/div/div[2]")))
                driver.execute_script("arguments[0].click();", matchunder1)
                time.sleep(1)          
                sub=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#playlist_13161 > a")))
                driver.execute_script("arguments[0].click();", sub)
                leno.append(p)
            print(leno)
            le=len(leno)
            lei=str(le)
            stake_amount1=wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='bets-stake-amount-"+lei+"']")))
            driver.execute_script("arguments[0].click();", stake_amount1)
            stake_amount1.send_keys("15")
            time.sleep(1)
            submit=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='main-right']/app-bet-sidebar/div[1]/div[1]/app-betslip/div/div/button")))
            driver.execute_script("arguments[0].click();", submit)
            time.sleep(3)
            sub=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#playlist_13161 > a")))
            driver.execute_script("arguments[0].click();", sub)
            time.sleep(3)
            final=[]
            continue
        else:
            time.sleep(20)
            continue
        if win==0:
            l=0
            timer1=WebDriverWait(driver, 800).until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[2]/app-market-panel[1]/div/app-market-header/div/div[1]/app-countdown/span"),"01:00"))
            print(timer1)
            coun()
            print(coun.ti)
            if com(coun.ti,c) == 0:
                c=[]
                win=+1
                l=0
            else:
                timer1=WebDriverWait(driver, 800).until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-list/div/div/div[2]/app-market-panel[1]/div/app-market-header/div/div[1]/app-countdown/span"),"00:30"))
                print(timer1)
                cow()
                if cow.li!=[]:
                    for row in cow.li:
                        row9=str(row)
                        if row9!="":
                            row1=row9.strip("('',)")
                            mt1=wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='main-content']/app-event-list/div/div/div[2]/app-market-panel[1]/div/app-market/div/app-match-result/div[2]/app-match-cell/div/a[1]/span[2]")))
                            mt2=wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='main-content']/app-event-list/div/div/div[2]/app-market-panel[1]/div/app-market/div/app-match-result/div[3]/app-match-cell/div/a[1]/span[2]")))
                            mt3=wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='main-content']/app-event-list/div/div/div[2]/app-market-panel[1]/div/app-market/div/app-match-result/div[4]/app-match-cell/div/a[1]/span[2]")))
                            mt4=wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='main-content']/app-event-list/div/div/div[2]/app-market-panel[1]/div/app-market/div/app-match-result/div[5]/app-match-cell/div/a[1]/span[2]")))
                            mt5=wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='main-content']/app-event-list/div/div/div[2]/app-market-panel[1]/div/app-market/div/app-match-result/div[6]/app-match-cell/div/a[1]/span[2]")))
                            mt6=wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='main-content']/app-event-list/div/div/div[2]/app-market-panel[1]/div/app-market/div/app-match-result/div[7]/app-match-cell/div/a[1]/span[2]")))
                            mt7=wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='main-content']/app-event-list/div/div/div[2]/app-market-panel[1]/div/app-market/div/app-match-result/div[8]/app-match-cell/div/a[1]/span[2]")))
                            mt8=wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='main-content']/app-event-list/div/div/div[2]/app-market-panel[1]/div/app-market/div/app-match-result/div[9]/app-match-cell/div/a[1]/span[2]")))
                            mt9=wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='main-content']/app-event-list/div/div/div[2]/app-market-panel[1]/div/app-market/div/app-match-result/div[10]/app-match-cell/div/a[1]/span[2]")))
                            mt10=wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='main-content']/app-event-list/div/div/div[2]/app-market-panel[1]/div/app-market/div/app-match-result/div[11]/app-match-cell/div/a[1]/span[2]")))
                            how=[mt1.text,mt2.text,mt3.text,mt4.text,mt5.text,mt6.text,mt7.text,mt8.text,mt9.text,mt10.text]
                            why=[mt1,mt2,mt3,mt4,mt5,mt6,mt7,mt8,mt9,mt10]
                            def find_indices(search_list, search_item):
                                for (index, item) in enumerate(search_list):
                                  if search_item in item:
                                      return index 
                            cl=find_indices(how,row1)
                            final.append(cl)
                        else:
                            continue
                    result = []
                    for i in final: 
                        if i not in result: 
                            result.append(i)
                    leno=[]
                    c=[]
                    for p in itertools.islice(result,0,2):
                        mt1=wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='main-content']/app-event-list/div/div/div[2]/app-market-panel[1]/div/app-market/div/app-match-result/div[2]/app-match-cell/div/a[1]/span[2]")))
                        mt2=wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='main-content']/app-event-list/div/div/div[2]/app-market-panel[1]/div/app-market/div/app-match-result/div[3]/app-match-cell/div/a[1]/span[2]")))
                        mt3=wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='main-content']/app-event-list/div/div/div[2]/app-market-panel[1]/div/app-market/div/app-match-result/div[4]/app-match-cell/div/a[1]/span[2]")))
                        mt4=wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='main-content']/app-event-list/div/div/div[2]/app-market-panel[1]/div/app-market/div/app-match-result/div[5]/app-match-cell/div/a[1]/span[2]")))
                        mt5=wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='main-content']/app-event-list/div/div/div[2]/app-market-panel[1]/div/app-market/div/app-match-result/div[6]/app-match-cell/div/a[1]/span[2]")))
                        mt6=wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='main-content']/app-event-list/div/div/div[2]/app-market-panel[1]/div/app-market/div/app-match-result/div[7]/app-match-cell/div/a[1]/span[2]")))
                        mt7=wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='main-content']/app-event-list/div/div/div[2]/app-market-panel[1]/div/app-market/div/app-match-result/div[8]/app-match-cell/div/a[1]/span[2]")))
                        mt8=wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='main-content']/app-event-list/div/div/div[2]/app-market-panel[1]/div/app-market/div/app-match-result/div[9]/app-match-cell/div/a[1]/span[2]")))
                        mt9=wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='main-content']/app-event-list/div/div/div[2]/app-market-panel[1]/div/app-market/div/app-match-result/div[10]/app-match-cell/div/a[1]/span[2]")))
                        mt10=wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='main-content']/app-event-list/div/div/div[2]/app-market-panel[1]/div/app-market/div/app-match-result/div[11]/app-match-cell/div/a[1]/span[2]")))
                        how=[mt1.text,mt2.text,mt3.text,mt4.text,mt5.text,mt6.text,mt7.text,mt8.text,mt9.text,mt10.text]
                        why=[mt1,mt2,mt3,mt4,mt5,mt6,mt7,mt8,mt9,mt10]
                        mn=how[p]
                        dl=why[p]
                        c.append(mn)
                        driver.execute_script("arguments[0].click();", dl)
                        time.sleep(1)
                        #OVER2.5
                        matchunder1=wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/app-root/div[1]/app-scheduled/div/main/app-event-detail/div/div/div[2]/app-event-detail-content/div[3]/app-market/div/app-over-under-football/div/div[2]/div/app-odd[1]/div/div/div[2]")))
                        driver.execute_script("arguments[0].click();", matchunder1)
                        time.sleep(1)          
                        sub=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#playlist_13161 > a")))
                        driver.execute_script("arguments[0].click();", sub)
                        leno.append(p)
                    print(leno)
                    le=len(leno)
                    lei=str(le)
                    if l==0:    
                        stake_amount1=wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='bets-stake-amount-"+lei+"']")))
                        driver.execute_script("arguments[0].click();", stake_amount1)
                        stake_amount1.send_keys("45")
                        time.sleep(1)
                        submit=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='main-right']/app-bet-sidebar/div[1]/div[1]/app-betslip/div/div/button")))
                        driver.execute_script("arguments[0].click();", submit)
                        time.sleep(3)
                        sub=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#playlist_13161 > a")))
                        driver.execute_script("arguments[0].click();", sub)
                        time.sleep(3)
                        final=[]
                        l=+1
                        continue
                    else:
                        stake_amount1=wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='bets-stake-amount-"+lei+"']")))
                        driver.execute_script("arguments[0].click();", stake_amount1)
                        stake_amount1.send_keys("135")
                        time.sleep(1)
                        submit=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='main-right']/app-bet-sidebar/div[1]/div[1]/app-betslip/div/div/button")))
                        driver.execute_script("arguments[0].click();", submit)
                        time.sleep(3)
                        sub=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#playlist_13161 > a")))
                        driver.execute_script("arguments[0].click();", sub)
                        time.sleep(3)
                        final=[]
                        l=+1
                        win=+1
                        continue        
        
    except (ElementClickInterceptedException,ElementNotInteractableException,ElementNotSelectableException,ElementNotVisibleException,InvalidElementStateException,InvalidSelectorException,NoSuchAttributeException,StaleElementReferenceException,TimeoutException) as e:
        continue

