import os

def main():
	folder = "C:\\Users\\aftaa\\Pictures\\Wallpapers"
	destination = "C:\\Users\\aftaa\\Pictures\\Wallpapers"

	for count, filename in enumerate(os.listdir(folder)):
		dst = "Wallpaper_" + str(count) + ".jpg"

		#rename all the files

		os.rename(os.path.join(folder, filename), os.path.join(destination, dst))

# Driver Code
if __name__ == '__main__':
	main()