@Echo off
color a
IF Not Exist "%~dp0\Output" mkdir "%~dp0\Output"
python "%~dp0\704557zip.py" "%~1"
IF Exist "%~dp0\Output\xContent" rmdir /S /Q "%~dp0\Output\xContent"
pause