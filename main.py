import json,os,urllib.request as u
V=[0,100,320,330,500,900,0]
N=[33,31,18,14,-14,-18,-31,-33]
B=[15,17,-15,-17];F=[1,-1,16,-16];D=B+F
M={4:3,7:1,0:2,116:12,119:4,112:8}
X=[0];O=50000;J={};I=10**5;BM=[0];LG=[]
def W(m):return "".join(chr(97+(x&7))+str(1+(x>>4)) for x in (m&127,m>>7&127))+" pnbrqk"[m>>14].strip()
def P(f):
 b=[0]*128;i=112;w=f.split()
 for ch in w[0]:
  if ch=="/":i-=24
  elif"/"<ch<":":i+=int(ch)
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
  if q*s<=0:continue
  t=abs(q)
  if t==1:
   d=16*s;L=7*(s>0);T=[];o=f+d
   if not b[o]:
    T.append(o)
    if f>>4==1+5*(s<0) and not b[f+2*d]:T.append(f+2*d)
   for o in (f+d-1,f+d+1):
    if not o&136 and(b[o]*s<0 or o==e):T.append(o)
   for o in T:
    for p in (5,4,3,2)if o>>4==L else(0,):Z(f|o<<7|p<<14)
  else:
   for o in (N,B,F,D,D)[t-2]:
    x=f+o
    while not x&136 and b[x]*s<=0:
     Z(f|x<<7)
     if b[x] or t%4==2:break
     x+=o
 k=60-56*s
 if b[k]==6*s and not A(b,k,-s):
  for g,h,r in ((1,1,3),(2,-1,-4)):
   if a&(g<<2*(s<0)) and not (b[k+h] or b[k+2*h] or h<0 and b[k-3]) and b[k+r]==4*s and not(A(b,k+h,-s)or A(b,k+2*h,-s)):Z(k|k+2*h<<7)
 return m
def Y(b,m,s,a):
 f=m&127;t=m>>7&127;p=m>>14;n=b[:];q=n[f];n[f]=0
 if abs(q)==1 and not n[t] and f&7!=t&7:n[t-16*s]=0
 n[t]=p*s if p else q
 if abs(q)==6 and abs(f-t)==2:
  d=(t>f)*2-1;v=f+3*d-(d<0);n[f+d]=n[v];n[v]=0
 return n,a&~(M.get(f,0)|M.get(t,0)),f+16*s if abs(q)==1 and abs(t-f)==32 else -1
def E(b,s,k,o):
 t=0
 for i,p in enumerate(b):
  if p:
   a=abs(p);f=i&7;r=i>>4;g=(p>0)*2-1;c=6-abs(2*f-7)-abs(2*r-7)
   t+=V[a]*g
   if a<2:t+=g*(8*(r if p>0 else 7-r)+3-abs(f-3))
   elif a<4:t+=(6-a)*c*g
   elif a==5:t+=c*g
 t+=30*(b.count(3)>1)-30*(b.count(-3)>1)
 for j,q in ((k,s),(o,-s)):t+=20*q*sum(0<=j+d*q<128 and b[j+d*q]==q for d in range(15,18))
 return t*s
C=lambda b,m:10*V[abs(b[m>>7&127]or(abs(b[m&127])==1 and m&7!=(m>>7&127)&7))]+500*(m>>14)-5*abs(b[m&127])
def S(b,s,a,e,d,al,be,pl,ks,os):
 X[0]+=1
 if X[0]>O:1/0
 oa=al;ob=be
 ky=(tuple(b),s,a,e);te=J.get(ky)if d>0 else None
 if te and te[0]>=d and abs(te[1])<9000 and pl>0:
  v,f=te[1],te[2]
  if f==0 or f==1 and v>=be or f==2 and v<=al:return v
  if f==1:al=max(al,v)
  else:be=min(be,v)
 k=A(b,ks,-s)
 if d<=0:
  if pl>16:return E(b,s,ks,os)
  if not k:
   st=E(b,s,ks,os)
   if st>=be:return be
   al=max(al,st)
 d+=k and pl<24
 ms=G(b,s,a,e)
 if not ms:return -9999+pl if k else 0
 if d<=0 and not k and not (ms:=[m for m in ms if C(b,m)>0]):return al
 ms.sort(key=lambda m:(-C(b,m)-8000*(m==te[3]if te else 0),m))
 if pl==0:ms=[m for m in ms if W(m)in LG]
 bs=-I;bm=0
 for m in ms:
  n,na,ne=Y(b,m,s,a)
  nk=(m>>7&127) if abs(b[m&127])==6 else ks
  if A(n,nk,-s):continue
  v=-S(n,-s,na,ne,d-1,-be,-al,pl+1,os,nk)
  if v>bs:bs,bm=v,m
  al=max(al,v)
  if al>=be:break
 if not bm:return -9999+pl if k else 0 if d>0 else al
 if d>0 and abs(bs)<9000:
  J[ky]=d,bs,0 if oa<bs<ob else 1+(bs<=oa),bm
  len(J)>20000 and J.clear()
 if pl==0:BM[0]=bm
 return bs if d>0 else al
def H(g):
 b,s,a,e=P(g["fen"]);LG[:]=g["legal_moves"]
 if len(LG)<2:return min(LG)
 ks=b.index(6*s);os=b.index(-6*s);X[0]=BM[0]=0
 try:
  for d in range(1,9):S(b,s,a,e,d,-I,I,0,ks,os)
 except:pass
 return W(BM[0]) if BM[0] else min(LG)
def R(p,o):
 for _ in"123":
  try:return json.load(u.urlopen(os.getenv("MAKEFUN_ENV_URL")+p,json.dumps(o).encode()))
  except:pass
 1/0
def T():
 while (g:=R("/game",{}))["status"]!="done":
  while g["status"]=="your_move":
   d=min(g["legal_moves"])
   try:m=H(g)
   except:m=d
   for mv in (m,d):
    try:g=R("/move",{"game":g["game"],"move":mv});break
    except:pass
   else:return
if __name__=="__main__":T()
