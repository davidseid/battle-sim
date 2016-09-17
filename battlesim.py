#author: David Seidenberg
#project: Pokemon style turn based game for reddit intermediate python projects

'''
GOAL
Write a simple game that allows the user and the computer to take turns selecting moves to use against each other.
Both the computer and the player should start out at the same amount of health (such as 100), 
and should be able to choose between the three moves:

The first move should do moderate damage and has a small range (such as 18-25).
The second move should have a large range of damage and can deal high or low damage (such as 10-35).
The third move should heal whoever casts it a moderate amount, similar to the first move.

After each move, a message should be printed out that tells the user what just happened, 
and how much health the user and computer have. Once the user or the computer's health reaches 0, the game should end.

SUBGOALS
When someone is defeated, make sure the game prints out that their health has reached 0, and not a negative number.
When the computer's health reaches a set amount (such as 35%), increase it's chance to cast heal.
Give each move a name.
'''
from random import *
from time import sleep

#Welcomes user
print "\n\nHello and welcome to this turn-based 'Pokemon style' game I made."
print "You and the computer each start with 100 health."
print "You must fight each other, taking turns, the last one standing wins."

print '''
Here is the move list:

1. Punch: Do moderate damage within a small range
2. Fireball Kick: Do high or low damage depending on luck! 
3. Heal: Heal a moderate amount
''' 

user_health = 100
comp_health = 100
user_turn = True
space = "\n" * 100

while True:
	health_status = '''
	You now have %r health.
	The computer has %r health.''' % (user_health, comp_health)
	if user_turn == True:
		print health_status
		if comp_health > 0:
			move = raw_input("\nChoose a move >> ")
			if move == "1":
				damage = randint(18,25)
				comp_health -= damage
				if comp_health <= 0:
					print space
					print "You puched the computer, causing %r damage!" % (damage)
					print "The computer's health is 0! You won!\n"
					break
				elif comp_health > 0: 
					print space
					print "You punched the computer, causing %r damage." % (damage)
					print "The computer has %r total health left." % (comp_health)
					user_turn = False
					sleep(3)
					
			elif move == "2":
				damage = randint(10,35)
				comp_health -= damage
				if comp_health <= 0:
					print space
					print "Your fireball kick caused %r damage!" % (damage)
					print "You computer's health is 0! You won!\n"
					break
				elif comp_health > 0:
					print space
					print "Your fireball kick caused %r damage." % (damage)
					print "The computer has %r total health left." % (comp_health)
					user_turn = False
					sleep(3)
			
			elif move == "3":
				recover = randint(18,25)
				user_health += recover
				print "\nYou healed %r points." % (recover)
				if user_health > 100:
					user_health = 100
				user_turn = False
				sleep(3)
		
	elif user_turn == False:
		if user_health > 0:
			if comp_health >= 35:
				move = randint(1,3)
			elif comp_health < 35:
				at_risk = [1,2,3,3]
				move = choice(at_risk)
			if move == 1:
				damage = randint(18,25)
				user_health -= damage
				if damage >= (user_health + damage):
					print space
					print "The computer punched you, causing %r damage to you." % (damage + user_health)
					print "Your health is 0! You lose.\n"
					break
				elif user_health > 0:
					print space
					print "The computer punched you, causing %r damage to you." % (damage)
					user_turn = True
	
			elif move == 2:
				damage = randint(10,35)
				user_health -= damage
				if damage >= (user_health + damage):
					print space
					print "The computer did a fireball kick, causing %r damage to you." % (damage + user_health)
					print "Your health is 0! You lose.\n"
					break
				elif user_health > 0:
					print space
					print "The computer did a fireball kick, causing %r damage to you." % (damage)
					user_turn = True
			
			elif move == 3:
				recover = randint(18,25)
				comp_health += recover
				print space
				print "The computer healed itself %r points." % (recover)
				if comp_health > 100:
					comp_health = 100
				user_turn = True
		
		
