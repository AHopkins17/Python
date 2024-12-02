# File Organizer for Basic File Operations Script
import os

def main():
        # Create folder
        os.mkdir("myfiles")
        # Create subfolders 
        os.mkdir("myfiles/docs")
        os.mkdir("myfiles/images")
        os.mkdir("myfiles/videos")

# Call Main 
if __name__ == "__main__":
    main()   
