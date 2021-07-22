from photos import Photos
import urllib.request, json


class PhotoAlbum:

    def __init__(self):
        pass

    def run(self):
        with urllib.request.urlopen("https://jsonplaceholder.typicode.com/photos") as url:
            data = json.loads(url.read().decode())
            will_proceed = True
            while will_proceed:
                user_option = input("Type the album number you would like to view contents of: ")
                output_dict = [x for x in data if x['albumId'] == int(user_option)]
                print(" > photo-album " + str(user_option))
                for x in output_dict:
                    print("[" + str(x.get('id')) + "]" + " " + x.get('title'))
                will_proceed = False

