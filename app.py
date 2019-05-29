import os

from upload.Uploader import Uploader


def reload_static_site():
    items = [
        "index.html",
        "refresh.js"
    ]
    bucket_name = "wmorgan85-iot-dashboard"
    path = os.path.dirname(__file__)
    file_paths = [os.path.join(path, "res", "static", item) for item in items]
    u = Uploader()

    for i in range(len(items)):
        u.upload_file(file_paths[i], bucket_name, items[i], show_progress=True)
        print(".")


if __name__ == "__main__":
    reload_static_site()
