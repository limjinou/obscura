
import urllib.request
import re
import os

urls = [
    'https://instantclassicfilm.com/trendz-glow-4',
    'https://instantclassicfilm.com/gs',
    'https://instantclassicfilm.com/16840f08294b13'
]

targets = [
    '토요타 Motor CPD',
    '토레스 EVX',
    '셀파렉스 루틴챌린지 (차준환)'
]

base_dir = r"c:\Users\임진우\OneDrive\Desktop\obscura\프로젝트 아카이브"

def get_images():
    for i, url in enumerate(urls):
        name = targets[i]
        print(f"Scraping {name}...")
        target_dir = os.path.join(base_dir, name)
        os.makedirs(target_dir, exist_ok=True)
        
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as resp:
                html = resp.read().decode('utf-8', 'ignore')
            
            # Find images in data-src attribute or src attribute (Squarespace often uses data-src)
            found = re.findall(r'https?://[^\s\"\'\(\)]+[\w-]\.(?:jpg|jpeg|png|webp)', html)
            # Find also squarespace CDN urls specifically
            found += re.findall(r'https?://images\.squarespace-cdn\.com/content/[^\s\"\'\(\)]+', html)
            
            seen = set()
            count = 1
            for img in found:
                if count > 5: break
                # Normalize URL (remove format parameters for now)
                clean_img = img.split('?')[0]
                if clean_img in seen: continue
                seen.add(clean_img)
                
                # Filter logos
                if any(x in clean_img.lower() for x in ['logo', 'icon', 'nav', 'avatar']): continue
                
                # Add format parameter for better quality if it's squarespace
                final_url = img
                if 'squarespace-cdn.com' in img and '?' not in img:
                    final_url = img + "?format=1500w"
                
                try:
                    ireq = urllib.request.Request(final_url, headers={'User-Agent': 'Mozilla/5.0'})
                    with urllib.request.urlopen(ireq, timeout=10) as r:
                         with open(os.path.join(target_dir, f"Still{count}.jpg"), "wb") as f:
                             f.write(r.read())
                    print(f"  Saved Still{count}")
                    count += 1
                except:
                    pass
            print(f"Total for {name}: {count-1}")
        except Exception as e:
            print(f"Error {name}: {e}")

if __name__ == "__main__":
    get_images()
