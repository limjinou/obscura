
import urllib.request
import os

# Confirmed ID for Cha Jun-hwan
cha_id = "79j-3u6uW80"
# Guessing Toyota ID from search results or common car commercial patterns
toyota_id = "9Vq_6K3w_4A" # Dummy if not found, let's search one last time

projects = [
    {
        "name": "셀파렉스 루틴챌린지 (차준환)",
        "id": cha_id,
        "frames": ["maxresdefault", "0", "1", "2", "3"]
    }
]

base_dir = r"c:\Users\임진우\OneDrive\Desktop\obscura\프로젝트 아카이브"

def download():
    for item in projects:
        target_dir = os.path.join(base_dir, item['name'])
        os.makedirs(target_dir, exist_ok=True)
        for i, frame in enumerate(item['frames']):
            url = f"https://img.youtube.com/vi/{item['id']}/{frame}.jpg"
            filepath = os.path.join(target_dir, f"Still{i+1}.jpg")
            try:
                req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req) as resp:
                    with open(filepath, "wb") as f:
                        f.write(resp.read())
                print(f"Saved {item['name']} Still{i+1}")
            except: pass

if __name__ == "__main__":
    download()
