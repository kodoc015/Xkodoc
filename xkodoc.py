## xkodoc.py
# -*- coding: utf-8 -*-
import os
import sys
from time import sleep as timeout
from core.corexkodoc import *

def main():
	banner()
	print "   (1) Hacking"
	print "   (2) Spammer"
	print "   (3) Sosmed"
	print "   (4) Other"
	print "   (4) Back!!!\n"
	xkodoc = raw_input("xkodoc > ")
	
	#Hacking
	if xkodoc == "1" or xkodoc == "01":
		print "\n    (01) Nmap"
		print "    (02) Red Hawk"
		print "    (03) sqlmap"
		print "    (04) sqlmate"
		print "    (05) sqliv"
		print "    (06) sqldump"
		print "    (07) sqlokmed"
		print "    (08) sqlscan"
		print "    (09) wpscan"
		print "    (10) wordpresscan"
		print "    (11) webdav"
		print "    (12) dtect"
		print "    (13) admin-finder"
		print "    (14) owscan"
		print "    (15) bruteforce gmail"
		print "    (00) Back to main menu\n"
		hacking = raw_input("xkodoc > ")
		
		if hacking == "01" or hacking == "1":
			nmap()
		elif hacking == "02" or hacking == "2":
			red_hawk()
		elif hacking == "03" or hacking == "3":
			sqlmap()
		elif hacking == "04" or hacking == "4":
			sqlmate()
		elif hacking == "05" or hacking == "5":
		     sqliv()
		elif hacking == "06" or hacking == "6":
		    sqldump()  
		elif hacking == "07" or hacking == "7":
		   sqlokmed()     	
		elif hacking == "08" or hacking == "8":
		    sqlscan()
		elif hacking == "09" or hacking == "9":
		    wpscan()
		elif hacking == "10":
		    wordpresscan()  
		elif hacking == "11":
		    webdav()
		elif hacking == "12":
		    dtect() 
		elif hacking == "13":
		    admin_finder()   
		elif hacking == "14":
		    owscan()  
		elif hacking == "15":
		    brute_gmail()    
		elif hacking == "00" or hacking == "0":
			restart_program()
		else:
			print "\nERROR: Wrong Input"
			timeout(2)
			restart_program()
			
    #spammer
	elif xkodoc == "2" or xkodoc == "02":
		print "\n    (01) Spammer-Email"
		print "    (02) Spammer-Grab"
		print "    (03) Hac"
		print "    (04) santet-online"
		print "    (05) SpazSMS\n"
		print "    (06) Spam-TLP"
		print "    (07) Spam Tokopedia"
		print "    [00] Back to main menu\n"
		spammer = raw_input("xkodoc > ")
		
		if spammer == "01" or spammer == "1":
			spammer_email()
		elif spammer == "02" or spammer == "2":
			spammer_grab()
		elif spammer == "03" or spammer == "3":
			hac()
		elif spammer == "04" or spammer == "4":
			sanlen()
		elif spammer == "05" or spammer == "5":
			spazsms()
		elif spammer == "06" or spammer == "6":
			spam_tlp()
		elif spammer == "07" or spammer == "7":
		    spam_tokped()
		elif spammer == "00" or spammer == "0":
			restart_program()
		else:
			print "\nERROR: Wrong Input"
			timeout(2)
			restart_program()
			
	#sosmed
	elif sosmed == "3" or sosmed == "03":
	    print "\n    (01) Instabot"
	    print "    (02) MBF (FB)"
	    print "    (03) Auto IG"
	    print "    (04) osif"
	    sosmed = raw_input("xkodoc >")
	    
	    if sosmed == "01" or sosmed == "1":
	        instabot()
	    elif sosmed == "02" or sosmed == "2":
	        mbf()
	    elif sosmed == "03" or sosmed == "3":
	        auto_ig()
	    elif sosmed == "04" or sosmer == "4":
	        osif()
	    else:
	        print "\nERROR:Wrong Input"
	        timeout(2)
	        restart_program()
	#other
	elif xkodoc == "4" or xkodoc == "04":
		print "\n    [01] Hashbuster"
		print "    [02] Ngrok"
		print "    [03] Sudo"
		print "    [04] Metasploit"
		print "    [00] Back to main menu\n"
		moretool = raw_input("xkodoc > ")
		
		if other == "01" or other == "1":
			hash_buster()
		elif other == "02" or other == "2":
			ngrok()
		elif other == "03" or other == "3":
			sudo()
		elif other == "04" or other == "4":
			metasploit()
		elif other == "00" or other == "0":
			restart_program()
		else:
			print "\nERROR: Wrong Input"
			timeout(2)
			restart_program()
	
	elif xkodoc == "10":
		sys.exit()
	
	else:
		print "\nERROR: Wrong Input"
		timeout(2)
		restart_program()

if __name__ == "__main__":
	main()
