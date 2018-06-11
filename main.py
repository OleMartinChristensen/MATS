# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 15:11:45 2018

@author: olem
"""
import astropy.units as u
import src.satellite_propagator as satprop
import datetime
from astroquery.vizier import Vizier
import astropy.coordinates as coord
import numpy as np
import warnings

#test position with STK values and Odin
d = datetime.datetime(2018,4,3,0,0,0)

position_ecef = satprop.get_position(d,satellite="MATS",tlefile="./test_file/mats.tle")
position_stk = np.array([1225.20392,-6818.719807,200.492145])
error = np.array([position_ecef.x.value,position_ecef.y.value,position_ecef.z.value]) - \
        position_stk
        
error_tot = np.sqrt(error.dot(error.T))*1e3;
if error_tot>100:
    warnings.warn("Satellite position off by more than 100 m")

velocity_stk = np.array([-1.524601,-0.038234,7.512187])
error = np.array([position_ecef.v_x.value,position_ecef.v_y.value,position_ecef.v_z.value]) - \
        velocity_stk

error_tot = np.sqrt(error.dot(error.T))*1e3;
if error_tot>500:
    warnings.warn("Satellite velocity off by more than 500 m/s")

        
position_ecef.transform_to(coord.GCRS(obstime=d)).set_representation_cls('cartesian')
position_eci_stk = np.array([-2508.510645,6457.675701,205.086445])       
error = np.array([position_ecef.cartesian.x.value,position_ecef.cartesian.y.value,position_ecef.cartesian.z.value]) - \
        position_eci_stk
        
error_tot = np.sqrt(error.dot(error.T))*1e3;
if error_tot>100:
    warnings.warn("Satellite position off by more than 100 m")

velocity_stk_eci = np.array([1.031261,0.146421,7.510402])
error = np.array([position_ecef.velocity.d_x.value,position_ecef.velocity.d_y.value,position_ecef.velocity.d_z.value]) - \
        velocity_stk_eci

error_tot = np.sqrt(error.dot(error.T))*1e3;
if error_tot>500:
    warnings.warn("Satellite velocity off by more than 500 m/s")

#Find look vector for tangent point of MATS (92 km in orbit plane)

#Find orbit plane for two positions




#test star gazing
Vizier.ROW_LIMIT = 50
catalog_list = Vizier.find_catalogs('UCAC4')
catalogs = Vizier.get_catalogs(catalog_list.keys())

v = Vizier(columns=['_RAJ2000', '_DEJ2000', 'Vmag'], column_filters={"Vmag":"<10"})

result = v.query_region(coord.SkyCoord(ra=299.590, dec=35.201,
                                            unit=(u.deg, u.deg),frame='icrs'),
                            width="60m",height="60m",catalog=["I/322A"])