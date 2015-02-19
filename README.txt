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

