import requests

chunk = 256
url = 'Online video link that extension in vdeo formate'
r= requests.get(url,stream=True)
total_size = int(r.headers['content-length'])
print(total_size)
with open('1.mp4', 'wb') as f:
    for chunk in r.iter_content(chunk_size=chunk):
        f.write(chunk)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        