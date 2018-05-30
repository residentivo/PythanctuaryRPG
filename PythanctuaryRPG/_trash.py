import numpy as np
from PIL import ImageGrab
from PIL import Image
import cv2
import time 
import pyautogui
from directkeys import PressKey, W, A, S, D
import pytesseract

#def screen_record(): 
#    last_time = time.time()
#    while True:
#        #printscreen_pil =  ImageGrab.grab(bbox=(0,40,1300,640))
#        #printscreen_numpy =   np.array(printscreen_pil.getdata(),dtype='uint8')\
#        printscreen =  np.array(ImageGrab.grab(bbox=(0,40,1300,640)))
#        print('loop took {} seconds'.format(time.time()-last_time))
#        last_time = time.time()
#        cv2.imshow('window',cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB))
#        if cv2.waitKey(25) & 0xFF == ord('q'):
#            cv2.destroyAllWindows()
#            break
src_path = "d:\\Projetos\\PythanctuaryRPG\\PythanctuaryRPG\\OCROut\\"
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

def process_img(image):
    original_image = image
    # convert to gray
    processed_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # edge detection
    #processed_img =  cv2.Canny(processed_img, threshold1 = 200, threshold2=300)
    return processed_img

def main():
    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)

    last_time = time.time()
    while True:        
        screen =  np.array(ImageGrab.grab(bbox=(0,40,1300,640)))
        print('Frame took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        new_screen = process_img(screen)
        cv2.imshow('window', new_screen)
        #cv2.imshow('window',cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
        
    kernel = np.ones((1, 1), np.uint8)
    new_screen = cv2.dilate(new_screen, kernel, iterations=1)
    new_screen = cv2.erode(new_screen, kernel, iterations=1)
    cv2.imwrite(src_path + "removed_noise.png", new_screen)
    #new_screen = cv2.adaptiveThreshold(new_screen, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
    #cv2.imwrite(src_path + "thres.png", new_screen)	
    result = pytesseract.image_to_string(Image.open(src_path + "removed_noise.png"))
    #result = pytesseract.image_to_string(Image.open(src_path + "thres.png"))
    #result = pytesseract.image_to_string(new_screen)
    print(result)
    file_object  = open('ocr.text', 'w')
    file_object.write(result)
    file_object.close() 

def get_string(img_path):
    # Read image with opencv
    img = cv2.imread(img_path)

    # Convert to gray
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)

    # Write image after removed noise
    cv2.imwrite(src_path + "removed_noise.png", img)

    #  Apply threshold to get image with only black and white
    #img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

    # Write the image after apply opencv to do some ...
    #cv2.imwrite(src_path + "thres.png", img)

    #tmp = Image.open(src_path + "thres.png")

    # Recognize text with tesseract for python
    result = pytesseract.image_to_string(img)

    # Remove template file
    #os.remove(temp)

    return result
    
#pathloc = 'D:\\Projetos\\PythanctuaryRPG\\OCR\\ocr2.png'
  
#print( pytesseract.image_to_string( Image.open(pathloc) ) ) # Extraindo o texto da imagem
#print( '--- Start recognize text from image ---')
#textFinded = get_string(src_path + "2.png")
#print( "------ Done -------" )
#print( textFinded )
#print( "------ End -------" )

#from IPython.display import Image


main()

 

##apply ORC
#img = Image.open(src_path + "Capture.PNG")

##img = Image.open(src_path + "cropCap.PNG")
##print( "image ",img.size[0],img.size[1])

##Complete crop correct
#areaInfo = (0,478,1275,587)
#cropped_img = img.crop(areaInfo)
#cropped_img.save("D:\\Projetos\\PythanctuaryRPG\\PythanctuaryRPG\\OCROut\\areainfo_Capture.png")

#retorno = get_string("D:\\Projetos\\PythanctuaryRPG\\PythanctuaryRPG\\OCROut\\areainfo_Capture.png")

#print('-------------------- PARSED TEXT --------------------')
#print(retorno)


#this part try break equaly, but not worked
#w = 24
#h = 17	
#startX = 0
#starty = 0
#qtdW = img.size[0] / w
#qtdH = img.size[1] / h
#x =0
#y=0
##area = (0, 0, largura, comprimento)
##print("area {},{},{},{}",area)
##for x in list(range(0,qtdLar)):
#while y < qtdW:
#	x=0
#	while x < qtdH:	
#	#for y in list(range(0,qtdCom)):
#		tx = startX + x * qtdH
#		ty = starty + y * qtdW
#		area = (tx,ty, w + tx, h + ty)
#		print("index, area ",x,y,area)
#		cropped_img = img.crop(area)
#		#if cropped_img.getbbox():
#		#	cropped_img.save("D:\\Projetos\\PythanctuaryRPG\\PythanctuaryRPG\\OCROut\\" + str(x) + "_" + str(y) + "_cropCap.png")
#		cropped_img.save("D:\\Projetos\\PythanctuaryRPG\\PythanctuaryRPG\\OCROut\\" + str(x) + "_" + str(y) + "_cropCap.png")
#		#cv2.imwrite(src_path + str(x) + "_" + str(y) + "_cropCap.png", cropped_img)
#		x+=1		
#	y+=1
#	#cropped_img = img.crop(area)
#	#cv2.imwrite(src_path +  + "cropCap.png", np.array(cropped_img))
	


#cropped_img.show()



