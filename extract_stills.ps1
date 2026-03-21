
$ErrorActionPreference = "SilentlyContinue"

# Project data
$p1 = "토요타 Motor CPD"
$p2 = "토레스 EVX"
$p3 = "셀파렉스 루틴챌린지 (차준환)"
$p4 = "이자카야 산주코루 홍보영상"
$p5 = "풍류 행사 영상 스케치"

$urls = @{
    $p1 = "https://instantclassicfilm.com/trendz-glow-4";
    $p2 = "https://instantclassicfilm.com/gs";
    $p3 = "https://instantclassicfilm.com/16840f08294b13"
}

$baseDir = "c:\Users\임진우\OneDrive\Desktop\obscura\프로젝트 아카이브"

# Instant Classic Film
foreach ($name in $urls.Keys) {
    $u = $urls[$name]
    $target = Join-Path $baseDir $name
    if (-not (Test-Path $target)) { New-Item -ItemType Directory -Path $target }
    
    $req = Invoke-WebRequest -Uri $u
    $imgs = $req.Images.Src | Where-Object { $_ -match "\.(jpg|jpeg|png)$" } | Select-Object -Unique
    
    $c = 1
    foreach ($im in $imgs) {
        if ($c -gt 5) { break }
        if ($im -match "^/") { $im = "https://instantclassicfilm.com" + $im }
        $local = Join-Path $target "Still$c.jpg"
        Invoke-WebRequest -Uri $im -OutFile $local
        $c++
    }
}

# LOOKUP MEDIA (work004, work005)
$lookup = @{
    $p4 = "work004";
    $p5 = "work005"
}

foreach ($name in $lookup.Keys) {
    $id = $lookup[$name]
    $target = Join-Path $baseDir $name
    if (-not (Test-Path $target)) { New-Item -ItemType Directory -Path $target }
    
    for ($i = 1; $i -le 5; $i++) {
        $u = "https://lookupmedia.co.kr/images/works/$id/still$i.jpeg"
        $local = Join-Path $target "Still$i.jpg"
        Invoke-WebRequest -Uri $u -OutFile $local
        if (-not (Test-Path $local -PathType Leaf)) {
            # try thumb for first one
            if ($i -eq 1) {
                Invoke-WebRequest -Uri "https://lookupmedia.co.kr/images/works/$id/thumb.png" -OutFile $local
            }
        }
    }
}
