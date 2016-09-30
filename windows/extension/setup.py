from distutils.core import setup, Extension

module_dbr = Extension('dbr',
                        sources = ['dbr.c'], 
                        include_dirs=["F:\\Python27\\Lib\\site-packages\\numpy\\core\\include\\numpy", 'F:\\Program Files (x86)\\Dynamsoft\Barcode Reader 4.2\\Components\\C_C++\\Include'],
                        library_dirs=['F:\\Program Files (x86)\\Dynamsoft\Barcode Reader 4.2\\Components\\C_C++\\Lib'],
                        libraries=['DBRx86'])

setup (name = 'DynamsoftBarcodeReader',
        version = '1.0',
        description = 'Python barcode extension',
        ext_modules = [module_dbr])
