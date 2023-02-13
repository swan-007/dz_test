from unittest import TestCase
from dz_2 import put_path, check_path, base_host, headers


class testya(TestCase):

      def test_put_path(self):
          expected_res = ['<Response [201]>', '<Response [409]>']
          res = put_path(base_host, headers)
          self.assertIn(res, expected_res )


      def test_check_path(self):
          expected_res = '<Response [200]>'
          res = check_path(base_host, headers)
          self.assertEqual(res, expected_res)
