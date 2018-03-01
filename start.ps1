if (Get-Item * -Include env) {
    Write-Output "[StartScript] Activating virtual environment...";
    env\Scripts\activate;
    Write-Output "[StartScript] Making Django migrations...";
    Start-Process python.exe -ArgumentList 'manage.py migrate' -Wait -NoNewWindow;
    Write-Output "[StartScript] Starting...";
    Start-Process python.exe -ArgumentList 'manage.py start_service --config configs\app.json' -NoNewWindow;
} else {
    Write-Warning "No environment found, running 'setup'";
    Start-Process cmd.exe -ArgumentList '/C setup.bat' -Wait -NoNewWindow;
    Start-Process cmd.exe -ArgumentList '/C start.bat' -NoNewWindow;
}
