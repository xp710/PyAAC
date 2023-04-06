# TODO: add saving settings
import aac
import pyttsx3

variables = {
    'running': True,
    'engine': pyttsx3.init(),
    'lastSentence': '',
    'replacements': {},
}

aac.Initialize(variables)

while variables['running']:
    aac.GetInput(variables)
