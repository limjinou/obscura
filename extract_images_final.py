
import urllib.request
import urllib.error
import os
import re

# Final Project List for the Workspace
projects = [
    {
        "name": "토요타 Motor CPD",
        "url": "https://instantclassicfilm.com/trendz-glow-4",
        "type": "ICF"
    },
    {
        "name": "토레스 EVX",
        "url": "https://instantclassicfilm.com/gs",
        "type": "ICF"
    },
    {
        "name": "셀파렉스 루틴챌린지 (차준환)",
        "url": "https://instantclassicfilm.com/16840f08294b13",
        "type": "ICF"
    },
    {
        "name": "이자카야 산주코루 홍보영상",
        "id": "work004",
        "type": "LOOKUP"
    },
    {
        "name": "풍류 행사 영상 스케치",
        "id": "work005",
        "type": "LOOKUP"
    }
]

base_dir = r"c:\Users\임진우\OneDrive\Desktop\obscura\프로젝트 아카이브"

def download_image(url, path):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            with open(path, "wb") as out_file:
                out_file.write(response.read())
        return True
    except Exception as e:
        return False

def download_stills():
    for p in projects:
        print(f"Processing: {p['name']}")
        target_dir = os.path.join(base_dir, p['name'])
        if not os.path.exists(target_dir):
            os.makedirs(target_dir, exist_ok=True)

        stills = []
        if p['type'] == "ICF":
            try:
                # Scrape HTML for image URLs using urllib
                req = urllib.request.Request(p['url'], headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req) as response:
                    html = response.read().decode('utf-8', errors='ignore')
                
                # Find direct image URLs in common Squarespace pattern
                found_imgs = re.findall(r'https?://[^\s\"\'\(\)]+[\w-]\.(?:jpg|jpeg|png|webp)', html)
                
                for img in list(set(found_imgs)):
                    if any(x in img.lower() for x in ['logo', 'icon', 'nav', 'avatar', 'profile', 'facebook', 'instagram', 'squarespace-icon']):
                        continue
                    if 'static1.squarespace.com' in img or 'squarespace-cdn.com' in img:
                        stills.append(img)
                    elif 'images.unsplash.com' in img:
                        stills.append(img)
            except Exception as e:
                print(f"Error scraping {p['name']}: {e}")
        
        elif p['type'] == "LOOKUP":
            stills.append(f"https://lookupmedia.co.kr/images/works/{p['id']}/thumb.png")
            for i in range(1, 15):
                 stills.append(f"https://lookupmedia.co.kr/images/works/{p['id']}/still{i}.jpeg")
                 stills.append(f"https://lookupmedia.co.kr/images/works/{p['id']}/still{i}.jpg")
        
        # Download at least 5
        count = 1
        for s_url in stills:
            if count > 5:
                break
            
            ext = s_url.split('.')[-1].split('?')[0].lower()
            if ext not in ['jpg', 'jpeg', 'png', 'webp']: ext = 'jpg'
            
            filename = f"Still{count}.{ext}"
            filepath = os.path.join(target_dir, filename)
            
            if download_image(s_url, filepath):
                print(f"  Saved {filename}")
                count += 1
                
        print(f"Total downloaded for {p['name']}: {count-1}")

if __name__ == "__main__":
    download_stills()
