import cv2
import screen
import os.path as path
from templateMatching import getMatches, highlightRois

testMode = True
testImage = 'test9.png'

matchingThreshold = 0.88

values = ['ace', 'king', 'queen', 'jack', 'ten', 'nine', 'eight', 'seven', 'six', 'five', 'four', 'three', 'two']

vlaues2 = ['1','2','3','4','5','6','7',
          '8','9','X','J','Q','K']
cardsFound = set()
def getImage(name):
    filename = name+".png"
    image = cv2.imread(path.join('images2', filename))
    image = screen.imageToBw(image)
    return image


valuesDict = {}
for value in vlaues2:
    valuesDict[value] = getImage(value)

def watchAndDisplayCards():
    if testMode:
        image = cv2.imread ('tests/'+testImage)
        screen.showImage(image)
    image = screen.imageToBw(image)
    
    allvaluesmap = []
    for value in valuesDict:
        valueTemplate = valuesDict[value]
        valueMatches = getMatches(image,valueTemplate,matchingThreshold)
        valuesmap = map(lambda match: {'topLeft': (match[0], match[1]), 'name': value}, valueMatches)
        allvaluesmap+=valuesmap
    if testMode:
        image = cv2.imread('tests/'+testImage)
    image = highlightRois(image, allvaluesmap,(30,30))
    screen.showImage(image)
    
        
watchAndDisplayCards()