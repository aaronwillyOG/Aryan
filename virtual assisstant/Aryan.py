from instruction import *

def main():
    wakeword = wake_word()
    if "aryan" in wakeword:
        talk(gr.rg())
    
    exit_program = False
    
    while not exit_program :
        exit_program = play_Aryan()

if __name__ == '__main__':
    main()