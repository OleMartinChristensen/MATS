# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 16:31:32 2017

@author: olem
"""
from orbit_predictor.sources import EtcTLESource

def get_position(time,satellite="MATS",tlefile=None):

    #returns position of MATS using a tle file. If no file specifed Odin 
    #position is used. 

    source = EtcTLESource(tlefile)
    predictor = source.get_predictor(satellite, precise=True)
    position = predictor.get_position(time)
    
    return position