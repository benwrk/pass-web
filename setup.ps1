Remove-Item -Recurse -Force env;
Start-Process python.exe -ArgumentList '-m pip install virtualenv --no-cache-dir' -Verb RunAs -Wait;
virtualenv env;
env\Scripts\activate;
pip install -r requirements.txt --no-cache-dir;
python.exe manage.py makemigrations service_app;
