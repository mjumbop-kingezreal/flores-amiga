import pathlib, urllib.request, re, json
root=pathlib.Path(__file__).parent
ua='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
def fetch(url):
 return urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':ua}),timeout=30).read()
items=[('cormorant-garamond-latin','Cormorant+Garamond:wght@400','https://fonts.gstatic.com/s/cormorantgaramond/v21/co3umX5slCNuHLi8bLeY9MK7whWMhyjypVO7abI26QOD_v86GnM.ttf'),('cormorant-garamond-italic-latin','Cormorant+Garamond:ital,wght@1,400','https://fonts.gstatic.com/s/cormorantgaramond/v21/co3smX5slCNuHLi8bLeY9MK7whWMhyjYrGFEsdtdc62E6zd58jDOjw.ttf'),('manrope-latin','Manrope:wght@400','https://fonts.gstatic.com/s/manrope/v20/xn7_YHE41ni1AdIRqAuZuw1Bx9mbZk79FO_F.ttf')]
results=[]
for name,family,ttf_url in items:
 css=fetch('https://fonts.googleapis.com/css2?family='+family+'&display=swap').decode()
 (root/(name+'.css')).write_text(css)
 urls=re.findall(r'url\(([^)]+\.woff2)\)',css)
 if urls:
  url=urls[-1]; out=root/(name+'.woff2'); out.write_bytes(fetch(url)); print(str(out),out.stat().st_size,flush=True)
  results.append({'file':str(out),'source':url,'format':'woff2'})
 else:
  out=root/(name+'.ttf'); out.write_bytes(fetch(ttf_url)); print(str(out),out.stat().st_size,flush=True)
  results.append({'file':str(out),'source':ttf_url,'format':'ttf'})
for family in ['cormorantgaramond','manrope']:
 url='https://raw.githubusercontent.com/google/fonts/main/ofl/'+family+'/OFL.txt'
 (root/(family+'-OFL.txt')).write_bytes(fetch(url))
(root/'font-sources.json').write_text(json.dumps(results,indent=2))
