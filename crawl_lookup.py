import os
import requests

projects = [
    {
        "id": "work020",
        "name": "영로",
        "date": "2025-01",
        "role": "Gaffer (Shin HyungJun)",
        "type": "Film",
        "stills": ["still1.jpg", "still2.jpg", "still3.jpg", "still4.jpg"]
    },
    {
        "id": "work006",
        "name": "태키타카",
        "date": "2025",
        "role": "Production (LOOKUP MEDIA)",
        "type": "Etc (Variety)",
        "stills": ["thumb.png"] # work006 stills array was empty in data.js, but thumbnail exists
    },
    {
        "id": "work024",
        "name": "두번의 장례",
        "date": "2025-04",
        "role": "Gaffer (Shin HyungJun)",
        "type": "Film",
        "stills": ["still1.jpg", "still2.jpg", "still3.jpg", "still4.jpg"]
    },
    {
        "id": "work022",
        "name": "트로픽",
        "date": "2025-04",
        "role": "Gaffer (Shin HyungJun)",
        "type": "Film",
        "stills": ["still1.jpg", "still2.jpg", "still3.jpg", "still4.jpg"]
    }
]

# For 태키타카, if stills are empty, maybe we can try still1.png just in case? Or use thumbnail.
# Or check if there are common patterns.
# I'll check work006 images folder pattern.

base_url = "https://lookupmedia.co.kr/images/works/"
output_base = "프로젝트 아카이브"

def download_images():
    for p in projects:
        print(f"Processing {p['name']} ({p['id']})...")
        folder = os.path.join(output_base, p['name'])
        if not os.path.exists(folder):
            os.makedirs(folder)
        
        # Save info.txt
        info_path = os.path.join(folder, "정보.txt")
        with open(info_path, "w", encoding="utf-8") as f:
            f.write(f"프로젝트명: {p['name']}\n")
            f.write(f"구분: {p['type']}\n")
            f.write(f"날짜: {p['date']}\n")
            f.write(f"역할: {p['role']}\n")
        
        # Download stills
        for i, s in enumerate(p['stills']):
            url = f"{base_url}{p['id']}/{s}"
            print(f"Downloading {url}...")
            try:
                r = requests.get(url, timeout=10)
                if r.status_code == 200:
                    ext = s.split('.')[-1]
                    file_name = f"Still{i+1}.{ext}"
                    with open(os.path.join(folder, file_name), "wb") as f:
                        f.write(r.content)
                    print(f"Saved {file_name}")
                else:
                    # Try jpeg if jpg fails
                    if '.jpg' in s:
                        url2 = url.replace('.jpg', '.jpeg')
                        r2 = requests.get(url2, timeout=10)
                        if r2.status_code == 200:
                            file_name = f"Still{i+1}.jpeg"
                            with open(os.path.join(folder, file_name), "wb") as f:
                                f.write(r2.content)
                            print(f"Saved {file_name} (jpeg)")
                            continue
                    print(f"Failed to download {url} (Status {r.status_code})")
            except Exception as e:
                print(f"Error {url}: {e}")

download_images()
