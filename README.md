# flaskr_blog
> This is a repository for my Python Flask server blueprint

### Virtual Environment Installation (MacOs Catalina)
 1- Create the project's base folder/directory
 
 2- Navigate to the base folder/directory (cd to it)
 
 3- Run the following command in your terminal (to create local virtual environment)

    python3 -m venv env
 
 4- Activate the virtual environment using the command below
 
    pipenv shell

you can also cd to the `venv` folder and run `. bin/activate`

5- Install dependencies using the pip3 command as shown below

    pip3 install flask


### Libraries not recognized
If libraries are not recognized it's because the env is not activated
Once you navigate to the `venv` folder and run `. bin/activate` everything
should be fine. All this is assuming that you have `pip` and `virtualenv` installed on your system.


#### Then install **virtualenv** using pip3

    sudo pip3 install virtualenv 

#### Now create a virtual environment 

    virtualenv venv 

#### Active your virtual environment:    
    
    source venv/bin/activate
    
#### Using fish shell:    
    
    source venv/bin/activate.fish

#### To deactivate:

    deactivate
    
## Set Flask environment variables
#### MacOs and Linux
    $ export FLASK_APP=flaskr
    $ export FLASK_ENV=development
    $ flask run
##### Windows cmd
    > set FLASK_APP=flaskr
    > set FLASK_ENV=development
    > flask run
#### Windows PowerShell
    > $env:FLASK_APP = "flaskr"
    > $env:FLASK_ENV = "development"
    > flask run