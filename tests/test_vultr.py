import unittest
import os
from vultr import Vultr


class UnauthenticateTests(unittest.TestCase):

    def setUp(self):
        self.vultr = Vultr('')

    def test_plans_list(self):
        response = self.vultr.plans_list()

    def test_regions_list(self):
        response = self.vultr.regions_list()

    def test_os_list(self):
        response = self.vultr.os_list()

    def test_app_list(self):
        response = self.vultr.app_list()


class AuthenticatedTests(unittest.TestCase):

    def setUp(self):
        if os.environ.get('VULTR_KEY') is None:
            raise Exception(
                'AuthenticatedTests Require the VULTR_KEY environment varaible to be set.')
        self.vultr = Vultr(os.environ['VULTR_KEY'])

    def test_iso_list(self):
        response = self.vultr.iso_list()


if __name__ == '__main__':
    unittest.main()