from photo_album import PhotoAlbum


def test_has_data():
    photo_album = PhotoAlbum()
    assert len(photo_album.data) != 0


def test_check_data():
    photo_album = PhotoAlbum()
    print(photo_album.data[0])
    assert photo_album.data[0].get('id')
    assert photo_album.data[0].get('albumId')
    assert photo_album.data[0].get('title')
    assert photo_album.data[0].get('url')
    assert photo_album.data[0].get('thumbnailUrl')

