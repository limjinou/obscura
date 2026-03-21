
import urllib.request
import os

# Confirmed IDs from YouTube
# For Toyota, we'll try a common ID or skip if not found
yt_data = [
    {
        "name": "토레스 EVX",
        "id": "Tlk1sRwUlks",
        "frames": ["maxresdefault", "0", "1", "2", "3"]
    },
    {
        "name": "셀파렉스 루틴챌린지 (차준환)",
        "id": "F072S_eJk_s",
        "frames": ["maxresdefault", "0", "1", "2", "3"]
    },
    {
        "name": "이자카야 산주코루 홍보영상",
        "id": "cFpCfgA204Y",
        "frames": ["maxresdefault", "0", "1", "2", "3"]
    }
]

base_dir = r"c:\Users\임진우\OneDrive\Desktop\obscura\프로젝트 아카이브"

def download():
    for item in yt_data:
        print(f"Processing {item['name']}...")
        target_dir = os.path.join(base_dir, item['name'])
        os.makedirs(target_dir, exist_ok=True)
        
        for i, frame in enumerate(item['frames']):
            url = f"https://img.youtube.com/vi/{item['id']}/{frame}.jpg"
            filename = f"Still{i+1}.jpg"
            filepath = os.path.join(target_dir, filename)
            
            try:
                # Use a proper User-Agent to avoid blocks
                req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req, timeout=10) as resp:
                    with open(filepath, "wb") as f:
                        f.write(resp.read())
                print(f"  Saved {filename}")
            except Exception as e:
                print(f"  Failed {filename}: {e}")

if __name__ == "__main__":
    download()
