import speech_recognition as speak
import pyttsx3

# Initialise the bot for speech recognition
listening_bot = speak.Recognizer()

# Initialising the bot for text to speech conversion
reading_bot = pyttsx3.init()

# Setting the properties for reading_bot
voices = reading_bot.getProperty('voices')
# male voice - 0 ; female voice - 1
reading_bot.setProperty('voice', voices[1].id)
# reading speed
reading_bot.setProperty('rate', 130)


# Function to convert speech into text
def speech_to_text():
    # loop to listen for speech
    while True:
        try:
            # Accessing the microphone for getting input
            with speak.Microphone() as mic:
                # Prepare recognizer to get the input
                listening_bot.adjust_for_ambient_noise(mic, duration=0.2)

                # recognizer listening for user's input
                audio = listening_bot.listen(mic)

                # Use the Google recognize module to recognize audio
                heard = listening_bot.recognize_google(audio)

                return heard

        except speak.RequestError as error:
            print("Could not request response: {0}".format(error))
        except speak.UnknownValueError:
            print("Unknown Error occurred")

    return


# Function to convert text into speech
def text_to_speech(text):
    # read the text
    reading_bot.say(text)
    reading_bot.runAndWait()


print("Speak I'm listening...")

while True:
    # Function call for speech to text conversion
    text = speech_to_text()

    # Function call for text to speech Conversion
    text_to_speech(text)

    # This print statement will verify what the recognizer heard
    print("I heard: "+text)

    # Condition statement for termination
    if text == "all done":
        break


