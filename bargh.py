"""
Hossein Jalili
feb-13-2022
version 1.0.0
Issuance of Electricity bill of Iran

"""
from selenium import webdriver
import os
import time
from selenium.webdriver.common.keys import Keys
import jdatetime
import subprocess
import platform
import getpass
import socket

#----------------------------------------------
clear=lambda : os.system("cls")
now = jdatetime.datetime.now()
#-------------------
def ghabz():
    i=1
    lines=[]
    while True:
        print("---------------- try",str(i)," -----------------")
        billing__id=input('\nBilling ID: for example: 1234567891234\n')
        print('\nyour Billing ID is: '+billing__id,"\n")
        if billing__id.isdigit()==False:
            clear()
            print('\nplease enter a valid number(0-9)\n')
            i += 1
            
        else:
            if len(billing__id)==13:
                break
            else:
                i += 1
                clear()
                print('\nplease enter a valid 13_number (1234567891234)\n')
                
    #----------------------------------------------

    path = os.path.dirname(os.path.abspath(__file__))
    address=os.path.join(path, 'chromedriver.exe')
    driver = webdriver.Chrome(executable_path=address)
    driver.get('https://bargheman.com/power?billId='+billing__id)


    #----------------------------------------------
    time.sleep(5)

    try:
        company_name=(driver.find_element_by_xpath('//*[@id="billInfo"]/div/div/div[1]/div/div[2]').text)
    except:
        company_name="can't connect to server"
    try:    
        Meter_body_number=(driver.find_element_by_xpath('//*[@id="billInfo"]/div/div/div[5]/div/div[2]').text)
    except:
        Meter_body_number="can't connect to server"
    try:
        consumer_name=(driver.find_element_by_xpath('//*[@id="billInfo"]/div/div/div[3]/div/div[2]').text)
    except:
        consumer_name="can't connect to server"
    try:
        payment_dead_line=(driver.find_element_by_xpath('//*[@id="billInfo"]/div/div/div[8]/div/div[2]').text)
    except:
        payment_dead_line="can't connect to server"
    try:
        phase=(driver.find_element_by_xpath('//*[@id="billInfo"]/div/div/div[7]/div/div[2]').text)
    except:
        phase="can't connect to server"
    try:
        ampere=(driver.find_element_by_xpath('//*[@id="billInfo"]/div/div/div[9]/div/div[2]').text)
    except:
        ampere="can't connect to server"
    try:
        contractual_power=(driver.find_element_by_xpath('//*[@id="billInfo"]/div/div/div[11]/div/div[2]').text)
    except:
        contractual_power="can't connect to server"
    try:
        tariff=(driver.find_element_by_xpath('//*[@id="billInfo"]/div/div/div[13]/div/div[2]').text)
    except:
        tariff="can't connect to server"
    try:
        city_name=(driver.find_element_by_xpath('//*[@id="billInfo"]/div/div/div[10]/div/div[2]').text)
    except:
        city_name="can't connect to server"
    try:
        Payment_code=(driver.find_element_by_xpath('//*[@id="billInfo"]/div/div/div[4]/div/div[2]').text)
    except:
        Payment_code="can't connect to server"
    try:
        Average_monthly_consumption=(driver.find_element_by_xpath('//*[@id="billInfo"]/div/div/div[15]/div/div[2]').text)
    except:
        Average_monthly_consumption="can't connect to server"
    try:
        Course_consumption=(driver.find_element_by_xpath('//*[@id="billInfo"]/div/div/div[16]/div/div[2]').text)
    except:
        Course_consumption="can't connect to server"
    try:
        Amount=(driver.find_element_by_xpath('//*[@id="billInfo"]/div/div/div[6]/div/div[2]').text)
    except:
        Amount="can't connect to server"
    time.sleep(2)
    clear()

    print("---------------- try",str(i)," -----------------")
    print("Today is: \t",now)
    print('your billing id : \t'+billing__id,"\n")
    print("Payment code :\t\t",Payment_code)
    print("payment dead-line :\t",payment_dead_line)
    print("Meter body number :\t",Meter_body_number)
    print("company name :\t\t",company_name)
    print("consumer name :\t\t",consumer_name)
    print("phase :\t\t\t",phase)
    print("ampere :\t\t",ampere)
    print("contractual power :\t",contractual_power)
    print("tariff :\t\t",tariff)
    print("city name :\t\t",city_name)

    Average_monthly_consumption_=''.join([n for n in Average_monthly_consumption if n.isdigit()])
    print("Average monthly consumption :\t",Average_monthly_consumption_,"kw/h")

    Course_consumption_=''.join([n for n in Course_consumption if n.isdigit()])
    print("Course consumption :\t\t",Course_consumption_,"kw/h")
    

    rrr=''.join([n for n in Amount if n.isdigit()])
    print("\nThe amount payable to the bank : ",rrr,"Rial")

    if t.startswith('Y') or t.startswith('y'):
        try:
            lines=lines+[
            " Issuance of Electricity bill",
            "\nToday is:                     ",str(now),
            "\nyour billing id :             ",str(billing__id),
            "\nPayment code :                ",str(Payment_code),
            "\npayment dead-line :           ",str(payment_dead_line),
            "\nMeter body number :           ",str(Meter_body_number),
            "\ncompany name :                ",str("company_name"),
            "\nconsumer name :               ",str("consumer_name"),
            "\nphase :                       ",str(phase),
            "\nampere :                      ",str(ampere),
            "\ncontractual power :           ",str(contractual_power),
            "\ntariff :                      ",str("tariff"),
            "\ncity name :                   ",str("city_name"),
            "\nAverage monthly consumption : ",str(Average_monthly_consumption_),
            "\nCourse consumption :          ",str(Course_consumption_),
            "\nThe amount payable to the bank------> : ",str(rrr)]
            # print(lines)
            t_time="-"+str(now.year)+"-"+str(now.month)+"-"+str(now.day)+"-"+str(now.hour)+"-"+str(now.second)              
            
            with open(str(billing__id)+t_time+'.txt', 'w') as f:
                for line in lines:
                    f.write(line)
                    f.write('\n')
        except:
            print("\ncan't save file")


    print("\n10 sec utill quit ")
    time.sleep(10)
    driver.quit()
    # print("\nquit is done\n")
    print("----------------------------------------------")

clear()
while True:
    clear()
    print("\nDeveloped by #ho3j ")
    print("____________________________________")
    try:
        
        host_name = socket.gethostname()
        ip_addr = socket.gethostbyname(host_name)
        print("os : \t\t\t",platform.system())
        print("Windows version : \t",platform.release())
        # print("Windows 32/64bit : \t",platform.machine())
        # print("Windows User : \t\t",getpass.getuser())
        print ("Host Name: \t\t {0}".format(host_name))
        print ("IP Address: \t\t {0}".format(ip_addr))
    except:
        print("can not print Information of windows ")

    try:
        print("____________________________________\n")
        print("                Hi, Good Luck ",getpass.getuser())
        # print("----------")
        print("""
            Issuance of Electricity bill 
        |*************************************|
        |   1 :  Show only in the app         |
        |   2 :  View and with save txt file  |
        |   3 :  quit app                     |
        ***************************************
        """)
        i=int(input("Enter number of function :\t"))
        if i ==1:
            t="n"
            ghabz()
        elif i==2:
            t="y"
            ghabz()
        elif i==3:
            break
        else :
            clear()
            print("wrong  number !!! " ,end="\n \n")
            print( end=" ")
            qq = input("Enter 'Q' to quit app \n or 'Enter' to continue : \t ").lower()
            if qq =="q" :
                break
            else :
                clear()
                continue
    except:
        clear()
        print("Enter number !")

#----------------------------------------------