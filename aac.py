from commands import commandList

def Initialize(variables):
    commandList['/l'].do(variables, ['/l'])
    variables['engine'].runAndWait()
    commandList['/pl'].do(variables, ['/pl'])
    print('Welcome to PyAAC, if you need help, type /h')


def CheckAndReplace(variables, toSay):
    for w in variables['replacements'].keys():
        if w in toSay:
            toSay = toSay.replace(w, variables['replacements'][w])
    return toSay

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
        toSay = CheckAndReplace(variables, toSay)
        variables['engine'].say(toSay)
        variables['engine'].runAndWait()
