class Camera:
    def take_photo(self):
        print("Photo taken!")
class MusicPlayer:
    def play_music(self):
        print("Playing music!")

class Smartphone(Camera, MusicPlayer):
    pass

smartphone = Smartphone()
smartphone.take_photo()
smartphone.play_music()
