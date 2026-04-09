import cv2
import numpy as np
import matplotlib.pyplot as plt

def to_linear(img):
    return np.power(img / 255.0, 2.2)

def to_srgb(img):
    return np.clip(np.power(img, 1/2.2) * 255.0, 0, 255).astype(np.uint8)

def run(fileLoc:str):
    filedir = fileLoc + "Pictures"
    images = []

    for i in range(1, 251):
        strin = str(i).zfill(4)
        print("Reading Picture #" + strin + "")
        
        img = cv2.imread(filedir + "/" + strin + ".png")
        if img is None:
            print("Warning: Picture " + strin + " not found. Skipping.")
            continue
        
        img_linear = to_linear(img.astype(np.float32))
        images.append(img_linear)

    print("Stacking images...")
    stack = np.stack(images[0:5], axis=0)
    stack1 = np.stack(images[0:25], axis=0)
    stack2 = np.stack(images[0:50],axis=0)
    stack3 = np.stack(images[0:100],axis=0)
    stack4 = np.stack(images[0:250],axis=0)

    print("Averaging in linear space...")
    avgImage_linear = np.mean(stack, axis=0)
    avgImage_linear1 = np.mean(stack1, axis=0)
    avgImage_linear2 = np.mean(stack2, axis=0)
    avgImage_linear3 = np.mean(stack3, axis=0)
    avgImage_linear4 = np.mean(stack4, axis=0)
    firstImage_linear = images[0]

    imgList = [firstImage_linear,avgImage_linear,avgImage_linear1,avgImage_linear2,avgImage_linear3,avgImage_linear4]
    imgNames = ["1","5","25","50","100","250"]

    for i in range(0,6):
        print("Starting " + imgNames[i] + " Creation")
        avgImageRGB = to_srgb(imgList[i])
        smoothedImageRGB = cv2.bilateralFilter(avgImageRGB,9,75,75)
        denoisedImageRGB = cv2.fastNlMeansDenoising(avgImageRGB)
        gaussianImageRGB = cv2.GaussianBlur(avgImageRGB,(5,5),0)
        tempImg1 = to_linear(denoisedImageRGB)
        tempImg2 = to_linear(smoothedImageRGB)
        tempImg3 = to_linear(gaussianImageRGB)
        comboImageRGB = to_srgb(cv2.addWeighted(tempImg1, .5, tempImg2, .5, 0))
        comboImageRGB1 = to_srgb(cv2.addWeighted(tempImg1, .75, tempImg2, .25, 0))
        comboImageRGB2 = to_srgb(cv2.addWeighted(tempImg1, .25, tempImg2, .75, 0))
        comboImageRGB3 = to_srgb(cv2.addWeighted(tempImg3,.33, to_linear(comboImageRGB),.66,0))
        cv2.imwrite(("output/" + filedir + "/rough" + fileLoc + imgNames[i] + ".png"), avgImageRGB)
        cv2.imwrite(("output/" + filedir + "/smoothed" + fileLoc + imgNames[i] + ".png"), smoothedImageRGB)
        cv2.imwrite(("output/" + filedir + "/denoised" + fileLoc + imgNames[i] + ".png"), denoisedImageRGB)
        cv2.imwrite(("output/" + filedir + "/combo5050" + fileLoc + imgNames[i] + ".png"), comboImageRGB)
        cv2.imwrite(("output/" + filedir + "/combo7525" + fileLoc + imgNames[i] + ".png"), comboImageRGB1)
        cv2.imwrite(("output/" + filedir + "/combo2575" + fileLoc + imgNames[i] + ".png"), comboImageRGB2)
        cv2.imwrite(("output/" + filedir + "/combo333333" + fileLoc + imgNames[i] + ".png"), comboImageRGB3)

strs = ["SpaceExplorer","VoxelHouse","Mario"]
for strin in strs:
    print("Beginning " + strin + " run... \nThis may take a while...")
    run(strin)

print("Finished with the file creation!\nHave a great day!")