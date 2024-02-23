import os

target = input("Domain target: ")
os.system(f"bash Dcm -t {target} -e doc,docx,docm,dot,dotx,dotm,ppt,pptx,pps,ppsx,ppsm,pptm,potm,pot,csv,pdf,xls,xlsx,xslsm,xlt,xltx,xltm,sql,txt,7z,zip,rar,tar,tar.gz,tar.xz")
