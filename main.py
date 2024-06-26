import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser #for open browser to run youtub etc....
import os



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')#getting details of current voice
print(voices[0].id)#for voice print 
engine.setProperty('voice',voices[0].id)#changing index, changes voices. 1 for female


def speak(audio):
    engine.say(audio)# this use for passing voisc or audio
    engine.runAndWait()#this is use to run or execute our voice 


def wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<=18:
        speak("Good Aftenoon!")
    else:
        speak("Good Evening!")  
    speak("I am jarvis sir . Please tell me how may I help you")      

def takecommand():
    #it takr micro input from user and return string output
    r = sr.Recognizer()#this function use for Recognize audio
    with sr.Microphone() as source:
        print("Listening..........")
        r.pause_threshold = 1 #sometime when we speak i pause suddnly and our line is incomple in that case this function wait for 1sec .
        audio = r.listen(source)

    try:
        print("Recognition.....")
        query = r.recognize_google(audio, language='en-in')

        print(f"User said : {query}\n")
    except Exception as e:
         print("Say that again please.....")
         return "None"
    return query
# def takeCommand():
#     #It takes microphone input from the user and returns string output

#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         r.pause_threshold = 1
#         audio = r.listen(source)
#     try:
#         print("Recognizing...")    
#         query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
#         print(f"User said: {query}\n")  #User query will be printed.

#     except Exception as e:
#         # print(e)    
#         print("Say that again please...")   #Say that again will be printed in case of improper voice 
#         return "None" #None string will be returned
#     return query    
# def sendEmail(to,content):{#using smtp package we can able to send emails with gmail.
    
# }
 

if __name__ == "__main__":# our main function 
    wishMe()
    while True:
        query = takecommand().lower()
     #logic to executing task based on query 
        if 'wikipedia' in query:#this is run due to import wikipedia
            speak('Search wikipedia.....')
            query= query.replace('wikipedia',"")
            results=wikipedia.summary(query,sentences=2)
            speak('According to wikipedia')
            print(results)
            speak(results)
        elif 'open youtube' in query:#this is run due to import webbrowser
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")  
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")    

        elif 'play music' in query:#using import os 
            music_dir='D:\\Videos\\My Music (1)'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir , the time {strtime}")   
        elif 'open code' in query:
            codepath = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        elif 'quit' in query:
            exit();    
        
        # elif 'email to me' in query :
        #     try:
        #         speak("What should I say?")
        #         content = takecommand()
        #         to = "meyouEmail@gmail.com"
        #         speak("Email has been sent!")
        #     except Exception as e:
        #         print(e)
        #         speak("sorrymay friend sumit bahi. I am not able to sent this email.")

