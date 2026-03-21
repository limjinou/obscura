
@echo off
setlocal enabledelayedexpansion

REM Pungnyu (work005)
set "target=프로젝트 아카이브\풍류 행사 영상 스케치"
if not exist "!target!" mkdir "!target!"
for /L %%i in (1,1,5) do (
    echo Downloading Pungnyu Still %%i...
    curl -f -o "!target!\Still%%i.jpg" "https://lookupmedia.co.kr/images/works/work005/still%%i.jpeg"
)

REM Izakaya (work004)
set "target=프로젝트 아카이브\이자카야 산주코루 홍보영상"
if not exist "!target!" mkdir "!target!"
echo Downloading Izakaya Still 1 (Thumb)...
curl -f -o "!target!\Still1.jpg" "https://lookupmedia.co.kr/images/works/work004/thumb.png"
for /L %%i in (1,1,4) do (
    set /a next=%%i+1
    echo Downloading Izakaya Still !next!...
    curl -f -o "!target!\Still!next!.jpg" "https://lookupmedia.co.kr/images/works/work004/still%%i.jpeg"
)
