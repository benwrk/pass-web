env\Scripts\activate
Start-Process python.exe -ArgumentList 'manage.py migrate' -Wait
Start-Process python.exe -ArgumentList 'manage.py start_service --config configs\app.json'
