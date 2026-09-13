#!/usr/bin/env python3
"""Static site generator for mohamedkmahdy.github.io.
Run: python3 build.py   (from the site/ directory)"""
import os, html, shutil

SITE = os.path.dirname(os.path.abspath(__file__))
OUT_PROJ = os.path.join(SITE, 'projects')

NAME  = "Mohamed K. Mahdy"
ROLE  = "AEC Solutions Architect &amp; AI Specialist"
LEDE  = "I build the software layer between engineers and their models, and the AI layer above it."
BASE  = "https://mohamedkmahdy.github.io"

# ---------------------------------------------------------------- projects
P = [
dict(slug="aps-raumbuch", title="APS Raumbuch", tag="Cloud · openBIM",
  card="ACC-connected room book generator that also runs fully offline against IFC.",
  stack="React · FastAPI · Autodesk Platform Services · AEC Data Model API · IFC",
  head="Cloud-connected, vendor-neutral",
  body=["Authenticates against APS, browses Autodesk Construction Cloud, opens a model in the APS Viewer, extracts every room and the furniture inside it, and exports a formatted German <em>Raumbuch</em> to Excel or PDF.",
        "<strong>Cross-model association.</strong> Rooms living in a linked geometry node joined to furniture in the main model through baked room parameters, with deduplication, because partial linked copies share element ids.",
        "Queries the AEC Data Model GraphQL API directly rather than scraping the Viewer's property database, which is faster and works before the model finishes loading."],
  result="Not locked to one vendor: the same extraction runs <strong>fully offline</strong> against an uploaded IFC file via IfcOpenShell.",
  media=[]),

dict(slug="revit-automation", title="Revit Automation Suite", tag="9 tools · video",
  card="Nine production Revit plugins: model management, interior finishes, quantity take-off. With demos.",
  stack="C# · Revit API · WPF · Excel interop",
  head="Nine production Revit plugins",
  body=["A suite of enterprise Revit add-ins built for architecture and engineering teams, covering model management, interior finishes workflows, quantity take-off and bulk file operations. Each one replaced a manual process that consumed engineering hours every week.",
        "All demos below are recorded against a generic sample model."],
  result="",
  media=[
    ("video","video/genq-boq-generator.mp4","GenQ: BOQ Generator","Automatically generates a full detailed bill of quantities in Excel, straight from the model."),
    ("video","video/revit-transmitter.mp4","Revit-Transmitter","Detaches models with preserve or delete worksets, purges unused elements, and prepares issue-ready files."),
    ("video","video/materials-manager.mp4","Materials Manager","Exports project material data to Excel, edits it, and syncs it back, keeping design and technical teams aligned."),
    ("video","video/finishes-manager.mp4","Finishes Manager","Walls, floors, ceilings and wall bases, exported, edited in Excel, and written back to the model."),
    ("video","video/finishes-drawer.mp4","Finishes Drawer","Reads room finishes and draws the wall, floor and wall-base geometry automatically."),
    ("video","video/worksets-manager.mp4","Worksets Manager","Creates standard worksets from Excel or by UNIFORMAT, then assigns every element to the right one."),
    ("video","video/uniformat-assigner.mp4","Uniformat Assigner","Filters elements by category and assigns UNIFORMAT classification across the whole project."),
    ("video","video/auto-joiner.mp4","Auto Joiner","Joins and unjoins every intersecting element of selected categories in one pass."),
    ("video","video/transfer-types.mp4","Transfer Types","Selects Revit projects from a folder tree and transfers types and families between them in bulk."),
    ("img","img/image47.png","Finishes Drawer: interface",""),
    ("img","img/image52.png","Uniformat Assigner: interface",""),
    ("img","img/image54.png","Auto Joiner: interface",""),
  ]),

dict(slug="clash-management", title="Clash Management", tag="Navisworks · WPF",
  card="BEACON and COLLIDE: clash grouping, status sync, and matrix generation.",
  stack="C# · Navisworks API · WPF",
  head="4,000 clashes, 200 actual problems",
  body=["<strong>BEACON</strong> is a Navisworks plugin that groups clashes by mass and proximity, syncs status across NWF files, and automates grouping, renaming and un-grouping. Clash coordination stops being a full-time job and becomes a review step.",
        "<strong>COLLIDE</strong> is a standalone WPF application that builds clash matrices from discipline and category rules, then exports XML configurations directly into Navisworks."],
  result="",
  media=[("img","img/image31.png","BEACON: Navisworks clash grouping",""),
         ("img","img/image32.png","COLLIDE: clash matrix generator","Disciplines, categories, priorities and tolerances defined once, exported as a Navisworks-ready XML configuration.")]),

dict(slug="curtain-panels", title="Curtain Panel Suite", tag="Parametric · 4 tools",
  card="Generator → Scheduler → Drawings → Tagger. A facade from parametric definition to annotated documentation.",
  stack="C# · Revit API · adaptive families",
  head="Geometry that builds itself",
  body=["One tool chain taking a curtain wall facade from parametric definition through to fully annotated documentation.",
        "<strong>Panel Generator</strong> creates and edits curtain panels across the facade. <strong>Panel Scheduler</strong> builds and exports panel schedules. <strong>Panel Drawings</strong> generates a dedicated view for every panel type. <strong>Panel Tagger</strong> tags and dimensions the whole set automatically."],
  result="",
  media=[("img","img/image55.jpeg","Panel Generator",""),
         ("img","img/image56.jpeg","Panel Scheduler",""),
         ("img","img/image57.jpeg","Panel Drawings",""),
         ("img","img/image58.jpeg","Panel Tagger","")]),

dict(slug="bim-analytics", title="BIM Analytics", tag="Power BI · 9 dashboards",
  card="Model health, clash detection, issues and resourcing: automated reporting pipelines on ACC and BIM 360.",
  stack="Power BI · DAX · SharePoint · BIM 360 / ACC · Revizto",
  head="Making model health visible to people who never open Revit",
  body=["A suite of automated Power BI dashboards and reporting pipelines built for BIM coordination, covering model health, clash detection, open issues, ACC administration, resourcing and team-level assessment.",
        "Each dashboard reads directly from project data and refreshes on a schedule, so coordination status is current without anyone assembling a report. Deployed as project-specific intelligence hubs on SharePoint."],
  result="Built across three organisations: Dewan, Obermeyer and Sweco.",
  media=[("img","img/image12.png","Project intelligence hub: home page",""),
         ("img","img/image10.png","SharePoint deployment",""),
         ("img","img/image11.png","SharePoint: project structure",""),
         ("img","img/image13.png","Automated reporting",""),
         ("img","img/image14.png","Model health dashboard",""),
         ("img","img/image15.png","Model health: detail",""),
         ("img","img/image16.png","Clash detection dashboard","Clash trend over time, live counts per discipline pair, and current totals by element test."),
         ("img","img/image17.png","Issues dashboard",""),
         ("img","img/image18.png","ACC admin dashboard",""),
         ("img","img/image19.png","Resources dashboard",""),
         ("img","img/image20.png","Resources: allocation",""),
         ("img","img/image21.png","Resources: detail",""),
         ("img","img/image22.png","Team level assessment",""),
         ("img","img/image23.png","Team level: breakdown",""),
         ("img","img/image24.png","Team level: detail","")]),

dict(slug="model-health", title="VITAL &amp; ANT", tag="Scheduled services",
  card="Nightly model-health checks and automated deliverable exports. Nothing depends on someone remembering.",
  stack="C# · Revit API · Navisworks · Power BI · Windows scheduler",
  head="Nothing should depend on someone remembering",
  body=["<strong>VITAL</strong> is a bulk Revit model checker with a built-in scheduler. It runs check-sets across every project on a nightly cycle and extracts performance metrics into Power BI, so degradation is caught before it becomes a problem.",
        "<strong>ANT</strong> is a background service that exports NWC and DWG deliverables every night. Nobody has to remember, and nothing is missed before a deadline."],
  result="Boring by design. <strong>Reliability is the feature.</strong>",
  media=[("img","img/image9.png","VITAL: scheduled check configuration","Projects and check-sets defined once, then run unattended on a nightly cycle."),
         ("img","img/image7.png","ANT: bulk export configuration","")]),

dict(slug="acc-integrations", title="ACC Integrations", tag="KEEPR · Sheet Bridge",
  card="Automated weekly backup of ACC and BIM 360, plus bulk attribute editing across cloud projects.",
  stack="C# · WPF · Autodesk Platform Services · ACC / BIM 360 APIs",
  head="Disaster recovery and bulk editing for the cloud",
  body=["<strong>KEEPR</strong> is a desktop application using Autodesk Platform Services to schedule and manage weekly backups of ACC and BIM 360 projects. Cloud-hosted does not mean backed up; this closes that gap.",
        "<strong>Sheet Bridge</strong> is a web application for bulk-editing ACC and BIM 360 sheet attributes, replacing a slow one-at-a-time process in the web UI."],
  result="",
  media=[("img","img/image25.png","KEEPR",""),
         ("img","img/image26.png","KEEPR: backup scheduling",""),
         ("img","img/image27.png","KEEPR: project selection",""),
         ("img","img/image28.png","KEEPR: run history",""),
         ("img","img/image29.png","KEEPR: log",""),
         ("img","img/image30.png","Sheet Bridge: bulk attribute editor","")]),

dict(slug="speckle-llm", title="Speckle + LLM", tag="2023",
  card="Natural-language queries over 3D models, before it was a category.",
  stack="Speckle · LLM · natural-language model queries",
  head="I put an LLM on BIM data before it was a category",
  body=["In 2023 I connected Speckle to a large language model so project teams could ask questions about a 3D model in plain language. At the time there was no name for this.",
        "The lesson has shaped everything since: <strong>the model was never the hard part.</strong> The hard part is getting clean, queryable, structured data out of the authoring tools, which is what most of my work has been about ever since."],
  result="Later built a custom <strong>Speckle–Revit connector</strong> for a separate client, extending open interoperability between the two platforms.",
  media=[]),
]

CAPS = [
 ("AEC development","Revit API · Navisworks API · Dynamo · Grasshopper · RhinoCommon · pyRevit · Desite MD"),
 ("Cloud &amp; interoperability","Autodesk Platform Services · AEC Data Model API · Speckle · IFC / IfcOpenShell · ACC · BIM 360"),
 ("AI &amp; agents","Model Context Protocol · Claude API · multi-agent orchestration · Azure OpenAI · LLM evaluation"),
 ("Geospatial","Spatial data mining · distributed GIS &amp; cloud computing · geospatial data harmonisation · photogrammetry &amp; remote sensing · mobile laser scanning · earth-observation data science"),
 ("Software","C# .NET (WPF / MVVM) · Python · React · FastAPI · Node.js · GraphQL · SQL · pytest · Pydantic"),
 ("Data &amp; BI","Power BI · Power Automate · Power Apps · SharePoint · pandas · machine learning"),
]

CSS = """
:root{--bg:#fff;--bg-alt:#f6f7f8;--fg:#16191c;--fg-soft:#5b656e;--fg-faint:#8b959d;
--accent:#1F4E5F;--accent-soft:#e5eef1;--line:#e3e7ea;--card:#fff;
--mono:ui-monospace,SFMono-Regular,"SF Mono",Menlo,Consolas,monospace;
--sans:-apple-system,BlinkMacSystemFont,"Segoe UI",Inter,Roboto,Helvetica,Arial,sans-serif;--maxw:940px}
@media (prefers-color-scheme:dark){:root{--bg:#0e1113;--bg-alt:#14181b;--fg:#e8ecef;--fg-soft:#9aa5ad;
--fg-faint:#6b757d;--accent:#6fb3c9;--accent-soft:#152a33;--line:#232a2f;--card:#131719}}
:root[data-theme="dark"]{--bg:#0e1113;--bg-alt:#14181b;--fg:#e8ecef;--fg-soft:#9aa5ad;--fg-faint:#6b757d;
--accent:#6fb3c9;--accent-soft:#152a33;--line:#232a2f;--card:#131719}
:root[data-theme="light"]{--bg:#fff;--bg-alt:#f6f7f8;--fg:#16191c;--fg-soft:#5b656e;--fg-faint:#8b959d;
--accent:#1F4E5F;--accent-soft:#e5eef1;--line:#e3e7ea;--card:#fff}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--fg);font-family:var(--sans);font-size:16px;
line-height:1.65;-webkit-font-smoothing:antialiased}
.wrap{max-width:var(--maxw);margin:0 auto;padding:0 24px}
a{color:var(--accent);text-decoration:none}a:hover{text-decoration:underline}
.label{font-family:var(--mono);font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--fg-faint);margin:0 0 14px}
header{padding:84px 0 56px;border-bottom:1px solid var(--line)}
h1{font-size:clamp(30px,5.4vw,46px);line-height:1.12;margin:0 0 10px;letter-spacing:-.022em;font-weight:650}
.role{font-family:var(--mono);font-size:clamp(12px,2.1vw,14px);color:var(--accent);letter-spacing:.06em;margin:0 0 26px}
.lede{font-size:clamp(17px,2.5vw,20px);line-height:1.55;max-width:44ch;margin:0 0 18px}
.sub{color:var(--fg-soft);max-width:62ch;margin:0 0 30px}
.links{display:flex;flex-wrap:wrap;gap:10px}
.btn{display:inline-block;padding:9px 15px;border:1px solid var(--line);border-radius:7px;font-size:14px;
color:var(--fg);background:var(--card);transition:.15s}
.btn:hover{border-color:var(--accent);color:var(--accent);text-decoration:none}
.btn.primary{background:var(--accent);border-color:var(--accent);color:#fff}
.btn.primary:hover{opacity:.9;color:#fff}
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(130px,1fr));gap:1px;background:var(--line);
border:1px solid var(--line);border-radius:9px;overflow:hidden;margin:40px 0 0}
.stat{background:var(--bg);padding:18px 16px}
.stat b{display:block;font-size:23px;font-weight:650;letter-spacing:-.02em}
.stat span{font-family:var(--mono);font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--fg-faint)}
section{padding:60px 0;border-bottom:1px solid var(--line)}
h2{font-size:13px;font-family:var(--mono);letter-spacing:.15em;text-transform:uppercase;color:var(--fg-faint);
font-weight:500;margin:0 0 32px}
/* project cards */
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(290px,1fr));gap:18px}
.card{display:block;border:1px solid var(--line);border-radius:11px;overflow:hidden;background:var(--card);
color:var(--fg);transition:.16s}
.card:hover{border-color:var(--accent);transform:translateY(-2px);text-decoration:none}
.card .thumb{aspect-ratio:16/9;background:var(--bg-alt);overflow:hidden;display:grid;place-items:center;border-bottom:1px solid var(--line)}
.card .thumb img{width:100%;height:100%;object-fit:cover;display:block}
.card .thumb .glyph{font-family:var(--mono);font-size:13px;letter-spacing:.16em;text-transform:uppercase;color:var(--fg-faint)}
.card .cbody{padding:16px 18px 18px}
.card h3{font-size:17px;margin:0 0 5px;letter-spacing:-.012em;font-weight:640}
.card .tag{font-family:var(--mono);font-size:10px;letter-spacing:.09em;text-transform:uppercase;
color:var(--accent);background:var(--accent-soft);padding:3px 7px;border-radius:5px;display:inline-block;margin-bottom:9px}
.card p{margin:0;font-size:14.5px;color:var(--fg-soft);line-height:1.55}
.card .more{font-family:var(--mono);font-size:11px;letter-spacing:.09em;text-transform:uppercase;color:var(--accent);margin-top:11px;display:block}
/* project page */
.crumb{font-family:var(--mono);font-size:11.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--fg-faint);
padding:26px 0 0;display:block}
.stack{font-family:var(--mono);font-size:12px;color:var(--fg-faint);margin:0 0 20px}
.proj-body p{margin:0 0 13px;color:var(--fg-soft);max-width:70ch}
.proj-body p strong{color:var(--fg);font-weight:620}
.result{margin-top:18px;padding:13px 16px;background:var(--bg-alt);border-left:2px solid var(--accent);
border-radius:0 7px 7px 0;font-size:15px;color:var(--fg)}
.gallery{display:grid;gap:34px;margin-top:8px}
figure{margin:0}
figure video,figure img{width:100%;border:1px solid var(--line);border-radius:9px;display:block;background:var(--bg-alt)}
figcaption{margin-top:10px}
figcaption b{display:block;font-size:15px;font-weight:640;margin-bottom:3px}
figcaption span{font-size:14px;color:var(--fg-soft);line-height:1.55}
.caps{display:grid;grid-template-columns:repeat(auto-fit,minmax(255px,1fr));gap:22px}
.cap h4{font-family:var(--mono);font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:var(--accent);margin:0 0 7px;font-weight:600}
.cap p{margin:0;font-size:14.5px;color:var(--fg-soft);line-height:1.6}
.cat{display:grid;grid-template-columns:repeat(auto-fit,minmax(215px,1fr));gap:18px 26px}
.cat div h4{font-size:13px;margin:0 0 5px;font-weight:640}
.cat div p{margin:0;font-size:13.5px;color:var(--fg-soft);font-family:var(--mono);line-height:1.75}
.about{display:grid;grid-template-columns:1.55fr 1fr;gap:44px}
.about p{margin:0 0 14px;color:var(--fg-soft);max-width:64ch}.about p strong{color:var(--fg)}
.edu{border-left:1px solid var(--line);padding-left:24px}
.edu div{margin-bottom:19px}.edu b{display:block;font-size:14.5px;font-weight:620}
.edu span{display:block;font-size:13px;color:var(--fg-soft)}
.edu em{display:block;font-family:var(--mono);font-size:11px;color:var(--fg-faint);font-style:normal;margin-top:2px}
@media(max-width:720px){.about{grid-template-columns:1fr;gap:30px}
.edu{border-left:0;border-top:1px solid var(--line);padding:24px 0 0}}
footer{padding:52px 0 66px}footer .lede{margin-bottom:22px}
.meta{margin-top:34px;font-size:12.5px;color:var(--fg-faint);font-family:var(--mono)}
#tt{position:fixed;top:16px;right:16px;z-index:10;width:34px;height:34px;border:1px solid var(--line);
background:var(--card);color:var(--fg-soft);border-radius:8px;cursor:pointer;font-size:14px;line-height:1;
display:grid;place-items:center}
#tt:hover{color:var(--accent);border-color:var(--accent)}
"""

JS = """(function(){var r=document.documentElement,t=document.getElementById('tt'),s=null;
try{s=localStorage.getItem('theme')}catch(e){}
if(s)r.setAttribute('data-theme',s);
t.addEventListener('click',function(){var c=r.getAttribute('data-theme');
if(!c)c=window.matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light';
var n=c==='dark'?'light':'dark';r.setAttribute('data-theme',n);
try{localStorage.setItem('theme',n)}catch(e){}});})();"""

def head(title, desc, css_path, og_img, url):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="{url}">
<meta property="og:site_name" content="{NAME}">
<meta property="og:image" content="{BASE}/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{BASE}/og-image.png">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><rect width='100' height='100' rx='18' fill='%231F4E5F'/><text y='.9em' x='50' text-anchor='middle' font-size='62' font-family='monospace' fill='white'>M</text></svg>">
<link rel="stylesheet" href="{css_path}">
</head>
<body>
<button id="tt" type="button" aria-label="Toggle colour theme">◐</button>
"""

def thumb_for(p):
    for kind, src, *_ in p['media']:
        if kind == 'img':
            return f'<img src="{src}" alt="" loading="lazy">'
    for kind, src, *_ in p['media']:
        if kind == 'video':
            return f'<video src="{src}" muted playsinline preload="metadata"></video>'
    return f'<span class="glyph">{p["title"]}</span>'

# ---------------------------------------------------------------- index
def build_index():
    cards = "".join(f"""
      <a class="card" href="projects/{p['slug']}.html">
        <div class="thumb">{thumb_for(p)}</div>
        <div class="cbody">
          <span class="tag">{p['tag']}</span>
          <h3>{p['title']}</h3>
          <p>{p['card']}</p>
          <span class="more">View project →</span>
        </div>
      </a>""" for p in P)

    caps = "".join(f'<div class="cap"><h4>{t}</h4><p>{b}</p></div>' for t, b in CAPS)

    return head(f"{NAME} | AEC Solutions Architect &amp; AI Specialist",
                "Revit &amp; Navisworks tooling, Autodesk Platform Services, and multi-agent LLM systems over BIM data. Munich.",
                "style.css", "og-image.png", BASE) + f"""
<header><div class="wrap">
  <p class="label">Munich, Germany</p>
  <h1>{NAME}</h1>
  <p class="role">{ROLE}</p>
  <p class="lede">{LEDE}</p>
  <p class="sub">Five years shipping production tooling for architecture and engineering: Revit and Navisworks
  plugins, background services, desktop applications, and cloud integrations that turn manual coordination work
  into systems that run overnight without supervision. Currently owning the AI and automation roadmap for the
  BIM&nbsp;+&nbsp;Data Science department at Sweco, alongside an M.Sc. at TUM.</p>
  <div class="links">
    <a class="btn primary" href="mailto:mohamedkmahdy@outlook.com">Get in touch</a>
    <a class="btn" href="https://www.linkedin.com/in/mohamedkmahdy/" rel="noopener">LinkedIn</a>
    <a class="btn" href="https://github.com/MohamedKMahdy" rel="noopener">GitHub</a>
  </div>
  <div class="stats">
    <div class="stat"><b>~20</b><span>Tools shipped</span></div>
    <div class="stat"><b>5+</b><span>Years in AEC</span></div>
    <div class="stat"><b>6</b><span>Organisations</span></div>
    <div class="stat"><b>895</b><span>Consulting hours</span></div>
  </div>
</div></header>

<section><div class="wrap"><h2>Selected work</h2><div class="cards">{cards}</div></div></section>

<section><div class="wrap"><h2>Capability</h2><div class="caps">{caps}</div></div></section>

<section><div class="wrap"><h2>Background</h2><div class="about">
  <div>
    <p>I trained as an architectural engineer and moved into software because the interesting problems in
    construction are data problems. Most firms are sitting on valuable project data trapped in disconnected
    tools and manual workflows. I build the systems that connect it.</p>
    <p>That has meant Revit and Navisworks plugins in Cairo, model-health and clash-analytics platforms in
    Dubai, and enterprise automation in Munich. Along the way I delivered <strong>18 independent client
    engagements across 895 billable hours</strong> with a 5.0 average rating, doubling my rate over the period.</p>
    <p>My M.Sc. at TUM added the half I was missing: graduate work in geospatial information science, spatial
    data mining, photogrammetry and remote sensing alongside semantic modelling and software engineering.
    <strong>BIM, GIS and AI are converging, and very few people work across all three.</strong></p>
  </div>
  <div class="edu">
    <div><b>Technical University of Munich</b><span>M.Sc. Information Technologies for the Built Environment</span><em>Expected 2026</em></div>
    <div><b>Information Technology Institute</b><span>Intensive Code Camp: BIM Automation Development</span><em>2022 · Giza</em></div>
    <div><b>Alexandria University</b><span>B.Sc. Architectural Engineering</span><em>2014–2020</em></div>
    <div><b>Autodesk</b><span>Certified Professional, Revit Architecture</span><em>2020</em></div>
  </div>
</div></div></section>

<footer><div class="wrap">
  <p class="label">Get in touch</p>
  <p class="lede">Open to conversations about AEC software, openBIM tooling, and AI in the built environment.</p>
  <div class="links">
    <a class="btn primary" href="mailto:mohamedkmahdy@outlook.com">mohamedkmahdy@outlook.com</a>
    <a class="btn" href="https://www.linkedin.com/in/mohamedkmahdy/" rel="noopener">LinkedIn</a>
    <a class="btn" href="https://github.com/MohamedKMahdy" rel="noopener">GitHub</a>
  </div>
  <p class="meta">Munich, Germany · English: professional working proficiency (IELTS Academic 6.5) · Arabic: native · German: A2</p>
</div></footer>
<script>{JS}</script>
</body></html>"""

# ---------------------------------------------------------------- project page
def build_project(p):
    gal = ""
    if p['media']:
        items = ""
        for kind, src, cap, *rest in p['media']:
            note = rest[0] if rest else ""
            el = (f'<video src="../{src}" controls muted playsinline preload="metadata"></video>'
                  if kind == 'video' else f'<img src="../{src}" alt="{cap}" loading="lazy">')
            items += f'<figure>{el}<figcaption><b>{cap}</b>{f"<span>{note}</span>" if note else ""}</figcaption></figure>'
        gal = f'<section><div class="wrap"><h2>Demos &amp; interface</h2><div class="gallery">{items}</div></div></section>'

    body = "".join(f"<p>{b}</p>" for b in p['body'])
    res = f'<div class="result">{p["result"]}</div>' if p['result'] else ""

    return head(f"{p['title']} | {NAME}", html.unescape(p['card']), "../style.css",
                "../og-image.png", f"{BASE}/projects/{p['slug']}.html") + f"""
<div class="wrap"><a class="crumb" href="../index.html">← {NAME}</a></div>
<header style="padding-top:26px"><div class="wrap">
  <p class="label">{p['tag']}</p>
  <h1>{p['head']}</h1>
  <p class="stack">{p['stack']}</p>
  <div class="proj-body">{body}</div>
  {res}
</div></header>
{gal}
<footer><div class="wrap">
  <p class="label">Get in touch</p>
  <p class="lede">Open to conversations about AEC software, openBIM tooling, and AI in the built environment.</p>
  <div class="links">
    <a class="btn primary" href="mailto:mohamedkmahdy@outlook.com">mohamedkmahdy@outlook.com</a>
    <a class="btn" href="../index.html">All work</a>
    <a class="btn" href="https://www.linkedin.com/in/mohamedkmahdy/" rel="noopener">LinkedIn</a>
  </div>
</div></footer>
<script>{JS}</script>
</body></html>"""

# ---------------------------------------------------------------- write
os.makedirs(OUT_PROJ, exist_ok=True)
open(os.path.join(SITE, 'style.css'), 'w').write(CSS)
open(os.path.join(SITE, 'index.html'), 'w').write(build_index())
for p in P:
    open(os.path.join(OUT_PROJ, p['slug'] + '.html'), 'w').write(build_project(p))
print(f"built: index.html, style.css, {len(P)} project pages")
for p in P:
    n = len(p['media'])
    print(f"  projects/{p['slug']}.html  ({n} media)" if n else f"  projects/{p['slug']}.html")
