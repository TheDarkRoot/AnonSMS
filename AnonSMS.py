#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from os import system as s



banner = """
    #    ####################  #####  #     #  #####  
   # #   #    #  ####  #    # #     # ##   ## #     # 
  #   #  ##   # #    # ##   # #       # # # # #       
 #     # # #  # #    # # #  #  #####  #  #  #  #####  
 ####### #  # # #    # #  # #       # #     #       # 
 #     # #   ## #    # #   ## #     # #     # #     # 
 #     # #    #  ####  #    #  #####  #     #  #####  
"""

print(banner)

Number = input(" Phone Number: ")

Message = input("\n Message: ")

arlk = Message[0:70]

drlm = input("\n >>> Send a message? [Y/N]: ")

if drlm == "y" or drlm == "Y":
    print("\n"+Number+"\n"+arlk+"\n")
    resp = requests.post('https://textbelt.com/text', {
  'phone': Number,
  'message': arlk,
  'key': 'textbelt',
    })
    print(resp.json())

elif drlm == "n" or drlm == "N":
    quit()
else:
    print("\n Incorrect operation.")

