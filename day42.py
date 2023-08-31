#Task 1: Spelling Checker
from textblob import TextBlob
print("\n*******************Task 1: Spelling Checker*******************")
def spelling_checker():
    while True:
        word = input('Enter a word : ')
        cword = TextBlob(word).correct()
        
        if word == cword:
            return f"Correct Word"
        
        elif word != cword:
            question = input(f"Did you mean {cword} ?\nType yes/no:")
            if question == 'yes':
                return cword
            else:
                print('Please try again')

return_spell = spelling_checker()
print(return_spell)


#Task 2:  Create an Alarm clock
print("\n*******************Task 2:  Create an Alarm clock*******************")
import winsound
import datetime

def set_alarm():
    hour = input("Enter hour(01-12): ")
    minute = input("Enter minute(00-59): ")
    zone = input("Enter AM/PM: ")
    alarm_time = hour + ':' + minute + " " + zone
    print(f"Alarm will go off at {alarm_time}")
    
    while True:
        cur_time = datetime.datetime.now().strftime("%I:%M %p")
        if cur_time == alarm_time:
            for i in range(3):
                print("Wake UP")
                winsound.PlaySound("SystemExit",winsound.SND_ALIAS)
            break
set_alarm()