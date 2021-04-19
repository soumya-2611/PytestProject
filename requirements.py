#https://demo.nopcommerce.com/
#https://admin-demo.nopcommerce.com/
#import below things from settings
import pytest
import allure_pytest
import pytest_html
import xdist


# open normal cmd run pip install pytest
# C:\Users\Soumya.Mohanty>where python
# C:\Users\Soumya.Mohanty\AppData\Local\Programs\Python\Python39\python.exe
#
#
# copy C:\Users\Soumya.Mohanty\AppData\Local\Programs\Python\Python39 to windows evnt variable
#
# copy testcasepackage right click and copy path(copying absolute path)
#
# go to normal cmd and cd paste the path
#
#
# C:\Users\Soumya.Mohanty\Desktop\python39\PytestProject\testcasespackage>pytest
#
# C:\Users\Soumya.Mohanty\Desktop\python39\PytestProject\testcasespackage>cd C:\Users\Soumya.Mohanty\Desktop\python39\PytestProject\testcasespackage
#
# C:\Users\Soumya.Mohanty\Desktop\python39\PytestProject\testcasespackage>pytest -vs test_login.py

#to run testcases paralley pytest -vs -n=2 test_login.py --browse chrome(pytest xdist this is possible)

#to run html report:(from settings install pytest-metadata)
#pytest -vs -n=2 --html=C:\\Users\\Soumya.Mohanty\\Desktop\\python39\\PytestProject\\reportsfolder\\rport.html   test_login.py --browse chrome

#C:\Users\Soumya.Mohanty\Desktop\python39\PytestProject\testcasespackage>pytest -vs test_login_ddt.py

#to run sanity regression
#pytest -s -v -m "sanity or regression" --html=C:\\Users\\Soumya.Mohanty\\Desktop\\python39\\PytestProject\\reportsfolder\\rport.html  C:\\Users\\Soumya.Mohanty\\Desktop\\python39\\PytestProject\\testcasespackage\\  --browse chrome

#pytest -s -v -m "sanity and regression" --html=C:\\Users\\Soumya.Mohanty\\Desktop\\python39\\PytestProject\\reportsfolder\\rport.html  C:\\Users\\Soumya.Mohanty\\Desktop\\python39\\PytestProject\\testcasespackage\\  --browse chrome

#pytest -vs -m "sanity and regression"   C:\\Users\\Soumya.Mohanty\\Desktop\\python39\\PytestProject\\testcasespackage\\  --browse chrome


#to run run.bat
#open folder C:\Users\Soumya.Mohanty\Desktop\python39\PytestProject
#create txt file run and give extension .bat
#to comment a command   use "rem" at the starting




#https://github.com/soumya-2611/PytestProject.git

# TRIANZ+Soumya.Mohanty@TRI02L-PF2ANVAC MINGW64 ~/Desktop/python39/PytestProject
# $ git init
# Initialized empty Git repository in C:/Users/Soumya.Mohanty/Desktop/python39/PytestProject/.git/
#
# TRIANZ+Soumya.Mohanty@TRI02L-PF2ANVAC MINGW64 ~/Desktop/python39/PytestProject (master)
# $ git remote add origin https://github.com/soumya-2611/PytestProject.git
#
# TRIANZ+Soumya.Mohanty@TRI02L-PF2ANVAC MINGW64 ~/Desktop/python39/PytestProject (master)
# $ git config --global user.name "soumya"
#
# TRIANZ+Soumya.Mohanty@TRI02L-PF2ANVAC MINGW64 ~/Desktop/python39/PytestProject (master)
# $ git config --global user.email "soumya1126@gmail.com"
#
# TRIANZ+Soumya.Mohanty@TRI02L-PF2ANVAC MINGW64 ~/Desktop/python39/PytestProject (master)
# $ git status





