@ECHO OFF
REM set date_time_str=%DATE:~10,4%-%DATE:~7,2%-%DATE:~4,2% %TIME:~0,2%:%TIME:~3,2%:%TIME:~6,2%

set todaystr=%DATE:~10,4%%DATE:~7,2%%DATE:~4,2%
set base_path=%USERPROFILE%\Desktop\%todaystr%
REM echo %base_path%
REM - check if latest path exists, creates if needs be
IF EXIST %base_path% (
		echo %base_path% exists
	) ELSE (
		echo %base_path% does not exist
		mkdir %base_path%
	)
REM - Opens latest rolder
explorer %base_path%

@ECHO ON