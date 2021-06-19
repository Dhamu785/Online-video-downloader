#importing the module
import requests


#Size 
chunk = 256

#Link of the online video
url = 'Online video link that extension in vdeo formate'

#To get the details of the video
r= requests.get(url,stream=True)

#To find the total size of the video
total_size = int(r.headers['content-length'])
print(total_size)

#To open a file in write bytes mode
with open('1.mp4', 'wb') as f:
  
    #To get the content of the video by bytes
    for chunk in r.iter_content(chunk_size=chunk):
      
        #To write the bytes in the opened file
        f.write(chunk)
