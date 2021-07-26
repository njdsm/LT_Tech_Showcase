#!/usr/bin/env python3

import urllib.request, json


class PhotoAlbum:
    def __init__(self):
        self.data = []
        try:
            with urllib.request.urlopen("https://jsonplaceholder.typicode.com/photos") as url:
                self.data = json.loads(url.read().decode())
        except:
            user_input = input("Something went wrong getting the data. Would you still like to continue? Y/N")

    def run(self):
        try:
            print(" > photo-album " + "1")
            current_album = 1
            for x in self.data:
                if current_album != x.get('albumId'):
                    print("\n > photo-album " + str(x.get('albumId')) + "\n")
                current_album = x.get('albumId')
                print("[" + str(x.get('id')) + "]" + " " + x.get('title'))
            return self.data
        except:
            user_input = input("Something went wrong getting the data. Would you still like to continue? Y/N")
            if user_input == "Y" or user_input == "y":
                return self.data
            else:
                exit()

    def run_interactive(self, data):
        active = True
        while active:
            user_option = self.display_menu()
            if user_option == 1:
                self.get_by_album_id(data)
            elif user_option == 2:
                self.get_by_image_id(data)
            elif user_option == 3:
                print("Goodbye!")
                active = False
            else:
                print("Not a valid option try again.")
                return self.run_interactive(data)

    def display_menu(self):
        print("The data is above if you need to see it feel free to scroll up.")
        print("What would you like to do?")
        print("1: View list of images from a specific album?")
        print("2: View details of a specific image by id?")
        print("3: Exit the program.")
        user_input = self.try_parse_int(input("\n" + ": "))
        validate_user_selection = self.validate_main_menu(user_input)
        return validate_user_selection[1]

    def validate_main_menu(self, user_input):
        """Validation function that checks if 'user_input' argument is an int 1-3."""
        switcher = {
            1: (True, 1),
            2: (True, 2),
            3: (True, 3),
        }
        return switcher.get(user_input, (False, None))

    def try_parse_int(self, value):
        """Attempts to parse a string into an integer, returns 0 if unable to parse."""
        try:
            return int(value)
        except:
            return 0

    def get_by_album_id(self, data):
        try:
            user_input = self.try_parse_int(input("What is the album id you want to see?\n: "))
            for x in data:
                if user_input == x.get('albumId'):
                    print("[" + str(x.get('id')) + "]" + " " + x.get('title'))
        except:
            print("No album matching that id!")

    def get_by_image_id(self, data):
        try:
            user_input = self.try_parse_int(input("What is the image id you want to see?" + "\n: "))
            if user_input == 0:
                print("Not a valid number.")
            else:
                not_found = True
                for x in data:
                    if user_input == x.get('id'):
                        not_found = False
                        print("Album: " + "[" + str(x.get('albumId')) + "]")
                        print("Title: " + x.get('title'))
                        print("Url: " + x.get('url'))
                        print("Thumbnail: " + x.get('thumbnailUrl'))
                if not_found:
                    print("No image matching that Id.")
        except:
            print("No image matching that id!")


