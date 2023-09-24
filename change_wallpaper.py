import subprocess
import os
import random

def change_wallpaper_from_folder(folder_path):
    # Get a list of image files in the specified folder
    image_files = [f for f in os.listdir(folder_path) if f.endswith((".jpg", ".jpeg", ".png", ".gif", ".bmp"))]

    if not image_files:
        print("No valid image files found in the folder.")
        return

    # Choose a random image from the list
    random_wallpaper = random.choice(image_files)
    wallpaper_path = os.path.join(folder_path, random_wallpaper)

    # Use the gsettings command to set the wallpaper
    command = ["gsettings", "set", "org.gnome.desktop.background", "picture-uri", f"file://{wallpaper_path}"]

    try:
        subprocess.run(command, check=True)
        print(f"Wallpaper changed to {random_wallpaper} successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error changing wallpaper: {e}")

if __name__ == "__main__":
    # Specify the path to the folder containing wallpapers
    wallpaper_folder = "/home/batman/Pictures/WallPapers"

    # Call the function to change the wallpaper
    change_wallpaper_from_folder(wallpaper_folder)
