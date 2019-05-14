import sys
sys.path.append('..')

import unittest
from selenium import webdriver
from selenium.webdriver.support.color import Color
import ast
from  ForceLineProject.app import app
from pyvirtualdisplay import Display


class TestApp(unittest.TestCase):
    def test_resposta_da_vida_universo_e_todas_as_coisas(self):
        application = app.test_client()
        response = application.get('/pagina1/')
        print(response.data.decode('utf-8') )
        self.assertIn('42',response.data.decode('utf-8'))

    def test_element_color(self):
        display = Display(visible=0, size=(800, 800))  
        display.start()
        options = webdriver.ChromeOptions()
        self.driver =webdriver.Chrome() 
        self.driver.get('http://localhost:8000/pagina1/') 
        elem = self.driver.find_element_by_tag_name('h1')
        rgb = elem.value_of_css_property('color')
      
        hex = Color.from_string(rgb).hex
        self.assertTrue(hex)
        self.driver.close()

if __name__ == '__main__':
    unittest.main()