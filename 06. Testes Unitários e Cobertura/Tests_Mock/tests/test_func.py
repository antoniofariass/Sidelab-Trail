from unittest import mock, TestCase
import unittest

from app import facebook, google, data

#utilizar no inicio do codigo 
""" def setUp(self):
    self.patcher = mock.patch('app.google.get_data',return_value = 'data_2')
    self.patcher.start()
"""

#utilizar no final do codigo
""" def tearDow(self):
    self.patcher.stop() 
"""

class TestApi(unittest.TestCase):
    
    @mock.patch('app.facebook.get_data',return_value = 'data_3')
    @mock.patch('app.google.get_data',return_value = 'data_2') #vai no diretorio da funcao e altera o valor do return 
    def test_external_api(self,googl,fb): # a ordem dos parametros eh do mock mais proximo, ou seja, começa de baixo para cima 
        self.assertEqual(google.call_google_api(),'data_2')
        self.assertEqual(facebook.call_facebook_api(),'data_3')

    #or 
 
    def test_external_api(self,googl,fb): 
        with mock.patch('app.google.get_data',return_value = 'data_2'):
            self.assertEqual(google.call_google_api(),'data_2')



