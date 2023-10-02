import subprocess
import os
import random

def get_gnome_color_scheme():
    try:
        # Use the gsettings command to get the current GNOME theme
        theme_output = subprocess.check_output(["gsettings", "get", "org.gnome.desktop.interface", "gtk-theme"]).decode("utf-8").strip()
        print(theme_output)
        # Check if the theme contains "dark"
        if "dark" in theme_output.lower():
            print("here")
            return "dark"
        else:
            return "light"
    except subprocess.CalledProcessError:
        # Handle any errors or defaults here
        return "light"  # Default to light if there's an error

def change_wallpaper_from_folder(folder_path):
    # Get the current GNOME color scheme (light or dark)
    gnome_color_scheme = get_gnome_color_scheme()

    # Get a list of image files in the specified folder
    image_files = [f for f in os.listdir(folder_path) if f.endswith((".jpg", ".jpeg", ".png", ".gif", ".bmp"))]

    if not image_files:
        print("No valid image files found in the folder.")
        return

    # Choose a random image from the list
    random_wallpaper = random.choice(image_files)
    wallpaper_path = os.path.join(folder_path, random_wallpaper)

    # Use the gsettings command to set the wallpaper based on the color scheme
    if gnome_color_scheme == "dark":
        command_uri = ["gsettings", "set", "org.gnome.desktop.background", "picture-uri-dark", f"file://{wallpaper_path}"]
    else:
        command_uri = ["gsettings", "set", "org.gnome.desktop.background", "picture-uri", f"file://{wallpaper_path}"]

    print(gnome_color_scheme)

    try:
        subprocess.run(command_uri, check=True)
        print(f"Wallpaper changed to {random_wallpaper} successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error changing wallpaper: {e}")

if __name__ == "__main__":
    # Specify the path to the folder containing wallpapers
    wallpaper_folder = "/home/batman/Pictures/WallPapers"

    # Call the function to change the wallpaper
    change_wallpaper_from_folder(wallpaper_folder)
