#!/usr/bin/env python3
from photo_album import PhotoAlbum

if __name__ == '__main__':
    album = PhotoAlbum()
    data = album.run()
    album.run_interactive(data)
