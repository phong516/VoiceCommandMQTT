import numpy as np

from tensorflow.keras import models
import tensorflow as tf
from IPython import display

from recording_helper import record_audio, terminate
from tf_helper import preprocess_audiobuffer

# !! Modify this in the correct order
commands = ['Cham', 'Dung', 'Nhanh', 'Lui', 'Phai', 'Tien', 'Trai']

loaded_model = models.load_model("saved_model")

def predict_mic():
    audio = record_audio()    
    spec = preprocess_audiobuffer(audio)
    prediction = loaded_model(spec)
    max_value = np.max(tf.nn.softmax(prediction[0]))
    
    label_pred = np.argmax(prediction, axis=1)
    command = commands[label_pred[0]]
    # print("Predicted label:", command) if max_value > 0.7 else print("No command detected")
    print("Predicted label:", command)
    print("Accuracy: ", max_value)
    return command

if __name__ == "__main__":
    # from turtle_helper import move_turtle
    while True:
        per = input("Press enter to predict")
        command = predict_mic()
        # move_turtle(command)
        # if command == "stop":
        #     terminate()
        #     break