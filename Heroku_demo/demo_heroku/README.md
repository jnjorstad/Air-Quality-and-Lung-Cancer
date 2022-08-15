# demo_heroku
temporary repository for demo  
<br>

# Heroku Deployment


Resource:  
https://devcenter.heroku.com/articles/github-integration  

<br>

## Setup Repo  
1.  Make a new branch and eleminate all folders and files not related to the flask app.
1.  Add those files to the gitignore so those files can not be added back to the repo in the case of a merge from the local main branch.
1.  Add Procfile
1.  Create conda environment that matches supported versions of python - https://devcenter.heroku.com/articles/python-support#supported-runtimes 
1.  We will use `python-3.9.13`
1.  Check existing environment in terminal/gitbash:  type `conda env list`.  You can activate each environment and test the version is you are unsure with `python --version`.
1.  If you do not have an environment for this python version then first make the environment.  First check which conda environments are available.  Type `conda search python`.  Most likely an exact match doesn't exist so choose the version that is closest.  
1.  Type `conda create -n PythonData3912 python=3.9.12 anaconda`.  Type `y` when asked if to proceed.
1.  Activate the Python Environment. Check the version - `python --version`.  It should be 3.9.x.  If it is not 3.9.12 then that is okay; as long as its close.  
1.  Take note of the python packages installed in the base.  Type `conda list`
1.  Now we will test our environment with the existing files.  
1.  Create virtualenvironment `py -m venv env`
1.  Activate virtualenvironment ` source env/Scripts/activate`
1.  Next run `pip freeze > requirements.txt`.  This will create a requirements.txt file but it will be empty.  As we install packages then this file will include the package name and version.  
1.  `pip install gunicorn`
1.  `pip install flask`
1.  `pip install numpy`
1.  `pip install sklearn`
1.  Now if you rerun `pip freeze > requirements.txt` you will see the packages installed from the Python 3.9.12 environment.  
1.  Now see if you can run `app.py`.  If a module is missing then run `pip install <module name>`.  Once the app is running and works as previously, shut down the flask server.  
1.  Next run `pip freeze > requirements.txt`.
1.  Create a `runtime.txt` file that contains this one line `python-3.9.13`.  Note:  I updated this line so it matches the python version compliant with heroku.  
1.  This completes the generation of the three files needed by Heroku - `requirements.txt`, `runtime.txt`, and `Procfile`.

<br>

## Deployment Instructions
1.  Login to Heroku Dashboard
1.  Create New App
1.  Select Unique Name (next)
1.  Select Deployment Method:  Github
1.  Login to Github and grant permission
1.  Search for your repo name.
1.  Select automate updates 
1.  Deploy the desired branch.
1.  Select deploy branch button

<br>

## Generated Link:  
https://mpg-estimator.herokuapp.com/  

## Deactivate Environments
conda:  `source deactivate`
virtual environment:  `deactivate`

<br>

## Other Resources:
https://devcenter.heroku.com/articles/upgrading-to-the-latest-stack
https://elements.heroku.com/buildpacks/tensorflow/tensorflow 
https://docs.python.org/3/tutorial/venv.html#creating-virtual-environments  
https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment  