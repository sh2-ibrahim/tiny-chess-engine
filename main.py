import json,os,urllib.request as u
V=[0,100,320,330,500,900,0]
N=[33,31,18,14,-14,-18,-31,-33]
B=[15,17,-15,-17];F=[1,-1,16,-16];D=B+F
X=[0];O=25000;K={};I=99999
class Q(Exception):pass
def W(m):
 f=m&127;t=m>>7&127;return chr(97+(f&7))+str(1+(f>>4))+chr(97+(t&7))+str(1+(t>>4))+" pnbrqk"[m>>14].strip()
def P(f):
 b=[0]*128;i=112;w=f.split()
 for ch in w[0]:
  if ch=="/":i-=24
  elif ch.isdigit():i+=int(ch)
  else:b[i]=("pnbrqk".index(ch.lower())+1)*((ch<"a")*2-1);i+=1
 s=1-2*(w[1]=="b");e=w[3]
 return b,s,sum(1<<"KQkq".index(ch) for ch in w[2] if ch!="-"),16*ord(e[1])+ord(e[0])-881 if e!="-" else -1
def A(b,s,y):
 for Z,p in (((-15*y,-17*y),1),(N,2),(D,6)):
  for o in Z:
   t=s+o
   if not t&136 and b[t]==p*y:return 1
 for i,o in enumerate(D):
  t=s+o
  while not t&136 and not b[t]:t+=o
  if not t&136 and b[t]*y in (3+(i>3),5):return 1
 return 0
def G(b,s,a,e):
 m=[];Z=m.append
 for f,q in enumerate(b):
  if f&136 or q*s<=0:continue
  t=abs(q)
  if t==1:
   d=16*s;L=7*(s>0);T=[];o=f+d
   if not b[o]:
    T.append(o)
    if f>>4==1+5*(s<0) and not b[f+2*d]:T.append(f+2*d)
   for o in (f+d-1,f+d+1):
    if not o&136 and (b[o]*s<0 or o==e):T.append(o)
   for o in T:
    if o>>4==L:
     for p in (5,4,3,2):Z(f|o<<7|p<<14)
    else:Z(f|o<<7)
  else:
   for o in (N,B,F,D,D)[t-2]:
    x=f+o
    while not x&136 and b[x]*s<=0:
     Z(f|x<<7)
     if b[x] or t==2 or t==6:break
     x+=o
 k=4 if s>0 else 116
 if b[k]==6*s and not A(b,k,-s):
  for g,h,r in ((1,1,3),(2,-1,-4)):
   if a&(g<<2*(s<0)) and not (b[k+h] or b[k+2*h] or h<0 and b[k-3]) and b[k+r]==4*s and not A(b,k+h,-s) and not A(b,k+2*h,-s):Z(k|k+2*h<<7)
 return m
def Y(b,m,s,a):
 f=m&127;t=m>>7&127;p=m>>14;n=b[:];q=n[f];n[f]=0
 if abs(q)==1 and not n[t] and f&7!=t&7:n[t-16*s]=0
 n[t]=p*s if p else q
 if abs(q)==6 and abs((f&7)-(t&7))==2:
  d=(t>f)*2-1;v=f+3*d-(d<0);n[f+d]=n[v];n[v]=0
 for x,k in ((4,3),(7,1),(0,2),(116,12),(119,4),(112,8)):
  if x in (f,t):a&=~k
 return n,a,f+16*s if abs(q)==1 and abs(t-f)==32 else -1
def L(b,s,a,e):return [(m,n,na,ne) for m in G(b,s,a,e) for n,na,ne in [Y(b,m,s,a)] if not A(n,n.index(6*s),-s)]
def E(b,s):
 t=0
 for i,p in enumerate(b):
  if i&136 or not p:continue
  a=abs(p);f=i&7;r=i>>4;g=1 if p>0 else -1;c=6-abs(2*f-7)-abs(2*r-7)
  t+=V[a]*g
  if a<2:t+=g*(8*(r if p>0 else 7-r)+3-abs(f-3))
  elif a<4:t+=(6-a)*c*g
  elif a==5:t+=c*g
 for q in (1,-1):
  k=b.index(6*q)
  for o in (15,16,17):
   z=k+o*q
   if 0<=z<128 and b[z]==q:t+=20*q
 return t*s
def C(b,m):
 f=m&127;t=m>>7&127;return 10*V[abs(b[t] or (abs(b[f])==1 and f&7!=t&7))]+500*(m>>14)-5*abs(b[f])
def S(b,s,a,e,d,al,be,pl):
 X[0]+=1
 if X[0]>O:raise Q
 k=A(b,b.index(6*s),-s)
 if d<=0:
  if pl>16:return E(b,s)
  if not k:
   st=E(b,s)
   if st>=be:return be
   al=max(al,st)
 if k and pl<24:d+=1
 ms=L(b,s,a,e)
 if not ms:return -9999+pl if k else 0
 if d<=0 and not k:ms=[z for z in ms if C(b,z[0])>0]
 ms.sort(key=lambda z:(-C(b,z[0])-8000*(z[0]==K.get(pl)),z[0]))
 bs=-I
 for m,n,na,ne in ms:
  v=-S(n,-s,na,ne,d-1,-be,-al,pl+1)
  bs=max(bs,v);al=max(al,v)
  if al>=be:
   if C(b,m)<1:K[pl]=m
   break
 return bs if d>0 else al
def H(g):
 b,s,a,e=P(g["fen"]);Lg=g["legal_moves"]
 ms=[z for z in L(b,s,a,e) if W(z[0]) in Lg]
 if len(ms)<2:return W(ms[0][0]) if ms else min(Lg)
 ms.sort(key=lambda z:(-C(b,z[0]),z[0]))
 X[0]=0;bm=ms[0][0]
 for d in range(1,9):
  try:
   al=-I;cm=bm;cs=-I
   for m,n,na,ne in ms:
    v=-S(n,-s,na,ne,d-1,-I,-al,1)
    if v>cs:cs=v;cm=m
    al=max(al,v)
   bm=cm;ms.sort(key=lambda z:(z[0]!=bm,-C(b,z[0]),z[0]))
  except Q:break
 return W(bm)
def R(p,o):
 for _ in range(3):
  try:return json.load(u.urlopen(u.Request(os.getenv("MAKEFUN_ENV_URL")+p,data=json.dumps(o).encode())))
  except Exception as x:z=x
 raise z
def T():
 while 1:
  g=R("/game",{})
  if g["status"]=="done":break
  while g["status"]=="your_move":
   d=min(g["legal_moves"])
   try:m=H(g)
   except Exception:m=d
   for mv in (m,d):
    try:g=R("/move",{"game":g["game"],"move":mv});break
    except Exception:pass
   else:return
if __name__=="__main__":T()
