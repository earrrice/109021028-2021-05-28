from glob import glob
import sys
from PIL import Image

def imgconvert(origName,newImgName,newimgformat):
    try:
        im=Image.open(origName)
        if newimgformat=="jpeg":
            im=im.convert('RGB')
        im.save(newImgName+newimgformat,newimgformat)
    except FileNotFoundError as fnfe:
        print(fnfe)

if __name__=="__main__":
    if len(sys.argv)>1:
        if sys.argv[1]=="-jpg2png":
            imList=glob("*.[jJ][pP][gG]")
            newimgformat="png"
        if sys.argv[1]=="-png2jpg":
            imList=glob("*.[pP][nN][gG]")
            newimgformat="jpeg"
        for imgname in imList:
            imgconvert(imgname,imgname[:-3],newimgformat)