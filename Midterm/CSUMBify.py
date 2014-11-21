def addTextCustom(pic, text):
 mystyle = makeStyle(mono, italic + bold, 22)
 addTextWithStyle(pic, 60, 70, text, mystyle, blue)
 return pic

def frame(pic):
  framepic = makePicture('C:\\Users\\GRAM\\Documents\\CST 205\\Photos\\wave-midterm frame.jpg')
  #Allowable picture area:  (0,90) to (263,270)  
  centerX=131
  centerY=180
  copyInto(pic,framepic,centerX-getWidth(pic)/2,centerY-getHeight(pic)/2)
  return framepic
  
def csumbify(pic):
 
  otterpic = makePicture('C:\\Users\\GRAM\\Documents\\CST 205\\Photos\\otter.jpg')
  pic=bluetint(pic)
  framedpic=frame(pic)
  addTextCustom(framedpic,"BIG waves. big IDEAS.")
  copyInto(otterpic,framedpic,299,200)
  return framedpic
  
def bluetint(pic):
    pixels = getPixels(pic)
    for p in pixels:
        r = getRed(p)
        g = getGreen(p)
        b = getBlue(p)
          
        setRed(p, b * .25)
        setGreen(p, (b * .50))
        setBlue(p, b)
        
    return(pic)
