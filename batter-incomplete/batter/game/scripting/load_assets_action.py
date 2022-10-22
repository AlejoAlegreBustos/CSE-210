from game.scripting.action import Action
import pathlib


class LoadAssetsAction(Action):


    def __init__(self, audio_service, video_service):
        self._audio_service = audio_service
        self._video_service = video_service


    def execute(self, cast, script, callback):
        # path=pathlib.Path(__file__)
        path= r"C:\Users\Alejo Alegre Bustos\Desktop\BYU\CSE-210\batter-incomplete\batter\assets"
        self._audio_service.load_sounds( path + r"\sounds")
        self._video_service.load_fonts(path + r"\fonts")
        self._video_service.load_images(path + r"\images")
        

