import os
import requests
import re
from urllib.parse import urljoin

projects = [
    {"name": "SMTECH", "url": "https://instantclassicfilm.com/arte-1"},
    {"name": "ARTE", "url": "https://instantclassicfilm.com/master-card"},
    {"name": "유명한 아이 - Master card", "url": "https://instantclassicfilm.com/ride-or-die-feathash-swan"},
    {"name": "다농바이오", "url": "https://instantclassicfilm.com/trendz-glow"},
    {"name": "수돗물 공익 캠페인", "url": "https://instantclassicfilm.com/trendz-glow-3"}
]

base_dir = "프로젝트 아카이브"

def fetch_and_save(project):
    print(f"Fetching {project['name']} from {project['url']}...")
    try:
        r = requests.get(project['url'], timeout=10, headers={'User-Agent': 'Mozilla/5.0'})
        if r.status_code == 200:
            # Look for Adobe Portfolio images with hash
            # Pattern: https://cdn.myportfolio.com/...jpg?h=...
            matches = re.findall(r'https://cdn\.myportfolio\.com/[^\"\' ]+\?(?:h=[a-f0-9]+|[^\"\' ]+)', r.text)
            
            if matches:
                # Prioritize rw_1920 or similar
                img_url = matches[0]
                for m in matches:
                    if '_rw_1920.jpg' in m or '_rw_1200.jpg' in m:
                        img_url = m
                        break
                
                print(f"Found image: {img_url}")
                img_r = requests.get(img_url, timeout=10, headers={'User-Agent': 'Mozilla/5.0'})
                if img_r.status_code == 200:
                    dir_path = os.path.join(base_dir, project['name'])
                    if not os.path.exists(dir_path):
                        os.makedirs(dir_path)
                    
                    ext = "png" if ".png" in img_url.lower() else "jpg"
                    file_path = os.path.join(dir_path, f"Still1.{ext}")
                    
                    with open(file_path, "wb") as f:
                        f.write(img_r.content)
                    print(f"Saved to {file_path}")
                else:
                    print(f"Failed to download image (Code {img_r.status_code}) from {img_url}")
            else:
                print("No images found on page.")
        else:
            print(f"Failed to load page: {r.status_code}")
    except Exception as e:
        print(f"Error: {e}")

for p in projects:
    fetch_and_save(p)
    print("-" * 20)
