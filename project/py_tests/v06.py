from project.lib.audio_notification import Audio_Notification
from time import sleep, time

audio = Audio_Notification(27, True)

print("testing beep() method")
audio.beep()
sleep(1)