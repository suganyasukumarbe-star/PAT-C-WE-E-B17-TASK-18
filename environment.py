from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def before_scenario(context, scenario):
    # Sets up the execution driver before every test case execution
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def after_scenario(context, scenario):
    # Safely releases driver processes after scenarios conclude
    if hasattr(context, 'driver'):
        context.driver.quit()
