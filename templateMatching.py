import cv2
import numpy as np
def getMatches(image, template, threshold):
    result = cv2.matchTemplate(image,template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(result>=threshold)
    results = zip(*loc[::-1])
    return results
def highlightRois(image, roisCoords, roiWidthHeight):
    rois = []
    for roisCoord in roisCoords:
        roiTopLeft = roisCoord["topLeft"]
        name = roisCoord["name"]
        roiBottomRight = tuple([sum(x)for x in zip(roiTopLeft, roiWidthHeight)])
        roi = image[roiTopLeft[1]:roiBottomRight[1], roiTopLeft[0]:roiBottomRight[0]]
        rois.append({'topLeft': roiTopLeft, 'bottomRight': roiBottomRight, 'area': roi, 'name': name})
    mask = np.zeros(image.shape, dtype="uint8")
    image = cv2.addWeighted(image, 0.75, mask, 0.01, 0)
    
    for roi in rois:
        image[roi['topLeft'][1]:roi['bottomRight'][1], roi['topLeft'][0]:roi['bottomRight'][0]] = roi['area']
        cv2.putText(image, roi['name'][0], roi['topLeft'], cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255), 2)
        
    return image