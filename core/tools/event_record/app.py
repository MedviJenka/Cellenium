from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class BrowserInteractionRecorder:

    def __init__(self, url):
        chrome_options = Options()
        logging_prefs = {'browser': 'ALL'}
        chrome_options.set_capability('goog:loggingPrefs', logging_prefs)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        self.url = url

    def open_url_and_inject_js(self):
        self.driver.get(self.url)
        # JavaScript to add a click event listener to the entire document
        self.driver.execute_script("""
             document.addEventListener('click', function(event) {
                 var path = event.path || (event.composedPath && event.composedPath());
                 var elementClicked = path ? path[0] : event.target;
                 console.log('Click event:', elementClicked.tagName, 'ID:', elementClicked.id, 'Class:', elementClicked.className);
             });
         """)

    def retrieve_logs(self, level='INFO'):
        logs = self.driver.get_log('browser')
        for log in logs:
            if log['level'] == level:
                print(log)

    def close_browser(self):
        self.driver.quit()


recorder = BrowserInteractionRecorder(url='https://www.google.com')
if __name__ == "__main__":
    text = input("type 'q' when you're done interacting with the page...")
    recorder.open_url_and_inject_js()

    if text == 'q':
        try:
            recorder.retrieve_logs()
        finally:
            recorder.close_browser()
