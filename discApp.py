import discord
import random

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        #the exact phrase the user inputs
        inputSentence = message.content

        #if the message is sent by the bot itself ignore it
        if message.author == client.user:
            return
    
        if inputSentence.startswith('!jeff'):
            await message.channel.send("pls don't eat me")

        if inputSentence.startswith('!mike'):
            await message.channel.send("the one who got away")

        if inputSentence.startswith('!dylan'):
            await message.channel.send("dyly dyl uwu")

        if inputSentence.startswith('!jin'):
            await message.channel.send("Jeff's hyung")

        if inputSentence.startswith('!bon'):
            await message.channel.send("bon bon")

        if inputSentence.startswith('!law'):
            await message.channel.send("lawy poopoo <3")
        if inputSentence.startswith("!lawyum"):
            await message.channel.send("o thats yummy")

        if inputSentence.startswith("!brian"):
            await message.channel.send("eat my ass")

        if inputSentence.startswith('!echo'):
            afterEcho = inputSentence.replace("!echo", "")
            await message.channel.send(afterEcho)
        
        if inputSentence.startswith("!shake"):
            responseList = ["yes",
                            "no",
                            "maybe",
                            "idk but at least dylan is cute",
                            "hmph"]
            response = random.choice(responseList)
            await message.channel.send(response)

        
        if inputSentence.startswith("!attention"):
            await message.channel.send("Give me attention <@149365468984115200>")
        if inputSentence.startswith("!buicommands"):
            await message.channel.send("!jeff, !mike, !law, !dylan,!bon, !jin, !echo, !shake, !attention")


        if inputSentence.startswith("duck"):
            oneLiners = ["what the duck are you doing??",
                    "how the honking hell did you get that idea?"]

            response = random.choice(oneLiners)

            await message.channel.send(response)
        

        '''
        GAME TIME GAME TIME
        GAME TIME GAME TIME
        GAME TIME GAME TIME
        GAME TIME GAME TIME
        GAME TIME GAME TIME
        GAME TIME GAME TIME
        '''
        #nice

        if inputSentence.startswith("!adventure"):
            await message.channel.send("adventure time")

            await message.channel.send("You are the main character of this story, {}".format(message.author.mention))
            await message.channel.send("Choose your class... You can be a warrior or a mage lmao")

            mainCharID = message.author.id
            characterSelected = False



            while not characterSelected:
                next_msg = await client.wait_for('message', check = lambda message: mainCharID == message.author.id)
                if next_msg.content == "warrior":
                    await message.channel.send("You have chosen a warrior")
                    mainCharStats = statGenerator(warrior_hp, warrior_atk, warrior_shield)
                    mainChar = ClassType(message.author.id, mainCharStats[0], mainCharStats[1],mainCharStats[2])
                    characterSelected = True

                elif next_msg.content == "mage":
                    await message.channel.send("You have chosen a magician")
                    mainCharStats = statGenerator(mage_hp, mage_atk, mage_shield)
                    mainChar = ClassType(message.author.id, mainCharStats[0], mainCharStats[1],mainCharStats[2])
                    characterSelected = True

            #character creation to start here and to set your health here...
            mainCharHEALTH = mainChar.health
            mainCharATTACK = mainChar.attack
            mainCharShield = mainChar.shield
            await message.channel.send("... your stats are " + str(mainCharHEALTH) +" health, " +str(mainCharATTACK) +" attack, and " + str(mainCharShield) + " shield.")

        
            #generate Level 1 Monster!!!
            monsterOneStats = statGenerator(ggoblin_hp, ggoblin_atk, ggoblin_shield)
            monsterOne = ClassType("Green Goblin", monsterOneStats[0], monsterOneStats[1], monsterOneStats[2], 10)

            await message.channel.send("You're checking urself out and then you encounter a gren gobolin he uggo af")
            await message.channel.send("It's stats are " + str(monsterOne.health) +" health, " + str(monsterOne.attack)+" attack, and " + str(monsterOne.shield) + " shield."
            + ". KILL IT!!!")

            #game loop
            while mainCharHEALTH > 0:
                next_msg = await client.wait_for('message', check =  lambda message: mainCharID == message.author.id)

                #If player chooses to attack
                if next_msg.content == "!attack":
                    #Player method onto monsterOne as attack
                    atk_this_turn = mainChar.take_turn(monsterOne, "attack")
                    
                    #Maybe change this into a function that will randomize what the monster does? (Game Logic)
                    opponent_atk = monsterOne.take_turn(mainChar, "attack")


                    await message.channel.send("You did " + str(atk_this_turn) + " damage this turn!")
                    await message.channel.send("The monster has blocked " +str(atk_this_turn) + " damage with it's armor! It has " + str(monsterOne.health) + " health and " + str(monsterOne.current_shield) +
                     " shield remaining.")
                    
                    await message.channel.send("The Monster did " + str(opponent_atk) + " damage this turn!")
                    await message.channel.send("You have " + str(mainChar.health) + " remaining.")

                #If player chooses to defend
                if next_msg.content == "!defend":
                    #Player method onto monsterOne as "defend"
                    shield_this_turn = mainChar.take_turn(monsterOne, "defend")

                    #Maybe change this into a function that will randomize what the monster does? (Game Logic)
                    opponent_atk = monsterOne.take_turn(mainChar, "attack")

                    await message.channel.send("You gained " + str(shield_this_turn) + " shield this turn")

                    await message.channel.send("The Monster did " + str(opponent_atk) + " damage this turn but you managed to block " + str(shield_this_turn) + " of it!")
                    await message.channel.send("You have " + str(mainChar.health) + " remaining.")
                    

                    

                if monsterOne.health <= 0:
                    await message.channel.send("Congratulations, you've slayed the evil uggo green gobo")
                    break
                if mainChar.health <= 0:
                    await message.channel.send("Lmao you died to him you succ")
                    break
                
            



class ClassType:
    #Each ClassType will have a name, health, attack, and shield
    #Health, attack and Shield are pre-determined "ranges" 
    #current_shield starts off as 0 for everybody
    def __init__(self, name, health, attack, shield, current_shield = 0):
        self.name = name
        self.health = health
        self.attack = attack
        self.shield = shield
        self.current_shield = current_shield

    #turn based combat
    def take_turn(self, opponent, action):
        #self is the either the human or computer (depends on who's turn it is)
        #opponent is opposite of the human or computer
        #action is either "attack" or "defend"

        #Defining functionality with attacking
        def do_attack():
            points = random.randint(0, self.attack)
            init_points = points

            #if there's a shield, break the shield first and then hit the health with remaining hitpoints

            if opponent.current_shield >= 0:
                before_hit = opponent.current_shield
                opponent.current_shield -= points

                #Can't have less than 0 shield
                if opponent.current_shield <= 0:
                    opponent.current_shield = 0
                
            #update points with the remaining points after shield break
            points = points - before_hit

            #if there are any more points remaining, attack their health
            if points >= 1:
                opponent.health -= points
            #return initial hitpoints assigned earlier for commentary
            return init_points

        def do_defend():
            points = random.randint(0, self.shield)
            self.current_shield += points
            return points

        
        #Running the appropriate function based on the input
        if action == "attack":
            return do_attack()
        elif action == "defend":
            return do_defend()

        return


def statGenerator(health, atk, shield):
    f_health = random.randint(health[0],health[1])
    f_atk = random.randint(atk[0], atk[1])
    f_shield = random.randint(shield[0],shield[1])
    return f_health, f_atk, f_shield


warrior_hp = [50,75]
warrior_atk = [5,12]
warrior_shield = [3,6]

mage_hp = [40,60]
mage_atk = [7,16]
mage_shield = [1,4]

ggoblin_hp = [10,20]
ggoblin_atk = [3,9]
ggoblin_shield = [1,5]


client = MyClient()
client.run('NzgzMTM3NjAyNTc5NTk1MzA0.X8WXug.eGy4dggf3eM5Wik7XU_ZBfnsd14')