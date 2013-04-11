# -*- coding: utf-8 -*-
#
#
# TheVirtualBrain-Framework Package. This package holds all Data Management, and 
# Web-UI helpful to run brain-simulations. To use it, you also need do download
# TheVirtualBrain-Scientific Package (for simulators). See content of the
# documentation-folder for more details. See also http://www.thevirtualbrain.org
#
# (c) 2012-2013, Baycrest Centre for Geriatric Care ("Baycrest")
#
# This program is free software; you can redistribute it and/or modify it under 
# the terms of the GNU General Public License version 2 as published by the Free
# Software Foundation. This program is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of 
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public
# License for more details. You should have received a copy of the GNU General 
# Public License along with this program; if not, you can download it here
# http://www.gnu.org/licenses/old-licenses/gpl-2.0
#
#
"""
Created on Mar 20, 2013

.. moduleauthor:: Bogdan Neacsa <bogdan.neacsa@codemart.ro>
"""
if __name__ == "__main__":
    from tvb_library_test import setup_test_console_env
    setup_test_console_env()
    
import unittest

from tvb.datatypes import arrays
from tvb.basic.traits.util import str_class_name
from tvb.basic.traits.core import FILE_STORAGE_DEFAULT
from tvb_library_test.base_testcase import BaseTestCase
        
class CoreTest(BaseTestCase):
    
    def test_traits_default(self):
        array_dt = arrays.FloatArray()
        self.assertEqual(array_dt.trait.file_storage, FILE_STORAGE_DEFAULT)
        self.assertEqual(array_dt.trait.order_number, 0)
        self.assertEqual(array_dt.trait.required, True)
        self.assertEqual(array_dt.trait.use_storage, True)
        self.assertEqual(array_dt.trait.range_interval, None)
     
     
    def test_traits_specific(self):
        array_dt = arrays.FloatArray(file_storage = "txt",
                                     order = 6,
                                     required = False,
                                     use_storage = False,
                                     range = [1, 2, 3])
        self.assertEqual(array_dt.trait.file_storage, 'txt')
        self.assertEqual(array_dt.trait.order_number, 6)
        self.assertEqual(array_dt.trait.required, False)
        self.assertEqual(array_dt.trait.use_storage, False)
        self.assertEqual(array_dt.trait.range_interval, [1, 2, 3]) 
    
    
    def test_str_class_name(self):
        self.assertEqual(str_class_name(arrays.FloatArray), 'tvb.datatypes.arrays.FloatArray')
        self.assertEqual(str_class_name(arrays.FloatArray, True), 'FloatArray')
        self.assertEqual(str_class_name(1), '1')
    
        
def suite():
    """
    Gather all the tests in a test suite.
    """
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(CoreTest))
    return test_suite


if __name__ == "__main__":
    #So you can run tests from this package individually.
    TEST_RUNNER = unittest.TextTestRunner()
    TEST_SUITE = suite()
    TEST_RUNNER.run(TEST_SUITE) 