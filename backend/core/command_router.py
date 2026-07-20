class CommandRouter:

    def __init__(self):
        self.commands = {}
    def register(self, command_name, function):
        self.commands[command_name] = function   
    def execute(self, command_name):
        if command_name in self.commands:
            self.commands[command_name]()
        else:
            print("Unknown command. Type 'help' to see available commands.")