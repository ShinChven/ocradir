#!/usr/bin/env python3

# Import necessary libraries
import os
import argparse
from PIL import Image, ImageFile
import pytesseract

def is_valid_image(file_path):
    """
    Check if a given file is a valid image.

    Parameters:
    - file_path (str): Path to the file to check.

    Returns:
    - bool: True if valid image, False otherwise.
    """
    try:
        # Open the file in binary read mode
        with open(file_path, 'rb') as f:
            # Create an image parser from Pillow
            img_parser = ImageFile.Parser()
            
            while True:
                # Read the file in chunks
                chunk = f.read(1024)
                # If we've reached the end of the file, stop reading
                if not chunk:
                    break
                # Feed the chunk into the image parser
                img_parser.feed(chunk)
                # If a valid image is detected by the parser, return True
                if img_parser.image:
                    return True
            # If no valid image is detected, return False
            return False
    except Exception as e:
        # If any errors occur, print the error and return False
        print(f"Error validating {file_path}: {str(e)}")
        return False

def ocr_image_to_md(input_folder, language='chi_sim'):
    """
    Perform OCR on all valid images in the given directory and save the results as .md files.

    Parameters:
    - input_folder (str): Directory containing the images.
    - language (str): Language for OCR (default is Simplified Chinese 'chi_sim').
    """
    # Custom configuration for Tesseract OCR
    custom_config = r'--oem 3 --psm 6'
    
    # Iterate over all files in the directory
    for filename in os.listdir(input_folder):
        # Only process image files with specific extensions
        if filename.endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
            file_path = os.path.join(input_folder, filename)
            
            # If the image is not valid, skip processing it
            if not is_valid_image(file_path):
                print(f"Skipping invalid image {filename}")
                continue
            
            try:
                # Open the image and convert it to RGB mode (if not already in RGB)
                image = Image.open(file_path).convert('RGB')
                # Perform OCR on the image
                text = pytesseract.image_to_string(image, lang=language, config=custom_config)
                
                # Save the OCR output to a .md file with the same name as the image
                md_filename = os.path.splitext(filename)[0] + '.md'
                with open(os.path.join(input_folder, md_filename), 'w') as md_file:
                    md_file.write(text)
            except pytesseract.pytesseract.TesseractError as e:
                # Print errors related to Tesseract
                print(f"Error processing {filename}: {e}")
            except Exception as e:
                # Print any other unexpected errors
                print(f"Unexpected error processing {filename}: {e}")

def main():
    """
    Main function to parse command line arguments and start the OCR process.
    """
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Perform OCR on all images in a directory and save to .md files.")
    parser.add_argument("input_folder", help="Path to the directory containing the images to be processed.")
    parser.add_argument("-l", "--language", choices=['chi_sim', 'chi_tra'], default='chi_sim', help="Language for OCR ('chi_sim' for Simplified Chinese, 'chi_tra' for Traditional Chinese). Default is 'chi_sim'.")
    args = parser.parse_args()

    # Start the OCR process with the provided arguments
    ocr_image_to_md(args.input_folder, language=args.language)

if __name__ == "__main__":
    # If this script is executed directly, run the main function
    main()
