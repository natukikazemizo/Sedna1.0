bl_info = {
    "name": "Hello World",
    "author": "Natukikazemizo",
    "version": (1, 0),
    "blender": (2, 81, 0),
    "location": "",
    "description": "Sample to try enabling and disabling add-ons",
    "warning": "",
    "support": "TESTING",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Object"
}


def register():
    print("Add-on Hello World has been activated.")


def unregister():
    print("Add-on Hello World has been disabled.")


if __name__ == "__main__":
    register()
