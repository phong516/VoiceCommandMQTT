import numpy as np
from tensorflow.keras import models
import tensorflow as tf

import pyaudio

class VoiceComamnd:
    def __init__(self, model : any):
        self.model = models.load_model(model)
        self.commands = ['Chậm', 'Dừng', 'Nhanh', 'Lùi', 'Phải', 'Tiến', 'Trái']
        self.FRAMES_PER_BUFFER = 3200
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 16000
        self.p = pyaudio.PyAudio()

        seed = 42
        tf.random.set_seed(seed)
        np.random.seed(seed)
    
    def __RecordAudio(self):
        stream = self.p.open(
        format=self.FORMAT,
        channels=self.CHANNELS,
        rate=self.RATE,
        input=True,
        frames_per_buffer=self.FRAMES_PER_BUFFER
    )
        frames = []
        seconds = 1
        for i in range(0, int(self.RATE / self.FRAMES_PER_BUFFER * seconds)):
            data = stream.read(self.FRAMES_PER_BUFFER)
            frames.append(data)

        stream.stop_stream()
        stream.close()
        
        return np.frombuffer(b''.join(frames), dtype=np.int16)
    
    def __TerminateRecord(self):
        self.p.terminate()

    def __GetSpectrogram(self, waveform):
        input_len = 16000
        waveform = waveform[:input_len]
        zero_padding = tf.zeros(
            [16000] - tf.shape(waveform),
            dtype=tf.float32)
        waveform = tf.cast(waveform, dtype=tf.float32)
        equal_length = tf.concat([waveform, zero_padding], 0)
        spectrogram = tf.signal.stft(
            equal_length, frame_length=255, frame_step=128)
        spectrogram = tf.abs(spectrogram)
        spectrogram = spectrogram[..., tf.newaxis]
        return spectrogram
    
    def __PreprocessAudioBuffer(self, waveform):
        waveform =  waveform / 32768
        waveform = tf.convert_to_tensor(waveform, dtype=tf.float32)
        spectogram = self.__GetSpectrogram(waveform)
        spectogram = tf.expand_dims(spectogram, 0)
        return spectogram
    
    def PredictMic(self):
        audio = self.__RecordAudio()    
        spec = self.__PreprocessAudioBuffer(audio)
        prediction = self.model(spec)
        max_value = np.max(tf.nn.softmax(prediction[0]))
        
        label_pred = np.argmax(prediction, axis=1)
        command = self.commands[label_pred[0]]
        print("Predicted label:", command)
        print("Accuracy: ", max_value)
        return command

