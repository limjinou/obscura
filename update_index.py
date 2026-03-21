import bs4

with open('index.html', encoding='utf-8') as f:
    html = f.read()

soup = bs4.BeautifulSoup(html, 'html.parser')

data = [
    {
        'id': 'pax-item-14',
        'title': '토요타 Motor CPD',
        'displayTitle': 'TOYOTA',
        'category': 'COMMERCIAL',
        'year': '2025',
        'role': 'FULL PROD.',
        'still': './프로젝트 아카이브/토요타 Motor CPD/Still1.jpg'
    },
    {
        'id': 'pax-item-15',
        'title': '토레스 EVX',
        'displayTitle': 'TORRES',
        'category': 'COMMERCIAL',
        'year': '2023',
        'role': 'GAFFER',
        'still': './프로젝트 아카이브/토레스 EVX/Still1.jpg'
    },
    {
        'id': 'pax-item-16',
        'title': '셀파렉스 루틴챌린지 (차준환)',
        'displayTitle': 'CELL',
        'category': 'COMMERCIAL',
        'year': '2023',
        'role': 'GAFFER',
        'still': './프로젝트 아카이브/셀파렉스 루틴챌린지 (차준환)/Still1.png'
    },
    {
        'id': 'pax-item-17',
        'title': '이자카야 산주코루 홍보영상',
        'displayTitle': 'IZAKAYA',
        'category': 'PRODUCTION',
        'year': '2025',
        'role': 'FULL PROD.',
        'still': './프로젝트 아카이브/이자카야 산주코루 홍보영상/Still1.jpg'
    },
    {
        'id': 'pax-item-18',
        'title': '풍류 행사 영상 스케치',
        'displayTitle': 'PUNGNYU',
        'category': 'PRODUCTION',
        'year': '2024',
        'role': 'FULL PROD.',
        'still': './프로젝트 아카이브/풍류 행사 영상 스케치/Still1.jpg'
    }
]

stack = soup.select('.pax-bg-stack')[0]
track = soup.select('.pax-track')[0]

for p in data:
    img = soup.new_tag('img', alt=p['title'], src=p['still'])
    img['class'] = 'pax-bg-plate'
    img['data-id'] = p['id']
    stack.append(img)
    stack.append(bs4.NavigableString('\n                '))

    thumb = soup.new_tag('div', attrs={
        'class': 'pax-thumb-item',
        'data-category': p['category'],
        'data-dir': f"{p['category']} // {p['role']}",
        'data-target': p['id'],
        'data-title': p['title']
    })
    
    wrapper = soup.new_tag('div', attrs={'class': 'pax-thumb-image-wrapper'})
    w_img = soup.new_tag('img', alt=p['title'], src=p['still'])
    wrapper.append(w_img)
    thumb.append(wrapper)
    
    meta = soup.new_tag('div', attrs={'class': 'pax-metadata-panel'})
    
    lbl1 = soup.new_tag('span', attrs={'class': 'pax-meta-lbl'})
    lbl1.string = 'Client'
    val1 = soup.new_tag('span', attrs={'class': 'pax-meta-val'})
    val1.string = p['title']
    
    lbl2 = soup.new_tag('span', attrs={'class': 'pax-meta-lbl'})
    lbl2.string = 'Type'
    val2 = soup.new_tag('span', attrs={'class': 'pax-meta-val'})
    val2.string = p['category']
    
    lbl3 = soup.new_tag('span', attrs={'class': 'pax-meta-lbl'})
    lbl3.string = 'Role'
    val3 = soup.new_tag('span', attrs={'class': 'pax-meta-val'})
    val3.string = p['role']
    
    lbl4 = soup.new_tag('span', attrs={'class': 'pax-meta-lbl'})
    lbl4.string = 'Year'
    val4 = soup.new_tag('span', attrs={'class': 'pax-meta-val'})
    val4.string = p['year']
    
    for meta_node in [lbl1, val1, lbl2, val2, lbl3, val3, lbl4, val4]:
        meta.append(meta_node)
        
    thumb.append(meta)
    
    track.append(thumb)
    track.append(bs4.NavigableString('\n                        '))


with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))
print('Successfully added 5 new projects to index.html')
