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
position = satprop.get_position(d,satellite="MATS",tlefile="./test_file/mats.tle")
positions_from_STK = (1225.203926,-6818.719807,200.492145)
error = np.array(position.position_ecef) - np.array(positions_from_STK)
error_tot = error.dot(error.T)*1e3;
if error_tot>10:
    warnings.warn("Satellite position off by more than 10 m")


#Find look vector for tangent point of MATS (92 km in orbit plane)


#test star gazing
Vizier.ROW_LIMIT = 50
catalog_list = Vizier.find_catalogs('UCAC4')
catalogs = Vizier.get_catalogs(catalog_list.keys())

v = Vizier(columns=['_RAJ2000', '_DEJ2000', 'Vmag'], column_filters={"Vmag":"<10"})

result = v.query_region(coord.SkyCoord(ra=299.590, dec=35.201,
                                            unit=(u.deg, u.deg),frame='icrs'),
                            width="60m",height="60m",catalog=["I/322A"])