import os

def rename_images_by_filename(folder_path):
    """
    Renames images in a folder sequentially based on their original filenames.

    Args:
        folder_path: Path to the folder containing the images.
    """

    images = []
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            images.append(filename)

    # Sort images alphabetically
    images.sort()

    # Rename images sequentially
    for i, filename in enumerate(images):
        new_filename = f"image_{i+1:04d}{os.path.splitext(filename)[1]}"  # Pad with zeros
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_filename)
        os.rename(old_path, new_path)

if __name__ == "__main__":
    folder_path = input("Enter the path to the folder: ")
    rename_images_by_filename(folder_path)
    print("Renaming completed.")