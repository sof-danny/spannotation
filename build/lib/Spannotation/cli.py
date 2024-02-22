from Spannotation.mask_generator import MaskGenerator

def main():
    folder_path = input("Enter the path to your images folder: ")
    save_path = input("Enter the path to save masks: ")

    generator = MaskGenerator()
    generator.process_folder(folder_path, save_path)

if __name__ == "__main__":
    main()
