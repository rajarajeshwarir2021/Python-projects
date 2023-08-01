from filestack import Client

API_KEY = "YOUR_API_KEY"


class FileSharer:
    """
    Class to facilitate Cloud based file sharing
    """

    def __init__(self, filepath, api_key=API_KEY):
        self.api_key = api_key
        self.filepath = filepath

    def share(self):
        client = Client(self.api_key)
        new_file_link = client.upload(filepath=self.filepath)
        return new_file_link.url