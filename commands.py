import os


class Command():
    def __init__(self, name, helpText):
        self.name = name
        self.helpText = helpText

    def do(self, variables, commands):
        pass


class Help(Command):
    def __init__(self):
        Command.__init__(self, 'Help', 'Syntax: "/h [command]"')

    def do(self, variables, commands):
        if len(commands) > 1:
            print(commandList[commands[1]].helpText)
        else:
            for k in commandList:
                print(k, commandList[k].name)


class Exit(Command):
    def __init__(self):
        Command.__init__(self, 'Exit', 'Syntax: "/x"')

    def do(self, variables, commands):
        variables['running'] = False


class Voice(Command):
    def __init__(self):
        Command.__init__(self, 'Voice', 'Syntax: "/v [voice]"\n'
                                        'Syntax for [voice]: "accent+voice" e.g. "english-us+f3"')

    def do(self, variables, commands):
        if len(commands) > 1:
            variables['engine'].setProperty('voice', commands[1])
        else:
            for v in variables['voices']:
                print(v.id)


class Repeat(Command):
    def __init__(self):
        Command.__init__(self, 'Repeat', 'Repeats the last sentence.')

    def do(self, variables, commands):
        variables['engine'].say(variables['lastSentence'])
        variables['engine'].runAndWait()


class Speed(Command):
    def __init__(self):
        Command.__init__(self, 'Speed', 'Display or change speed.\n'
                                        'Syntax: "/s [speed]"')

    def do(self, variables, commands):
        if len(commands) > 1:
            variables['engine'].setProperty('rate', int(commands[1]))
            variables['engine'].runAndWait()
        else:
            print(variables['engine'].getProperty('rate'))


class ClearScreen(Command):
    def __init__(self):
        Command.__init__(self, 'Clear Screen', 'Clears the screen.\n'
                                               'Syntax: "/c"')

    def do(self, variables, commands):
        os.system('clear')


commandList = {
    '/h': Help(),
    '/x': Exit(),
    '/r': Repeat(),
    '/v': Voice(),
    '/s': Speed(),
    '/c': ClearScreen(),
}
