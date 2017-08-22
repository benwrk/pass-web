python.exe -m pip install virtualenv;
virtualenv env;
env\Scripts\activate;
pip install -r requirements.txt;
[System.Console]::WriteLine("Setup finished. Please see log above for errors and warnings.");
