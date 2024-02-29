from lib import *

def play_Aryan():

    instruction = input_instruction()
    print(instruction)
    if "open" in instruction:
        app = instruction.replace('open', " ")
        app = app.replace(" ","")
        talk("opening" + app)
        open(app, match_closest=True)

    elif "close" in instruction:
        app = instruction.replace('close', " ")
        app = app.replace(" ","")
        talk("closing" + app)
        close(app, match_closest=True)
    
    elif "play" in instruction:
        song = instruction.replace('play', " ")
        talk("playing" + song)
        kit.playonyt(song)

    elif ("search" in instruction) or ("google" in instruction):
        if "search" in instruction:
            article = instruction.replace('search', " ")
            talk("searching " + article)
            kit.search(article)

        elif "google" in instruction:
            article = instruction.replace('google', " ")
            talk("searching for " + article + " on google")
            kit.search(article)

    # elif 'email' in instruction:
    #     get_email_info()

    elif 'time' in instruction:
        time = datetime.now().strftime('%I %M %p')
        print("Current Time: " + datetime.now().strftime('%I : %M %p'))
        talk('Current time' + time)

    elif 'date' in instruction:
        date_ = datetime.now().strftime('%d %m %Y')
        my_date = date.today()
        day = calendar.day_name[my_date.weekday()]
        print(day+ ' ' + date_)
        talk("Today is" + day +". "+ date_)

    elif 'how are you' in instruction:
        talk('I am Fine, how about you?')
    
    elif 'what is your name' in instruction:
        talk('I am Aryan, what can i do for you')

    elif 'terminate' in instruction:
        talk('Sure. Have a nice day.')
        return True


    elif ("what is" in instruction) or ("who is" in instruction) or ("provide info on" in instruction) or ("provide info about" in instruction) or ("provide information on") or ("provide information about"):
        if "what is" in instruction:
            article = instruction.replace("what is", "")
            talk("collecting info from the web about" + article)
            info = wp.summary(article, 20)
            print(info)
            talk(info)
        
        elif "who is" in instruction:
            article = instruction.replace("who is", "")
            talk("collecting info from the web regarding" + article)
            info = wp.summary(article, 1)
            print(info)
            talk(info)

        elif "provide info on" in instruction:
            article = instruction.replace('provide info on', " ")
            talk("getting that from the web " + article)
            info = wp.summary(article, 20)
            print(info)
            talk(info)

        elif "provide info about" in instruction:
            article = instruction.replace('provide info about', " ")
            talk("here is what i found " + article)
            info = wp.summary(article, 20)
            print(info)
            talk(info)

        else:
            article = instruction.replace('provide information on', " ")
            talk("here is what i found about " + article +", from the web")
            info = wp.summary(article, 1)
            print(info)
            talk(info)
            
    else:
        talk("Please repeat")