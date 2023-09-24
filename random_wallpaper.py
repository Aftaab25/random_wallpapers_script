# importing wallpapers
import random
import ctypes

# wn: wallpaper number
wn = random.randint(0, 20)

# print(wn)

path = "C:\\Users\\aftaa\\Pictures\\Wallpapers\\Wallpaper_" + str(wn) + ".jpg"
# print(path)

# Change Wallpaper
ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 3)