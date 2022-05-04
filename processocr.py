try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import glob
import codecs

file = codecs.open("data.txt", "w", "utf-8")
file.write(u'\ufeff')
file.close()
files = glob.glob('vkdata/*')
files.sort()
for fname in files:
    print fname
    data=pytesseract.image_to_data(Image.open(fname), lang='vie+khm', output_type=pytesseract.Output.DICT)
    print data
    exit(1)
    # with codecs.open('data.txt', 'a', 'utf-8') as file:
    #     file.write(data)