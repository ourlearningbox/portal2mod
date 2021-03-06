SET STEAM_FOLDER=C:\Users\Pichau\Programas\Steam\

SET ORIG_FOLDER=%~dp0
SET VSCRIPT_FILES=*.nut
SET MAP_FILES=*.bsp
SET ORIG_VSCRIPT_FOLDER=nut_scripts\
SET ORIG_MAP_FOLDER=maps\
SET ORIG_VSCRIPT_FILES=%ORIG_FOLDER%%ORIG_VSCRIPT_FOLDER%%VSCRIPT_FILES%
SET ORIG_MAP_FILES=%ORIG_FOLDER%%ORIG_MAP_FOLDER%%MAP_FILES%

SET PORTAL2_FOLDER=steamapps\common\Portal 2\portal2\
SET PORTAL2_FOLDER=%STEAM_FOLDER%%PORTAL2_FOLDER%
SET VSCRIPT_FOLDER=scripts\vscripts\
SET VSCRIPT_FOLDER=%PORTAL2_FOLDER%%VSCRIPT_FOLDER%
SET MAP_FOLDER=maps\
SET MAP_FOLDER=%PORTAL2_FOLDER%%MAP_FOLDER%

IF EXIST %STEAM_FOLDER% (
    IF EXIST %VSCRIPT_FOLDER% (
        xcopy "%ORIG_VSCRIPT_FILES%" "%VSCRIPT_FOLDER%" /sy
        IF EXIST %MAP_FOLDER% (
            xcopy "%ORIG_MAP_FILES%" "%MAP_FOLDER%" /sy
        ) ELSE (
            ECHO "VSCRIPT FOLDER NOT FOUND."
            ECHO "OPEN install.bat AND EDIT MAP_FOLDER VARIABLE ACCORDINGLY."
            PAUSE
        )
    ) ELSE (
        ECHO "VSCRIPT FOLDER NOT FOUND."
        ECHO "OPEN install.bat AND EDIT VSCRIPT_FOLDER VARIABLE ACCORDINGLY."
        PAUSE
    )
) ELSE (
    ECHO "STEAM FOLDER NOT FOUND."
    ECHO "OPEN install.bat AND EDIT STEAM_FOLDER VARIABLE ACCORDINGLY."
    PAUSE
)
