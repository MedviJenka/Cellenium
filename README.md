# Cellenium

Projects name came from Selenium that is integrated with Excel Cells, thus 
makes a very convenient way to test and keep the data visual and easy to maintain.

### _setup_

1. navigate to core\environment\environment.py
   * at main run create method
   * activate venv from venv\scripts\activate.bat or activate.ps1

2. Fill config reader path:
   * copy Cellenium project path.
   * navigate to <Project Path>\core\infrastructure\constants\data.py
   * edit GLOBAL_PATH with you project path.

3. Fill tests\_data\test_suite.xlsx file and start to write your tests.

4. Fill the elements in the tests\_data\page_base.xlsx

5. navigate to tests\test_main.py and run _test_main_ function to create virtual environment 


_You're ready to go._

