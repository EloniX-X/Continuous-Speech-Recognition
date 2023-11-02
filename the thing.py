import speech_recognition as sr


r = sr.Recognizer()

def recognize_speech_from_mic():
    
    with sr.Microphone() as source:
        print("Calibrating for ambient noise. Please wait...")
        r.adjust_for_ambient_noise(source, duration=2)
        print("Calibration complete. You may start speaking.")

        while True:  
            try:
                print("Listening...")
                audio = r.listen(source, timeout=1, phrase_time_limit=5)  
                print("Processing...")

                
                text = r.recognize_google(audio)
                print(f"You said: {text}")

            except sr.WaitTimeoutError:
               
                print("No speech detected. Please speak again.")
                continue
            except sr.UnknownValueError:
             
                print("Could not understand the audio. Please speak again.")
                continue
            except sr.RequestError as e:
             
                print(f"Could not request results; {e}")
                continue
            except KeyboardInterrupt:
                
                print("Program terminated by user.")
                break


recognize_speech_from_mic()
