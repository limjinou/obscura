
import urllib.request
import re
import os

projects = [
    {"name": "토요타 Motor CPD", "url": "https://instantclassicfilm.com/trendz-glow-4"},
    {"name": "토레스 EVX", "url": "https://instantclassicfilm.com/gs"},
    {"name": "셀파렉스 루틴챌린지 (차준환)", "url": "https://instantclassicfilm.com/16840f08294b13"},
    {"name": "이자카야 산주코루 홍보영상", "url": "https://lookupmedia.co.kr/works.html", "id": "work004"},
    {"name": "풍류 행사 영상 스케치", "url": "https://lookupmedia.co.kr/works.html", "id": "work005"}
]

base_dir = r"c:\Users\임진우\OneDrive\Desktop\obscura\프로젝트 아카이브"

def scrape():
    for p in projects:
        name = p['name']
        print(f"Scraping {name}...")
        target_dir = os.path.join(base_dir, name)
        os.makedirs(target_dir, exist_ok=True)
        
        # Method 1: Try the direct URL
        stills = []
        try:
            req = urllib.request.Request(p['url'], headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as resp:
                html = resp.read().decode('utf-8', 'ignore')
            
            # Find all potential images
            # Squarespace often uses format like data-src="https://images.squarespace-cdn.com/content/v1/..."
            found = re.findall(r'https?://[^\s\"\'\(\)]+[\w-]\.(?:jpg|jpeg|png|webp)', html)
            found += re.findall(r'https?://images\.squarespace-cdn\.com/content/[^\s\"\'\(\)]+', html)
            
            for f in list(set(found)):
                if any(x in f.lower() for x in ['logo', 'icon', 'nav', 'avatar', 'profile', 'squarespace-icon', 'header']): continue
                stills.append(f)
        except: pass
        
        # Method 2: If Lookup Media, try the ID pattern
        if 'id' in p:
             stills.append(f"https://lookupmedia.co.kr/images/works/{p['id']}/thumb.png")
             for i in range(1, 11):
                 stills.append(f"https://lookupmedia.co.kr/images/works/{p['id']}/still{i}.jpeg")
                 # stills.append(f"https://lookupmedia.co.kr/images/works/{p['id']}/still{i}.jpg")
        
        # Download at least 5
        count = 1
        for s_url in stills:
            if count > 5: break
            
            # If it's squarespace, add format if missing
            final_url = s_url
            if 'squarespace-cdn.com' in s_url and '?' not in s_url:
                final_url = s_url + "?format=1500w"
            
            try:
                ireq = urllib.request.Request(final_url, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(ireq, timeout=10) as r:
                    content = r.read()
                    if len(content) < 10000: continue # Skip tiny images/icons
                    
                    ext = "jpg"
                    if ".png" in s_url.lower(): ext = "png"
                    
                    filename = f"Still{count}.{ext}"
                    with open(os.path.join(target_dir, filename), "wb") as f:
                        f.write(content)
                    print(f"  Saved Still{count}")
                    count += 1
            except: pass
            
        print(f"Total stills for {name}: {count-1}")

if __name__ == "__main__":
    scrape()
