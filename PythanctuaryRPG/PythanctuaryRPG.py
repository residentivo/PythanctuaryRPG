import numpy as np
from PIL import ImageGrab
from PIL import Image
import cv2
import time 
import pyautogui
from directkeys import ClickKey,DIK_1,DIK_2,DIK_3,DIK_4,DIK_F,DIK_A,DIK_RETURN
import pytesseract

src_path = "d:\\Projetos\\PythanctuaryRPG\\PythanctuaryRPG\\OCROut\\"
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

bbox=(0,40,1300,640)
#Botton Text
bT_x = 0 
bT_y = 540
bT_w = 1273
bT_h = 50


#read screen for image
def process_img():    	
	screen = np.array(ImageGrab.grab(bbox))	
	screen = cv2.cvtColor(screen , cv2.COLOR_BGR2GRAY)
	#update visualizer
	cv2.imshow('window', screen)
	if cv2.waitKey(25) & 0xFF == ord('q'):
		cv2.destroyAllWindows()
		return False
	return True,screen


def get_string(screen,x,y,w,h):
    # Read image with opencv
    #img = cv2.imread(img_path)
    
	# Convert to gray
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(screen, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)
    
    crop_img = img[y:y+h, x:x+w]
    #cv2.imshow("cropped", crop_img)
    	
	#save as tmp
    cv2.imwrite(src_path + "cropped.png",crop_img)

    # Recognize text with tesseract for python
    result = pytesseract.image_to_string(crop_img)

    return result

def isWaitEnter():
	isprocessed,screen = process_img()
	
	#crop area maybe

	texto = get_string(screen,bT_x,bT_y, bT_w,bT_h)
	
	print("parsed" + texto)

	if(texto == 'Press any key to continue...'): return False
	return isprocessed 

def hasMenu():
	return False

#click 2 keys, the command and enter to accept
def click(hexKey):
	ClickKey(hexKey)	
	time.sleep(1)
	ClickKey(DIK_RETURN)	
	time.sleep(1)

#for now, is start game static, driven to get menu
def startGame():
	click(DIK_1)#start game
	click(DIK_1)#class barbarian
	click(DIK_1)#overrite
	click(DIK_1)#maybe x
	click(DIK_2)#view perk
	click(DIK_1)#male
	click(DIK_3)#medium size
	ClickKey(DIK_RETURN)#dont have name, please	
	time.sleep(1)
	click(DIK_1)#old potato
	click(DIK_F)#finalize
	click(DIK_1)#NorthAriat
	click(DIK_1)#Human
	ClickKey(DIK_RETURN)#Confirm Human
	time.sleep(1)
	click(DIK_1)#Classic Mode
	click(DIK_A)#No Cinematic - image 16

	#now porcess bottom image until read "Press any key to continue..."
	while isWaitEnter(): pass

	ClickKey(DIK_RETURN)#end Cinematic
	time.sleep(1)
	print('WORDEK')

	#image 17
	#now porcess bottom image until read "Press any key to continue..."
	while isWaitEnter(): pass 
	
	ClickKey(DIK_RETURN)#end Cinematic
	time.sleep(1)
	print('WORKED - 17')
	


def main():
	for i in list(range(4))[::-1]:
		print(i+1)
		time.sleep(1)

	print("------------------------- Start Process -----------------------------")

	startGame()

	print("------------------------- End Process -----------------------------")

	#start process image
	#while process_img():
	#	#identify what part we are
	#	if(isWaitEnter()):
	#		print('send enter')
	#	pass


main()
