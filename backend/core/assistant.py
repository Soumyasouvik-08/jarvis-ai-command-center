from core.config import Config


class Jarvis:
    def start(self):
        print("=" * 50)
        print(f"Welcome to {Config.APP_NAME}")
        print(f"Version : {Config.VERSION}")
        print(f"Author  : {Config.AUTHOR}")
        print("=" * 50)
        print("Jarvis Kernel is Online.")