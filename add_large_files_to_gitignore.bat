@echo off
setlocal enabledelayedexpansion

set "REPO_ROOT=%~dp0"
set "GITIGNORE=%REPO_ROOT%.gitignore"
set "LIMIT=104857600"

if not exist "%GITIGNORE%" type nul > "%GITIGNORE%"

set "COUNT=0"
set "HEADER_WRITTEN=0"
echo Scanning for files over 100MB...

for /r "%REPO_ROOT%" %%F in (*) do (
    set "FILEPATH=%%F"
    set "SIZE=%%~zF"

    echo "!FILEPATH!" | findstr /i "\\\.git\\" >nul 2>&1
    if errorlevel 1 (
        if !SIZE! GTR %LIMIT% (
            set "REL=!FILEPATH:%REPO_ROOT%=!"
            set "REL=!REL:\=/!"
            set "ESCAPED=!REL:[=\[!"
            set "ESCAPED=!ESCAPED:]=\]!"

            set "FOUND=0"
            for /f "usebackq delims=" %%L in ("%GITIGNORE%") do (
                if "%%L"=="!ESCAPED!" set "FOUND=1"
            )

            if !FOUND!==0 (
                if !HEADER_WRITTEN!==0 (
                    echo.>> "%GITIGNORE%"
                    echo # Files over 100 MB (Automatically added)>> "%GITIGNORE%"
                    set "HEADER_WRITTEN=1"
                )
                echo !ESCAPED!>> "%GITIGNORE%"
                echo Added: !ESCAPED!
                set /a COUNT+=1
            )
        )
    )
)

echo.
echo Done. !COUNT! file(s) added to .gitignore.
pause
