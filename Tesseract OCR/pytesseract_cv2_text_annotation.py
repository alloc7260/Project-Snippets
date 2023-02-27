import pytesseract
import cv2

filename = 'Test.jpeg'
image = cv2.imread(filename)
results = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)

for i in range(0, len(results['text'])):
    x = results['left'][i]
    y = results['top'][i]
    w = results['width'][i]
    h = results['height'][i]
    text = results['text'][i]
    conf = int(float(results['conf'][i]))
    if conf > 70:
        text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 200), 2)

cv2.imshow("image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()