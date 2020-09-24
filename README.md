# PyCLONE
Tool for automating daily activities

**Instructions to use:**

 1. Clone the repo
 2. Install packages from requirements.txt
```
pip install -r requirements.txt
```  
 3. (case 1)Download geckodriver from below link and provide path of geckodriver in script   
 ```
 browser = webdriver.Firefox(executable_path=r'YOUR_GECKODRIVER_PATH')
 ```
 https://github.com/mozilla/geckodriver/releases
 
 4. (case 2) This script tells you time duration time since when in current company .Replace your joining date in script 
```
joining_day = datetime.date(year, month, day)
```
 5. Create python module out of this script
 ```
python setup.py sdist
python setup.py install
 ```
 6. Run module from any path on cmd 
 ```
 python -m pyclone
 ```
