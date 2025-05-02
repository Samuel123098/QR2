from tkinter import filedialog
from MakingQR import main as MakingQR
import lzma
import shutil
from cryptography.fernet import Fernet


def generate_key():
    key = Fernet.generate_key()
    with open('filekey.key', 'wb') as filekey:
        filekey.write(key)

def load_key():
    with open('filekey.key', 'rb') as filekey:
        key = filekey.read()
    fernet = Fernet(key)
    return(fernet)
def compress_with_lzma(input_file, output_file):
    with open(input_file, 'rb') as f_in:
        with lzma.open(output_file, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    print(f"Compressed to {output_file} using LZMA")


def main():
    file_directory = filedialog.askopenfilename()
    with open(file_directory, 'rb') as file:
        original = file.read()
        fernet = load_key()
        encrypted = fernet.encrypt(original)
        compress_with_lzma(file_directory, 'compressed.zip')

    MakingQR('compressed.zip')

if __name__ == '__main__':
    user_input = input("Would you like to Generate a new key? ").lower
    if user_input == 'yes':
        generate_key()
    main()
