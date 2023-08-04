import random

working = True

while working == True:
    userResponse = input("You: ")

    #list of userGreetings to check if any input has this in the list then the bot will respond with a greeting
    userGreetings = ["Hi!", "hi", "Hello!", "hello", "Sup!", "sup", "Wassup!", "wassup", "What's Up!", "What's up!", "what's up!", "whats up!", "Whats up!", "whats up",
    "what's up"]

    #responses for greetings from bot
    botGreetings = ["Hi!", "Hello!", "Sup", "What's Up!"]

    #if function to check if userGreetings input is inside of list and then give out a response from the bot
    if userResponse in userGreetings:
        randomGreeting = random.choice(botGreetings)
        print("Bot: " + randomGreeting)

    #list of userAdvice to check if any input has this in the list then the bot will respond with botAdvice
    userAdvice = ["advice", "help", "guidance", "pointers", "I need help with exercising", "I need adive on what workouts to do", "I need some pointers"
    "Can you give me some guidance?"]

    #responses for asking for help/advice/guidance
    botAdivce = ["Let me help!", "I can help!", "I'd love to help", "Let's work on it together", "I think I know a few things", 
    "I can give a few pointers", "Sure, no problem!"]

    #if function to check if userAdvice input is inside of list and then give out a response from the bot
    if userResponse in userAdvice:
        randomAdvice = random.choice(botAdivce)
        print("Bot: " + randomAdvice)

    #userBack
    userBack = ["back exercises", "back workout", "back"]

    #list of botBack for back exercises responses
    botBack = ["You can do some one-arm dumbbell rows", "You can do some bent-over rows", "You can do pull-ups", "You can do seated cable rows",
    "You can do some pull-downs", "If you want more of a lower back exercise you can do back extensions", "You can do reverse flyes",
    "You can also do straight-arm pulldowns"]

    #if function for back
    if userResponse in userBack:
        randomBack = random.choice(botBack)
        print("Bot: " + randomBack)

    #userChest
    userChest = ["chest exercises", "chest workout", "chest"]

    #list of botChest for chest exercises responses
    botChest = ["Pushups are always a great way to go!", "You can do a bench press", "You can do an incline bench press", "You can do a decline bench press",
    "How about some cable chest flys?", "You can workout your chest indirectly through triceps dips"]

    #if function for chest
    if userResponse in userChest:
        randomChest = random.choice(botChest)
        print("Bot: " + randomChest)

    #userLegs
    userLegs = ["legs exercises", "leg exercises", "legs workout", "leg workout", "legs", "leg"]

    #list of botLegs for leg exercises responses
    botLegs = ["A great leg exercise is squats", "A good variation of squats is split squats", "A good variation of squats is bulgarian squats", 
    "Never say no to weighted squats", "A leg extension will for sure get your legs worked out", "A leg press is a great machine variant of squats"]

    #if function for legs
    if userResponse in userLegs:
        randomLegs = random.choice(botLegs)
        print("Bot: " + randomLegs)

    #userBiceps
    userBiceps = ["biceps exercises", "biceps workout", "biceps", "bicep", "bicep workout", "bicep exercises", "biceps exercise", "bicep exercise"]

    #list of botBiceps for biceps exercises responses
    botBiceps = ["I recommend bicep curls!", "Good ol' bicep curls", "If you want the outer part of your biceps I would recommend hammer curls"]

    #if function for biceps
    if userResponse in userBiceps:
        randomBiceps = random.choice(botBiceps)
        print("Bot: " + randomBiceps)

    userTriceps = ["triceps exercises", "triceps workout", "triceps", "tricep", "tricep workout", "tricep exercises", "triceps exercise", "tricep exercise"]

    #list of botTriceps for triceps exercises responses
    botTriceps = ["A simple triceps exercise is the overhead triceps extension", "Can't really go wrong with triceps push-downs", "What about doing some dips?"]

    #if function for triceps
    if userResponse in userTriceps:
        randomTriceps = random.choice(botTriceps)
        print("Bot: " + randomTriceps)

    userEnd = ["Stop!", "stop", "close", "finish", "finito", "hasta lavista baby", "adios", "ba bye", "bye", "gtg", "end"]

    if userResponse in userEnd:
        working = False

