# import os

from upload import Uploader


def reload_static_site():
    items = []
    u = Uploader()
    for item in items:
        u.upload_file(item)


if __name__ == "__main__":
    reload_static_site()
