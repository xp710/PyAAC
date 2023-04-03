import os
import readline


def Help(variables, commands):
    for k in commandList:
        print(k, commandList[k][1])


def Exit(variables, commands):
    variables['running'] = False


def Voice(variables, commands):
    if len(commands) > 1:
        variables['engine'].setProperty('voice', commands[1])
    else:
        for v in variables['voices']:
            print(v.id)

def Repeat(variables, commands):
    variables['engine'].say(variables['lastSentence'])
    variables['engine'].runAndWait()


def Speed(variables, commands):
    if len(commands) > 1:
        variables['engine'].setProperty('rate', int(commands[1]))
        variables['engine'].runAndWait()
    else:
        print(variables['engine'].getProperty('rate'))


def ClearScreen(variables, commands):
    os.system('clear')


commandList = {
    '/h': (Help, 'Help'),
    '/x': (Exit, 'Exit'),
    '/r': (Repeat, 'Repeat last sentence'),
    '/v': (Voice, 'List or change voices'),
    '/s': (Speed, 'Display or change talking speed'),
    '/c': (ClearScreen, 'Clear screen'),
}