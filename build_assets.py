from pathlib import Path
from html import escape
import math
ROOT=Path(__file__).resolve().parent
A=ROOT/'assets'
BG='#111820';FG='#f2f4ee';MUTED='#9caeb9';LINE='#2b3946';LIME='#c7f36b'
def svg(w,h,body):
 return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img"><rect width="{w}" height="{h}" rx="22" fill="{BG}"/>{body}</svg>'
def text(x,y,s,size=16,color=FG,weight=400,spacing=0):
 return f'<text x="{x}" y="{y}" font-family="Arial, Helvetica, sans-serif" font-size="{size}" font-weight="{weight}" letter-spacing="{spacing}" fill="{color}">{escape(s)}</text>'
def path(d,color=LINE,width=1,extra=''):
 return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{width}" {extra}/>'
body=text(48,50,'ASTEROID—DESTROYER777',14,LIME,700,2)+text(48,104,'TIMОFEI / ТИМОФЕЙ',14,MUTED,400,1)
body+=text(43,193,'FROM DATA',86,FG,700,-4)+text(43,280,'TO DECISIONS.',86,FG,700,-4)
body+=text(48,337,'WEB SYSTEMS  /  GEOSPATIAL DATA  /  APPLIED MODELS',14,MUTED,400,1)
body+=path('M48 370H1152')+text(48,408,'BUILD · VISUALIZE · VERIFY',12,LIME,700,2)+text(904,408,'55.75° N   37.62° E',12,MUTED,400,1)
for i in range(10):
 y=95+i*24
 d='M'+ ' L'.join(f'{810+j*18},{y+math.sin(j*.36+i*.18)*28:.1f}' for j in range(20))
 body+=path(d,'#344735',1)
for r in [49,87,125]:body+=f'<ellipse cx="985" cy="202" rx="{r}" ry="{r*.64}" fill="none" stroke="{LIME if r==87 else LINE}" stroke-width="{1.5 if r==87 else 1}" transform="rotate(-32 985 202)"/>'
body+=path('M819 202H1151M985 76V326',LINE)+f'<circle cx="985" cy="202" r="6" fill="{LIME}"/><circle cx="1056" cy="142" r="5" fill="{FG}"/>'
(A/'header.svg').write_text(svg(1200,440,body))
projects=[('aqua','01','AQUA BEAVERS','Marine data → mapped insight','PYTHON · FASTAPI · GEOSPATIAL ML','#6bd6e4'),('ev-grid','02','EV—OPTION GRID','Urban demand → investment scenarios','JAVASCRIPT · THREE.JS · OPENSTREETMAP',LIME),('osnovanie','03','ОСНОВАНИЕ','Документы → проверка комплектности','PYTHON · SQLITE · INTERACTIVE WEB','#e9b49b'),('repo-doctor','04','REPO DOCTOR','Repository gaps → clear next steps','TYPESCRIPT · NODE.JS · CLI','#b7adff')]
for name,num,title,sub,stack,color in projects:
 b=text(38,40,f'{num} / SELECTED PROJECT',12,MUTED,400,2)+text(38,111,title,46,FG,700,-1)+text(40,153,sub,22,MUTED)+text(40,222,stack,12,color,700,1)+text(1104,42,'↗',25,color)
 b+=path('M760 54V226',LINE)
 if name=='aqua':
  for i in range(7):b+=path('M'+ ' L'.join(f'{804+j*13},{85+i*21+math.sin(j*.45+i*.65)*10:.1f}' for j in range(25)),color,1, 'opacity=".38"')
  for x,y,r in [(874,115,5),(960,172,6),(1045,102,4),(990,138,3),(865,166,3),(1051,178,5)]:b+=f'<circle cx="{x}" cy="{y}" r="{r}" fill="{color}"/>'
  b+=path('M922 104H987V163H922Z',color,2)
 elif name=='ev-grid':
  for i in range(6):
   x=812+i*45;b+=path(f'M{x} 172l108 -58M{x} 172l126 57',LINE)
  for x,y,h in [(870,170,40),(930,145,68),(987,170,48),(1042,140,31),(1022,204,44)]:
   b+=f'<path d="M{x} {y}v-{h}l22 -11 24 12v{h}l-22 11Z" fill="#24312b" stroke="{color}" stroke-width="1.2"/><path d="M{x} {y-h}l24 12v{h}m0 -{h}l22 -11" fill="none" stroke="{color}" stroke-width="1"/>'
 elif name=='osnovanie':
  for x,y in [(822,70),(1020,60),(1020,169)]:
   b+=f'<rect x="{x}" y="{y}" width="82" height="64" rx="8" fill="#202931" stroke="{LINE}"/>'
   b+=path(f'M{x+16} {y+20}h37m-37 11h50m-50 11h27',color,1.5)
  b+=path('M904 102H943V92H1020M943 102V201H1020',color,2)+f'<circle cx="943" cy="102" r="6" fill="{color}"/>'
 else:
  b+=f'<rect x="813" y="58" width="310" height="164" rx="12" fill="#19232d" stroke="{LINE}"/>'+path('M813 86H1123',LINE)
  for x in [831,847,863]:b+=f'<circle cx="{x}" cy="73" r="3" fill="{MUTED}"/>'
  for y,t,c in [(118,'$ repo-doctor .',FG),(148,'✓ README present',color),(175,'! License missing',MUTED),(202,'→ Clear next steps',color)]:b+=text(831,y,t,16,c)
 (A/f'{name}.svg').write_text(svg(1200,260,b))
