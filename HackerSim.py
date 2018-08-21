'''
LegendBegins
August, 2018
A short demo to simulate the process of hacking a system without the technical complexity.
Reset the game and timer with the command "reset" and exit with "terminate."
Runs in both Linux and Windows.
'''


import os
import signal
import time


dir_path = os.path.dirname(os.path.realpath(__file__))	#Get directory of file
	
def handler(signum, frame):								#Disable ctl-z
    pass

#signal.signal(signal.SIGTSTP, handler)					#Enable this line to remove the ability to use ctrl-z


instructions = '''\nThe game is simple. Hack the Usernited SolidStates government. Specifically, we want our hands on President Gerald Trombone's account on the National Cybernuke Admin Panel so we can end the threat of
Cyberia once and for all. We managed to shut down their Intrusion Detection Systems for six minutes--once that time is up, there's no chance of evading their defenses. They'll know. You have various tools and
commands at your disposal, so use them wisely. As the great hacker known as DChannel, you should have no trouble with this mission. Good luck, and H4PP33 H4(K1N9.

Targets: mail.uss.gov, vpn.uss.gov, cyber.uss.gov [INTERNAL ADMIN PANEL (cannot access without proxy)]

Commands:

scan [target] -- Analyzes the target to see if there are any vulerabilities to take advantage of

exploit [target] [vulnerability] -- Uses the vulnerability to gain access to the target

login [target] -- Try to log in with a username and password

proxy [target] -- Use a target you've taken control of (pwned) to give you access to internal systems

list -- Lists targets

hint -- Displays a hint of what to do next

help -- Displays this help'''

success = '''
::::    ::::  ::::::::::: ::::::::   :::::::: ::::::::::: ::::::::  ::::    :::       ::::::::  :::    :::  ::::::::   ::::::::  :::::::::: ::::::::   ::::::::  ::: 
+:+:+: :+:+:+     :+:    :+:    :+: :+:    :+:    :+:    :+:    :+: :+:+:   :+:      :+:    :+: :+:    :+: :+:    :+: :+:    :+: :+:       :+:    :+: :+:    :+: :+: 
+:+ +:+:+ +:+     +:+    +:+        +:+           +:+    +:+    +:+ :+:+:+  +:+      +:+        +:+    +:+ +:+        +:+        +:+       +:+        +:+        +:+ 
+#+  +:+  +#+     +#+    +#++:++#++ +#++:++#++    +#+    +#+    +:+ +#+ +:+ +#+      +#++:++#++ +#+    +:+ +#+        +#+        +#++:++#  +#++:++#++ +#++:++#++ +#+ 
+#+       +#+     +#+           +#+        +#+    +#+    +#+    +#+ +#+  +#+#+#             +#+ +#+    +#+ +#+        +#+        +#+              +#+        +#+ +#+ 
#+#       #+#     #+#    #+#    #+# #+#    #+#    #+#    #+#    #+# #+#   #+#+#      #+#    #+# #+#    #+# #+#    #+# #+#    #+# #+#       #+#    #+# #+#    #+#     
###       ### ########### ########   ######## ########### ########  ###    ####       ########   ########   ########   ########  ########## ########   ########  ###
'''

failureMessage = '''
 __    __     __     ______     ______     __     ______     __   __        ______   ______     __     __         ______     _____    
/\ "-./  \   /\ \   /\  ___\   /\  ___\   /\ \   /\  __ \   /\ "-.\ \      /\  ___\ /\  __ \   /\ \   /\ \       /\  ___\   /\  __-.  
\ \ \-./\ \  \ \ \  \ \___  \  \ \___  \  \ \ \  \ \ \/\ \  \ \ \-.  \     \ \  __\ \ \  __ \  \ \ \  \ \ \____  \ \  __\   \ \ \/\ \   ___   ___   ___
 \ \_\ \ \_\  \ \_\  \/\_____\  \/\_____\  \ \_\  \ \_____\  \ \_\\\\"\_\     \ \_\    \ \_\ \_\  \ \_\  \ \_____\  \ \_____\  \ \____-  /\__\ /\__\ /\__\ 
  \/_/  \/_/   \/_/   \/_____/   \/_____/   \/_/   \/_____/   \/_/ \/_/      \/_/     \/_/\/_/   \/_/   \/_____/   \/_____/   \/____/  \/__/ \/__/ \/__/
\n\nYour six minutes are up.
We expected more from the great hacker DChannel, but I suppose the USS government is just that good. The FBI is on its way, but don't worry. We'll bust you out before you know it...'''

deathMessage = '''
   ___                      _   _            _____              _           _          _ 
  / __|___ _ _  _ _  ___ __| |_(_)___ _ _   |_   _|__ _ _ _ __ (_)_ _  __ _| |_ ___ __| |
 | (__/ _ \ ' \| ' \/ -_) _|  _| / _ \ ' \    | |/ -_) '_| '  \| | ' \/ _` |  _/ -_) _` |
  \___\___/_||_|_||_\___\__|\__|_\___/_||_|   |_|\___|_| |_|_|_|_|_||_\__,_|\__\___\__,_|
                                                                                         '''

os.system('clear')
print('''                       uuuuuuuuuuuuuuuuuuuuu.
                   .u$$$$$$$$$$$$$$$$$$$$$$$$$$W.
                 u$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$Wu.
               $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$i
              $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
         `    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
           .i$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$i
           $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$W
          .$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$W
         .$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$i
         #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$.
         W$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$u       #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$~
$#      `"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$i        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$         $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#$.        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
 $$      $iW$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$!
 $$i      $$$$$$$#"" `"""#$$$$$$$$$$$$$$$$$#""""""#$$$$$$$$$$$$$$$W
 #$$W    `$$$#"            "       !$$$$$`           `"#$$$$$$$$$$#
  $$$     ``                 ! !iuW$$$$$                 #$$$$$$$#
  #$$    $u                  $   $$$$$$$                  $$$$$$$~
   "#    #$$i.               #   $$$$$$$.                 `$$$$$$
          $$$$$i.                """#$$$$i.               .$$$$#
          $$$$$$$$!         .   `    $$$$$$$$$i           $$$$$
          `$$$$$  $iWW   .uW`        #$$$$$$$$$W.       .$$$$$$#
            "#$$$$$$$$$$$$#`          $$$$$$$$$$$iWiuuuW$$$$$$$$W
               !#""    ""             `$$$$$$$##$$$$$$$$$$$$$$$$
          i$$$$    .                   !$$$$$$ .$$$$$$$$$$$$$$$#
         $$$$$$$$$$`                    $$$$$$$$$Wi$$$$$$#"#$$`
         #$$$$$$$$$W.                   $$$$$$$$$$$#   ``
          `$$$$##$$$$!       i$u.  $. .i$$$$$$$$$#""
             "     `#W       $$$$$$$$$$$$$$$$$$$`      u$#
                            W$$$$$$$$$$$$$$$$$$      $$$$W
                            $$`!$$$##$$$$``$$$$      $$$$!
                           i$" $$$$  $$#"`  """     W$$$$
                                                   W$$$$!
                      uW$$  uu  uu.  $$$  $$$Wu#   $$$$$$
                     ~$$$$iu$$iu$$$uW$$! $$$$$$i .W$$$$$$
             ..  !   "#$$$$$$$$$$##$$$$$$$$$$$$$$$$$$$$#"
             $$W  $     "#$$$$$$$iW$$$$$$$$$$$$$$$$$$$$$W
             $#`   `       ""#$$$$$$$$$$$$$$$$$$$$$$$$$$$
                              !$$$$$$$$$$$$$$$$$$$$$#`
                              $$$$$$$$$$$$$$$$$$$$$$!
                            $$$$$$$$$$$$$$$$$$$$$$$`
                             $$$$$$$$$$$$$$$$$$$$"
\n\n\n                 W E L C O M E   T O   T H E   G A M E . . .\n''')

email = '''\nFrom: President Gerald Trombone (potus@mail.uss.gov)\t\tTo: IT Lead, Lan Sysmin (infotech@mail.uss.gov)
\nSubject: VPN Failure
\nMessage Body:
Lan, help me out; I have a YUGE problem! Whenever I try to connect to the VPN, it won't let me; it says something like "ERROR: Could not authenticate to VPN Service." I really need to get on there or else I won't be able to watch Secretary Pewpe's new documentary, "How to troll your way into power." Could this be the work of the hacker known as DChannel? If it is, our infosec team is FIRED!
\nP.S. If you need my username and password to get me on the VPN, they're 'GeraldT' and 'Sp00kySkelly', respectively. I named it after a song I liked, just like infosec recommended!
\nThanks,\nPresident Trombone'''



hints = ['Perhaps if you started looking for vulnerabilities in the targets, you\'d find something interesting. Maybe you have some kind of scan available?', 'Did you find anything in your scan? If so, maybe you can exploit one of your targets.', 'Wow, look at that email. We can\'t use the VPN by logging in, but maybe if we had his credentials, we\'d be able to use it as a proxy...', 'Now you just have to log into the cybernuke admin panel? Nice! Be sure to hit Cyberia AND NO ONE ELSE.', 'You have reached the end of your game. Thanks for playing! Hope to see you in (SC)^2.\n--LegendBegins']
hintIndex = 0
proxied = False
reset = False
selfDestruct = False
startTime = time.time()
while True:
	try:

		if time.time() - startTime > 560 and not selfDestruct:
			print(failureMessage)
			selfDestruct = True

		if selfDestruct:
			while True:
				input = raw_input()		#Stuck in Game Over forever.
				input = input.lower()
				if input == 'reset':
					reset = True
					break
				elif input == 'terminate':
					break
			break

		input = raw_input('\n>> ')
		input = input.lower()
		if input == 'help':
			print(instructions)

		elif input == 'list':
			print('Targets: mail.uss.gov, vpn.uss.gov, cyber.uss.gov [INTERNAL (cannot access without proxy)]')

		elif input.startswith('scan'):
			if len(input.split()) < 2:	#No target provided
				continue
			target = input.split()[1]
			if target == 'mail.uss.gov':
				print('Vulnerabilities found: MS-1337')
				if hintIndex < 1:
					hintIndex = 1		#Next hint
			else:
				print('No vulnerabilities in database')

		elif input.startswith('login') or input.startswith('logon'):
			if len(input.split()) < 2:	#No target provided
				continue
			target = input.split()[1]
			if target == 'mail.uss.gov':
				uname = raw_input('Username: ')
				passname = raw_input('Password: ')
				if uname == 'GeraldT' and passname == 'Sp00kySkelly':
					if raw_input('Read Email? (Y/N): ').lower() == 'y':
						print(email)	
			elif target == 'vpn.uss.gov':
				uname = raw_input('Username: ')
				passname = raw_input('Password: ')
				if uname == 'GeraldT' and passname == 'Sp00kySkelly':
					print('\nThis is the Usernited SolidStates VPN service. Unauthorized access is NOT permitted. Please see your system administrator to set up a VPN connection or a proxy.')
			elif target == 'cyber.uss.gov':
				if not proxied:
					print('Could not access internal network. Please connect to a network proxy.')
				else:
					if raw_input('Welcome to the cybernuke launch system. Would you like to proceed? (y/n) ').lower() == 'y':			#Cybernuke Admin Panel accessed
						if raw_input('''\nWARNING: LAUNCHING A CYBER NUKE WILL DESTROY THE DIGITAL INFRASTRUCTURE OF WHATEVER NATION YOU ARE TARGETING.
ARE YOU SURE YOU WANT TO PROCEED? (y/n) ''').lower() == 'y':
							location = raw_input('\nPlease select target location: ')
							if 'uss' in location.lower() or 'solid' in location.lower():
								print('\n\nUnISNGDted SolidSTESFNISRPG: CyB3r w0rld desttttttttttttttttttr0yed. Have a niiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiice da')
								print('''\n\n\n\nTransmission:
Congrats. You played yourself. This is the last you'll be hearing from us. Not that it matters. Your new analogue nightmare has only just begun.
I hope you're not too attached to your tech, because you just destroyed it all.
Forever.
900d8y3.
-L3X L465''')
								print(deathMessage)
								selfDestruct = True
								while True:
									input = raw_input()		#Stuck in Game Over forever.
									input = input.lower()
									if input == 'reset':
										reset = True
										break
									elif input == 'terminate':
										break
								break
							else:
								print('\n\n\n' + location + '\'s cyberworld destroyed. Please take necessary precautionary measures.\n\n\n')
								if 'cyber' in location.lower():
									print(success)
									print('''\n\n\n\nTransmission:
Hey, good job out there. Cyberia is done for. You really are as impressive as they say--I have a feeling we'll be seeing a lot of each other in the future. You'd be a great fit with our friends down in
the (SC)^2 laboratories. Either way, you have successfully completed your mission and can expect a large sum deposited in your bank account within the next few days. We'll keep in touch.
Laters.
-L3X L465''')
									hintIndex = 4

		elif input.startswith('proxy'):
			if len(input.split()) < 2:	#No target provided
				continue
			target = input.split()[1]
			if target == 'vpn.uss.gov':
				if proxied:
					print('Already connected to internal network')
				else:
					uname = raw_input('Username: ')
					passname = raw_input('Password: ')
					if uname == 'GeraldT' and passname == 'Sp00kySkelly':
						print('Access Granted. Connection established.')
						proxied = True
						if hintIndex < 3:
							hintIndex = 3
					else:
						print('Credentials invalid. Connection refused.')
			elif target == 'mail.uss.gov':
				print('Cannot proxy through external service.')
			elif target == 'cyber.uss.gov':
				if proxied:
					print('Already connected to internal network')
				else:
					print('Could not connect to internal network.')

		elif input.startswith('exploit'):
			if len(input.split()) < 3:	#No target provided
				continue
			target = input.split()[1]
			exploit = input.split()[2]
			if exploit == 'ms-1337' and target == 'mail.uss.gov':
				if raw_input('Read Email? (Y/N): ').lower() == 'y':
					print(email)	
					if hintIndex < 2:
						hintIndex = 2
			else:
				print('Exploitation Failed.')			

		elif input == 'hint':
			print(hints[hintIndex])

		elif input == 'reset':
			reset = True
			break

		elif input == 'terminate':
			break
	except KeyboardInterrupt:
		print('')
		pass
if reset:
	#os.system('echo -e \'\\0033\\0143\'')					#Enable on Linux to clear screen
	os.system('python ' + dir_path + '/HackerSim.py')
