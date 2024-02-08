# Cellenium

Projects name came from Selenium that is integrated with Excel Cells, thus 
makes a very convenient way to test and keep the data visual and easy to maintain.

### _setup_

1. navigate to core\environment\setup.py
   * at main run create method
   * activate venv from venv\scripts\activate.bat or activate.ps1
   
2. Download credentials json from google cloud platform:
   * navigate to: https://console.cloud.google.com/welcome/new
   * login with your user
   * api services -> credentials  
   * click on + create credentials 
   * click on API Key
   * download json file 
   * change it to credentials.json (not mandatory)

3. Edit GOOGLE_SHEET_JSON variable to use Google sheets:
   * navigate to \core\infrastructure\constants\data.py
   * edit GOOGLE_SHEET_JSON variable with your downloaded credentials.json path.

4. Fill tests\_data\test_suite.xlsx file and start to write your tests.

5. Fill the elements in the tests\_data\page_base.xlsx

6. navigate to tests\test_main.py and run _test_main_ function to run the tests.
   _report=True_ for allure report. 


_You're ready to go._
