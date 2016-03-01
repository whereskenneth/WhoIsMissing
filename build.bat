"C:\Python34\python.exe" setup.py py2exe
for /f %%i in ('C:\Python34\python.exe -c "from __version__ import __version__; print(__version__)"') do set VERSION=%%i
"C:\Program Files (x86)\NSIS\makensis.exe" /DVERSION=v%VERSION% dist/who_is_missing.nsi