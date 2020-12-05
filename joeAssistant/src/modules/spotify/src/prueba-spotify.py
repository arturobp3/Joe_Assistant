import os
import sys

config_name = 'Spotify.exe'

# determine if application is a script file or frozen exe
'''if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
elif __file__:
    application_path = os.path.dirname(__file__)

config_path = os.path.join(application_path, config_name)'''

print("Hola")
print(sys.executable)