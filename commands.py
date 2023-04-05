import os
import json


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
            for v in variables['engine'].getProperty('voices'):
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


class Load(Command):
    def __init__(self):
        Command.__init__(self, 'Load File', 'Loads settings from the save file.')

    def do(self, variables, commands):
        with open('aac/aac.sav') as f:
            settings = f.read().splitlines()
            variables['engine'].setProperty('voice', settings[0])
            variables['engine'].setProperty('rate', int(settings[1]))


class PronunciationSave(Command):
    def __init__(self):
        Command.__init__(self, 'Pronunciation Save', 'Save a pronunciation for a word.\n'
                                                     'Syntax: /ps [word] [pronunciation]')

    def do(self, variables, commands):
        variables['replacements'][commands[1]] = commands[2]
        jsonFile = json.dumps(variables['replacements'])
        with open('aac/replacements.json', '+w') as f:
            f.write(jsonFile)


class PronunciationLoad(Command):
    def __init__(self):
        Command.__init__(self, 'Pronunciation Load', 'Load all pronunciations from file.')

    def do(self, variables, commands):
        with open('aac/replacements.json', '+r') as f:
            variables['replacements'] = json.load(f)

class PronunciationView(Command):
    def __init__(self):
        Command.__init__(self, 'Pronunciation View', 'View all saved pronunciations.')

    def do(self, variables, commands):
        for k in variables['replacements']:
            print(k, variables['replacements'][k])


commandList = {
    '/h': Help(),
    '/x': Exit(),
    '/r': Repeat(),
    '/v': Voice(),
    '/s': Speed(),
    '/c': ClearScreen(),
    '/l': Load(),
    '/ps': PronunciationSave(),
    '/pl': PronunciationLoad(),
    '/pv': PronunciationView(),
}
