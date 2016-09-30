## Environment
* [Dynamsoft Barcode Reader 4.2][0]
* Python 2.7.0
* OpenCV 2.4.10
* Windows 10
* USB webcam

## Installation
### What if you see the error ‘Unable to find vcvarsall.bat’ when building Python extension on Windows?
According to the answer from [StackOverflow][1], execute the following command based on the version of Visual Studio installed:
* Visual Studio 2010 (VS10): SET VS90COMNTOOLS=%VS100COMNTOOLS%
* Visual Studio 2012 (VS11): SET VS90COMNTOOLS=%VS110COMNTOOLS%
* Visual Studio 2013 (VS12): SET VS90COMNTOOLS=%VS120COMNTOOLS%
* Visual Studio 2015 (VS14): SET VS90COMNTOOLS=%VS140COMNTOOLS%

For example, build and install the extension with **Visual Studio 2015**:

```
SET VS90COMNTOOLS=%VS140COMNTOOLS%
python setup.py build install
```

Copy **DynamsoftBarcodeReaderx86.dll** and **cv2.pyd** to **Python27\Lib\site-packages**

## How to Run
1. Connect a webcam to your PC.
2. Run **app.py** or **app_thread.py**:
    ```
    python app.py
    ```
    ![webcam barcode reader with OpenCV Python](http://www.codepool.biz/wp-content/uploads/2016/09/opencv-python-webcam-barcode.PNG)

[0]:http://www.dynamsoft.com/Downloads/Dynamic-Barcode-Reader-Download.aspx
[1]:http://stackoverflow.com/questions/2817869/error-unable-to-find-vcvarsall-bat