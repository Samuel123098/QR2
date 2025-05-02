from tkinter import filedialog
import numpy as np
import cv2
import math
import os


def Qr_square(img,positionx,positiony):
    cv2.rectangle(img, (positionx-1, positiony-1), (positionx+7, positiony+7), [255,255,255], 1)
    x1,y1 = positionx, positiony
    x2,y2 = positionx + 6, positiony +6
    cv2.rectangle(img, (x1, y1), (x2, y2), [], 1)
    x3,y3 = positionx + 2 ,positiony + 2 
    x4,y4 =  positionx +4 ,positiony +4
    cv2.rectangle(img, (x3, y3), (x4, y4), [0], -1)
    return(positionx+7,positiony+7)

def nearest_resolution():
    file = open("test.bin", "r")
    Binary_count = len(file.readline())

    pixel_count = Binary_count / 2
    pixel_count += 108
    aspect_ratios = [
        (4, 3),
        (1, 1),
    ]

    best_match = None
    best_total = None

    for w_ratio, h_ratio in aspect_ratios:
        k = math.ceil(math.sqrt(pixel_count / (w_ratio * h_ratio)))
        width = w_ratio * k
        height = h_ratio * k
        total_pixels = width * height

        if best_total is None or total_pixels < best_total:
            best_total = total_pixels
            best_match = (width, height)

    return best_match
    

def make_Image():
    width, height = nearest_resolution()
    img = np.zeros((height, width, 3), np.uint8) 
    cv2.rectangle(img, (0, 0), (width, height), [255,255,255], -1)
    colours_Array = Qr_Mker()
    Qr_square_postions =[]

    x, y = Qr_square(img,0,0)
    Qr_square_postions.append([0,0,x,y]) # top left which works
    x, y = Qr_square(img,0,height-7)
    Qr_square_postions.append([0,height-8,x,y]) # bottom left
    x, y = Qr_square(img,width-7,0)
    Qr_square_postions.append([width-8,0,x,y]) # top right
    i = 0
    breakout = False
    for q in range(height):
        for n in range(width):
            for t in range(len(Qr_square_postions)):
                if n >= Qr_square_postions[t][0] and n <= Qr_square_postions[t][2] and q >= Qr_square_postions[t][1] and q <= Qr_square_postions[t][3]:
                    breakout = True
                    print(n,q)
                    break

            if breakout == True:
                breakout = False
                continue
            try:
                match colours_Array[i]:
                    case "BLACK":
                        img[q,n] = (0,0,0)
                    case "WHITE":
                        img[q,n] = (255,255,255)
                    case "RED":
                        img[q,n] = (0,0,255)
                    case "GREEN":
                        img[q,n] = (0,255,0)
            except:
                img[q,n] = (255,255,255)
          
            i += 1
    image_bordered = cv2.copyMakeBorder(src=img, top=1, bottom=1, left=1, right=1, borderType=cv2.BORDER_CONSTANT,value=[255,255,255]) 
    resized = cv2.resize(image_bordered, (width *8, height*8), 0, 0, interpolation = cv2.INTER_NEAREST)

    cv2.imshow("QR", resized)
    os.chdir("QRCODES")
    user_input = input("What would you like to name this file?")
    cv2.imwrite("{}.png".format(user_input), resized)
    cv2.waitKey(0)



def validation(line):
    if len(line) % 2 != 0:
        line = line + "0"
    if len(set(line)) == 2 and "0" in set(line) and "1" in set(line):
        print("")
    else:
        print("Incorrect Value")
        exit()

def Qr_Mker():
    file = open("test.bin", "r")
    line = file.readline()
    validation(line)
    colours_Array = []
    for i in range(1,len(line),2):
        match ("{}{}").format(line[i-1],line[i]):
            case "01":
                colours_Array.append("BLACK")
            case "00":
                colours_Array.append("WHITE")
            case "10":
               colours_Array.append("RED")
            case "11":
                colours_Array.append("GREEN")
    return colours_Array

def file_to_hex(file):    
    filename = file
    file_content = bytes
    hex_array = []
    hex_array_len = 0

    file_content = open(filename, "rb").readlines()
    for line in file_content:
        for byte in line:
                hex_array_len += 1
                hex_byte = hex(byte).replace("x", "").upper()
                if byte >= 16:
                    hex_byte = hex_byte.lstrip("0")
                hex_array.append(hex_byte)
        hex_to_binary(hex_array)

def hex_to_binary(hex_array):
    overall = ""
    for i in range(len(hex_array)):
        binary_value = bin(int(hex_array[i], 16))[2:].zfill(len(hex_array[i]) * 4)
        overall = str(overall) + str(binary_value)
    file = open("test.bin", "w")
    file.write(overall)

def main(file_directory):
    file_to_hex(file_directory)
    make_Image()

if __name__ == '__main__':
    file_directory = filedialog.askopenfilename()
    main(file_directory)

