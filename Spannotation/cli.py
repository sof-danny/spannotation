from Spannotation.mask_generator import MaskGenerator

def process_single_image(generator):
    image_path = input("Enter the path to your image: ")
    save_path = input("Enter the path to save the mask: ")
    generator.process_image(image_path, save_path)
    print("Image processing complete. Mask saved.")

def process_image_folder(generator):
    folder_path = input("Enter the path to your images folder: ")
    save_path = input("Enter the path to save masks: ")
    generator.process_folder(folder_path, save_path)
    print("Folder processing complete. Masks saved.")

def main():
    generator = MaskGenerator()
    while True: 
        choice = input("Do you want to process a single image (1) or a folder (2)? [1/2]: ")

        if choice == '1':
            process_single_image(generator)
            break  
        elif choice == '2':
            process_image_folder(generator)
            break 
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
