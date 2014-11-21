def frame(pic):
  framepic = makePicture('C:\\Users\\GRAM\\Documents\\CST 205\\Photos\\wave-midterm frame.jpg')
'C:\\Users\\GRAM\\Documents\\CST 205\\Photos\\wave-midterm frame.jpg')
#Allowable picture area:  (0,90) to (263,270)
  centerX=131
  centerY=90
  copyInto(innerpic,framepic,centerX-getWidth(innerpic)/2,centerY-getHeight(innerpic)/2)
  return framepic
def addOtter(pic)
  otterpic=makePicture('C:\\Users\\GRAM\\Documents\\CST 205\\Photos\\otter.png')
      
def CSUMBify(pic)
  otterpic=makePicture('C:\\Users\\GRAM\\Documents\\CST 205\\Photos\\otter.png')
  textColor = makeColor(51,255,255)
  framedpic=frame(pic)
  addText(framedpic,70,15,"Big waves. big Ideas.",textColor)
  copyInto(otterpic,framedpic,299,181)