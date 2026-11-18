# -*- coding: utf-8 -*-
import json, html, io, re, sys
import rename
LD=io.open("logo_dark.b64").read().strip(); LL=io.open("logo_light.b64").read().strip()
def esc(s): return html.escape(s or "", quote=False)

def load(n): return json.load(io.open(n, encoding="utf-8"))

TABS = [
 ("basics","Basics","t1_basics.json","t1_basics_practice.json",
  ["Output and variables","Data types","Type conversion","Input","Operators","Conditional statements"]),
 ("collections","Collections","t2_collections.json","t2_collections_practice.json",
  ["Loops","Lists","Tuples","Sets","Dictionaries"]),
 ("functions","Functions","t3_functions.json","t3_functions_practice.json",
  ["Defining functions","Function arguments","Lambda, map, filter and reduce","Recursion","Comprehensions"]),
 ("strings","Strings","t4_strings.json","t4_strings_practice.json",
  ["String indexing and slicing","String methods","String formatting","Regular expressions"]),
 ("oop","Files &amp; Classes","t5_oop.json","t5_oop_practice.json",
  ["File handling","Exception handling","Classes and objects","The four pillars of OOP"]),
 ("numpy","NumPy","t6_numpy.json","t6_numpy_practice.json",
  ["Creating arrays","Inspecting an array","Accessing elements","Array operations",
   "Aggregation","Broadcasting","Filtering","Sorting","Changing shape"]),
 ("pandas","pandas","t7_pandas.json","t7_pandas_practice.json",
  ["Series and DataFrame","Inspecting a DataFrame","Selecting columns","loc and iloc",
   "Filtering rows","Sorting","Counting values"]),
]


KW = (r'\b(for|in|if|else|elif|import|from|print|len|range|def|return|not|and|or|True|False|'
      r'None|lambda|while|as|try|except|finally|class|pass|with|del|is|break|continue|super)\b')

def _code_part(t):
    """Highlight one chunk of real code. Runs on ESCAPED text that contains no
    markup yet, so a keyword can never match inside a tag we inserted."""
    t = re.sub(KW, r'<span class="k">\1</span>', t)
    t = re.sub(r'(?<![\w.#])(\d+\.?\d*)(?![\w])', r'<span class="o">\1</span>', t)
    return t

def hl(code):
    """Split each line at its first # BEFORE inserting any markup. The comment
    half is only escaped, never keyword-scanned - otherwise `class` in a comment,
    or worse in the class="c" attribute of a span we just wrote, gets wrapped
    again and the raw markup leaks onto the page. (That bug shipped once.)"""
    out = []
    for line in code.split("\n"):
        i = line.find("#")
        if i == -1:
            out.append(_code_part(esc(line)))
        else:
            out.append(_code_part(esc(line[:i])) +
                       '<span class="c">' + esc(line[i:]) + '</span>')
    return "\n".join(out)

def cid(cat):
    return re.sub(r'[^a-z0-9]+','-',cat.lower()).strip('-')

def render(key, rows, practice, order):
    """Returns the reference body, its category keys, and the practice body.
    Practice NO LONGER sits inline under each category - it is collected
    separately and rendered into the Practice window."""
    cats={}
    for r in rows: cats.setdefault(r["cat"],[]).append(r)
    pr={}
    for p in practice: pr.setdefault(p["cat"],[]).append(p)
    keys=[c for c in order if c in cats]+[c for c in cats if c not in order]
    out=[]; pout=[]
    for cat in keys:
        # ids are scoped by tab: "Sorting" exists in BOTH NumPy and pandas, so an
        # unscoped id would be duplicated and the jump link would land in a hidden tab.
        c=cid(cat); n=len(pr.get(cat,[]))
        btn=('<button class="pbtn" data-prac="%s|%s">Practice <span>%d</span></button>'
             %(key,c,n)) if n else ''
        out.append('<h2 class="cat" id="c-%s-%s">%s%s</h2>'%(key,c,esc(cat),btn))
        for r in cats[cat]:
            out.append('<article class="e"><h3>%s</h3>'%esc(r["name"]))
            out.append('<div class="what"><p>%s</p></div>'%esc(r["desc"]))
            out.append('<div class="lbl mt">Code</div><pre><code>%s</code></pre>'%hl(r["code"]))
            if r.get("out"):
                out.append('<div class="lbl mt">Output</div><div class="out">%s</div>'%esc(r["out"]))
            out.append('</article>')
        if n:
            pout.append('<h2 class="pcat" id="p-%s-%s">%s <span>%d</span></h2>'
                        %(key,c,esc(cat),n))
            for i,p in enumerate(pr[cat],1):
                pout.append('<div class="pq"><div class="qn"><b>%d.</b> %s</div>'%(i,esc(p["q"])))
                pout.append('<details><summary>Show one way to do it</summary>'
                            '<pre><code>%s</code></pre>'%hl(p["code"]))
                if p.get("out"):
                    pout.append('<div class="lbl mt">Output</div><div class="out">%s</div>'%esc(p["out"]))
                pout.append('</details></div>')
    return "\n".join(out), keys, "\n".join(pout)

secs=[]; tabbtns=[]; psecs=[]; ptabs=[]; total=0; ptotal=0
for key,label,rf,pf,order in TABS:
    rows=rename.apply(load(rf)); practice=rename.apply(load(pf))
    body,keys,pbody=render(key,rows,practice,order)
    total+=len(rows); ptotal+=len(practice)
    tabbtns.append('<button class="tab" data-go="%s">%s <span>%d</span></button>'%(key,label,len(rows)))
    jump="".join('<a href="#c-%s-%s">%s</a>'%(key,cid(c),esc(c)) for c in keys)
    secs.append('<section class="sec" id="%s"><nav class="jump">%s</nav>%s</section>'
                %(key,jump,body))
    ptabs.append('<button class="ptab" data-ptab="%s">%s <span>%d</span></button>'
                 %(key,label,len(practice)))
    psecs.append('<div class="psec" id="ps-%s">%s</div>'%(key,pbody))

TABSTRIP = ("".join(tabbtns) +
  '<button class="tab popen" id="popen">Practice <span>%d</span></button>'%ptotal)

PRACWIN = ("""<div class="pwrap" id="pwrap" hidden>
 <div class="pbackdrop" data-close="1"></div>
 <div class="pwin">
  <div class="phead">
   <div class="ptitle">Practice <span>%d questions</span></div>
   <input class="pfind" id="pfind" type="search" placeholder="Filter questions" autocomplete="off">
   <button class="pclose" id="pclose">Close</button>
  </div>
  <div class="ptabs">%s</div>
  <div class="pbody" id="pbody">%s</div>
  <div class="pnone" id="pnone" hidden>Nothing matches that.</div>
 </div>
</div>""" % (ptotal, "".join(ptabs), "\n".join(psecs)))

CSS = """
:root{--paper:#fff;--ink:#17191c;--slate:#5f656e;--ash:#8c9199;--hair:#e6e6e8;--mist:#f4f4f5;
 --code-bg:#f7f8f9;--out-bg:#e9f1ec;--out-ink:#13543e;--peach:#fbe1d1;--sienna:#5d2a1a;
 --ser:'Source Serif 4',Georgia,serif;--sans:'Inter',system-ui,sans-serif;
 --mono:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}
[data-theme="dark"]{--paper:#0f1113;--ink:#eceef1;--slate:#a2a9b3;--ash:#767c85;--hair:#262b30;
 --mist:#1a1d21;--code-bg:#0a0c0e;--out-bg:#11271e;--out-ink:#7fd0a0;--peach:#3d2718;--sienna:#f3c8a8}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--paper:#0f1113;--ink:#eceef1;
 --slate:#a2a9b3;--ash:#767c85;--hair:#262b30;--mist:#1a1d21;--code-bg:#0a0c0e;--out-bg:#11271e;
 --out-ink:#7fd0a0;--peach:#3d2718;--sienna:#f3c8a8}}
*{box-sizing:border-box;margin:0;padding:0}
body{background:var(--paper);color:var(--ink);font-family:var(--sans);font-size:16px;line-height:1.6;
 -webkit-font-smoothing:antialiased}
.wrap{max-width:900px;margin:0 auto;padding:0 24px}
.brand{padding:26px 0 0}.brand img{height:29px;display:block}
.lg-l{display:none}[data-theme="dark"] .lg-d{display:none}[data-theme="dark"] .lg-l{display:block}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]) .lg-d{display:none}
 :root:not([data-theme="light"]) .lg-l{display:block}}
header{padding:20px 0 0}
h1{font-family:var(--ser);font-size:38px;font-weight:600;letter-spacing:-.4px;line-height:1.1}
.tabs{display:flex;gap:7px;flex-wrap:wrap;margin:22px 0 0;border-bottom:1px solid var(--hair);
 padding-bottom:14px}
.tab{font-family:var(--sans);font-size:14.5px;font-weight:600;color:var(--slate);background:none;
 border:1px solid var(--hair);border-radius:9999px;padding:7px 16px;cursor:pointer;
 display:flex;gap:7px;align-items:center}
.tab span{font-size:12px;font-weight:500;color:var(--ash);font-variant-numeric:tabular-nums}
.tab:hover{border-color:var(--sienna);color:var(--ink)}
.tab.on{background:var(--peach);border-color:var(--peach);color:var(--sienna)}
.tab.on span{color:var(--sienna);opacity:.7}
.sec{display:none}.sec.on{display:block}
.jump{display:flex;flex-wrap:wrap;gap:6px;padding:22px 0 6px}
.jump a{font-size:12.5px;color:var(--slate);text-decoration:none;background:var(--mist);
 border-radius:9999px;padding:4px 11px}
.jump a:hover{color:var(--ink)}
h2.cat{font-family:var(--ser);font-size:25px;font-weight:600;margin:34px 0 16px;
 padding-bottom:8px;border-bottom:2px solid var(--ink)}
.e{border:1px solid var(--hair);border-radius:12px;padding:18px 20px;margin-bottom:14px}
.e h3{font-size:18px;font-weight:600;margin-bottom:12px}
.lbl{font-size:10.5px;font-weight:600;letter-spacing:.11em;text-transform:uppercase;color:var(--ash);
 display:block;margin-bottom:5px}
.mt{margin-top:14px}
.what p{font-size:15px;color:var(--slate);line-height:1.55}
pre{background:var(--code-bg);border:1px solid var(--hair);border-radius:8px;padding:12px 14px;
 overflow-x:auto}
pre code{font-family:var(--mono);font-size:12.5px;line-height:1.65;white-space:pre;color:var(--ink)}
.c{color:var(--ash)}.k{color:#7a3ba8;font-weight:500}.o{color:#a8541f}
[data-theme="dark"] .k{color:#c99bf0}[data-theme="dark"] .o{color:#e0a86a}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]) .k{color:#c99bf0}
 :root:not([data-theme="light"]) .o{color:#e0a86a}}
.out{background:var(--out-bg);color:var(--out-ink);border-radius:8px;padding:11px 14px;
 font-family:var(--mono);font-size:12.5px;line-height:1.6;white-space:pre;overflow-x:auto}
h2.cat{display:flex;justify-content:space-between;align-items:baseline;gap:12px}
.pbtn{font-family:var(--sans);font-size:12.5px;font-weight:600;color:var(--sienna);
 background:var(--peach);border:0;border-radius:9999px;padding:5px 13px;cursor:pointer;
 display:inline-flex;gap:6px;align-items:center;white-space:nowrap;flex:none}
.pbtn span{font-size:11px;font-weight:500;opacity:.75;font-variant-numeric:tabular-nums}
.pbtn:hover{filter:brightness(.95)}
.tab.popen{background:var(--sienna);border-color:var(--sienna);color:var(--paper);margin-left:auto}
.tab.popen span{color:var(--paper);opacity:.72}
.tab.popen:hover{filter:brightness(1.12);color:var(--paper)}
.pwrap{position:fixed;inset:0;z-index:200;display:flex;align-items:center;justify-content:center;
 padding:28px}
.pwrap[hidden]{display:none}
.pbackdrop{position:absolute;inset:0;background:rgba(10,12,14,.55);backdrop-filter:blur(2px)}
.pwin{position:relative;display:flex;flex-direction:column;width:min(900px,100%);height:min(860px,100%);
 background:var(--paper);border:1px solid var(--hair);border-radius:16px;overflow:hidden;
 box-shadow:0 24px 70px rgba(0,0,0,.34)}
.phead{display:flex;align-items:center;gap:12px;padding:16px 20px;border-bottom:1px solid var(--hair);
 flex:none;flex-wrap:wrap}
.ptitle{font-family:var(--ser);font-size:22px;font-weight:600;flex:none}
.ptitle span{font-family:var(--sans);font-size:12.5px;font-weight:500;color:var(--ash);margin-left:8px}
.pfind{flex:1 1 180px;min-width:140px;font-family:var(--sans);font-size:14px;color:var(--ink);
 background:var(--mist);border:1px solid var(--hair);border-radius:9999px;padding:8px 15px}
.pfind:focus{outline:2px solid var(--sienna);outline-offset:1px}
.pclose{font-family:var(--sans);font-size:13.5px;font-weight:600;color:var(--slate);
 background:none;border:1px solid var(--hair);border-radius:9999px;padding:7px 15px;cursor:pointer;flex:none}
.pclose:hover{color:var(--ink);border-color:var(--sienna)}
.ptabs{display:flex;gap:6px;flex-wrap:wrap;padding:12px 20px;border-bottom:1px solid var(--hair);flex:none}
.ptab{font-family:var(--sans);font-size:13px;font-weight:600;color:var(--slate);background:none;
 border:1px solid var(--hair);border-radius:9999px;padding:5px 13px;cursor:pointer;
 display:flex;gap:6px;align-items:center}
.ptab span{font-size:11px;font-weight:500;color:var(--ash);font-variant-numeric:tabular-nums}
.ptab:hover{border-color:var(--sienna);color:var(--ink)}
.ptab.on{background:var(--peach);border-color:var(--peach);color:var(--sienna)}
.ptab.on span{color:var(--sienna);opacity:.7}
.pbody{flex:1 1 auto;overflow-y:auto;padding:4px 20px 26px;scroll-behavior:smooth}
.psec{display:none}.psec.on{display:block}
h2.pcat{font-family:var(--ser);font-size:21px;font-weight:600;margin:24px 0 4px;padding-bottom:7px;
 border-bottom:2px solid var(--ink);scroll-margin-top:8px}
h2.pcat span{font-family:var(--sans);font-size:12px;font-weight:500;color:var(--ash);margin-left:7px}
.pnone{display:none;padding:24px 20px;color:var(--ash);font-size:15px}
.pnone.on{display:block}
.pq{border-top:1px solid var(--hair);padding:12px 0}
.pq:first-of-type{border-top:0;padding-top:0}
.qn{font-size:15px;line-height:1.55}
.qn b{color:var(--sienna);margin-right:4px}
details{margin-top:9px}
summary{font-size:13px;font-weight:600;color:var(--slate);cursor:pointer;
 display:inline-block;padding:4px 12px;border:1px solid var(--hair);border-radius:9999px;
 background:var(--paper);list-style:none}
summary::-webkit-details-marker{display:none}
summary:hover{color:var(--ink);border-color:var(--sienna)}
details[open] summary{margin-bottom:9px}
footer{border-top:1px solid var(--hair);margin-top:44px;padding:20px 0 60px;color:var(--ash);font-size:14px}
.tt{position:fixed;right:16px;bottom:16px;background:var(--mist);border:1px solid var(--hair);
 color:var(--slate);border-radius:9999px;padding:8px 15px;font-size:13px;font-family:var(--sans);
 cursor:pointer;z-index:50}
button:focus-visible,a:focus-visible,summary:focus-visible{outline:2px solid var(--sienna);outline-offset:2px}
@media (max-width:640px){h1{font-size:29px}.wrap{padding:0 16px}h2.cat{flex-wrap:wrap}
 .pwrap{padding:0}.pwin{width:100%;height:100%;border-radius:0;border:0}
 .ptitle{font-size:19px}.phead{padding:13px 16px}.ptabs{padding:10px 16px}.pbody{padding:4px 16px 26px}}
"""

DOC = """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Python, NumPy and pandas &mdash; Reference</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Source+Serif+4:opsz,wght@8..60,400;8..60,600&family=Inter:wght@400;500;600&display=swap">
<style>%s</style></head>
<body>
<script>try{var t=localStorage.getItem("steep-theme");
 if(t==="dark"||t==="light")document.documentElement.setAttribute("data-theme",t);}catch(e){}</script>
<div class="wrap">
<div class="brand"><img class="lg-d" src="%s" alt="TAP Academy"><img class="lg-l" src="%s" alt="TAP Academy"></div>
<header>
 <h1>Python &middot; NumPy &middot; pandas</h1>
 <div class="tabs">%s</div>
</header>
%s
<footer>%d entries &middot; %d practice questions</footer>
</div>
%s
<button class="tt" id="tt">Theme</button>
<script>
(function(){
 var tabs=[].slice.call(document.querySelectorAll('.tab'));
 var secs=[].slice.call(document.querySelectorAll('.sec'));
 function show(id,setHash){
   tabs.forEach(function(b){b.classList.toggle('on',b.dataset.go===id);});
   secs.forEach(function(s){s.classList.toggle('on',s.id===id);});
   try{localStorage.setItem('pyref-tab',id);}catch(e){}
   if(setHash && location.hash.slice(1)!==id) history.replaceState(null,'','#'+id);
 }
 tabs.forEach(function(b){b.onclick=function(){show(b.dataset.go,true);window.scrollTo(0,0);};});
 var ids=secs.map(function(s){return s.id;});
 var start=ids[0],h=location.hash.slice(1);
 if(ids.indexOf(h)>=0) start=h;
 else{try{var v=localStorage.getItem('pyref-tab'); if(ids.indexOf(v)>=0) start=v;}catch(e){}}
 show(start,false);
 window.scrollTo(0,0);
 var m=['auto','light','dark'],i=0;
 try{var t=localStorage.getItem('steep-theme'); if(t) i=m.indexOf(t);}catch(e){}
 if(i<0)i=0;
 function ap(){var v=m[i];
  if(v==='auto') document.documentElement.removeAttribute('data-theme');
  else document.documentElement.setAttribute('data-theme',v);
  document.getElementById('tt').textContent=v.charAt(0).toUpperCase()+v.slice(1);
  try{localStorage.setItem('steep-theme',v);}catch(e){}}
 document.getElementById('tt').onclick=function(){i=(i+1)%%3;ap();};ap();
 // ---- Practice window ----
 var pwrap=document.getElementById('pwrap'), pbody=document.getElementById('pbody'),
     pfind=document.getElementById('pfind'), pnone=document.getElementById('pnone');
 var ptabs=[].slice.call(document.querySelectorAll('.ptab'));
 var psecs=[].slice.call(document.querySelectorAll('.psec'));
 var lastFocus=null;
 function ptabShow(key){
   ptabs.forEach(function(b){b.classList.toggle('on',b.dataset.ptab===key);});
   psecs.forEach(function(s){s.classList.toggle('on',s.id==='ps-'+key);});
   try{localStorage.setItem('pyref-ptab',key);}catch(e){}
 }
 function filter(){
   var q=pfind.value.trim().toLowerCase(), hits=0;
   psecs.forEach(function(sec){
     var shown=0, cat=null, catHits=0;
     [].slice.call(sec.children).forEach(function(el){
       if(el.tagName==='H2'){
         if(cat) cat.style.display = catHits ? '' : 'none';
         cat=el; catHits=0; return;
       }
       if(!el.classList.contains('pq')) return;
       var t=el.textContent.toLowerCase();
       var ok = !q || t.indexOf(q)>=0;
       el.style.display = ok ? '' : 'none';
       if(ok){shown++;catHits++;hits++;}
     });
     if(cat) cat.style.display = catHits ? '' : 'none';
     sec.dataset.hits=shown;
   });
   pnone.classList.toggle('on', q && hits===0);
 }
 function openPrac(key,catId){
   lastFocus=document.activeElement;
   pwrap.hidden=false;
   document.body.style.overflow='hidden';
   if(!key){ try{key=localStorage.getItem('pyref-ptab');}catch(e){} }
   if(!key || !document.getElementById('ps-'+key)) key=ptabs[0].dataset.ptab;
   ptabShow(key);
   pfind.value=''; filter();
   if(catId){
     var t=document.getElementById(catId);
     if(t) t.scrollIntoView();
   } else { pbody.scrollTop=0; }
   pfind.focus();
 }
 function closePrac(){
   pwrap.hidden=true;
   document.body.style.overflow='';
   if(lastFocus && lastFocus.focus) lastFocus.focus();
 }
 document.getElementById('popen').onclick=function(){
   var cur=null; secs.forEach(function(s){if(s.classList.contains('on')) cur=s.id;});
   openPrac(cur,null);
 };
 document.getElementById('pclose').onclick=closePrac;
 pwrap.addEventListener('click',function(e){ if(e.target.dataset.close) closePrac(); });
 ptabs.forEach(function(b){b.onclick=function(){ptabShow(b.dataset.ptab);pfind.value='';filter();pbody.scrollTop=0;};});
 pfind.addEventListener('input',filter);
 [].forEach.call(document.querySelectorAll('.pbtn'),function(b){
   b.onclick=function(){
     var parts=b.dataset.prac.split('|');
     openPrac(parts[0],'p-'+parts[0]+'-'+parts[1]);
   };
 });
 document.addEventListener('keydown',function(e){
   if(e.key==='Escape' && !pwrap.hidden) closePrac();
 });
})();
</script>
</body></html>""" % (CSS, LD, LL, TABSTRIP, "\n".join(secs), total, ptotal, PRACWIN)

errs=[]
for t in ["div","section","article","p","pre","code","h1","h2","h3","span","nav","a","button","header","footer","details","summary"]:
    o=len(re.findall(r"<%s[\s>]"%t,DOC)); c=DOC.count("</%s>"%t)
    if o!=c: errs.append("%s: %d open, %d close"%(t,o,c))
if errs:
    print("BUILD FAILED"); [print("  -",e) for e in errs]; sys.exit(1)

io.open("../public/index.html","w",encoding="utf-8").write(DOC)
print("built public/index.html  %d KB | %d tabs | %d entries | %d practice questions"
      %(len(DOC)//1024,len(TABS),total,ptotal))
