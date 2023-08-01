import time
import webbrowser
from filesharer import FileSharer
from kivy.app import App
from kivy.lang import Builder
from kivy.core.clipboard import Clipboard
from kivy.uix.screenmanager import Screen, ScreenManager

Builder.load_file("frontend.kv")


class CameraScreen(Screen):

    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)
        self.filepath = ""

    def start(self):
        """Starts camera and changes Button text and Camera texture"""
        self.ids.camera.opacity = 1
        self.ids.camera.play = True
        self.ids.camera_button.text = "Stop Camera"
        self.ids.camera.texture = self.ids.camera._camera.texture

    def stop(self):
        """Stops camera and changes Button text"""
        self.ids.camera.opacity = 0
        self.ids.camera.play = False
        self.ids.camera_button.text = "Start Camera"
        self.ids.camera.texture = None

    def capture(self):
        """Creates a filename with the current time, captures
        and saves a photo image under that filename"""
        current_time = time.strftime("%Y%m%d-%H%M%S")
        self.filepath = "images/" + current_time + ".png"
        self.ids.camera.export_to_png(self.filepath)
        self.manager.current = "image_screen"
        self.manager.current_screen.ids.img.source = self.filepath


class ImageScreen(Screen):

    link_message = "Create a link First!"

    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)
        self.url_link = ""

    def create_link(self):
        """Accesses the photo filepath, uploads it to web,
        and inserts the link in the label widget"""
        file_path = App.get_running_app().root.ids.camera_screen.filepath
        #file_sharer = FileSharer(file_path)
        #self.url_link = file_sharer.share()
        self.url_link = file_path
        self.ids.link.text = file_path

    def copy_link(self):
        """Copy the link to clipboard"""
        try:
            Clipboard.copy(self.url_link)
        except:
            self.ids.link.text = self.link_message

    def open_link(self):
        """Open the link in a web browser"""
        try:
            webbrowser.open(self.url_link)
        except:
            self.ids.link.text = self.link_message


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()