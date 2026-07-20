from core.config import Config
from core.command_router import CommandRouter

class Jarvis:
    def __init__(self):
        self.router = CommandRouter()

        self.router.register("help", self.show_help)
        self.router.register("version", self.show_version)

    def show_help(self):
        print("\nAvailable Commands")
        print("------------------")
        print("help     - Show available commands")
        print("version  - Show Jarvis version")
        print("about    - About Jarvis")
        print("exit     - Exit Jarvis\n")

    def show_version(self):
        print(f"\n{Config.APP_NAME}")
        print(f"Version : {Config.VERSION}\n")


    def start(self):
        print("=" * 50)
        print(f"Welcome to {Config.APP_NAME}")
        print(f"Version : {Config.VERSION}")
        print(f"Author  : {Config.AUTHOR}")
        print("=" * 50)

        print("\nType 'help' to see available commands.\n")

        while True:
            command = input("Jarvis > ").lower().strip()

            if command == "exit":
                print("Goodbye!")
                break

            self.router.execute(command)