# pySUNXI
Python Lib GPIOs

Copyright (c) 2013 Stefan Mavrodiev/Olimex LTD

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

This package provides class to control the GPIO on Allwinner sunxi platform.
Current release does no support any peripheral functions.

Example
=======

Typical usage::
    
    #!/usr/bin/env python

    import SUNXI_GPIO as GPIO

    #init module
    GPIO.init()
    
    #configure module
    GPIO.setcfg(GPIO.PIN#, GPIO.OUT)
    GPIO.setcfg(GPIO.PIN#, GPIO.IN)
        
    #read the current GPIO configuration
    config = GPIO.getcfg(GPIO.PIN#)
    
    #set GPIO high
    GPIO.output(GPIO.PIN#, GPIO.HIGH)
    
    #set GPIO low
    GPIO.output(GPIO.PIN#, GPIO.LOW)
    
    #read input
    state = GPIO.input(GPIO.PIN#)
    
    #cleanup 
    GPIO.cleanup()
    
SPI usage::

    #import SUNXI_SPI as SPI
    
    #init
    SPI.init(mode)
    
    #write
    SPI.write(byte1, byte2, byte3, ....)
    
    #read
    SPI.read(address, byte1, byte2, byte3, ....)
    
Where modes are:

    * 0 - POL=0 and PHA=0
    * 1 - POL=0 and PHA=1
    * 2 - POL=1 and PHA=0
    * 3 - POL=1 and PHA=1
    

Thanks also to: bianchina3


