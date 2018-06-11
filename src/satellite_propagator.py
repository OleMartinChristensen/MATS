# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 16:31:32 2017

@author: olem
"""
from orbit_predictor.sources import EtcTLESource
from astropy.coordinates import ITRS
from astropy import units as units
import numpy as np


def get_position(time,satellite="MATS",tlefile=None):

    #returns position of MATS using a tle file. If no file specifed Odin 
    #position is used. 

    source = EtcTLESource(tlefile)
    predictor = source.get_predictor(satellite, precise=True)
    predicted_position = predictor.get_position(time)
    position = ITRS(x=predicted_position.position_ecef[0]*units.km,
                    y=predicted_position.position_ecef[1]*units.km,
                    z=predicted_position.position_ecef[2]*units.km,
                    v_x = predicted_position.velocity_ecef[0]*units.km/units.s,
                    v_y = predicted_position.velocity_ecef[1]*units.km/units.s,
                    v_z = predicted_position.velocity_ecef[2]*units.km/units.s, obstime=time)

    
    return position

def det_orbit_plane(position):
   
    #returns normal vector of orbit (pos x vel) in ECI
    
    #transform to ECI if not
    eci_pos = position.transform_to(position.GCRS(obstime=position.obstime));
    eci_pos.set_representation_cls('cartesian')
    x,y,z = eci_pos.cartesian.d_xyz.value
    vx,vy,vz = eci_pos.velocity.d_xyz.value
    posvec = np.array([x,y,z])
    velvec = np.array([vx,vy,vz])
    normal_vector = np.cross(posvec,velvec)
    return normal_vector
    