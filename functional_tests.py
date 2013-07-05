import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # get the homepage of the app
        self.browser.get('http://localhost:8000')
        self.assertIn('To-Do', self.browser.title)
        # check header of page
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        # enter some input into the page
        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(input_box.get_attribute('placeholder'), 'Enter a to-do item')
        input_box.send_keys('Buy peacock feathers')
        input_box.send_keys(Keys.ENTER)
        # get the table from the response
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(any(row.text == '1: Buy peacock feathers' for row in rows),
                        "New to-do item did not appear in table")
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main()


browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'Django' in browser.title
browser.quit()
