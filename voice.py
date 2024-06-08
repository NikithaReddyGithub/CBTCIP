import sounddevice as sd
import wavio

def record_voice(duration, filename):
    # Set parameters for recording
    fs = 44100  # Sample rate
    channels = 2  # Number of audio channels (stereo)
    
    # Record audio
    print("Recording...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=channels, dtype='int16')
    sd.wait()  # Wait until recording is finished
    
    # Save the recorded audio to a WAV file
    print("Saving recorded audio to", filename)
    wavio.write(filename, recording, fs, sampwidth=2)

if __name__ == "__main__":
    duration = 5  # Recording duration in seconds
    filename = "recorded_voice.wav"  # Name of the output WAV file
    record_voice(duration, filename)
    print("Recording completed!")
