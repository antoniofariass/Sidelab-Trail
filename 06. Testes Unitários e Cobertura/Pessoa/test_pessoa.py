"""
class Pessoa
    __init__
        nome str
        sobrenome str 
        dados_obtidos bool (inicia como falso)

    API:
        obter_todos_os_dados -> method
            OK
            404

            (Dados_obtidos se torna true se dados obtidos com sucesso)
"""

import unittest 
from Pessoa import Pessoa
from unittest.mock import patch
import requests

class TestPessoa(unittest.TestCase):
    def setUp(self):
        self.p1 = Pessoa('Antonio', 'Farias')

    def test_pessoa_attr_nome_tem_o_valor_correto(self):
        self.assertEqual(self.p1._nome, 'Antonio')

    def test_pessoa_attr_nome_e_tipo_string(self):
        self.assertIsInstance(self.p1._nome, str)
    
    def test_pessoa_attr_sobrenome_tem_o_valor_correto(self):
        self.assertEqual(self.p1._sobrenome, 'Farias')
    
    def test_pessoa_attr_sobrenome_e_tipo_string(self):
        self.assertIsInstance(self.p1._sobrenome, str)
    
    def test_pessoa_attr_dados_obtidos_incia_falso(self):
        self.assertEqual(self.p1._dados, False)
    
    def test_obter_todos_os_dados_sucesso_OK(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True
        
        self.assertEqual(self.p1.obter_todos_os_dados(), 'CONECTADO')
        self.assertTrue(self.p1._dados)

    def test_obter_todos_os_dados_error_404(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = False
        
        self.assertEqual(self.p1.obter_todos_os_dados(), 'ERRO 404')
        self.assertFalse(self.p1._dados)

    def test_obter_todos_os_dados_sucesso_e_falha_sequencia(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True
        
        self.assertEqual(self.p1.obter_todos_os_dados(), 'CONECTADO')
        self.assertTrue(self.p1._dados)

        fake_request.return_value.ok = False
        
        self.assertEqual(self.p1.obter_todos_os_dados(), 'ERRO 404')
        self.assertFalse(self.p1._dados)


if __name__ == '__main__':
    unittest.main(verbosity=2)