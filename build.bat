@echo off
echo Building ED Material Tracker...
echo.

pip install pyinstaller --quiet 2>nul

pyinstaller --onefile --windowed --name "ED_Material_Tracker" ^
    --add-data "ed_material_tracker.py;." ^
    ed_material_tracker.py

echo.
echo Done! Executable is in: dist\ED_Material_Tracker.exe
pause
