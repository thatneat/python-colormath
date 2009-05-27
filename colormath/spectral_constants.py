"""
 Color Math Module (colormath) 
 Copyright (C) 2009 Gregory Taylor

 This program is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.

 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.

 You should have received a copy of the GNU General Public License
 along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

"""
Contains lookup tables, constants, and things that are generally static
and useful throughout the library.
"""
import numpy

STDOBSERV_X2 = numpy.array((
    0.001368000000, # 380nm
    0.004243000000,
    0.014310000000,
    0.043510000000,
    0.134380000000,
    0.283900000000,
    0.348280000000,
    0.336200000000,
    0.290800000000,
    0.195360000000,
    0.095640000000,
    0.032010000000,
    0.004900000000,
    0.009300000000,
    0.063270000000,
    0.165500000000,
    0.290400000000,
    0.433449900000,
    0.594500000000,
    0.762100000000,
    0.916300000000,
    1.026300000000,
    1.062200000000,
    1.002600000000,
    0.854449900000,
    0.642400000000,
    0.447900000000,
    0.283500000000,
    0.164900000000,
    0.087400000000,
    0.046770000000,
    0.022700000000,
    0.011359160000,
    0.005790346000,
    0.002899327000,
    0.001439971000  # 730nm
))

STDOBSERV_Y2 = numpy.array((
    0.000039000000, # 380nm
    0.000120000000,
    0.000396000000,
    0.001210000000,
    0.004000000000,
    0.011600000000,
    0.023000000000,
    0.038000000000,
    0.060000000000,
    0.090980000000,
    0.139020000000,
    0.208020000000,
    0.323000000000,
    0.503000000000,
    0.710000000000,
    0.862000000000,
    0.954000000000,
    0.994950100000,
    0.995000000000,
    0.952000000000,
    0.870000000000,
    0.757000000000,
    0.631000000000,
    0.503000000000,
    0.381000000000,
    0.265000000000,
    0.175000000000,
    0.107000000000,
    0.061000000000,
    0.032000000000,
    0.017000000000,
    0.008210000000,
    0.004102000000,
    0.002091000000,
    0.001047000000,
    0.000520000000 # 730nm
))

STDOBSERV_Z2 = numpy.array((
    0.006450001000, # 380nm
    0.020050010000,
    0.067850010000,
    0.207400000000,
    0.645600000000,
    1.385600000000,
    1.747060000000,
    1.772110000000,
    1.669200000000,
    1.287640000000,
    0.812950100000,
    0.465180000000,
    0.272000000000,
    0.158200000000,
    0.078249990000,
    0.042160000000,
    0.020300000000,
    0.008749999000,
    0.003900000000,
    0.002100000000,
    0.001650001000,
    0.001100000000,
    0.000800000000,
    0.000340000000,
    0.000190000000,
    0.000049999990,
    0.000020000000,
    0.000000000000,
    0.000000000000,
    0.000000000000,
    0.000000000000,
    0.000000000000,
    0.000000000000,
    0.000000000000,
    0.000000000000,
    0.000000000000 # 730nm
))

REFERENCE_ILLUM_D = numpy.array((
    24.45, #380nm
    29.83,
    49.25,
    56.45,
    59.97,
    57.76,
    74.77,
    87.19,
    90.56,
    91.32,
    95.07,
    91.93,
    95.70,
    96.59,
    97.11,
    102.09,
    100.75,
    102.31,
    100.00,
    97.74,
    98.92,
    93.51,
    97.71,
    99.29,
    99.07,
    95.75,
    98.90,
    95.71,
    98.24,
    103.06,
    99.19,
    87.43,
    91.66,
    92.94,
    76.89,
    86.56 # 730nm
))