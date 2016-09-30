import cv2
from dbr import *
import time
import threading

globalFrame = None;
condition = threading.Condition()

class BarcodeReaderThread (threading.Thread):
    def __init__(self, name, isRunning):
        threading.Thread.__init__(self)
        self.name = name
        self.isRunning = isRunning
    def run(self):
        global globalFrame, condition
        types = {
            0x3FFL: "OneD",
            0x1L  : "CODE_39",
            0x2L  : "CODE_128",
            0x4L  : "CODE_93",
            0x8L  : "CODABAR",
            0x10L : "ITF",
            0x20L : "EAN_13",
            0x40L : "EAN_8",
            0x80L : "UPC_A",
            0x100L: "UPC_E",
            0x200L: "INDUSTRIAL_25",
            0x2000000L: "PDF417",
            0x8000000L: "DATAMATRIX",
            0x4000000L: "QR_CODE"
        }

        frame = None
        while self.isRunning:
            condition.acquire()
            #  Wait until the frame is available
            frame = globalFrame
            while (frame is None):
                frame = globalFrame
                condition.wait()
            condition.release()

            results = decodeBuffer(frame)
            if (len(results) > 0):
                print "Total count: " + str(len(results))
                for result in results:
                    print "Type: " + types[result[0]]
                    print "Value: " + result[1] + "\n"

            time.sleep(0.05) # For improving video frame rate
        print "Quit thread"

def getImageName():
    localtime = time.localtime()
    capturetime = time.strftime("%Y%m%d%H%M%S", localtime)
    return capturetime + ".jpg"

def readBarcode():
    vc = cv2.VideoCapture(0)

    if vc.isOpened(): # try to get the first frame
        initLicense("<license>")
        rval, frame = vc.read()
    else:
        return
    
    windowName = "Barcode Reader"

    # Create a thread for barcode detection
    barcodeReaderThread = BarcodeReaderThread("Barcode Reader Thread", True)
    barcodeReaderThread.start()

    global globalFrame, condition
    while True:
        cv2.imshow(windowName, frame) # Render a frame on Window
        rval, frame = vc.read(); # Get a frame

        condition.acquire()
        globalFrame = frame
        condition.notify()
        condition.release()

        # 'ESC' for quit
        key = cv2.waitKey(20)
        if key == 27:
            barcodeReaderThread.isRunning = False
            barcodeReaderThread.join()
            break

    cv2.destroyWindow(windowName)

if __name__ == "__main__":
    print "OpenCV version: " + cv2.__version__
    readBarcode()
