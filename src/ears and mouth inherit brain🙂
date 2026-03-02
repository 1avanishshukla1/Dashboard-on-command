import pyttsx3
import speech_recognition as sr

class DashboardBot(Bot):
    def __init__(self, api_key, endpoint, dataset_path):
        super().__init__(api_key, endpoint, dataset_path)
        self.recognizer = sr.Recognizer()
        self.tts_engine = pyttsx3.init()

    def speech_to_text(self):
        a = input("Do you want to start the conversation? (yes/no): ")

        if a.lower() == "yes":
            try:
                with sr.Microphone() as source:
                    print("Listening for your command...")
                    audio = self.recognizer.listen(source)
                    user_command = self.recognizer.recognize_google(audio)
                    print(f"You said: {user_command}")
                    return user_command
            except Exception as e:
                print(f"Speech recognition error: {e}")
                return input("Please type your command: ")
        else:
            print("MICROPHONE IS OFF")
            return input("Type your command: ")

    def speak_text(self, text):
        self.tts_engine.say(text)
        self.tts_engine.runAndWait()

    def start_working(self):
        while True:
            user_command = self.speech_to_text()

            if not user_command:
                continue

            if user_command.lower() in ["exit", "quit", "stop"]:
                print("Ending the conversation. Goodbye!")
                break

            response = self.send_message(user_command)

            if "error" in response:
                print(response["error"])
                continue

            bot_reply = response["reply"]

            print(f"Bot: {bot_reply}")

            # IMPORTANT: do NOT execute again (already executed inside send_message)
            # self.execute_code_with_delimiters(bot_reply)

            self.speak_text(bot_reply[:100])
