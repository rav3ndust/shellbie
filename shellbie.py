import os
import subprocess
from gtts import gTTS as speech
# - - - Variables - - -
asst = "Shellbie"
options = [
        "Get Weather",
        "Get News",
        "Update the System",
        "Play Some Music",
        "Shut Down or Reboot Computer"
    ]
# - - - Functions - - -
def speak(content):
    tts = speech(text=content, lang="en")
    tts.save("output.mp3")
    os.system("mpg123 -q output.mp3")
    # clean up the file
    os.system("rm output.mp3")
def give_options():
    v1 = "Here are some options for you to choose from."
    v2 = "Please make a selection."
    speak(v1)
    for option in options:
        speak(option)
    speak(v2)
def greet():
    system_user = os.popen("echo $USER").read()
    current_date = os.popen("date").read()
    system_hostname = os.popen("echo $HOSTNAME").read()
    speak(f'Hi, {system_user}! My name is {asst}, running on {system_hostname}.')
    speak(f'The current date and time is {current_date}.')
    speak("What can I do for you today?")
    '''
    TODO: 
    - user should be able to make a selection and shellbie will act accordingly.
    - for example, if a user asks for the weather, shellbie should fetch it and speak it aloud for the relevant area.
    '''
# program start
greet()
give_options()
