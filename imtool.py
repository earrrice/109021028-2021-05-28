import sys
from PIL import Image,ImageFilter

def resizeimg(imgName):
    try:
        img=Image.open(imgName)
        print("Current size (width,height)",img.size)
        newWidth=int(input("new width:"))
        ratio=float(newWidth)/img.size[0]
        newHeight=int(img.size[1]*ratio)
        resizeimg=img.resize((newWidth,newHeight),Image.BILINEAR)
        print("new image size:",resizeimg.size)
        dotIndex=imgName.index(".")
        newImgName=imgName[:dotIndex]+"_resized"+imgName[dotIndex:]
        resizeimg.save(newImgName)
        print("Resized img is saved as ",newImgName,"\n")

    except FileNotFoundError as fnfe:
        print(fnfe)

def rotateImg(imgName):
    try:
        img=Image.open(imgName)
        print("旋轉選項:")
        print("1.左右選轉")
        print("2.上下選轉")
        print("3.旋轉90度")
        print("4.旋轉180度")
        print("5.旋轉270度")
        print("6.自訂")
        op1=input("你要進行的操作:")
        if op1=="1":
            newIm=img.transpose(Image.FLIP_LEFT_RIGHT)
            str1="_flip_LR"
        elif op1=="2":
            newIm=img.transpose(Image.FLIP_TOP_BOTTOM)
            str1="_flip_TB"
        elif op1=="3":
            newIm=img.transpose(Image.ROTATE_90)
            str1="_rotate_90"
        elif op1=="4":
            newIm=img.transpose(Image.ROTATE_180)
            str1="_rotate_180"
        elif op1=="5":
            newIm=img.transpose(Image.ROTATE_270)
            str1="_rotate_270"
        elif op1=="6":
            rotDegree=float(input("Rotate degree:"))
            newIm=img.rotate(rotDegree)
            str1="_rotate_"+str(rotDegree)
        dotIndex=imgName.index(".")
        newImgName=imgName[:dotIndex]+str1+imgName[dotIndex:]
        newIm.save(newImgName)
        print("rotated img is saved as ",newImgName,"\n")

    except FileNotFoundError as fnfe:
        print(fnfe)

def genThumbnail(imgName):
    try:
        img=Image.open(imgName)
        print("Current size (width,height)",img.size)
        newWidth,newHeight=map(int,input("請輸入縮圖尺寸:").split())
        img.thumbnail((newWidth,newHeight))
        dotIndex=imgName.index(".")
        newImgName=imgName[:dotIndex]+"_thumbnail"+imgName[dotIndex:]
        img.save(newImgName)
        print("thumbnail image is saved as ",newImgName,"\n")

    except FileNotFoundError as fnfe:
        print(fnfe)

def applyFilter(imgName):
    try:
        img=Image.open(imgName)
        print("濾鏡選項")
        print("1.模糊")
        print("2.輪廓")
        print("3.細節增強")
        print("4.邊緣增強")
        print("5.深度邊緣增強")
        print("6.浮雕效果")
        print("7.邊緣訊息")
        print("8.平滑效果")
        print("9.深度平滑效果")
        print("A.銳利化")
        op1=input("選擇濾鏡效果:")
        if op1=="1":
            newImg=img.filter(ImageFilter.BLUR)
            str1="_BLUR"
        elif op1=="2":
            newImg=img.filter(ImageFilter.CONTOUR)
            str1="_CONTOUR"
        elif op1=="3":
            newImg=img.filter(ImageFilter.DETAIL)
            str1="_DETAIL"
        elif op1=="4":
            newImg=img.filter(ImageFilter.EDGE_ENHANCE)
            str1="_EDGE_ENHANCE"
        elif op1=="5":
            newImg=img.filter(ImageFilter.EDGE_ENHANCE_MORE)
            str1="_EDGE_ENHANCE_MORE"
        elif op1=="6":
            newImg=img.filter(ImageFilter.EMBOSS)
            str1="_EMBOSS"
        elif op1=="7":
            newImg=img.filter(ImageFilter.FIND_EDGES)
            str1="_FIND_EDGES"
        elif op1=="8":
            newImg=img.filter(ImageFilter.SMOOTH)
            str1="_SMOOTH"
        elif op1=="9":
            newImg=img.filter(ImageFilter.SMOOTH_MORE)
            str1="_SMOOTH_MORE"
        elif op1=="A":
            newImg=img.filter(ImageFilter.SHARPEN)
            str1="_SHARPEN"
        dotIndex=imgName.index(".")
        newImgName=imgName[:dotIndex]+str1+imgName[dotIndex:]
        newImg.save(newImgName)
        print("Filter img is saved as ",newImgName,"\n")

    except FileNotFoundError as fnfe:
        print(fnfe)

def showMenu():
    print("========================")
    print("1:等比例縮放")
    print("2:圖片旋轉")
    print("3:產生縮圖")
    print("4:套用濾鏡")
    print("0:結束")

if __name__=="__main__":
    if len(sys.argv)>1:
        while True:
            showMenu()
            op=input("選擇功能:")
            if op=="1":
                resizeimg(sys.argv[1])
            elif op=="2":
                rotateImg(sys.argv[1])
            elif op=="3":
                genThumbnail(sys.argv[1])
            elif op=="4":
                applyFilter(sys.argv[1])
            elif op=="0":
                break
    else:
        print("argument error")
