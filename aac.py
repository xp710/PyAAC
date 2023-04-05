from commands import commandList

def Initialize(variables):
    commandList['/l'].do(variables, ['/l'])
    variables['engine'].runAndWait()
    commandList['/pl'].do(variables, ['/pl'])
    print('Welcome to PyAAC, if you need help, type /h')


def CheckAndReplace(variables, toSay):
    for w in variables['replacements'].keys():
        words = toSay.split(' ')
        # words = [w if item == variables['replacements'][w] else item for item in words]
        if w in words:
            for j in range(len(words)):
                if words[j] == w:
                    words[j] = variables['replacements'][w]
        toSay = ' '.join(words)
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
