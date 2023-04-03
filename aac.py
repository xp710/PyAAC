import readline

from commands import commandList


def Initialize(variables):
    variables['engine'].setProperty('voice', 'english-us+klatt')
    variables['engine'].setProperty('rate', 160)
    variables['engine'].runAndWait()
    print('Welcome to PyAAC, if you need help, type /h')


def GetInput(variables):
    toSay = input('> ') or ' '
    if toSay[0] == '/':
        commands = toSay.split(' ')
        try:
            commandList[commands[0]].do(variables, commands)
        except KeyError:
            print('Invalid command. Type "/h" for help.')
    else:
        variables['lastSentence'] = toSay
        variables['engine'].say(toSay)
        variables['engine'].runAndWait()
