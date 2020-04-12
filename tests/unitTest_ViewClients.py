# # automated unit test to ensure a window to add a new client appears
# when the "+ New" button is clicked
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

class CMS_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_cms(self):
        #login from the admin pane
        user = "akhila"
        pwd = "Gow@2805"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/admin")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000")
        assert "Logged In"
        time.sleep(5)

        # find the ‘view clients’ and click it
        elem = driver.find_element_by_xpath("/html/body/div/div/p[2]/a").click()
        time.sleep(5)
        continue_test = False
        try:
          #verify view clients page exists
            elem = driver.find_element_by_xpath("/html/body/nav/a")
            continue_test = True

        except NoSuchElementException:
            self.fail("View clients does not appear = View Clients button not present")
            assert False
            time.sleep(1)
        except:
            self.fail("View Clients NOT successful - error occurred: ")
            assert False
            time.sleep(1)
        time.sleep(2)
        #if test successful so far – set up the required inputs for a Client

def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()
