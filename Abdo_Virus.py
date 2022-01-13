#!/bin/python3
#This Tool is Simple Soon will be Is Big Tool Created By Abdo_Virus
#This Tool give simple report About target 
# You must download pakge before start
#pip3 install bs4
#pip3 install requests
#########import packge#####
from socket import gethostbyname as ip
from requests import get
from bs4 import BeautifulSoup as x
import json 
import time
########startcolor###########
red="\033[1;31m"
green="\033[1;32m"
blue="\033[1;34m"
yellow="\033[1;33m"
black="\033[1;30m"
purple="\033[1;35m"
even="\033[1;36m"
white="\033[1;37m"
#########copy wirte########
print(f'''
{red}          ___           ___           _                                                    
         (   )         (   )                       .-.                                     
  .---.   | |.-.     .-.| |    .--.     ___  ___  ( __)  ___ .-.     ___  ___      .--.    
 / .-, \  | /   \   /   \ |   /    \   (   )(   ) (''") (   )   \   (   )(   )   /  _  \   
(__) ; |  |  .-. | |  .-. |  |  .-. ;   | |  | |   | |   | ' .-. ;   | |  | |   . .' `. ;  
  .'`  |  | |  | | | |  | |  | |  | |   | |  | |   | |   |  / (___)  | |  | |   | '   | |  
 / .'| |  | |  | | | |  | |  | |  | |   | |  | |   | |   | |         | |  | |   _\_`.(___) 
{white}| /  | |  | |  | | | |  | |  | |  | |   | |  | |   | |   | |         | |  | |  (   ). '.   
; |  ; |  | '  | | | '  | |  | '  | |   ' '  ; '   | |   | |         | |  ; '   | |  `\ |  
' `-'  |  ' `-' ;  ' `-'  /  '  `-' /    \ `' /    | |   | |         ' `-'  /   ; '._,' '  
`.__.'_.   `.__.    `.__,'    `.__.'      '_.'    {black}(___) (___)         '.__.'     '.___.'   

                 
{red}█████████████████████
█████████████████████
{white}█████████████████████
█████████████████████
{black}█████████████████████
█████████████████████
█
█
█
█
█
█
█     
\t\tEgypt Hacker Army            
''')
print(f"{yellow}_____________________{green}A{red}b{even}d{blue}o{purple}{yellow}_{green}V{red}i{even}r{blue}u{purple}s{yellow}_____________________")
print("\n")
#####EndColor##############
sure=input(f"{green}First Sure if ip Change From Proxy Or Vpn Before Start {yellow}[{green}y{even},{red}n{yellow}]").lower()
print("\n")
if sure == "y":
	API=get("https://www.ipinfo.io").text
	API_DATE=json.loads(API)
	loc=API_DATE["loc"]
	ip=API_DATE["ip"]
	city=API_DATE["city"]
	country=API_DATE["country"]
	isp=API_DATE["org"]
	timezone=API_DATE["timezone"]
	print(f'''
	{green}[1]-Location {red}>>> {yellow}{loc}
	
	{green}[2]-Ip {red}>>> {yellow}{ip}
	
	{green}[3]-City {red}>>> {yellow}{city}
	
	{green}[4]-country {red}>>> {yellow}{country}
	
	{green}[5]-isp {red}>>> {yellow}{isp}
	
	{green}[4]-timezone {red}>>> {yellow}{timezone}
	''')
else:
	pass
print("\n")
print(f"{yellow}_____________________{green}A{red}b{even}d{blue}o{purple}{yellow}_{green}V{red}i{even}r{blue}u{purple}s{yellow}_____________________")
print("\n")
#######Sure ip##############
print(f"{green}You Must Enter The Url As {yellow}[{red}https://www.exmple.com{yellow}]")
print("\n")
print(f"{yellow}_____________________{green}A{red}b{even}d{blue}o{purple}{yellow}_{green}V{red}i{even}r{blue}u{purple}s{yellow}_____________________")
print("\n")
link=str(input(f"{yellow}Enter The Url {red}>>>{green} "))
print("\n")
try:
	domin=link.split("/")[2]
	target=ip(domin)
	print(f"{yellow}The Ip {purple}>>>{green} {target}")
except:
	print(f"{even}Ip {yellow}>>>{red} Not Found")
print("\n")	
print(f"{yellow}_____________________{green}A{red}b{even}d{blue}o{purple}{yellow}_{green}V{red}i{even}r{blue}u{purple}s{yellow}_____________________")
print("\n")
#########End Ip############
try:
	robot=get(f"{link}/robots.txt").text
	print(f"{green}The Response From Server Is \n {even}{robot}")
except:
	print(f"{red}Robots File Not Found In This Server")
print("\n")	
print(f"{yellow}_____________________{green}A{red}b{even}d{blue}o{purple}{yellow}_{green}V{red}i{even}r{blue}u{purple}s{yellow}_____________________")
print("\n")
##########robots.txt#########
try:
	head=get(link).headers
	for i in head:
		print(f"{even}{i} {red}>>> {blue}{head.get(i)}")
except:
	print(f"{red}The Headers Not Found")
print("\n")
print(f"{yellow}_____________________{green}A{red}b{even}d{blue}o{purple}{yellow}_{green}V{red}i{even}r{blue}u{purple}s{yellow}_____________________")
print("\n")
##########Headers##########
if len(domin.split('.')) == 3:
	the_sub=link.split("/")[2].split(".")[1]+"."+link.split("/")[2].split(".")[2]
	api=f"http://api.hackertarget.com/hostsearch/?q={the_sub}"
	print(f"{purple}{get(api).text}")
else:
	print(f"{purple}{get('http://api.hackertarget.com/hostsearch/?q={domin}').text}")
print("\n")
print(f"{yellow}_____________________{green}A{red}b{even}d{blue}o{purple}{yellow}_{green}V{red}i{even}r{blue}u{purple}s{yellow}_____________________")
print("\n")
##########Code In The Site ####
code=get(link).text
a=x(code,"html.parser")
print(f"{green}The {blue}Links{even} In {white}The {black}TargetSite")
links=a.find_all("a")
for i in links:
	print(f"{purple}{i.get('href')}")
print("\n")
print(f"{yellow}_____________________{green}A{red}b{even}d{blue}o{purple}{yellow}_{green}V{red}i{even}r{blue}u{purple}s{yellow}_____________________")
print("\n")
print(f"{green}The {blue}LinksImage{even} In {white}The {black}TargetSite")
links_2=a.find_all("img")
for i in links_2:
	print(f"{blue}{i.get('src')}")
print("\n")
print(f"{yellow}_____________________{green}A{red}b{even}d{blue}o{purple}{yellow}_{green}V{red}i{even}r{blue}u{purple}s{yellow}_____________________")
print("\n")
print(f"{green}The {blue}LinksScriptsFile{even} In {white}The {black}TargetSite")
links_3=a.find_all("script")
for i in links_3:
	print(f"{yellow}{i.get('src')}")
print("\n")
print(f"{yellow}_____________________{green}A{red}b{even}d{blue}o{purple}{yellow}_{green}V{red}i{even}r{blue}u{purple}s{yellow}_____________________")
print("\n")
print(f'''
{red}###############################
{green}# Created By Abdo_Virus Version 0.0#
#Soon This Tool is Group Tools For Hacking Scade , Websites , Mobile Apps ,Networks , .....)                        {red}#########################################
''')