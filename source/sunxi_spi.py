#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  SUNXI_SPI.py
#  
#  Copyright 2013 Stefan Mavrodiev <support@olimex.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.

import SUNXI_GPIO as GPIO
import sys
import time

MODE = 0
MOSI = GPIO.MOSI
MISO = GPIO.MISO
SCK = GPIO.SCK
CS = GPIO.CS
OUT = GPIO.OUT
IN = GPIO.INP
HIGH = GPIO.HIGH
LOW = GPIO.LOW
 
class ModeError(Exception):
    
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return 'Invalid mode selected: ' + repr(self.value)
        

def init(mode):
    
    print ("Selected mode: " + str(mode))
    
    if mode < 0 or mode > 3:
        raise ModeError(mode);        
    
    global MODE
    MODE = mode
    
    GPIO.init()
  
    
    GPIO.setcfg(MOSI, OUT)
    GPIO.setcfg(MISO, IN)
    GPIO.setcfg(SCK, OUT)
    GPIO.setcfg(CS, OUT)
    
    if mode == 0 or mode == 1:
        GPIO.output(CS, HIGH)
        GPIO.output(SCK, LOW)
        GPIO.output(MOSI, LOW)
    
    else:
        GPIO.output(CS, HIGH)
        GPIO.output(SCK, HIGH)
        GPIO.output(MOSI, HIGH)
        
    return
 
 
def read(address, n):
    
    pol = (MODE >> 1) & 1
    pha = MODE & 1 
    
    def SendByte(byte):
        for i in range(8):
            
            if pha == 0:
                if byte & 1:
                    if pol == 0:
                        GPIO.output(MOSI, HIGH)
                    else:
                        GPIO.output(MOSI, LOW)
                else:
                    if pol == 0:
                        GPIO.output(MOSI, LOW)
                    else:
                        GPIO.output(MOSI, HIGH)
            
            time.sleep(0.000001)
            if pol == 0:
                GPIO.output(SCK, HIGH)
            else:
                GPIO.output(SCK, LOW)
            if pha == 1:
                if byte & 1:
                    if pol == 0:
                        GPIO.output(MOSI, HIGH)
                    else:
                        GPIO.output(MOSI, LOW)
                else:
                    if pol == 0:
                        GPIO.output(MOSI, LOW)
                    else:
                        GPIO.output(MOSI, HIGH)
            time.sleep(0.000001)
            if pol == 0:
                GPIO.output(SCK, LOW)
            else:
                GPIO.output(SCK, HIGH)
        
            byte >>= 1
            
    def ReadByte():
        byte = 0
        
        for i in range(8):
            
            time.sleep(0.000001)
            if pol == 0:
                GPIO.output(SCK, HIGH)
            else:
                GPIO.output(SCK, LOW)
            
            if pha == 0:
                if GPIO.input(MISO) == 1:
                    if pol == 0:
                        byte |= 1
                    else:
                        byte |= 0
                else:
                    if pol == 0:
                        byte |= 0
                    else:
                        byte |= 1
                        
                if i != 7:
                    byte <<= 1
            
            time.sleep(0.000001)
            GPIO.output(SCK, LOW)
            
            if pha == 1:
                if GPIO.input(MISO) == 1:
                    if pol == 0:
                        byte |= 1
                    else:
                        byte |= 0
                else:
                    if pol == 0:
                        byte |= 0
                    else:
                        byte |= 1
                        
                if i != 7:
                    byte <<= 1
            
        return byte;
        
        
    GPIO.output(CS, LOW)
    time.sleep(0.000001)      
            
    SendByte(address)
    args = []
    for i in range(n):
        
        args.append(ReadByte())
        
    time.sleep(0.000001)
    GPIO.output(CS, HIGH)    
    
    return args
    
def write(*args):
    
    pol = (MODE >> 1) & 1
    pha = MODE & 1 
    
    def SendByte(byte):
        for i in range(8):
            
            if pha == 0:
                if byte & 0x80:
                    if pol == 0:
                        GPIO.output(MOSI, HIGH)
                    else:
                        GPIO.output(MOSI, LOW)
                else:
                    if pol == 0:
                        GPIO.output(MOSI, LOW)
                    else:
                        GPIO.output(MOSI, HIGH)
            
            time.sleep(0.000001)
            if pol == 0:
                GPIO.output(SCK, HIGH)
            else:
                GPIO.output(SCK, LOW)
            if pha == 1:
                if byte & 0x80:
                    if pol == 0:
                        GPIO.output(MOSI, HIGH)
                    else:
                        GPIO.output(MOSI, LOW)
                else:
                    if pol == 0:
                        GPIO.output(MOSI, LOW)
                    else:
                        GPIO.output(MOSI, HIGH)
            time.sleep(0.000001)
            if pol == 0:
                GPIO.output(SCK, LOW)
            else:
                GPIO.output(SCK, HIGH)
        
            byte <<= 1
        
    
   
    
    GPIO.output(CS, LOW)
    time.sleep(0.000001)      
            
    
    for i in range(len(args)):
        
        SendByte(args[i])
        
    time.sleep(0.000001)
    GPIO.output(CS, HIGH)
        
    return
    
    
