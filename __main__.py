import pyttsx3
import aac

variables = {
    'running': True,
    'engine': pyttsx3.init(),
    'lastSentence': '',
}
variables['voices'] = variables['engine'].getProperty('voices')
variables['rate'] = variables['engine'].getProperty('rate')

aac.Initialize(variables)

while variables['running']:
    aac.GetInput(variables)
