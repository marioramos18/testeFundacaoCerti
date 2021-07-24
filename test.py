from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import requests

LIMIT_RANGE = 99999
MIN_RANGE = -99999
BASE_URL = "http://177.71.114.188/"
      
class APITestCase(unittest.TestCase):
   
    def test_invalid_data(self):
        request_result = requests.get(BASE_URL)
        self.assertEqual(' Invalid data\n', request_result.text, 'first value and second value are not equal')
     
    def test_invalid_max_range(self):
       exceeded_limit_range = str(LIMIT_RANGE + 1)
       request_result = requests.get(BASE_URL + exceeded_limit_range)
       self.assertEqual(' Invalid range\n', request_result.text, 'invalid limit range')
    
    def test_invalid_min_range(self):
        less_minimum_range = str(MIN_RANGE - 1)
        request_result = requests.get(BASE_URL + less_minimum_range)
        self.assertEqual(' Invalid range\n', request_result.text, 'invalid minimum range')
   
    def test_must_return_english_data(self):
        request_result = requests.get(BASE_URL +'en/5')
        expected = { 'full': 'five' }
        self.assertEqual(expected, request_result.json())

    def test_must_return_full_limit_range_ptbr(self):
        request_result = requests.get(BASE_URL + str(LIMIT_RANGE))
        expected = { 'extenso' : 'noventa e nove mil e novecentos e noventa e nove' }
        self.assertEqual(expected, request_result.json())
    
    def test_must_return_full_limit_range_en(self):
        request_result = requests.get(BASE_URL + 'en/' + str(LIMIT_RANGE))
        expected = { 'full' : 'ninety nine thousand nine hundred ninety nine' }
        self.assertEqual(expected,  request_result.json())

    def test_must_return_full_minus_limit_range_ptbr(self):
        request_result = requests.get(BASE_URL + str(MIN_RANGE))
        expected = { 'extenso' : 'menos noventa e nove mil e novecentos e noventa e nove' }
        self.assertEqual(expected, request_result.json())

    def test_must_return_full_minus_limit_range_en(self):
        request_result = requests.get(BASE_URL + 'en/' + str(MIN_RANGE))
        expected = { 'full' : 'minus ninety nine thousand nine hundred ninety nine'}
        self.assertEqual(expected, request_result.json())

class APIInterfaceTestCase(unittest.TestCase):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    
    def test_invalid_data(self):
        self.driver.get(BASE_URL)
        result = self.driver.find_element_by_xpath('/html/body/pre').text
        expected = 'Invalid data'
        assert expected in result

    def test_invalid_max_range(self):
        self.driver.get(BASE_URL + str(LIMIT_RANGE + 1))
        result = self.driver.find_element_by_xpath('/html/body/pre').text
        expected = 'Invalid range'
        assert expected in result
        
    def test_invalid_min_range(self):
        self.driver.get(BASE_URL + str(MIN_RANGE - 1))
        result = self.driver.find_element_by_xpath('/html/body/pre').text
        expected = 'Invalid range'
        assert expected in result 

    def test_must_return_en_data(self):
        self.driver.get(BASE_URL + 'en/5')
        result = self.driver.find_element_by_xpath('/html/body/pre').text
        expected = '{ "full": "five" }'
        assert expected in result
    
    def test_must_return_full_limit_range_ptbr(self):
        self.driver.get(BASE_URL + str(LIMIT_RANGE))
        result = self.driver.find_element_by_xpath('/html/body/pre').text
        expected = '{ "extenso": "noventa e nove mil e novecentos e noventa e nove" }'
        assert expected in result

    def test_must_return_full_limit_range_en(self):
        self.driver.get(BASE_URL + 'en/' + str(LIMIT_RANGE))
        result = self.driver.find_element_by_xpath('/html/body/pre').text
        expected = '{ "full": "ninety nine thousand nine hundred ninety nine" }'
        assert expected in result

    def test_must_full_minus_limit_range_ptbr(self):
        self.driver.get(BASE_URL + str(MIN_RANGE))
        result = self.driver.find_element_by_xpath('/html/body/pre').text
        expected = '{ "extenso": "menos noventa e nove mil e novecentos e noventa e nove" }'
        assert expected in result

    def test_must_return_full_minus_limit_range_en(self):
        self.driver.get(BASE_URL + 'en/' + str(MIN_RANGE))
        result = self.driver.find_element_by_xpath('/html/body/pre').text
        expected = '{ "full": "minus ninety nine thousand nine hundred ninety nine" }'
        assert expected in result

if __name__ == "__main__":
    unittest.main()
