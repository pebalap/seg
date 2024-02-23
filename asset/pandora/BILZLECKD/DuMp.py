from subprocess import getoutput
from colorama import Fore, Style, init
import urllib.request
import time
import sys
import os
from os.path import exists
from googlesearch import search
import random
import argparse
import textwrap

global domain

def options():
    opt_parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, epilog=textwrap.dedent(
        '''Example: python3 Dump.py -t example.com -d
Example: python3 Dump.py -t example.com 
'''))
    requiredNamed = opt_parser.add_argument_group('required arguments')
    requiredNamed.add_argument(
        '-t', '--target', help='Specifies the website to search for.', required=True)
    opt_parser.add_argument(
        '-d', '--download', help='Downloads files for inspection and metadata enumeration.', action='store_true')
    opt_parser.add_argument(
        '-n', '--number', help='Number of results per page. Default is 10. Increased numbers risk timeouts.')        
    global args
    args = opt_parser.parse_args()
    if len(sys.argv) == 1:
        opt_parser.print_help()
        opt_parser.exit()

global success, info, fail
success, info, fail = Fore.GREEN + Style.BRIGHT, Fore.YELLOW + \
    Style.BRIGHT, Fore.RED + Style.BRIGHT
global file_types
file_types = ['doc', 'docx', 'docm', 'dot', 'dotx', 'dotm','ppt', 'pptx', 'pps', 'ppsx', 'ppsm', 'pptm', 'potm', 'pot','csv', 'pdf', 'xls', 'xlsx', 'xslsm', 'xlt', 'xltx', 'xltm', 'sql', 'txt' , '7z' , 'zip' , 'rar' , 'tar' , 'tar.gz' , 'tar.xz' ]
global user_agents
user_agents = ['user_agents.txt']

print ("""\033[92m
███   ▄█ █    ▄▄▄▄▄▄   █     ▄███▄   ██   ▄█▄    █  █▀ ▄███▄   ██▄   
█  █  ██ █   ▀   ▄▄▀   █     █▀   ▀  █ █  █▀ ▀▄  █▄█   █▀   ▀  █  █  
█ ▀ ▄ ██ █    ▄▀▀   ▄▀ █     ██▄▄    █▄▄█ █   ▀  █▀▄   ██▄▄    █   █ 
█  ▄▀ ▐█ ███▄ ▀▀▀▀▀▀   ███▄  █▄   ▄▀ █  █ █▄  ▄▀ █  █  █▄   ▄▀ █  █  
███    ▐     ▀             ▀ ▀███▀      █ ▀███▀    █   ▀███▀   ███▀  
                                       █          ▀                  
                                      ▀                              by BILZEXPLOIT 
 """)
def banner():
    styles = [Fore.LIGHTBLACK_EX, Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX,
              Fore.LIGHTGREEN_EX, Fore.LIGHTMAGENTA_EX, Fore.LIGHTWHITE_EX]
    random_index = random.randint(0, len(styles)-1)
    print(styles[random_index] + "")
    print('█     ▄███▄   ██   █  █▀ ▄███▄   ██▄       ')
    print('█     █▀   ▀  █ █  █▄█   █▀   ▀  █  █      ')
    print('█     ██▄▄    █▄▄█ █▀▄   ██▄▄    █   █     ')
    print('███▄  █▄   ▄▀ █  █ █  █  █▄   ▄▀ █  █      ')
    print('▀     ▀███▀      █   █   ▀███▀   ███▀      ')
    print('                 █   ▀                      ')
    print('                 ▀                           ')
    print('       Leaked Data From Site (website)                        ')
    print('                            Version 7.1 Pro Stables                              ')
    print('                       A project by Cr0DiX1337_                          ')
    print('SpecialL Thanks To:  by BILZEXPLOIT ')
    print('                  python3 Dump.py -h to start                    ' + Style.RESET_ALL)
    print("-" * 73)


def dump():
    request = 0
    path = domain
    isdir = os.path.isdir(path)
    if isdir is True:
        pass
    else:
        os.mkdir(domain)
    os.chdir(domain)
    for files in file_types:
        try:
            file_exists = exists('.google-cookie')
            if file_exists == True:
                os.remove('.google-cookie')    
            print(info + f'[Please Waitt.. Injected DataBase] Dumpper Database From Site for {files} extensions.')
            rand_user_agent = random.choice(user_agents)
            if args.number:
                num = int(args.number)
            if args.number is None:
                num = 10
            for results in search(f'site:{domain} filetype:{files}', tld='com', lang='en', num=int(f'{num}'), start=0, stop=None, pause=5):
                print(success + f'[{files} extension found] - {results}')
                opener=urllib.request.build_opener()
                opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
                urllib.request.install_opener(opener)                
                url_path = results
                head, tail = os.path.split(url_path)
                urllib.request.urlretrieve(url_path, f'{tail}')
                request = request + 1
                if request == 100:
                    break            
                filename = tail
                ext = os.path.splitext(filename)[1]
                if args.download:
                    if sys.platform.startswith('win32'):                
                        with exiftool.ExifTool(exif) as et:
                            metadata = et.get_metadata(filename)    
                            # print(metadata)
                            file_name = et.get_tag('File:FileName', filename)    
                            print(f"\nMetadata results for {filename}")
                            print('-' * 50)
                            file_size = et.get_tag('File:FileSize', filename)
                            file_size = file_size / 1000
                            if file_size < 1000:
                                file_size = str(round(file_size, 2))
                                print(f"File Size: {file_size}kb")  
                            elif file_size >= 1000:
                                file_size = file_size / 1000
                                file_size = str(round(file_size, 2))    
                                print(f'File Size: {file_size}mb')  
                            if ext == '.pdf':
                                file_title = et.get_tag('PDF:Title', filename)
                                print('File Title: ' + str(file_title))
                                create_date = et.get_tag('XMP:CreateDate', filename)
                                print('File Creation Date: ' + str(create_date))
                                author = et.get_tag('PDF:Author', filename)
                                print('Author: ' + str(author))
                                creator_software = et.get_tag('XMP:CreatorTool', filename)
                                print('Software: ' + str(creator_software))
                                extension_format = et.get_tag('XMP:Format', filename)
                                print('Extension Format: ' + str(extension_format))
                                pass
                            if ext == '.doc':
                                file_title = et.get_tag('FlashPix:Title', filename)
                                print('File Title: ' + file_title)
                                create_date = et.get_tag('FlashPix:CreateDate', filename)
                                print('File Creation Date: ' + str(create_date))
                                author = et.get_tag('FlashPix:Author', filename)
                                print('Author: ' + author)
                                creator_software = et.get_tag('FlashPix:Software', filename)
                                print('Software: ' + creator_software)
                                extension_format = et.get_tag('FlashPix:CompObjUserType', filename)
                                print('Extension Format: ' + str(extension_format))
                            if ext == '.docx':
                                file_title = et.get_tag('XMP:Title', filename)
                                print('File Title: ' + str(file_title))
                                create_date = et.get_tag('XML:CreateDate', filename)
                                print('File Creation Date: ' + str(create_date))
                                author = et.get_tag('XMP:Creator', filename)
                                print('Author: ' + author)
                                creator_software = et.get_tag('XML:Application', filename)
                                print('Software: ' + creator_software)
                                extension_format = et.get_tag('File:FileTypeExtension', filename)
                                print('Extension Format: ' + str(extension_format))        
                            if ext == '.docm':
                                file_title = et.get_tag('XMP:Title', filename)
                                print('File Title: ' + str(file_title))
                                create_date = et.get_tag('XML:CreateDate', filename)
                                print('File Creation Date: ' + str(create_date))
                                author = et.get_tag('XMP:Creator', filename)
                                print('Author: ' + author)
                                creator_software = et.get_tag('XML:Application', filename)
                                print('Software: ' + creator_software)
                                extension_format = et.get_tag('File:FileTypeExtension', filename)
                                print('Extension Format: ' + str(extension_format))   
                            if ext == '.dot':
                                file_title = et.get_tag('XMP:Title', filename)
                                print('File Title: ' + str(file_title))
                                create_date = et.get_tag('XML:CreateDate', filename)
                                print('File Creation Date: ' + str(create_date))
                                author = et.get_tag('XMP:Creator', filename)
                                print('Author: ' + author)
                                creator_software = et.get_tag('XML:Application', filename)
                                print('Software: ' + creator_software)
                                extension_format = et.get_tag('File:FileTypeExtension', filename)
                                print('Extension Format: ' + str(extension_format))    
                            if ext == '.dotx':
                                file_title = et.get_tag('XMP:Title', filename)
                                print('File Title: ' + str(file_title))
                                create_date = et.get_tag('XML:CreateDate', filename)
                                print('File Creation Date: ' + str(create_date))
                                author = et.get_tag('XMP:Creator', filename)
                                print('Author: ' + author)
                                creator_software = et.get_tag('XML:Application', filename)
                                print('Software: ' + creator_software)
                                extension_format = et.get_tag('File:FileTypeExtension', filename)
                                print('Extension Format: ' + str(extension_format))      
                            if ext == '.dotm':
                                file_title = et.get_tag('XMP:Title', filename)
                                print('File Title: ' + str(file_title))
                                create_date = et.get_tag('XML:CreateDate', filename)
                                print('File Creation Date: ' + str(create_date))
                                author = et.get_tag('XMP:Creator', filename)
                                print('Author: ' + author)
                                creator_software = et.get_tag('XML:Application', filename)
                                print('Software: ' + creator_software)
                                extension_format = et.get_tag('File:FileTypeExtension', filename)
                                print('Extension Format: ' + str(extension_format))             
                            if ext == '.ppt':
                                file_title = et.get_tag('FlashPix:Title', filename)
                                print('File Title: ' + file_title)
                                create_date = et.get_tag('FlashPix:CreateDate', filename)
                                print('File Creation Date: ' + str(create_date))
                                author = et.get_tag('FlashPix:Author', filename)
                                print('Author: ' + author)
                                creator_software = et.get_tag('FlashPix:Software', filename)
                                print('Software: ' + creator_software)
                                extension_format = et.get_tag('File:FileTypeExtension', filename)
                                print('Extension Format: ' + str(extension_format))
                            if ext == '.pptx':
                                file_title = et.get_tag('XMP:Title', filename)
                                print('File Title: ' + file_title)
                                create_date = et.get_tag('XML:CreateDate', filename)
                                print('File Creation Date: ' + str(create_date))
                                author = et.get_tag('XMP:Creator', filename)
                                print('Author: ' + author)
                                creator_software = et.get_tag('XML:Application', filename)
                                print('Software: ' + creator_software)
                                extension_format = et.get_tag('File:FileTypeExtension', filename)
                                print('Extension Format: ' + str(extension_format)) 
                            if ext == '.pps':
                                file_title = et.get_tag('XMP:Title', filename)
                                print('File Title: ' + file_title)
                                create_date = et.get_tag('XML:CreateDate', filename)
                                print('File Creation Date: ' + str(create_date))
                                author = et.get_tag('XMP:Creator', filename)
                                print('Author: ' + author)
                                creator_software = et.get_tag('XML:Application', filename)
                                print('Software: ' + creator_software)
                                extension_format = et.get_tag('File:FileTypeExtension', filename)
                                print('Extension Format: ' + str(extension_format)) 
                            if ext == '.ppsx':
                                file_title = et.get_tag('XMP:Title', filename)
                                print('File Title: ' + file_title)
                                create_date = et.get_tag('XML:CreateDate', filename)
                                print('File Creation Date: ' + str(create_date))
                                author = et.get_tag('XMP:Creator', filename)
                                print('Author: ' + author)
                                creator_software = et.get_tag('XML:Application', filename)
                                print('Software: ' + creator_software)
                                extension_format = et.get_tag('File:FileTypeExtension', filename)
                                print('Extension Format: ' + str(extension_format)) 
                            if ext == '.ppsm':
                                file_title = et.get_tag('XMP:Title', filename)
                                print('File Title: ' + file_title)
                                create_date = et.get_tag('XML:CreateDate', filename)
                                print('File Creation Date: ' + str(create_date))
                                author = et.get_tag('XMP:Creator', filename)
                                print('Author: ' + author)
                                creator_software = et.get_tag('XML:Application', filename)
                                print('Software: ' + creator_software)
                                extension_format = et.get_tag('File:FileTypeExtension', filename)
                                print('Extension Format: ' + str(extension_format)) 
                            if ext == '.pptx':
                                file_title = et.get_tag('XMP:Title', filename)
                                print('File Title: ' + file_title)
                                create_date = et.get_tag('XML:CreateDate', filename)
                                print('File Creation Date: ' + str(create_date))
                                author = et.get_tag('XMP:Creator', filename)
                                print('Author: ' + author)
                                creator_software = et.get_tag('XML:Application', filename)
                                print('Software: ' + creator_software)
                                extension_format = et.get_tag('File:FileTypeExtension', filename)
                                print('Extension Format: ' + str(extension_format))  
                            if ext == '.potm':
                                file_title = et.get_tag('XMP:Title', filename)
                                print('File Title: ' + file_title)
                                create_date = et.get_tag('XML:CreateDate', filename)
                                print('File Creation Date: ' + str(create_date))
                                author = et.get_tag('XMP:Creator', filename)
                                print('Author: ' + author)
                                creator_software = et.get_tag('XML:Application', filename)
                                print('Software: ' + creator_software)
                                extension_format = et.get_tag('File:FileTypeExtension', filename)
                                print('Extension Format: ' + str(extension_format)) 
                            if ext == '.pot':
                                file_title = et.get_tag('XMP:Title', filename)
                                print('File Title: ' + file_title)
                                create_date = et.get_tag('XML:CreateDate', filename)
                                print('File Creation Date: ' + str(create_date))
                                author = et.get_tag('XMP:Creator', filename)
                                print('Author: ' + author)
                                creator_software = et.get_tag('XML:Application', filename)
                                print('Software: ' + creator_software)
                                extension_format = et.get_tag('File:FileTypeExtension', filename)
                                print('Extension Format: ' + str(extension_format))  
                            if ext == '.xlsx':
                                tab_title = et.get_tag('XML:TitlesOfParts', filename)
                                print('Tab Titles: ' + str(tab_title))
                                create_date = et.get_tag('XML:CreateDate', filename)
                                print('File Creation Date: ' + str(create_date))
                                author = et.get_tag('XMP:Creator', filename)
                                print('Author: ' + author)
                                creator_software = et.get_tag('XML:Application', filename)
                                print('Software: ' + creator_software)
                                extension_format = et.get_tag('File:FileTypeExtension', filename)
                                print('Extension Format: ' + str(extension_format))     
                            if ext == '.xls':
                                file_title = et.get_tag('FlashPix:TitleOfParts', filename)
                                print('Tab Titles: ' + str(file_title))
                                create_date = et.get_tag('FlashPix:CreateDate', filename)
                                print('File Creation Date: ' + str(create_date))
                                author = et.get_tag('FlashPix:Author', filename)
                                print('Author: ' + author)
                                creator_software = et.get_tag('FlashPix:Software', filename)
                                print('Software: ' + creator_software)
                                extension_format = et.get_tag('File:FileTypeExtension', filename)
                                print('Extension Format: ' + str(extension_format))
                            if ext == '.xslsm':
                                file_title = et.get_tag('FlashPix:TitleOfParts', filename)
                                print('Tab Titles: ' + str(file_title))
                                create_date = et.get_tag('FlashPix:CreateDate', filename)
                                print('File Creation Date: ' + str(create_date))
                                author = et.get_tag('FlashPix:Author', filename)
                                print('Author: ' + author)
                                creator_software = et.get_tag('FlashPix:Software', filename)
                                print('Software: ' + creator_software)
                                extension_format = et.get_tag('File:FileTypeExtension', filename)
                                print('Extension Format: ' + str(extension_format))
                            if ext == '.xlt':
                                file_title = et.get_tag('FlashPix:TitleOfParts', filename)
                                print('Tab Titles: ' + str(file_title))
                                create_date = et.get_tag('FlashPix:CreateDate', filename)
                                print('File Creation Date: ' + str(create_date))
                                author = et.get_tag('FlashPix:Author', filename)
                                print('Author: ' + author)
                                creator_software = et.get_tag('FlashPix:Software', filename)
                                print('Software: ' + creator_software)
                                extension_format = et.get_tag('File:FileTypeExtension', filename)
                                print('Extension Format: ' + str(extension_format))
                            if ext == '.xltx':
                                file_title = et.get_tag('FlashPix:TitleOfParts', filename)
                                print('Tab Titles: ' + str(file_title))
                                create_date = et.get_tag('FlashPix:CreateDate', filename)
                                print('File Creation Date: ' + str(create_date))
                                author = et.get_tag('FlashPix:Author', filename)
                                print('Author: ' + author)
                                creator_software = et.get_tag('FlashPix:Software', filename)
                                print('Software: ' + creator_software)
                                extension_format = et.get_tag('File:FileTypeExtension', filename)
                                print('Extension Format: ' + str(extension_format))
                            if ext == '.xltm':
                                file_title = et.get_tag('FlashPix:TitleOfParts', filename)
                                print('Tab Titles: ' + str(file_title))
                                create_date = et.get_tag('FlashPix:CreateDate', filename)
                                print('File Creation Date: ' + str(create_date))
                                author = et.get_tag('FlashPix:Author', filename)
                                print('Author: ' + author)
                                creator_software = et.get_tag('FlashPix:Software', filename)
                                print('Software: ' + creator_software)
                                extension_format = et.get_tag('File:FileTypeExtension', filename)
                                print('Extension Format: ' + str(extension_format)) 
                            if ext == '.sql':
                                file_title = et.get_tag('FlashPix:TitleOfParts', filename)
                                print('Tab Titles: ' + str(file_title))
                                create_date = et.get_tag('FlashPix:CreateDate', filename)
                                print('File Creation Date: ' + str(create_date))
                                author = et.get_tag('FlashPix:Author', filename)
                                print('Author: ' + author)
                                creator_software = et.get_tag('FlashPix:Software', filename)
                                print('Software: ' + creator_software)
                                extension_format = et.get_tag('File:FileTypeExtension', filename)
                                print('Extension Format: ' + str(extension_format))
                            if ext == '.txt':
                                file_title = et.get_tag('FlashPix:TitleOfParts', filename)
                                print('Tab Titles: ' + str(file_title))
                                create_date = et.get_tag('FlashPix:CreateDate', filename)
                                print('File Creation Date: ' + str(create_date))
                                author = et.get_tag('FlashPix:Author', filename)
                                print('Author: ' + author)
                                creator_software = et.get_tag('FlashPix:Software', filename)
                                print('Software: ' + creator_software)
                                extension_format = et.get_tag('File:FileTypeExtension', filename)
                                print('Extension Format: ' + str(extension_format))
                            if ext == '7z':
                                file_title = et.get_tag('FlashPix:TitleOfParts', filename)
                                print('Tab Titles: ' + str(file_title))
                                create_date = et.get_tag('FlashPix:CreateDate', filename)
                                print('File Creation Date: ' + str(create_date))
                                author = et.get_tag('FlashPix:Author', filename)
                                print('Author: ' + author)
                                creator_software = et.get_tag('FlashPix:Software', filename)
                                print('Software: ' + creator_software)
                                extension_format = et.get_tag('File:FileTypeExtension', filename)
                                print('Extension Format: ' + str(extension_format))
                            if ext == 'zip':
                                file_title = et.get_tag('FlashPix:TitleOfParts', filename)
                                print('Tab Titles: ' + str(file_title))
                                create_date = et.get_tag('FlashPix:CreateDate', filename)
                                print('File Creation Date: ' + str(create_date))
                                author = et.get_tag('FlashPix:Author', filename)
                                print('Author: ' + author)
                                creator_software = et.get_tag('FlashPix:Software', filename)
                                print('Software: ' + creator_software)
                                extension_format = et.get_tag('File:FileTypeExtension', filename)
                                print('Extension Format: ' + str(extension_format))    
                            if ext == 'rar':
                                file_title = et.get_tag('FlashPix:TitleOfParts', filename)
                                print('Tab Titles: ' + str(file_title))
                                create_date = et.get_tag('FlashPix:CreateDate', filename)
                                print('File Creation Date: ' + str(create_date))
                                author = et.get_tag('FlashPix:Author', filename)
                                print('Author: ' + author)
                                creator_software = et.get_tag('FlashPix:Software', filename)
                                print('Software: ' + creator_software)
                                extension_format = et.get_tag('File:FileTypeExtension', filename)
                                print('Extension Format: ' + str(extension_format))
                            if ext == 'tar':
                                file_title = et.get_tag('FlashPix:TitleOfParts', filename)
                                print('Tab Titles: ' + str(file_title))
                                create_date = et.get_tag('FlashPix:CreateDate', filename)
                                print('File Creation Date: ' + str(create_date))
                                author = et.get_tag('FlashPix:Author', filename)
                                print('Author: ' + author)
                                creator_software = et.get_tag('FlashPix:Software', filename)
                                print('Software: ' + creator_software)
                                extension_format = et.get_tag('File:FileTypeExtension', filename)
                                print('Extension Format: ' + str(extension_format))
                            if ext == 'tar.gz':
                                file_title = et.get_tag('FlashPix:TitleOfParts', filename)
                                print('Tab Titles: ' + str(file_title))
                                create_date = et.get_tag('FlashPix:CreateDate', filename)
                                print('File Creation Date: ' + str(create_date))
                                author = et.get_tag('FlashPix:Author', filename)
                                print('Author: ' + author)
                                creator_software = et.get_tag('FlashPix:Software', filename)
                                print('Software: ' + creator_software)
                                extension_format = et.get_tag('File:FileTypeExtension', filename)
                                print('Extension Format: ' + str(extension_format))
                            if ext == 'tar.xz':
                                file_title = et.get_tag('FlashPix:TitleOfParts', filename)
                                print('Tab Titles: ' + str(file_title))
                                create_date = et.get_tag('FlashPix:CreateDate', filename)
                                print('File Creation Date: ' + str(create_date))
                                author = et.get_tag('FlashPix:Author', filename)
                                print('Author: ' + author)
                                creator_software = et.get_tag('FlashPix:Software', filename)
                                print('Software: ' + creator_software)
                                extension_format = et.get_tag('File:FileTypeExtension', filename)
                                print('Extension Format: ' + str(extension_format))
                    else:
                        print(f"\nMetadata results for {filename}")
                        print('-' * 50)
                        if ext == '.pdf':
                            cmd = f'exiftool {filename} -s -FileSize -*Title* -*CreateDate* -Author -CreatorTool -Format'
                            response = getoutput(cmd)
                            print(response + '\n')                        
                        if ext == '.doc':
                            cmd = f'exiftool {filename} -s -FileSize -Title -CreateDate -Author -Software -*CompObjUserType*'
                            response = getoutput(cmd)
                            print(response + '\n')                        
                        if ext == '.docx':
                            cmd = f'exiftool {filename} -s -FileSize -Title -CreateDate -Creator -Application -*FileTypeExtension*'
                            response = getoutput(cmd)
                            print(response + '\n')
                        if ext == '.docm':
                            cmd = f'exiftool {filename} -s -FileSize -Title -CreateDate -Creator -Application -*FileTypeExtension*'
                            response = getoutput(cmd)
                            print(response + '\n') 
                        if ext == '.dot':
                            cmd = f'exiftool {filename} -s -FileSize -Title -CreateDate -Creator -Application -*FileTypeExtension*'
                            response = getoutput(cmd)
                            print(response + '\n')
                        if ext == '.dotx':
                            cmd = f'exiftool {filename} -s -FileSize -Title -CreateDate -Creator -Application -*FileTypeExtension*'
                            response = getoutput(cmd)
                            print(response + '\n')
                        if ext == '.dotm':
                            cmd = f'exiftool {filename} -s -FileSize -Title -CreateDate -Creator -Application -*FileTypeExtension*'
                            response = getoutput(cmd)
                            print(response + '\n')
                        if ext == '.ppt':
                            cmd = f'exiftool {filename} -s -FileSize -Title -CreateDate -Author -Software -*FileTypeExtension*'
                            response = getoutput(cmd)
                            print(response + '\n')                        
                        if ext == '.pptx':
                            cmd = f'exiftool {filename} -s -FileSize -Title -CreateDate -Creator -Application -*FileTypeExtension*'
                            response = getoutput(cmd)
                            print(response + '\n')
                        if ext == '.pps':
                            cmd = f'exiftool {filename} -s -FileSize -Title -CreateDate -Creator -Application -*FileTypeExtension*'
                            response = getoutput(cmd)
                            print(response + '\n')
                        if ext == '.ppsx':
                            cmd = f'exiftool {filename} -s -FileSize -Title -CreateDate -Creator -Application -*FileTypeExtension*'
                            response = getoutput(cmd)
                            print(response + '\n')
                        if ext == '.ppsm':
                            cmd = f'exiftool {filename} -s -FileSize -Title -CreateDate -Creator -Application -*FileTypeExtension*'
                            response = getoutput(cmd)
                            print(response + '\n')
                        if ext == '.pptm':
                            cmd = f'exiftool {filename} -s -FileSize -Title -CreateDate -Creator -Application -*FileTypeExtension*'
                            response = getoutput(cmd)
                            print(response + '\n')
                        if ext == '.potm':
                            cmd = f'exiftool {filename} -s -FileSize -Title -CreateDate -Creator -Application -*FileTypeExtension*'
                            response = getoutput(cmd)
                            print(response + '\n')
                        if ext == '.pot':
                            cmd = f'exiftool {filename} -s -FileSize -Title -CreateDate -Creator -Application -*FileTypeExtension*'
                            response = getoutput(cmd)
                            print(response + '\n')
                        if ext == '.xls':
                            cmd = f'exiftool {filename} -s -FileSize -*Parts* -CreateDate -Author -Software -*FileTypeExtension*'
                            response = getoutput(cmd)
                            print(response + '\n')
                        if ext == '.xlsx':
                            cmd = f'exiftool {filename} -s -FileSize -*Parts* -CreateDate -Creator -Application -*FileTypeExtension*'
                            response = getoutput(cmd)
                            print(response + '\n')
                        if ext == '.xslsm':
                            cmd = f'exiftool {filename} -s -FileSize -*Parts* -CreateDate -Creator -Application -*FileTypeExtension*'
                            response = getoutput(cmd)
                            print(response + '\n')
                        if ext == '.xlt':
                            cmd = f'exiftool {filename} -s -FileSize -*Parts* -CreateDate -Creator -Application -*FileTypeExtension*'
                            response = getoutput(cmd)
                            print(response + '\n') 
                        if ext == '.xltx':
                            cmd = f'exiftool {filename} -s -FileSize -*Parts* -CreateDate -Creator -Application -*FileTypeExtension*'
                            response = getoutput(cmd)
                            print(response + '\n') 
                        if ext == '.xltm':
                            cmd = f'exiftool {filename} -s -FileSize -*Parts* -CreateDate -Creator -Application -*FileTypeExtension*'
                            response = getoutput(cmd)
                            print(response + '\n')
                        if ext == '.sql':
                            cmd = f'exiftool {filename} -s -FileSize -*Parts* -CreateDate -Creator -Application -*FileTypeExtension*'
                            response = getoutput(cmd)
                            print(response + '\n')
                        if ext == '.txt':
                            cmd = f'exiftool {filename} -s -FileSize -*Parts* -CreateDate -Creator -Application -*FileTypeExtension*'
                            response = getoutput(cmd)
                            print(response + '\n')
                        if ext == '.7z':
                            cmd = f'exiftool {filename} -s -FileSize -*Parts* -CreateDate -Creator -Application -*FileTypeExtension*'
                            response = getoutput(cmd)
                            print(response + '\n')
                        if ext == '.zip':
                            cmd = f'exiftool {filename} -s -FileSize -*Parts* -CreateDate -Creator -Application -*FileTypeExtension*'
                            response = getoutput(cmd)
                            print(response + '\n')
                        if ext == '.rar':
                            cmd = f'exiftool {filename} -s -FileSize -*Parts* -CreateDate -Creator -Application -*FileTypeExtension*'
                            response = getoutput(cmd)
                            print(response + '\n')
                        if ext == '.tar':
                            cmd = f'exiftool {filename} -s -FileSize -*Parts* -CreateDate -Creator -Application -*FileTypeExtension*'
                            response = getoutput(cmd)
                            print(response + '\n')
                        if ext == '.tar.gz':
                            cmd = f'exiftool {filename} -s -FileSize -*Parts* -CreateDate -Creator -Application -*FileTypeExtension*'
                            response = getoutput(cmd)
                            print(response + '\n')
                        if ext == '.tar.xz':
                            cmd = f'exiftool {filename} -s -FileSize -*Parts* -CreateDate -Creator -Application -*FileTypeExtension*'
                            response = getoutput(cmd)
                            print(response + '\n')
                time.sleep(1)
        except urllib.error.HTTPError as e:
            if e.code == 404:
                print(
                    fail + f'[Error Code 404] Web server is responding with 404 error. Skipping.')
                continue
            if e.code == 403:
                print(fail + f'[error Code 403] Web server is responding with 403 error. Skipping.')
            if e.code == 429:
                print(
                    fail + f'\n[Error Code 429] Google is timing out queries. Wait a while and try again.\n')
                quit()
        except OSError:
            continue
            #else:
             #   print(
              #      fail + f'\n[warn] Error code {e.code} identified. Please create a new issue on the Github repo so it can be added.\n')
               # continue
        except urllib.error.URLError:
            print(fail + f'[Error] File could not be downloaded. Skipping.')
            continue
        except ModuleNotFoundError:
            print(fail + f'[Error] Run sudo pip3 -r requirements.txt to install necessary imports.')
        except UnicodeDecodeError:
            continue

if __name__ == "__main__":
    try:
        init()
        banner()
        options()
        if sys.platform.startswith('win32'):
            cur_path = os.path.abspath(os.getcwd())     
            exif = f'{cur_path}\\tools\\exiftool.exe'           
        domain = args.target
        dump()
        print(info + f'\n[info] Dumpper Data for {domain} completed 100%.\n')

    except KeyboardInterrupt:
        print("\nYou either fat fingered this, or meant to do it. Either way, goodbye!\n")
        quit()
    except IndexError:
        print(fail + '\nSyntax - python3 dump.py -t <domain>\n')
