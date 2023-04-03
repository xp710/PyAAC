import readline

from commands import commandList


def Initialize(variables):
    variables['engine'].setProperty('voice', 'english-us+robosoft8')
    variables['engine'].setProperty('rate', 150)
    variables['engine'].runAndWait()


def GetInput(variables):
    toSay = input('> ') or ' '
    if toSay[0] == '/':
        commands = toSay.split(' ')
        try:
            commandList[commands[0]][0](variables, commands)
        except KeyError:
            print('Invalid command. Type "/h" for help.')
    else:
        variables['lastSentence'] = toSay
        variables['engine'].say(toSay)
        variables['engine'].runAndWait()
