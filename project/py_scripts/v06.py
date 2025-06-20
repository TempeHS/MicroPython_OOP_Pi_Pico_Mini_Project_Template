from audio_notification import Audio_Notification
from time import sleep

audio = Audio_Notification(27, True)



print('warning in 3 seconds')
sleep(3)
audio.warning_on()

