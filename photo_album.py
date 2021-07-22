import urllib.request, json


class PhotoAlbum:

    def run(self):
        with urllib.request.urlopen("https://jsonplaceholder.typicode.com/photos") as url:
            data = json.loads(url.read().decode())
            print(" > photo-album " + "1")
            current_album = 1
            for x in data:
                if current_album != x.get('albumId'):
                    print("\n > photo-album " + str(x.get('albumId')) + "\n")
                current_album = x.get('albumId')
                print("[" + str(x.get('id')) + "]" + " " + x.get('title'))
