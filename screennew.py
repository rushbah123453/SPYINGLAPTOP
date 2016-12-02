#!/usr/bin/env python -W ignore::DeprecationWarning
#!/usr/bin/env python3
import os
import sys
import datetime
from PIL import Image
from PIL import ImageGrab
import getpass
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from PIL import ImageQt
#from PyQt4 import QtGui, QtCore
#from PyQt4.QtGui import QImage
def screen_shot():
  
  SaveDirectory=r'C:\dell' #location to save image(screenshot)            #4
  ImageEditorPath=r'C:\WINDOWS\system32\mspaint.exe' #location of paint   #5

  img=ImageGrab.grab()  #taking screenshot
  time.sleep(3)
  saveas=os.path.join(SaveDirectory,'ScreenShot_'+'{0:%Y_%m_%d_%H_%M_%S}'.format(datetime.datetime.now())+'.jpg')
  img.save(saveas)
  
  eemail(saveas)            
def eemail(ImgFileName): 
  img_data = open(ImgFileName, 'rb').read()
  time.sleep(2)
  fromaddr = "xyz@gmail.com" #your mail address                           #1
  toaddr = "abc@gmail.com"#whom to send?                                  #2
  p_w_d ="your password"#password                                         #3
  #print(pwd)
  msg = MIMEMultipart()
  msg['From'] = "LOGGED IN"
  msg['To'] = toaddr
  #msg['Subject'] = "someone has logged into your laptop during "+ time.ctime() 
  body = "YOUR LAPTOP WAS LOGGED IN DURING "+time.ctime()
  msg.attach(MIMEText(body, 'plain'))
  image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
  msg.attach(image)
  #server.ehlo()
  server = smtplib.SMTP('smtp.gmail.com', 587)
  #server = smtplib.SMTP_SSL('smtp.googlemail.com', 465)
  print ("[+] Connecting To Mail Server.\n")
  server.starttls()
  print ("[+] Logging Into Mail Server.\n")
  server.login(fromaddr, p_w_d)
  text = msg.as_string()
 
  print ("[+] Sending Mail")
  #for i in range(10000):
  # msg['Subject'] = "someone has logged into your laptop during "+ time.ctime()   
  server.sendmail(fromaddr, toaddr, text)
  print ("[+] Mail Sent Successfully.\n")
  server.quit()

if __name__ == "__main__":
 screen_shot()

