## Prerequisites
* [Dynamsoft Barcode Reader for Raspberry Pi][0]
* Python 2.7.0
* OpenCV 3.0.0
* Raspberry Pi 2 or 3
* USB webcam

## Building and Installation
1. Open **setup.py** and modify the paths of include and lib files.
    
    ```
    include_dirs=["/usr/lib/python2.7/dist-packages/numpy/core/include/numpy", "<Your dbr path>/include"],
    library_dirs=['<Your dbr path>/lib'],
    ```
2. Build and install Python extension:
    
    ```
    sudo python setup.py build install
    ```

## How to Run
1. Connect a webcam to Raspberry Pi 2 or 3.
2. Run **app.py**: 

    ```
    python app.py
    ```

[0]:http://www.dynamsoft.com/Downloads/Dynamic-Barcode-Reader-for-Raspberry-Pi-Download.aspx 