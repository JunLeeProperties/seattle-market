import os
SRC=os.path.dirname(os.path.abspath(__file__))+'/'
import json
s=open(SRC+'template.html').read(); im=json.load(open(SRC+'img.json'))
for k,v in {'__LOGO__':im['logo'],'__FACE__':im['face'],'__QR__':im['qr'],'__DATA__':open(SRC+'data.json').read(),'__WEEKLY__':open(SRC+'weekly.json').read(),'__NOTES__':open(SRC+'../notes.json').read()}.items():
    s=s.replace(k,v)
open(SRC+'../index.html','w').write(s)
