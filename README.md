# PyCLONE
Tool for automating daily activities


**Feature:**
how to create installable python module
explained with two real use cases  
1. If you have joined an organisation, calculate since how many days you are there
2. Automate opening your favourite digital epaper ( its just automating opening browser and some clicks to 1 command ) 


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
 python -m pyclone daysincompany 0
 or
 python -m pyclone paper ak    

 ```
 [ak, bul, lk] are codename I have given to papers you can modify that.

when you run the command below
![cli](/images/cli.JPG)
this is final result, browser opened with window maximised and paper zoomed 
![result](/images/result.JPG)
