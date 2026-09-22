"""Prepara fuentes locales y una pequeña melodía instrumental original."""
from pathlib import Path
import math, urllib.request, wave, array

root = Path(__file__).parent / 'dist' / 'assets'
fonts = root / 'fonts'
fonts.mkdir(exist_ok=True)
font_urls = {
    'cormorant-garamond-latin.woff2': 'https://fonts.gstatic.com/s/cormorantgaramond/v21/co3umX5slCNuHLi8bLeY9MK7whWMhyjypVO7abI26QOD_v86KnTOig.woff2',
    'cormorant-garamond-italic-latin.woff2': 'https://fonts.gstatic.com/s/cormorantgaramond/v21/co3smX5slCNuHLi8bLeY9MK7whWMhyjYrGFEsdtdc62E6zd58jD-iNM8.woff2',
    'manrope-latin.woff2': 'https://fonts.gstatic.com/s/manrope/v20/xn7_YHE41ni1AdIRqAuZuw1Bx9mbZk79FN_C-bk.woff2'
}
for filename, url in font_urls.items():
    target = fonts / filename
    target.write_bytes(urllib.request.urlopen(url,timeout=45).read())
    print(target.name,target.stat().st_size)
(fonts / 'README.txt').write_text('Cormorant Garamond y Manrope: Google Fonts, SIL Open Font License.\nhttps://fonts.google.com/specimen/Cormorant+Garamond\nhttps://fonts.google.com/specimen/Manrope\n',encoding='utf8')

# Arpegios originales Cmaj7 / Am7 / Fmaj7 / Gsus: sin muestras ni grabaciones ajenas.
rate=22050
duration=48
samples=[0.]*(rate*duration)
chords=[[48,55,60,64,67,71],[45,52,57,60,64,67],[41,48,53,57,60,64],[43,50,55,60,62,67]]
for beat in range(64):
    midi=chords[(beat//8)%4][[0,2,3,4,5,4,3,2][beat%8]]
    freq=440*2**((midi-69)/12)
    start=int(beat*.75*rate)
    for j in range(min(int(4.5*rate),len(samples)-start)):
        t=j/rate
        envelope=(1-math.exp(-t*25))*math.exp(-t*1.35)
        tone=math.sin(2*math.pi*freq*t)+.22*math.sin(2*math.pi*freq*2*t)*math.exp(-t*2)+.06*math.sin(2*math.pi*freq*3*t)*math.exp(-t*3)
        samples[start+j]+=.16*envelope*tone
pcm=array.array('h')
for i,s in enumerate(samples):
    fade=min(1,i/(rate*2),(len(samples)-i)/(rate*4))
    pcm.append(int(max(-.95,min(.95,s))*fade*32767))
with wave.open(str(root/'audio'/'ambient.wav'),'wb') as out:
    out.setnchannels(1);out.setsampwidth(2);out.setframerate(rate);out.writeframes(pcm.tobytes())
print('ambient.wav',len(pcm)/rate,'seconds, original synthesized music')
