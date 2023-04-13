import pyttsx3

# Initialize the engine
engine = pyttsx3.init()

# Set properties for the audio file
engine.setProperty('rate', 150)    # Set speaking rate
engine.setProperty('volume', 0.7)  # Set speaking volume

# Convert text to speech
text = "Hello, how are you doing today?" # type any message you want
engine.say(text)

# Save the audio file
engine.save_to_file(text, 'audio_file.mp3')

engine.runAndWait()
