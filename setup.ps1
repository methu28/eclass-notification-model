$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot
py -3 -c "import sys; assert sys.version_info >= (3,12), 'Python 3.12+ required'"
if ($LASTEXITCODE -ne 0) { throw "Python 3.12 or newer is required" }
py -3 -m venv .venv
if ($LASTEXITCODE -ne 0) { throw "Could not create virtual environment" }
$python = Join-Path $PSScriptRoot ".venv\Scripts\python.exe"
& $python -m pip install --upgrade pip
if ($LASTEXITCODE -ne 0) { throw "pip upgrade failed" }
& $python -m pip install -r requirements.txt
if ($LASTEXITCODE -ne 0) { throw "Dependency install failed" }
& $python -m pytest -q
if ($LASTEXITCODE -ne 0) { throw "Tests failed" }
& $python run.py
if ($LASTEXITCODE -ne 0) { throw "Mesa run failed" }
Write-Host "Setup complete. See outputs/ for generated Mesa results."
