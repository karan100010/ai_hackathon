import astrisk
import telegram
import openai
import configparser
import speech_recognition as sr

# Set up your OpenAI API key


# 1. pickup the call
# 2. play the audio file
# 3. hangup the call
# 4. send the voice message to telegram
# 5. get response from telegram
# 6. call back the number and play the response to the user

class Workflow():

    def __init__(self):
        self.astrisk = astrisk.Astrisk()
        self.telegram = telegram.Telegram()
        #read the config file config.conf using config parser and wrtie the values to the variable api_key
        config = configparser.ConfigParser()
        config.read('config.conf')
        self.openai_key = config['api_key']
        self.openai_key=openai.api_key(self.openai_key)
        self.transcriber=sr.Recognizer()
    def call(self):
        self.astrisk.pickup()
        self.astrisk.play_audio("sound/hello.wav")
        self.astrisk.record_file("sound/record.wav")
        self.astrisk.play_audio("sound/goodbye.wav")
        self.astrisk.hangup()
        x=self.transcriber("sound/record.wav")
        added_prompt="you are a responder to a grivanace call and the caller has recorded a message for you. User: "
        end_prompt=".According to this message which of the four catagories describe the message best? catagories are: 1.Road related 2.Water related 3.Electricity related 4.Sanitationrelated 5.Other resposnd in the end of the message with cat: <catagory number>"
        print(x)
        response = openai.Completion.create(
            engine="davinci",
            prompt=added_prompt+" "+x+end_prompt,
            max_tokens=500
        )
        print(response.choices[0].text.strip())

if __name__ == "__main__":
    workflow = Workflow()
    workflow.call()






