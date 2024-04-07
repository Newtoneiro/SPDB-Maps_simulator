
$initScript = ".\database\init_tables.py"
$fillScript = ".\database\fill_tables.py"

Write-Host "Running init_tables.py..."
python.exe $initScript

Write-Host "Running fill_tables.py..."
python.exe $fillScript


Write-Host "Scripts executed successfully."