from __future__ import division
import time, random, sys

"""Code for easy mode monster"""

def monster_easy(h):
	print("A monster has attacked you!")
	time.sleep(2)
	mh = h
	print("Monster: %d HP" % mh)
	time.sleep(2)
	
	hlth = 50
	mgc = 10
	atk = 10

	if cls == 'MAGE':
		mgc = mgc + 10
		atk = atk - 5
	if cls == 'WARRIOR':
		atk = atk + 10
		mgc = mgc - 5
		
	sts = "Your status: \n Class: %s \n Health: %d \n Attack: %d \n Magic: %d" % (cls, hlth, atk, mgc)
	print(sts)
	time.sleep(4)
	monster = 'Heal', 'Attack', 'Cast', 'Flee'
	
	while (mh > 0) and (hlth > 0):
		activity = random.choice(monster)
		print("")
		print("Type A to attack, S to use a spell or H to heal.")
		move = input("")
		while move not in ('A', 'S', 'H'):
			print("Please TYPE A to Attack, S to use a spell or H to heal.")
			move = input("")
			
		if activity == 'Heal':
			mh = max(mh, mh + 2)
			print("The monster has healed! It restored some health!")
			print("Monster: %d HP" % mh)
		if activity == 'Attack':
			print("The monster has attacked! You took some damage!")
			hlth = hlth - 5
			print("You: %d HP" % hlth)
		if activity == 'Cast':
			print("The monster casts a spell! You took some damage!")
			hlth = hlth - 3
			print("You: %d HP" % hlth)
		if activity == 'Flee':
			print("The monster has fled!")
			return None	
			
		if move == 'A':
			print("Attacked the monster!")
			# Temporary
			if cls == 'MAGE':
				mh = mh - 5
			if cls == 'WARRIOR':
				mh = mh - 20
			else:
				mh = mh - 10
			print("Monster: %d HP" % mh)
		if move == 'S':
			# Also Temporary
			if cls == 'MAGE':
				mh = mh - 20
			if cls == 'WARRIOR':
				mh = mh - 5
			else:
				mh = mh - 10
			print("Used a spell!")
			print("Monster: %d HP" % mh)
		if move == 'H':
			hlth = max(50, hlth + 3)
			print("You restored some health.")
			print("You: %d HP" % hlth)
			
	if mh <= 0:
		print("The monster has been defeated!")
		time.sleep(1)
		return None
	elif hlth <= 0:
		print("You have died. Game OVER!")
		sys.exit("Quitting game")
		
	
""" Code for Medium mode monster. """
	
def monster_medium(h):
	print("A monster has attacked you!")
	time.sleep(2)
	mh = h
	print("Monster: %d HP" % mh)
	time.sleep(2)
	
	hlth = 50
	mgc = 10
	atk = 10

	if cls == 'MAGE':
		mgc = mgc + 10
		atk = atk - 5
	if cls == 'WARRIOR':
		atk = atk + 10
		mgc = mgc - 5
		
	sts = "Your status: \n Class: %s \n Health: %d \n Attack: %d \n Magic: %d" % (cls, hlth, atk, mgc)
	print(sts)
	time.sleep(4)
	monster = 'Heal', 'Attack', 'Cast', 'Flee'
	
	while (mh > 0) and (hlth > 0):
		activity = random.choice(monster)
		print("Type A to attack, S to use a spell or H to heal.")
		move = input("")
		while move not in ('A', 'S', 'H'):
			print("Please TYPE A to Attack, S to use a spell or H to heal.")
			move = input("")
			
			
		if activity == 'Heal':
			mh = max(mh, mh + 5)
			print("The monster has healed! It restored some health!")
			print("Monster: %d HP" % mh)
		if activity == 'Attack':
			print("The monster has attacked! You took some damage!")
			hlth = hlth - 7
			print("You: %d HP" % hlth)
		if activity == 'Cast':
			print("The monster casts a spell! You took some damage!")
			hlth = hlth - 5
			print("You: %d HP" % hlth)
		if activity == 'Flee':
			print("The monster has fled!")
			return None
			
		if move == 'A':
			print("Attacked the monster!")
			# Temporary
			if cls == 'MAGE':
				mh = mh - 5
			if cls == 'WARRIOR':
				mh = mh - 20
			else:
				mh = mh - 10
			print("Monster: %d HP" % mh)
		if move == 'S':
			# Also Temporary
			if cls == 'MAGE':
				mh = mh - 20
			if cls == 'WARRIOR':
				mh = mh - 5
			else:
				mh = mh - 10
			print("Used a spell!")
			print("Monster: %d HP" % mh)
		if move == 'H':
			hlth = max(50, hlth + 3)
			print("You restored some health.")
			print("You: %d HP" % hlth)
			
	if mh <= 0:
		print("The monster has been defeated!")
		time.sleep(1)
		return None
	elif hlth <= 0:
		print("You have died. Game OVER!")
		sys.exit("Quitting game")
		
""" Code for Hard mode monster. They don't flee. Allowed one attack before death."""
	
def monster_hard(h):
	print("A monster has attacked you!")
	time.sleep(2)
	mh = h
	print("Monster: %d HP" % mh)
	time.sleep(2)
	
	hlth = 50
	mgc = 10
	atk = 10

	if cls == 'MAGE':
		mgc = mgc + 10
		atk = atk - 5
	if cls == 'WARRIOR':
		atk = atk + 10
		mgc = mgc - 5
		
	sts = "Your status: \n Class: %s \n Health: %d \n Attack: %d \n Magic: %d" % (cls, hlth, atk, mgc)
	print(sts)
	time.sleep(4)
	monster = 'Heal', 'Attack', 'Cast'
	
	while (mh > 0) and (hlth > 0):
		activity = random.choice(monster)
		print("Type A to attack, S to use a spell or H to heal.")
		move = input("")
		while move not in ('A', 'S', 'H'):
			print("Please TYPE A to Attack, S to use a spell or H to heal.")
			move = input("")
			
		if move == 'A':
			print("Attacked the monster!")
			# Temporary
			if cls == 'MAGE':
				mh = mh - 5
			if cls == 'WARRIOR':
				mh = mh - 20
			else:
				mh = mh - 10
			print("Monster: %d HP" % mh)
		if move == 'S':
			# Also Temporary
			if cls == 'MAGE':
				mh = mh - 20
			if cls == 'WARRIOR':
				mh = mh - 5
			else:
				mh = mh - 10
			print("Used a spell!")
			print("Monster: %d HP" % mh)
		if move == 'H':
			hlth = max(50, hlth + 3)
			print("You restored some health.")
			print("You: %d HP" % hlth)
			
		if activity == 'Heal':
			mh = max(mh, mh + 2)
			print("The monster has healed! It restored some health!")
			print("Monster: %d HP" % mh)
		if activity == 'Attack':
			print("The monster has attacked! You took some damage!")
			hlth = hlth - 5
			print("You: %d HP" % hlth)
		if activity == 'Cast':
			print("The monster casts a spell! You took some damage!")
			hlth = hlth - 3
			print("You: %d HP" % hlth)
		
	if mh <= 0:
		print("The monster has been defeated!")
		time.sleep(1)
		return None
	elif hlth <= 0:
		print("You have died. Game OVER!")
		sys.exit("Quitting game")
		
		
""" Code for boss monster """

def boss_monster(h):
	print("A boss has attacked you!")
	time.sleep(2)
	mh = h
	print("Boss: %d HP" % mh)
	time.sleep(2)
	
	hlth = 50
	mgc = 10
	atk = 10

	if cls == 'MAGE':
		mgc = mgc + 10
		atk = atk - 5
	if cls == 'WARRIOR':
		atk = atk + 10
		mgc = mgc - 5
		
	sts = "Your status: \n Class: %s \n Health: %d \n Attack: %d \n Magic: %d" % (cls, hlth, atk, mgc)
	print(sts)
	time.sleep(4)
	monster = 'Heal', 'Attack', 'Cast'
	
	while (mh > 0) and (hlth > 0):
		activity = random.choice(monster)
		print("Type A to attack, S to use a spell or H to heal.")
		move = input("")
		while move not in ('A', 'S', 'H'):
			print("Please TYPE A to Attack, S to use a spell or H to heal.")
			move = input("")
			
		if move == 'A':
			print("Attacked the monster!")
			# Temporary
			if cls == 'MAGE':
				mh = mh - 5
			if cls == 'WARRIOR':
				mh = mh - 20
			else:
				mh = mh - 10
			print("Monster: %d HP" % mh)
		if move == 'S':
			# Also Temporary
			if cls == 'MAGE':
				mh = mh - 20
			if cls == 'WARRIOR':
				mh = mh - 5
			else:
				mh = mh - 10
			print("Used a spell!")
			print("Monster: %d HP" % mh)
		if move == 'H':
			hlth = max(50, hlth + 10)
			print("You restored some health.")
			print("You: %d HP" % hlth)
			
		if activity == 'Heal':
			mh = max(mh, mh + 7)
			print("The boss monster has healed! It restored some health!")
			print("Monster: %d HP" % mh)
		if activity == 'Attack':
			print("The boss monster has attacked! You took some damage!")
			hlth = hlth - 9
			print("You: %d HP" % hlth)
		if activity == 'Cast':
			print("The boss monster used gigablast! You took some damage!")
			hlth = hlth - 15
			print("You: %d HP" % hlth)
		
	if mh <= 0:
		print("Congratulations! You defeated the boss!")
		time.sleep(1)
		print("%s gained 978 EXP. Not that it matters..." % name)
		return None
	elif hlth <= 0:
		print("You have died. SORRY! GAME OVER!")
		sys.exit("Quitting game")


""" Code for monster encounters. Useful! """

def monster_encounter(a, b, c):
	if dif == 'EASY':
		monster_easy(a)
	elif dif == 'MEDIUM':
		monster_medium(b)
	elif dif == 'HARD':
		monster_hard(c)
		
""" Code(s) for timed input """

def dodge_trap(prompt, timeout, word):
	start = time.time()
	s = input("(%ds) %s" % (timeout, prompt) )
	stop = time.time()
	
	if stop-start > timeout:
		print("You were too slow! The trap knocked you out and you fell unconscious...")
		time.sleep(50)
		print("...")
		time.sleep(3)
		print("You finally came to. You get up and exit the corridor.")
	elif s == word:
		print("You did it!")
	else:
		print("Close enough..You dodged the rock.")
		
def password(prompt, timeout, word):
	start = time.time()
	s = input("(%ds) %s" % (timeout, prompt) )
	stop = time.time()
	
	if stop-start > timeout:
		print("The spirit speaks: \n\t'You were too slow. Now I'm going to make you fall asleep for 50 seconds.")
		time.sleep(1)
		print("...")
		time.sleep(50)
		print("...")
		time.sleep(3)
		print("You finally came to.")
		time.sleep(1)
		print("The spirit speaks again: \n\tI see you woke up. You can go upstairs now, I'm bored.")
	elif s in str(word):
		print("You did it!")
	else:
		print("WRONG!")
		s = input("(%ds) %s" % (timeout, prompt) )
		
		if stop-start > timeout:
			print("The spirit speaks: \n\t'You were too slow. Now I'm going to make you fall asleep for 50 seconds.")
			time.sleep(1)
			print("...")
			time.sleep(50)
			print("...")
			time.sleep(3)
			print("You finally came to.")
			time.sleep(1)
			print("The spirit speaks again: \n\tI see you woke up. You can go upstairs now, I'm bored."	)
				
		elif s in str(word):
			print("You did it!")
				
		else:
			print("Sorry you got it wrong twice. Game OVER!")
			sys.exit("Quitting game")
		
def password2(prompt, timeout, word):
	start = time.time()
	s = input("(%ds) %s" % (timeout, prompt) )
	stop = time.time()
	
	if stop-start > timeout:
		print("The spirit speaks: \n\t'You were too slow. Now I'm going to make you fall asleep for 50 seconds. (again)")
		time.sleep(1)
		print("...")
		time.sleep(50)
		print("...")
		time.sleep(3)
		print("You finally came to.")
		time.sleep(1)
		print("The spirit speaks again: \n\tI see you woke up. You can get out of the trap now, I just wanted some company.")
	elif s == word:
		print("You did it!")
	else:
		print("WRONG!")
		s = input("(%ds) %s" % (timeout, prompt) )
		
		if stop-start > timeout:
			print("The spirit speaks: \n\t'You were too slow. Now I'm going to make you fall asleep for 50 seconds.")
			time.sleep(1)
			print("...")
			time.sleep(50)
			print("...")
			time.sleep(3)
			print("You finally came to.")
			time.sleep(1)
			print("The spirit speaks again: \n\tI see you woke up. You can get out of the trap now, I just wanted some company.")
			
		elif s == word:
			print("You did it!")
			
		else:
			print("Sorry you got it wrong twice. Game OVER!")
			sys.exit("Quitting game")
		

""" Main Game """
		
print("Welcome to Python RPG! Whenever you're ready to play, hit ENTER.")
input()
time.sleep(2)	
print("Choose your difficulty level:")
time.sleep(1)
print(" Type EASY, MEDIUM, or HARD")
dif = input("")
while dif not in ('EASY', 'MEDIUM', 'HARD'):
		print("Please type either EASY, MEDIUM, or HARD with capital letters.")
		dif = input("")
print("You have chosen to play in %s mode" % dif)
time.sleep(2)
print("Next, choose your class.")
time.sleep(1)
print(" Type ADVENTURER, WARRIOR or MAGE.")
cls = input("")


while cls not in ('ADVENTURER', 'WARRIOR', 'MAGE'):
		print("Please type either ADVENTURER, WARRIOR, or MAGE with capital letters.")
		cls = input("")
		
if cls == 'ADVENTURER':
	print("You have chosen to play as an %s" % cls)
elif cls == 'WARRIOR':
	print("You have chosen to play as a %s" % cls)
elif cls == 'MAGE':
	print("You have chosen to play as a %s" % cls)
else:
	print("Please type either ADVENTURER, WARRIOR, or MAGE with capital letters.")
	cls = input("")
time.sleep(1)
print(" Finally pick a name for your player")
time.sleep(1)
name = input("")
time.sleep(1)
print("...")
time.sleep(1)
print("OK!")
time.sleep(1)
print("The adventure of %s, the %s will start! You will be playing this game in %s mode." % (name, cls, dif))
time.sleep(3)
print("...")
time.sleep(1)
print("")
print("You find yourself at the base of a tall stone tower.")
time.sleep(2)
print("A sign at the front reads: \n'This is the tall stone tower of tallness. \nThose who reach the secret room on the third floor of this tower will receive a magical prize.'")
time.sleep(1)
print("You notice the number 27 written on the back of the sign.")
time.sleep(3)
print("Enter the tall stone tower?")
print(" Type YES or NO. ")
ent = input("")

while ent not in ('YES', 'NO'):
	print("Please type either YES to enter or NO to leave.")
	ent = input("")

if ent == 'NO':
	while ent == 'NO':
		print("Now is not the time to chicken out! There's a prize waiting! Say YES!")
		ent = input("")
if ent == 'YES':
	print("Entered the stone tower.")
	print("...")
else:
	print("I'll take that as a yes. Entering the tower!")
time.sleep(2)

print("The lights are dim...It's hard to move around.")
time.sleep(1)
print("Use some magic to light the area? Type YES or NO.")
choice1 = input("")
while choice1 not in ('YES', 'NO'):
	print("Please type either YES to use magic or NO to continue walking.")
	choice1 = input("")

if choice1 == 'NO':
	print("Chose not to light the area.")
elif choice1 == 'YES':
	print("You cast a spell for light. A key on the ground catches your eye. You pick it up.")
time.sleep(1)
print("You continue walking, eventually reaching a long corridor.")
time.sleep(1)
monster_encounter(80, 80, 85)
time.sleep(2)
print("Continuing through the corridor, you hear a noise.")
time.sleep(2)
print("The sound is coming from the walls. You've set off a trap!")
time.sleep(2)
dodge_trap("You have 5 seconds to type DODGE to dodge the trap!", 5, 'DODGE')
time.sleep(2)
monster_encounter(80, 85, 85)
time.sleep(1)
print("Just as you catch your breath...")
time.sleep(2)
monster_encounter(80, 80, 85)
time.sleep(2)
print("You've finally reached the first flight of stairs.")
time.sleep(2)
print("However a magical barrier is blocking the way.")
time.sleep(2)
print("The magical spirit of irrelevance speaks: ")
print("")
time.sleep(1)
print("	Before you go to the second floor, you must tell me the number you saw at the front of the tower.")
print("")
time.sleep(2)
print("	Oh and you only have 5 seconds to type it in. LOL")
time.sleep(2)
password('Type in your answer', 5, 27)
time.sleep(2)
print("You reached the second floor.")
time.sleep(2)
print("The room isn't very large, as you can see the stairs to the third floor from across the room.")
time.sleep(3)
monster_encounter(90, 90, 95)
print("")
print("As you make your way to the other side of the room, three more monsters charge at you.")
print("")
time.sleep(2)
print("How convenient...")
time.sleep(1)
monster_encounter(90, 90, 95)
monster_encounter(90, 90, 95)
monster_encounter(90, 90, 95)
print("")
time.sleep(2)
print("After that sorry excuse for game content, you finally reach the second flight of stairs.")
time.sleep(2)
print("A large taurus-like demon blocks the way. It carries a trident in one hand and a mace in the other.")
print("")
time.sleep(2)
print("What would you like to do?")
time.sleep(2)
print("\tType: \n\t\tTAUNT to taunt the demon\n\t\tSTARE to stare it down\n\t\tFLUTE to use your Pokeflute\n\t\tJOKE to tell it a joke")
choice2 = input("")
while choice2 not in ('TAUNT', 'STARE', 'FLUTE', 'JOKE'):
	print("Please type either TAUNT, STARE, FLUTE, or JOKE.")
	choice2 = input("")
if choice2 == 'TAUNT':
	time.sleep(1)
	print("You made fun of the taurus'.")
	time.sleep(1)
	print("Its self-esteem lowered! You were able to pass.")
if choice2 == 'STARE':
	time.sleep(1)
	print("You stared down the taurus.")
	time.sleep(1)
	print("Taurus became self-conscious about its image. You were able to pass.")
if choice2 == 'FLUTE':
	time.sleep(1)
	print("You used your Pokeflute.")
	time.sleep(1)
	print("It was ineffective. Taurus is awake. Regardless, the demon finds your lack of knowledge humorous and allows you to pass.")
if choice2 == 'JOKE':
	time.sleep(1)
	print("You told the taurus a joke.")
	time.sleep(1)
	print("Taurus finds your comedic style dry and uninspired. (tough crowd)")
	time.sleep(1)
	print("Taurus becomes bored and falls asleep. Allowing you to pass.")

time.sleep(1)
print("")
print("You reach the third floor.")
monster_encounter(95, 95, 95)
time.sleep(1)
print("As you walk through this floor, you begin to wonder if anything will happen to you other than just monster attacks.")
time.sleep(4)
print("...")
monster_encounter(95, 100, 110)
time.sleep(3)
print("The secret room is somewhere on this floor.")
time.sleep(2)
print("Suddenly, a pitfall trap activates under your feet - trapping you.")
time.sleep(2)
print("")
print("The magical spirit of irrelevance returns again.")
print("")
print("\t'Haha! Payback for passing me before.'")
print("")
time.sleep(1)
print("\n>%s disregards logistics of pitfall trap on third floor" % name)
print("")
time.sleep(2)
print("\t'If you want to escape the trap, you'll have to tell me the answer to this question:'")
time.sleep(3)
print("\t'This is the tall stone tower of _______?  \n\tI'll give you 10 seconds.'")
time.sleep(2)
password2('Type your answer here', 10, 'tallness')
time.sleep(2)
print("")
print("Escaped the trap.")
time.sleep(1)
print("")
monster_encounter(100, 105, 125)
print("")
time.sleep(1)
print("Slowly but surely you make your way to the entrance of the secret room.")
time.sleep(1)
print("A demonic-looking padlock is keeping the door locked.")
time.sleep(2)
if choice1 == 'YES':
	print("You remember the key you found on the first floor. It unlocks the padlock.")
	print("")
	time.sleep(2)
	print("All of a sudden, the lock transforms into a giant pig monster.")
	print("")
	time.sleep(2)
	print("It seems the key took away a portion of its health.")
	time.sleep(1)
	print("Get ready for the last fight!!")
	boss_monster(150)
else:
	print("Suddenly the lock transforms into a giant pig monster.")
	print("")
	time.sleep(2)
	print("Get ready for the last fight!!")
	boss_monster(250)
print("")
time.sleep(2)
print("The door to the secret room opens up.")
print("")
time.sleep(1)
print("A gold chest sits in the middle of the room. \nYou walk to the chest and open it up.")
print("")
time.sleep(1)
print("Inside you find a note. The notes says:")
time.sleep(2)
print("\t Dear %s, while you were off fighting those hordes of monsters, \nI decided to take the prize for myself. \nSincerely Taurus." % name)
time.sleep(4)
print("...")
time.sleep(2)
print("The end.")
sys.exit








	
	
	

