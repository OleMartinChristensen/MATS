# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 15:11:45 2018

@author: olem
"""
import astropy.units as u
import satellite_propagator
import datetime
from astroquery.vizier import Vizier
import astropy.coordinates as coord

#test position with STK values and Odin

d = datetime.datetime(2018,3,15)
position,velocity = satellite_propagator.get_position(d,satellite="mats",tlefile="tle_mats.txt")




Vizier.ROW_LIMIT = 50
catalog_list = Vizier.find_catalogs('UCAC4')
catalogs = Vizier.get_catalogs(catalog_list.keys())

v = Vizier(columns=['_RAJ2000', '_DEJ2000', 'Vmag'], column_filters={"Vmag":"<10"})

result = v.query_region(coord.SkyCoord(ra=299.590, dec=35.201,
                                            unit=(u.deg, u.deg),frame='icrs'),
                            width="60m",height="60m",catalog=["I/322A"])