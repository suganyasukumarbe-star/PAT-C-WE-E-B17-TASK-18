from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException


class BasePage:
    """Parent class providing foundational Selenium wrappers with robust exception handling."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def navigate_to(self, url):
        try:
            self.driver.get(url)
        except Exception as e:
            print(f"Error navigating to {url}: {str(e)}")
            raise e

    def find_element(self, locator):
        try:
            return self.wait.until(EC.presence_of_element_frame_to_be_available_and_switch_to_it(locator))
        except TimeoutException:
            raise TimeoutException(f"Element with locator {locator} not found within time limit.")
        except NoSuchElementException:
            raise NoSuchElementException(f"Element with locator {locator} does not exist on the page.")

    def click_element(self, locator):
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except ElementClickInterceptedException:
            raise ElementClickInterceptedException(f"Click blocked on element: {locator}")
        except TimeoutException:
            raise TimeoutException(f"Element {locator} not clickable within time limit.")

    def send_keys_to_element(self, locator, text):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            element.clear()
            element.send_keys(text)
        except TimeoutException:
            raise TimeoutException(f"Element {locator} not visible to input text.")

    def is_element_displayed(self, locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()
        except TimeoutException:
            return False
