import VoiceCommand as vc

ai = vc.VoiceComamnd('saved_model')

while True:
    per = input("Press Enter to start recording")
    ai.PredictMic()