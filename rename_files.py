import os

# Function to rename multiple files
def main():
    path = "C:\\Users\\MrBagel55\\Music\\Desktop\\merhbaa\\database"
    i = 0

    for filename in os.listdir(path):
        pic_path = os.path.join(path, filename)

        if os.path.isdir(pic_path):
            for pic_name in os.listdir(pic_path):
                old_pic_path = os.path.join(pic_path, pic_name)
                new_pic_name = f"{filename}.jpg"
                new_pic_path = os.path.join(pic_path,new_pic_name)
                try:
                    os.rename(old_pic_path, new_pic_path)
                except Exception as e:
                    print(f"Error renaming {old_pic_path}: {e}")
                break
        
# Driver Code
if __name__ == '__main__':
    # Calling main() function
    main()
