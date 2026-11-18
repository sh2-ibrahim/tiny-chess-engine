import json,os,urllib.request as u
U=os.environ.get("MAKEFUN_ENV_URL")
V=[0,100,320,330,500,900,0]
N=[33,31,18,14,-14,-18,-31,-33]
J=[1,-1,16,-16,15,17,-15,-17]
D=[15,17,-15,-17,1,-1,16,-16]
def W(m):
 f=m&127;t=m>>7&127;p=m>>14
 return chr(97+(f&7))+str(1+(f>>4))+chr(97+(t&7))+str(1+(t>>4))+(" pnbrqk"[p] if p else "")
def P(f):
 b=[0]*128;i=112;w=f.split()
 for ch in w[0]:
  if ch=="/":i-=24
  elif ch.isdigit():i+=int(ch)
  else:b[i]=("pnbrqk".index(ch.lower())+1)*(ch.isupper()*2-1);i+=1
 s=1 if w[1]=="w" else -1;e=w[3]
 return b,s,sum(1<<i for i,ch in enumerate("KQkq") if ch in w[2]),(ord(e[1])-49)*16+ord(e[0])-97 if e!="-" else -1
def A(b,s,y):
 for O,p in (((-15,-17) if y>0 else (15,17),1),(N,2),(J,6)):
  for o in O:
   t=s+o
   if not t&136 and b[t]==p*y:return 1
 for i,o in enumerate(D):
  t=s+o
  while not t&136:
   q=b[t]
   if q:
    if q*y in (3+(i>3),5):return 1
    break
   t+=o
 return 0
def G(b,s,a,e):
 m=[];Z=m.append
 for f,q in enumerate(b):
  if f&136 or q*s<=0:continue
  t=abs(q)
  if t==1:
   d=16*s;L=7 if s>0 else 0;T=[];o=f+d
   if not b[o]:
    T.append(o)
    if f>>4==(1 if s>0 else 6) and not b[f+2*d]:T.append(f+2*d)
   for o in (f+d-1,f+d+1):
    if not o&136 and (b[o]*s<0 or o==e):T.append(o)
   for o in T:
    if o>>4==L:
     for p in (5,4,3,2):Z(f|o<<7|p<<14)
    else:Z(f|o<<7)
  else:
   for o in N if t==2 else J if t==6 else D[:4] if t==3 else D[4:] if t==4 else D:
    x=f+o
    while not x&136 and b[x]*s<=0:
     Z(f|x<<7)
     if b[x] or t==2 or t==6:break
     x+=o
 k=4 if s>0 else 116
 if b[k]==6*s:
  for g,h,r in ((1,1,3),(2,-1,-4)):
   if a&(g if s>0 else 4*g) and not b[k+h] and not b[k+2*h] and (h>0 or not b[k-3]) and b[k+r]==4*s and not A(b,k,-s) and not A(b,k+h,-s) and not A(b,k+2*h,-s):Z(k|k+2*h<<7)
 return m
def Y(b,m,s,a):
 f=m&127;t=m>>7&127;p=m>>14;n=b[:];q=n[f];n[f]=0
 if abs(q)==1 and not n[t] and f&7!=t&7:n[t-16*s]=0
 n[t]=p*s if p else q
 if abs(q)==6 and abs((f&7)-(t&7))==2:
  if t>f:n[f+1]=n[f+3];n[f+3]=0
  else:n[f-1]=n[f-4];n[f-4]=0
 for x,k in ((4,3),(7,1),(0,2),(116,12),(119,4),(112,8)):
  if f==x or t==x:a&=~k
 return n,a,f+16*s if abs(q)==1 and abs(t-f)==32 else -1
def L(b,s,a,e):
 r=[]
 for m in G(b,s,a,e):
  n,na,ne=Y(b,m,s,a)
  if not A(n,n.index(6*s),-s):r.append((m,n,na,ne))
 return r
def R(p,o):
 z=None
 for _ in range(3):
  try:
   q=u.Request(U+p,data=json.dumps(o).encode())
   with u.urlopen(q) as r:return json.load(r)
  except Exception as x:z=x
 raise z
def H(g):
 b,s,a,e=P(g["fen"]);k=None;r=None
 for m in g["legal_moves"]:
  f=(ord(m[1])-49)*16+ord(m[0])-97;t=(ord(m[3])-49)*16+ord(m[2])-97
  v=V[abs(b[t])] if b[t] else 100*(abs(b[f])==1 and m[0]!=m[2])
  p=V["pnbrqk".index(m[4])+1] if len(m)>4 else 0
  c=(-v,-p,V[abs(b[f])],m)
  if k is None or c<k:k=c;r=m
 return r
def T():
 while 1:
  g=R("/game",{})
  if g["status"]=="done":break
  while g["status"]=="your_move":
   try:m=H(g)
   except Exception:m=sorted(g["legal_moves"])[0]
   try:g=R("/move",{"game":g["game"],"move":m})
   except Exception:
    try:g=R("/move",{"game":g["game"],"move":sorted(g["legal_moves"])[0]})
    except Exception:return
if __name__=="__main__":T()
