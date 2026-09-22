import urllib.request, pathlib, io, json, concurrent.futures
from PIL import Image, ImageOps, ImageDraw
root=pathlib.Path(__file__).parent
items=[
('sunflower-field','https://images.unsplash.com/photo-1599270613570-a620f2e59f75?w=1100&q=85&fit=max','https://unsplash.com/photos/sunflower-field-under-blue-sky-during-sunset-kW1P8R-UoWI','todd kent','Unsplash'),
('yellow-bouquet','https://images.pexels.com/photos/5987197/pexels-photo-5987197.jpeg?w=1000&auto=compress','https://www.pexels.com/photo/bouquet-of-yellow-flowers-in-vase-5987197/','Jill Burrow','Pexels'),
('yellow-tulips','https://images.unsplash.com/photo-1612072589004-1ab4c720dc13?w=1000&q=85&fit=max','https://unsplash.com/photos/yellow-tulips-bouquet-on-white-surface-I-EPxSc_ics','Birgith Roosipuu','Unsplash'),
('sunset-flowers','https://images.pexels.com/photos/7819667/pexels-photo-7819667.jpeg?w=1100&auto=compress','https://www.pexels.com/photo/photo-of-a-sunflower-field-during-sunset-7819667/','Ömer Hakkı','Pexels'),
('pressed-flowers','https://images.pexels.com/photos/11591470/pexels-photo-11591470.jpeg?w=1000&auto=compress','https://www.pexels.com/photo/pressed-flowers-and-a-leaf-on-a-white-paper-11591470/','Merve Bayar','Pexels'),
('close-sunflower','https://images.pexels.com/photos/36789591/pexels-photo-36789591.jpeg?w=1000&auto=compress','https://www.pexels.com/photo/close-up-of-a-vibrant-yellow-sunflower-bloom-36789591/','Dr Photographer','Pexels')]
def fetch(item):
 name,url,page,author,provider=item
 raw=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=35).read()
 im=ImageOps.exif_transpose(Image.open(io.BytesIO(raw))).convert('RGB'); im.thumbnail((1100,1100),Image.Resampling.LANCZOS)
 out=root/(name+'.webp'); im.save(out,'WEBP',quality=84,method=6)
 result=dict(name=name,path=str(out),image_url=url,source_url=page,author=author,provider=provider,license_url='https://unsplash.com/license' if provider=='Unsplash' else 'https://www.pexels.com/license/',size=out.stat().st_size,dimensions=im.size)
 print(json.dumps(result),flush=True); return result
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool: results=list(pool.map(fetch,items))
(root/'sources.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
sheet=Image.new('RGB',(900,680),'#efe6d2'); draw=ImageDraw.Draw(sheet)
for i,r in enumerate(results):
 im=Image.open(r['path']); im=ImageOps.fit(im,(280,300))
 x=10+(i%3)*300; y=10+(i//3)*340; sheet.paste(im,(x,y)); draw.text((x,y+306),r['name'],fill='#302519')
sheet.save(root/'contact-sheet.jpg',quality=90)
