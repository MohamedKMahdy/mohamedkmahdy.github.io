#!/usr/bin/env python3
"""Static site generator for mohamedkmahdy.com (hosted on Cloudflare Pages, deployed on every push to main).
Run: python3 build.py   (from the site/ directory)"""
import os, re, html, hashlib

SITE = os.path.dirname(os.path.abspath(__file__))
OUT_PROJ = os.path.join(SITE, 'projects')

NAME  = "Mohamed K. Mahdy"
ROLE  = "BIM &amp; AI Solutions Architect"
LEDE  = "I build BIM automation that runs without supervision, and AI on BIM data whose answers can be checked."
BASE  = "https://mohamedkmahdy.com"
DOMAIN = "mohamedkmahdy.com"  # written to CNAME so the old mohamedkmahdy.github.io address keeps redirecting here
EMAIL = "mohamedkmahdy@outlook.com"
LINKEDIN = "https://www.linkedin.com/in/mohamedkmahdy/"
GITHUB = "https://github.com/MohamedKMahdy"

# Filter chips on the index; each project lists the keys it belongs to in `cats`.
CATS = [("revit","Revit"), ("clash","Navisworks &amp; clashes"), ("cloud","Cloud &amp; web"),
        ("data","Data &amp; dashboards"), ("ai","AI")]
# Shown large under "Selected work", one per area of expertise; the rest go in the "More projects" grid.
FEATURED = ["bimnox", "speckle-llm", "aps-raumbuch"]

# ---------------------------------------------------------------- projects
P = [
dict(slug="bimnox", title="Bimnox", tag="Revit 2023 to 2027 · batch", cats="revit cloud",
  card="Runs model checks and exports on dozens of Revit models at once, on a schedule, with nobody sitting at the computer.",
  plain="Architects and engineers keep their designs in Revit models. Every week someone has to open dozens of them, check them for errors and save copies in the formats other teams need. Bimnox does that on its own. You pick the models and the tasks once; it runs them every week and puts the results in one folder.",
  head="Set up a job once, let it run every week.",
  problem="Everyone agrees model checks and deliverable exports matter. Nobody has time to run them by hand on dozens of models every week, so they get skipped.",
  stack=["C#", ".NET Framework 4.8 / .NET 8 / .NET 10", "Revit API", "WPF", "Autodesk Platform Services", "Windows Task Scheduler"],
  body=["<strong>Bimnox</strong> (BIM Nightly Orchestration and eXport) is a desktop program plus a helper that runs inside Revit without a window. It can do seven tasks in one pass: an Autodesk Model Checker run, IFC and NWC exports, PDF and DWG exports of the sheets, a model health report and a report of what changed. It starts the right installed Revit in the background, opens each model once, runs everything you picked and closes it again without saving.",
        "Models can come from four places: selected models in Autodesk Construction Cloud (ACC), a whole ACC folder, a folder on your computer or network, or a fixed list of files. Folders are read again on every run, so new models get picked up, and the results can go back up to ACC.",
        "<strong>The second run is the cheap one.</strong> If a model hasn't changed since the last good run, Bimnox skips it. Everything lands in one output folder with a history workbook for Excel and Power BI, and a Teams message after each run if you want one.",
        "The same code also builds three single-task apps, each with its own name and icon, for teams that only need one job: <strong>Bulk Model Checker</strong>, <strong>IFC Bulk Export</strong> and <strong>NWC Bulk Export</strong>.",
        "I first built scheduled checks and exports like this in 2023. Bimnox is the version I'd want to inherit: nothing depends on someone remembering."],
  result="<strong>One codebase</strong> covers every Revit version from 2023 to 2027 and sends each model to an installed Revit that can open it. German and English interface, and it installs per user without admin rights.",
  media=[]),  # screenshots in MEDIA below

dict(slug="aps-raumbuch", title="Raumbuch", tag="Revit + web", cats="revit cloud",
  card="Builds a room book, every room and everything in it, straight from the building model. A Revit add-in, plus a web app that also opens IFC files.",
  plain="A room book (Raumbuch in German) lists every room in a building with its size, finishes and furniture. Usually someone types it up by hand. Raumbuch builds it from the 3D model and exports it to Excel, PDF and an interactive web page.",
  head="One room book, two routes to it.",
  problem="A room book lists every room and everything in it. Most teams still put it together by hand, room by room, and start over when the design changes.",
  stack=["C#", "Revit API", "React", "Vite", "FastAPI", "APS Viewer", "Model Derivative API", "web-ifc", "three.js"],
  body=["<strong>The Revit add-in</strong> (Revit 2023 to 2027) works out which room every piece of furniture and equipment stands in, linked models included, and writes the room number and name onto it. Then it makes one cropped floor plan per room and exports the room book to Excel, to a PDF with one page per room, and to an interactive HTML page that works offline. The three steps sit in one panel, in German and English.",
        "<strong>The web app</strong> signs in to Autodesk Construction Cloud, lets you browse hubs, projects and folders in every Autodesk data region, and opens a model in the browser with a floor plan next to the 3D view. It finds the rooms in the 3D model, in Autodesk's model data, or in the 2D plans if neither has them. Furniture from the main model and every linked model goes into one coordinate system and is matched to a room by parameter, by position, or by the nearest room within 2 m.",
        "Both export the same formatted German <em>Raumbuch</em>: Excel, PDF, and a single-file HTML dashboard whose charts double as filters."],
  result="I didn't want it tied to one vendor. IFC files open <strong>without any login</strong>, are read in the browser and never leave your machine, and you can load several at once as one model.",
  media=[("img","img/raumbuch-dashboard.jpg","The room book dashboard","One offline HTML file with summary tiles, charts that filter and the room table. Rendered from the real template with sample data."),
         ("imgn","img/raumbuch-panel.png","The Revit add-in panel","Model status, the three steps, the export formats and the settings, in one panel.")]),

dict(slug="clash-management", title="SORTIE", tag="Navisworks · clash tools", cats="clash",
  card="Sorts thousands of Navisworks clashes by building zone, and keeps their status and comments when the clash test runs again.",
  plain="Before a building is built, designers combine the models from every discipline and let software look for places where things collide, such as a pipe running through a beam. These are called clashes, and one check can find thousands. SORTIE groups them by area of the building so each team can see its share, and it carries notes and decisions over when the check is repeated.",
  head="4,000 clashes, 200 actual problems.",
  problem="A clash run can report thousands of clashes when the real coordination problems number a few hundred. Sorting them by area by hand, and losing every status and comment when the test reruns, eats days.",
  stack=["C#", "Navisworks API 2022 to 2027", "WPF", "xUnit"],
  body=["<strong>SORTIE</strong> (Status Organiser, Renamer and Transferrer for Interference Events) is an add-in for Navisworks Manage 2022 to 2027. It does three jobs.",
        "<strong>Zones.</strong> It groups clashes by the zone they sit in, one group per zone, or puts the zone name in front of each clash name. A zone can be any 3D object: a mass, a room, or a separate zones model. It uses the real shape, not a box around it, and where zones overlap the smallest one wins.",
        "<strong>Status transfer.</strong> It saves each clash's status, assignee, approval, description and comments, then puts them back on the same clashes in this file or another one, even from a Navisworks XML clash report. Clashes are matched by their unique ID first, then by the pair of elements.",
        "<strong>Clean up.</strong> It takes clashes back out of their groups, or strips the zone names off again."],
  result="Every action only touches the clash tests you tick, and it undoes in <strong>one step</strong>. If a clash could match two others, SORTIE leaves it alone instead of guessing.",
  media=[("img","img/sortie-zones.png","Grouping clashes by zone","Zones come from any 3D objects; a clash belongs to the zone its clash point lies in."),
         ("img","img/sortie-logo.png","The SORTIE mark","")]),

dict(slug="rimacos", title="Rimacos", tag="openBIM · clash matrices", cats="clash",
  card="Replaces a huge hand-filled clash matrix with a few rules, then writes the clash tests for Navisworks and for open-source tools.",
  plain="A clash matrix is a big table that says which parts of a building should be checked against which, for example pipes against beams. On large projects it has thousands of cells that someone fills in by hand. Rimacos replaces the table with a few rules and produces the checks, reports and files that several programs need, including open formats any software can read.",
  head="Rules, not cells.",
  problem="A clash matrix grows with the square of the number of groups. At some point you're maintaining thousands of cells by hand, then turning them into thousands of clash tests. That doesn't scale.",
  stack=["Python", "IfcOpenShell / IfcClash", "IDS 1.0", "BCF", "Navisworks XML", "openpyxl", "pytest"],
  body=["<strong>Rimacos</strong> (Rule-based Interference Matrices And Clash tests on Open Standards) turns a short list of rules into the whole matrix and the files to run it: search sets and clash tests for Navisworks, clash sets for the open-source IfcClash tool with BCF results, an IDS file that checks the models actually contain what the groups select on, and an Excel matrix and HTML report for the BIM execution plan.",
        "A rule says how two sets of elements are tested against each other. Each side can be everything, a discipline, a tag or a single group, and the most specific rule wins. You edit the matrix, the groups and the rules in a small editor that runs in your browser.",
        "Groups pick elements by IFC class and type, property filters and classification codes, and models are found by their ISO 19650 file names. That's what lets the same matrix run on free, open tools too."],
  result="A classic 133-group matrix had <strong>8,778 cells</strong>. Rimacos rebuilds every one of them from <strong>4 rules</strong>, and the merged output needs <strong>79 clash tests</strong> instead of 8,778.",
  media=[("img","img/rimacos-editor.jpg","The matrix editor","Discipline matrix, the rule behind each cell, and the group pairs it decides.")]),

dict(slug="speckle-llm", title="ARVENT", tag="Speckle · local AI", cats="ai cloud",
  card="Answers questions about a 3D building model in plain language, right in the model's comment threads. It runs on a local AI model, so the data stays on the machine.",
  plain="Most people on a building project never open the 3D model, but they still have questions about it. ARVENT lets them ask in a comment, for example how many doors have no fire rating, and replies with the answer, the exact data behind it and a link that shows those parts in the model. It also checks each new version of the model against the project's written requirements.",
  head="I connected AI to building models before it was a trend.",
  problem="Most people on a project never open the model, but they still have questions about it: what this panel's insulation value is, how many doors have no fire rating, whether the latest version still meets the specification.",
  stack=["Python", "FastAPI", "Speckle (GraphQL, webhooks, specklepy)", "Ollama", "Llama 3.1", "SQLite"],
  body=["In 2023 I connected Speckle, an open platform for sharing 3D building models, to a large language model, so a project team could ask a model questions in plain language. <strong>ARVENT</strong> (Assistant for Requirements, Verification and Element Notes in Threads) is the 2026 rebuild. It runs on a <strong>local Llama model through Ollama</strong>, so model data and project documents never leave the machine.",
        "It lives in Speckle's comment threads. Select an element and ask about it, and it answers from the element's properties and any attached specification PDF, with page references. Ask about the whole model and it answers that too. Every time a new version comes in, it checks it against rules taken from the specification. Each failing rule gets its own thread that highlights the elements, and ARVENT replies there once a later version fixes them.",
        "<strong>The language model never does the maths and never writes the database query.</strong> It only fills in a structured query plan that's limited to real field names. Code checks and fixes that plan, runs it, and shows the exact query and result in every reply. The model can suggest rules from the specification, but nothing runs until a person approves it.",
        "Along the way I also built a custom connector between Speckle and Revit for another client."],
  result="What I learned in 2023 still holds: <strong>the AI was never the hard part.</strong> Getting clean, structured data out of the design tools is.",
  media=[("img","img/arvent-card.png","The ARVENT mark",""), ("img","img/arvent-logo.png","The mark on light and dark backgrounds","On white, on the dark header band and as an icon.")]),

dict(slug="qubecta", title="Qubecta", tag="Revit · cost planning", cats="revit",
  card="Turns the quantities in a Revit model into a priced bill of quantities and a cost plan, exported to Excel, PDF or the German GAEB tender format.",
  plain="To estimate what a building will cost, quantity surveyors measure how much of each material and component it needs, then price it. Much of that information is already in the 3D model. Qubecta reads it from the model, suggests prices and categories, and produces the cost documents in the formats that estimators and tender software use.",
  head="A priced bill and a cost plan without leaving Revit.",
  problem="Quantity surveyors often measure again what the model already knows. It's slow, and every design change means doing it over.",
  stack=["C#", "Revit API 2022 to 2027", ".NET Framework 4.8 / .NET 8 / .NET 10", "ClosedXML", "PDFsharp", "GAEB DA XML 3.3", "xUnit"],
  body=["<strong>Qubecta</strong> (QUantities, Bills, Elements, Costs, Tendering and Assembly codes) is an add-in for Revit 2022 to 2027. You tick the element types you want to price and give each one a unit, a section in the bill (CSI MasterFormat 2018, RICS NRM2 or your own list), a group in the cost plan (UniFormat, RICS NRM1, DIN 276 or your own list), a rate and a description. Typing all that by hand gets old fast, so <strong>Qubecta suggests it</strong>: from your earlier projects, from codes already in the model, and from each type's name and materials. Every suggestion says why, and nothing changes until you've checked it.",
        "Then it measures the model and gives you the bill by trade and the cost plan by building element, with the cost per m² of floor area and the usual additions: site overheads, contingency, VAT. It exports to Excel, PDF and CSV, and to <strong>GAEB DA XML</strong>, the format German tendering and costing software expects, checked against the official schemas. The cost codes also go back into the model, so Revit schedules and IFC exports carry them.",
        "It measures the whole model in one pass, filters by construction phase, design option and floor, and counts linked models that are placed more than once. Categories are matched by Revit's internal IDs, so it works whatever language Revit is in. Doors and windows can take their cost group from the wall or roof they sit in, and walls and floors from whether they're external or load-bearing."],
  result="Tested inside Revit on Autodesk's Snowdon Towers sample model: <strong>392 types, 294 suggestions, 136 bill lines</strong>, a cost plan by element, and a GAEB export that passes the official 3.3 schemas.",
  media=[("img","img/qubecta-tabs.jpg","Set up, bill and cost plan","Three numbered steps in one panel, shown with a sample model."),
         ("img","img/qubecta-suggest-export.jpg","Suggestions and export","Each suggestion says why; exports include GAEB X83 and X82."),
         ("imgn","img/qubecta-revit.png","Docked in Revit","DIN 276 suggestions with their checks, from the in-Revit test on the Snowdon Towers sample."),
         ("video","video/qubecta-earlier.mp4","An earlier version","Generating a detailed bill of quantities in Excel.")]),

dict(slug="rifadex", title="RIFADEX", tag="Revit · interior finishes", cats="revit",
  card="Draws the wall, floor, skirting and ceiling finishes of every room in Revit, and keeps them right when the design changes.",
  plain="Every room in a building gets finishes: plaster or tiles on the walls, a floor covering, skirting boards and a ceiling. In a 3D model each one has to be drawn by hand, and redrawn whenever a room changes. RIFADEX lets you pick the finishes per room, then draws and updates them automatically.",
  head="Finish walls, floors, skirting and ceilings that follow the rooms.",
  problem="Modelling interior finishes by hand, room by room, is slow, and every design change leaves finishes that no longer fit the room.",
  stack=["C#", "Revit API 2024 to 2027", ".NET Framework 4.8 / .NET 8 / .NET 10", "WPF", "extensible storage", "no third-party libraries"],
  body=["You pick a wall, floor, skirting and ceiling finish for each room, one at a time or many at once, in this model or in a linked architect's model. RIFADEX draws a finish wall along each side of the room, a floor with cut-outs for columns and shafts, skirting that stops at doors, and a ceiling at the room height. Door and window openings in the walls behind get cut through the finish walls. Lengths are shown and typed in the project's own units.",
        "<strong>Plan, preview, apply.</strong> You see every change before anything is drawn. Run it again and it updates the finishes that are already there instead of drawing new ones, so tags and schedules keep working: a new code changes the type, a room that changed shape gets redrawn, openings follow moved doors, and a wall moved by up to 500 mm takes its finish with it. A type you changed by hand stays, so a feature wall survives. The linked model is never touched.",
        "Finish types and materials are edited in a table or in Excel, where a new row makes a new type, with an optional naming convention. One settings file holds the company standard, so any template works and nothing has to be added to a project first.",
        "<strong>RIFADEX</strong> (Revit Interior Finishes: Assignment, Drawing and Excel eXchange) rebuilds the in-house finishes tools I wrote years ago as one company-neutral package."],
  result="Tested inside Revit from start to finish, 57 checks in Revit 2026: drawing, redrawing, hand edits, door openings, a moved and rotated linked model, and an Excel round trip. <strong>One codebase for Revit 2024 to 2027</strong>, with no third-party libraries.",
  media=[("img","img/rifadex-room-finishes.png","Room Finishes","Codes per room from a linked model, then save and draw. Captured in Revit 2026."),
         ("imgn","img/rifadex-ribbon.png","The RIFADEX ribbon panel","Four tools: Room Finishes, Finish Types, Finish Materials and Settings."),
         ("img","img/rifadex-finish-types.png","Finish Types","Edit types here or in Excel; a row marked NEW creates a new type."),
         ("img","img/rifadex-materials.png","Finish Materials","The same table and Excel round trip for materials."),
         ("img","img/rifadex-settings.png","Settings","The company standard: finish parameters, types, materials, naming and Excel."),
         ("video","video/finishes-drawer.mp4","An earlier version: drawing finishes","Reads room finishes and draws the walls, floors and skirting."),
         ("video","video/finishes-manager.mp4","An earlier version: finish types","Finish types exported, edited in Excel and written back to the model."),
         ("video","video/materials-manager.mp4","An earlier version: finish materials","The same round trip for finish materials.")]),

dict(slug="acc-integrations", title="LARBACC", tag="ACC · backups", cats="cloud",
  card="Copies your Autodesk Construction Cloud projects to your own drive every week, downloading only what changed.",
  plain="Many construction teams keep all their project files in Autodesk Construction Cloud, an online file platform. If a folder is deleted there or a subscription ends, the files can be lost. LARBACC copies the projects you choose to your own drive every week and keeps the last few copies.",
  head="Stored in the cloud is not the same as backed up.",
  problem="Projects in Autodesk Construction Cloud feel safe because they're in the cloud. But a deleted folder or an ended subscription can still take years of work with it.",
  stack=["C#", ".NET 8", "WPF", "Autodesk Platform Services (PKCE)", "Data Management API"],
  body=["<strong>LARBACC</strong> (Local, Automatic, Rotating Backups of Autodesk Construction Cloud) keeps dated copies of ACC and BIM 360 projects on a local or network drive. You choose the projects and folders, a destination and a weekly time. It downloads the latest version of every document and keeps the last few backups. The interface is in German and English.",
        "<strong>Only changes get downloaded.</strong> If a document hasn't changed since the last backup, LARBACC links to the earlier copy instead of downloading it again (a file-system feature called a hard link). Later runs are fast, and five backups don't take five times the space. A run only counts as a backup once its complete file list is written, so a crash or power cut can't leave a half-finished folder that looks complete.",
        "Sign-in uses PKCE, so there's no secret key inside the program. If LARBACC was closed when a backup was due, it runs at the next start, and a failed run tries again after 15 minutes, 1 hour and 4 hours."],
  result="It started as a desktop front end for Stewart Celani's MIT-licensed <a href=\"https://github.com/stewartcelani/autodesk-construction-cloud-backup\" rel=\"noopener\">autodesk-construction-cloud-backup</a>, and keeps that history and credit.",
  media=[]),  # screenshots in MEDIA below

dict(slug="family-validation", title="Family Validation", tag="Revit · content library", cats="revit",
  card="Checks and cleans whole folders of Revit families against a company standard, without anyone opening Revit.",
  plain="Revit models are built from reusable components called families, such as a door, a chair or a light fitting. Companies keep libraries of hundreds of them, and one badly made family can slow down every project that uses it. Family Validation checks a whole folder of families against the company's rules, fixes what it safely can, and writes a report.",
  head="Clean families in, clean library out.",
  problem="One badly built family, say one with a CAD drawing imported inside it or in the wrong category, slows down every project that loads it. Nobody checks hundreds of them by hand.",
  stack=["C#", "Revit API 2023 to 2027", "WPF", ".NET Framework 4.8 / .NET 8 / .NET 10", "no third-party libraries"],
  body=["A small launcher runs Revit in the background, opens every family in a folder and checks it: the file name against the naming rules (fixing the category prefix when that's safe), imported CAD inside the family (removed, linked CAD kept), whether the name matches the category, required parameters, file size limits, and optionally a classification code like DIN 276 or Uniclass. What comes out is ready for the company library or the Autodesk Content Catalog.",
        "<strong>Safe by design.</strong> The original is copied aside before anything happens, and if that copy fails the family is skipped. Cleaned copies go into their own folder, originals are never changed, and a dry run writes the full report without touching a file.",
        "The rules live in a visual editor, so the people who own the standard can maintain it without writing code. Name patterns are built from blocks, and the editor won't save a rule set the check would reject."],
  result="<strong>No third-party libraries.</strong> It's .NET and the Revit API only, built separately for the .NET version each Revit release ships with.",
  media=[("img","img/family-validation-logo.png","The Family Validation mark","")]),

dict(slug="cloud-revisions", title="Cloud Revisions", tag="Revit add-in", cats="revit data",
  card="Lists every revision cloud in a Revit model with its sheet and revision details, and exports the list to Excel or an offline dashboard.",
  plain="When a drawing changes, designers mark the change with a revision cloud, a wavy outline with a revision number next to it. On a big project there are hundreds of them spread over many drawing sheets. Cloud Revisions collects them all into one list, so anyone can see what changed, where, and in which revision.",
  head="One list of every change marked on the drawings.",
  problem="Keeping track of which revision clouds are on which sheets, and under which revision, usually means clicking through the sheets one by one.",
  stack=["C#", "Revit API 2023 to 2027", ".NET Framework 4.8 / .NET 8 / .NET 10", "dependency-free Excel and HTML"],
  body=["Revision clouds are notes drawn on the drawings, and Autodesk's online data services either don't expose them or only partly. Revit itself is the only complete source, so this had to be a Revit add-in.",
        "It lists every revision cloud in the open model with its view, the sheet it's on and all its revision details: sequence, number, date, description, whether it's been issued, and by and to whom. Then it exports a formatted Excel workbook or a single-file HTML dashboard with filters that work like Power BI's. Everything sits in one panel on its own Revit tab, in German or English."],
  result="Neither export needs Excel, an online service or even internet access. The add-in writes both files itself, so they work on locked-down <strong>company networks</strong> too.",
  media=[("img","img/cloud-revisions-dashboard.jpg","The revision cloud dashboard","Filters by revision, view type, issue status and sheet, with linked charts. Rendered from the real template with sample data."),
         ("img","img/cloud-revisions-logo.png","The Cloud Revisions mark","")]),

dict(slug="revit-automation", title="Revit Automation Suite", tag="4 tools · video", cats="revit",
  card="Four Revit tools that take over repetitive model tasks: preparing files for issue, organising worksets, joining elements and copying types between projects.",
  plain="In Revit, many routine jobs mean clicking through the same steps again and again, such as cleaning up a model before sending it out or copying standard settings into each project. Each of these four tools does one such job automatically, across a whole model or many projects at once.",
  head="Small tools for the jobs nobody wants to do by hand.",
  problem="Small, repetitive Revit tasks, such as setting up worksets, joining elements, copying types between projects and cleaning models before issue, add up to hours of engineering time every week.",
  stack=["C#", "Revit API", "WPF", "Excel interop"],
  body=["A set of Revit add-ins for architecture and engineering teams: model management, worksets, element joins and bulk file operations. Each one replaced a manual routine that was costing engineers hours every week.",
        "The quantity and finishes tools from the same years have since grown into products of their own, <a href=\"qubecta.html\">Qubecta</a> and <a href=\"rifadex.html\">RIFADEX</a>, and they're shown there. All demos below use a generic sample model."],
  result="",
  media=[
    ("video","video/revit-transmitter.mp4","Revit-Transmitter","Detaches models with worksets kept or removed, purges unused elements and prepares files ready for issue."),
    ("video","video/worksets-manager.mp4","Worksets Manager","Creates standard worksets from Excel or by UniFormat code, then puts every element in the right one."),
    ("video","video/auto-joiner.mp4","Auto Joiner","Joins and unjoins every overlapping element of the chosen categories in one pass."),
    ("video","video/transfer-types.mp4","Transfer Types","Choose Revit projects from a folder tree and copy types and families between them in bulk."),
    ("img","img/image54.png","Auto Joiner: interface",""),
  ]),

dict(slug="bim-analytics", title="BIM Analytics", tag="Power BI · 9 dashboards", cats="data",
  card="Power BI dashboards that show model health, open clashes, issues and team workload to the people who never open the models.",
  plain="Project managers need to know whether the 3D models are in good shape, how many design conflicts are still open and who is working on what. That information sits inside model files and cloud platforms they rarely open. These dashboards pull it out automatically and show it in charts that update on their own.",
  head="Making model health visible to people who never open Revit.",
  problem="Model health is invisible to the people who never open Revit, and they are most of the people making decisions about a project.",
  stack=["Power BI", "DAX", "SharePoint", "BIM 360 / ACC", "Revizto", "Python"],
  body=["Automated Power BI dashboards and reporting pipelines for BIM coordination: model health, clash detection, open issues, ACC account administration, resourcing and team assessment.",
        "Each dashboard reads straight from project data and refreshes on a schedule, so the coordination status is current without anyone building a report by hand. They're published as project information hubs on SharePoint.",
        "In 2026 I decoded one programme's 52 Power BI files (model health across 376 Revit models, clash trends, issues and account administration) and rebuilt them as <strong>one self-contained HTML page</strong>. It opens offline in any browser, doesn't need Power BI, and leaves out every personal detail."],
  result="Built and improved across three organisations.",
  media=[("img","img/image12.png","Project information hub: home page",""),
         ("img","img/image10.png","SharePoint deployment",""),
         ("img","img/image11.png","SharePoint: project structure",""),
         ("img","img/image13.png","Automated reporting",""),
         ("img","img/image14.png","Model health dashboard",""),
         ("img","img/image15.png","Model health: detail",""),
         ("img","img/image16.png","Clash detection dashboard","Clash trend over time, live counts per discipline pair, and current totals by test."),
         ("img","img/image17.png","Issues dashboard",""),
         ("img","img/image18.png","ACC admin dashboard",""),
         ("img","img/image19.png","Resources dashboard",""),
         ("img","img/image20.png","Resources: allocation",""),
         ("img","img/image21.png","Resources: detail",""),
         ("img","img/image22.png","Team assessment",""),
         ("img","img/image23.png","Team assessment: breakdown",""),
         ("img","img/image24.png","Team assessment: detail","")]),

dict(slug="curtain-panels", title="Curtain Panel Suite", tag="Revit · facades · 4 tools", cats="revit",
  card="Four Revit tools that take a glass facade from design to finished drawings: create the panels, list them, draw each type and label everything.",
  plain="Large glass facades are made of hundreds of panels, often in many slightly different shapes. Each panel type needs its own drawing, a schedule and dimensions. These four tools create the panels from a design rule, then produce the schedules, drawings and labels automatically.",
  head="Geometry that builds itself.",
  problem="Documenting a complex facade panel by panel, with a schedule, a view and dimensions for every type, is slow and easy to get wrong.",
  stack=["C#", "Revit API", "adaptive families"],
  body=["One chain of tools that takes a curtain wall facade (a facade made of glass and frame panels) from a design rule to fully annotated drawings.",
        "<strong>Panel Generator</strong> creates and edits curtain panels across the facade. <strong>Panel Scheduler</strong> builds and exports panel schedules. <strong>Panel Drawings</strong> creates a separate view for every panel type. <strong>Panel Tagger</strong> labels and dimensions the whole set automatically."],
  result="",
  media=[("img","img/image55.jpeg","Panel Generator",""),
         ("img","img/image56.jpeg","Panel Scheduler",""),
         ("img","img/image57.jpeg","Panel Drawings",""),
         ("img","img/image58.jpeg","Panel Tagger","")]),
]

FEATURES = {
'bimnox': [
 'Seven tasks in one pass: Autodesk Model Checker, IFC export, NWC export for Navisworks, PDF and DWG export of sheets, a model health report and a change report',
 'Each model is opened once for all tasks and closed again without saving',
 'Four kinds of source: selected ACC models, an ACC folder, a local or network folder, or a fixed list of Revit files',
 'Folders are read again at every run, so models added later are included',
 'Works with every installed Revit from 2023 to 2027; each model opens in a version that can read it, and older models are upgraded in memory only, never saved',
 'Weekly runs through the Windows Task Scheduler, even while the program is closed',
 'Works with ACC in both directions: models are downloaded for the run, and the exported files and reports can be uploaded back',
 'Skips a model when its source, settings and results have not changed since the last successful run',
 'PDF of every sheet, of a sheet set saved in the model, or of sheets whose numbers match a pattern; one PDF per sheet or one per model',
 'Model health report per model: warnings, families, CAD imports, links, views, groups and rooms',
 'Change report: the elements added, deleted and changed since the last report',
 'A time limit per model: a model that hangs is closed and reported while the others carry on',
 'One output folder (a SharePoint library synced with OneDrive works), a history workbook for Excel and Power BI, and a Teams message after each run',
 'Three single-task versions from the same code, each with its own name and icon: Bulk Model Checker, IFC Bulk Export and NWC Bulk Export',
 'German and English interface; installs per user without admin rights'],
'aps-raumbuch': [
 'Revit add-in for Revit 2023 to 2027: one panel with three steps and a highlighted next action, in German and English',
 'Finds the room each piece of furniture and equipment stands in, also across linked models, and writes the room number and name onto it',
 'Creates one cropped floor plan per room, named by room number and name',
 'Exports the room book as Excel (area, volume and height as real numbers you can add up and filter), as a PDF with a cover and one page per room with its plan and furniture, and as an offline HTML dashboard',
 'Settings choose which room details go into the PDF, which furniture categories count, and how the room plans look',
 'Web app: Autodesk sign-in, with hubs, projects and folders from all Autodesk data regions (US, Europe, Australia) in one list',
 'Web app: 3D viewer with a floor plan beside it; selecting a room highlights its furniture and cuts the room out of the model',
 "Web app: rooms from the 3D model, from Autodesk's model data or from the 2D plans; furniture from the main model and every linked model in one coordinate system",
 'Furniture is matched to rooms by parameter, by position, or by the nearest room within 2 m; anything left over is listed separately',
 'Searchable room table grouped by floor, with area totals and furniture grouped by category and type',
 'IFC files open in the browser without any login; several files form one combined model, and nothing is uploaded',
 'In IFC mode, selecting a room shows it from above with its furniture',
 'Dashboard export: one offline HTML file with summary tiles, charts that act as filters, a room table with plan images and a CSV download'],
'clash-management': [
 'Groups clashes by the zone their clash point lies in, one group per zone, or adds the zone in front of each clash name',
 'Zones can be any 3D objects: masses, rooms, generic models or a separate zones model',
 'Uses the real zone shape, with a simple bounding box as a faster option for simple zones',
 'Where zones overlap, the smallest wins; clashes outside every zone go to a "No zone" group',
 "The zone name comes from the object's name or from any of its properties",
 'Saves the status, assignee, approval, description and comments of clashes to a file',
 'Loads them onto the same clashes in this or another Navisworks file, also from a Navisworks XML clash report',
 'Matches clashes by their unique ID first, then by the pair of clashing elements; a clash with two possible matches is left alone',
 'Clean up: moves clashes out of their groups, or removes the zone names again',
 'Every action works on the clash tests you tick and is one undo step',
 'One add-in for Navisworks Manage 2022 to 2027, with its own ribbon tab, keyboard shortcuts and a per-user install'],
'rimacos': [
 'Clash rules instead of matrix cells: a rule says how two sets of elements are tested, and the most specific rule wins',
 'Each side of a rule can be everything, a discipline, a tag or a single clash group',
 'Test types: hard clash, conservative hard clash, clearance, duplicate and none, each with a tolerance and a severity',
 'Group priorities decide which side is responsible for fixing each clash',
 'Navisworks output: search sets and Clash Detective tests as XML files, ready to import',
 'Open-source output: IfcClash sets that run on IFC models and report results as BCF',
 'An IDS 1.0 file (buildingSMART) that checks the models contain the classes, codes and properties the groups rely on',
 'An Excel matrix for the BIM execution plan, which can be edited and imported again',
 'HTML report and CSV list of tests, optionally with clash counts per test and discipline pair',
 'Groups select by IFC class and type, property filters, classification codes and Revit categories',
 'Models are found by their ISO 19650 file names',
 'Local browser editor for the matrix, groups, rules and tests; imports classic matrix workbooks',
 'Tests can be merged or kept one per pair of groups'],
'speckle-llm': [
 'Answers questions about a selected element from its properties and any attached specification PDF, with page references',
 'Answers questions about the whole model, such as counts, totals and breakdowns per floor',
 'Keeps every element of the latest version of each model in a local SQLite database',
 'The language model only fills in a structured query plan; code checks and corrects it and runs it as a safe database query',
 'Each reply shows the exact query and result, plus a link that opens exactly those elements in the Speckle viewer',
 'Suggests rules from specification PDFs; a person approves them before they run',
 'Checks every new model version and opens one pinned thread per failing rule, highlighting the elements in the viewer',
 'Replies "Resolved" when a later version fixes the problem',
 'Missing values are reported as missing, never invented, and page references are checked against the documents',
 'Runs on a local Llama model through Ollama, so model data and documents never leave the machine',
 'Works with both Speckle data formats (version 2 Revit parameters and version 3 properties)',
 'Webhook server with signature checks and protection against duplicate retries; a command line for indexing, questions and checks; Docker setup with GPU support'],
'qubecta': [
 'Unit, bill section, cost plan group, rate and description for each element type',
 'Built-in code lists: CSI MasterFormat 2018, RICS NRM2 and NRM1, UniFormat II and DIN 276; Uniclass 2015, OmniClass and Revit assembly code files are read as they are',
 "Suggestions from earlier projects, from codes already in the model, and from each type's name and materials, each with its reason",
 'Doors and windows can take their group from the wall or roof they sit in; walls and floors from whether they are external or load-bearing',
 'Measures count, length, area, volume, perimeter and weight (from material density), with one line per material layer if you want',
 'Filters by construction phase, design option and floor; counts linked models placed more than once',
 'Bill of quantities by trade and cost plan by building element, with cost per m² of gross floor area',
 'Additions on the running total: site overheads, overheads and profit, contingency and VAT; a waste percentage; extra items that are not in the model',
 'Exports to Excel, PDF and CSV, and to GAEB DA XML 3.3 (X83 tender, X82 priced estimate), checked against the official schemas',
 "Writes the cost codes back into the model's Assembly Code, so schedules and IFC exports carry them",
 'Settings and rates are saved in the model; price lists move between projects as Excel files',
 'Works in any Revit language; one panel for Revit 2022 to 2027'],
'rifadex': [
 'Choose wall, floor, skirting and ceiling finishes per room, in this model or a linked model',
 'Set finishes for many rooms at once; filter by floor, by search or by any room property; group rooms by name',
 'Draws finish walls along the room edges, a floor per room with cut-outs, skirting that stops at doors, and a ceiling at the room height',
 'Cuts door and window openings through the finish walls from the walls behind, linked or not',
 'Plan, preview, apply: every change is shown before anything is drawn',
 'Running it again updates existing finishes in place, keeps hand edits, and does not bring back skirting you deleted',
 'A wall moved by up to 500 mm takes its finish wall with it, keeping the same element and its tags; walls are matched by the side that faces the room, so opposite walls of a narrow room are never mixed up',
 'Revit warnings during updates are handled and logged instead of popping up',
 "Height and floor offset can be set per room; lengths in the project's units",
 'Remove drawn finishes per room and surface; a count of what was drawn in each room',
 'Finish types and materials in a table or in Excel; new rows create new types',
 'Optional naming convention built from parts you choose',
 'One settings file holds the company standard and can be shared from a server; any template works',
 'No extra project parameters and no third-party libraries; Revit 2024 to 2027 from one codebase'],
'acc-integrations': [
 'Choose ACC and BIM 360 projects, folders and a destination; the latest version of every document is saved under its ACC name',
 'One dated folder per project and run, with a report and a list of every file and its ACC version',
 'Unchanged documents are linked to the previous backup instead of downloaded again',
 'Keeps the last few backups per project (5 by default) and never deletes anything after a run that had failures',
 'A run only becomes a backup once its file list is written; failed and cancelled runs are kept and labelled',
 'Include or leave out any folder; new folders follow the choice made for their parent folder',
 'Weekly schedule on any days and time, running from the Windows notification area and optionally starting with Windows',
 'Missed backups run at the next start; failed ones are retried after 15 minutes, 1 hour and 4 hours',
 'Secure sign-in (PKCE) with no secret key shipped in the program; an optional key is stored encrypted for the Windows user',
 '1 to 8 downloads at once, a test run that downloads nothing, and daily logs',
 'German and English interface'],
'family-validation': [
 'Checks a whole folder of Revit families without the user opening Revit: a launcher runs a hidden Revit',
 'File name against the naming convention, with a safe automatic fix of the category prefix',
 'Removes imported CAD drawings, keeps linked CAD files, and can also check families nested inside others',
 "Checks that each family's category matches its name",
 'Required family parameters: present, of the right kind, and optionally filled in',
 'File size warning and error limits',
 'Optional classification code check against DIN 276, Uniclass or your own pattern',
 'Originals are copied aside before anything else; cleaned copies go to their own folder; originals are never changed',
 'Dry run that writes the full report without changing a file',
 'Excel report sorted worst first, plus a log',
 'Visual rules editor: name patterns from blocks, refuses rules that would fail, keeps backups, and imports rule sets from colleagues',
 'Revit 2023 to 2027, German and English, no third-party libraries'],
'cloud-revisions': [
 'Lists every revision cloud in the open model',
 'For each cloud: ID, view and view type, the sheet it appears on, revision sequence, number, date, description, issue status, issued by and to, comment and mark',
 'Filters by revision, by clouds on sheets only, and by issued revisions only',
 'Formatted Excel workbook with a fixed header row and filters',
 'Offline HTML dashboard with summary tiles, filter buttons, linked charts and a searchable, sortable table',
 'Neither export needs Excel, online resources or internet access',
 'One panel on its own Revit tab, in German or English, with an explanation for every option',
 'Revit 2023 to 2027, no extra software needed'],
'revit-automation': [
 'Revit-Transmitter: prepares models for issue by detaching them with worksets kept or removed, purging unused elements and saving clean copies',
 'Worksets Manager: creates standard worksets from Excel or by classification, and puts every element in the right one',
 'Auto Joiner: joins or unjoins every overlapping element of the chosen categories in one go, so walls, floors and beams meet cleanly',
 'Transfer Types: copies types and families between many projects chosen from a folder tree'],
'bim-analytics': [
 'Model health dashboards from Autodesk Model Checker results across every project',
 'Clash detection dashboards: the trend per report date, a matrix of discipline pairs, and the clash tests',
 'Issue dashboards from BIM 360 and ACC: causes, companies, status and timelines',
 'ACC account administration: user load, products, companies, project sizes and model opening times',
 'Resourcing and team assessment dashboards',
 'Project information hubs on SharePoint with scheduled refresh',
 'Offline rebuild: 52 Power BI files decoded into one self-contained HTML page with a project picker on every tab, no Power BI needed, and no personal data'],
'curtain-panels': [
 'Panel Generator: creates and edits curtain panels across the whole facade',
 'Panel Scheduler: builds and exports panel schedules',
 'Panel Drawings: creates a separate view for every panel type',
 'Panel Tagger: labels and dimensions the whole set automatically']}

# Plain explanations of the technical words used on the project pages. A page lists only the
# terms that appear in its own text, in this order.
GLOSSARY = [
 ("BIM", r"\bBIM\b", "Building Information Modelling: designing a building as a shared 3D model that also holds data about every part, instead of separate drawings."),
 ("Revit", r"\bRevit\b", "Autodesk's main software for designing buildings as BIM models. Most architects and engineers use it."),
 ("Navisworks", r"\bNavisworks\b", "Autodesk software that combines the models of all disciplines into one and checks them for clashes."),
 ("Add-in", r"\badd-ins?\b", "A small program that runs inside another program, here inside Revit or Navisworks, and adds new buttons and features to it."),
 ("Family", r"\bfamil(y|ies)\b", "A reusable Revit component, such as a door, a window, a chair or a light fitting."),
 ("Sheet", r"\bsheets?\b", "A drawing page in Revit, ready to print or send out."),
 ("Workset", r"\bworksets?\b", "A part of a shared Revit model that one team member can edit while others work on the rest."),
 ("Linked model", r"\blinked (architect's )?models?\b", "A model from another file, often from another team, shown inside your model for reference but kept separate from it."),
 ("Schedule", r"\b(panel|Revit) schedules?\b|\bschedules keep\b", "A table in Revit that lists elements and their data, for example every door with its size."),
 ("Curtain wall", r"\bcurtain (wall|panel)s?\b", "A building facade made of glass and frame panels hung on the structure, like most office towers."),
 ("Clash", r"\bclash(es)?\b", "A place where two parts of a building model collide, for example a pipe running through a beam."),
 ("ACC / BIM 360", r"\b(ACC|BIM 360|Autodesk Construction Cloud)\b", "Autodesk Construction Cloud, an online platform where project teams store and share models and documents. BIM 360 is the older version."),
 ("IFC", r"\bIFC\b", "An open file format for building models that any BIM software can read. It is maintained by buildingSMART."),
 ("NWC", r"\bNWC\b", "The file format Navisworks uses to bring in Revit models."),
 ("DWG", r"\bDWG\b", "The standard file format for CAD drawings."),
 ("Autodesk Model Checker", r"\bModel Checker\b", "A free Autodesk tool that checks Revit models against a list of rules and writes a report."),
 ("BCF", r"\bBCF\b", "An open format for passing model issues, such as clashes, between different BIM programs."),
 ("IDS", r"\bIDS\b", "An open format that lists the information a model must contain, so that it can be checked automatically."),
 ("ISO 19650", r"\bISO 19650\b", "The international standard for managing information on BIM projects, including how files are named."),
 ("Speckle", r"\bSpeckle\b", "An open platform for sharing and viewing 3D building models online."),
 ("Language model", r"\b(language model|LLM|Llama)\b", "An AI model that reads and writes text, like the one behind ChatGPT. Llama is a free one that can run on your own computer."),
 ("GAEB", r"\bGAEB\b", "The German standard file format for construction tenders and cost estimates."),
 ("Power BI", r"\bPower BI\b", "Microsoft's software for interactive charts and dashboards."),
]

MEDIA = {'bimnox': [('img', 'img/bimnox-jobs.png', 'A weekly job', 'Models from ACC, the Revit version each one opens in, and the tasks to run. Made-up data.'), ('img', 'img/bimnox-tasks.png', 'Seven tasks, one pass', ''), ('img', 'img/bimnox-pdf.png', 'PDF export of the sheets', ''), ('img', 'img/bimnox-reports.png', 'Model health and change reports', ''), ('img', 'img/bimnox-schedule.png', 'Output, history, Teams and the weekly schedule', ''), ('img', 'img/bimnox-results.png', 'Results per model and task', 'Skipped models show why they were skipped; failures say what to fix.'), ('img', 'img/bimnox-mark.png', 'The Bimnox mark', 'A line cube with a green moon, on dark and light.'), ('img', 'img/bimnox-editions.png', 'The edition icons', 'Bimnox, Bulk Model Checker, IFC Bulk Export and NWC Bulk Export.'), ('img', 'img/bimnox-edition-modelcheck.png', 'Bulk Model Checker edition', ''), ('img', 'img/bimnox-edition-ifc.png', 'IFC Bulk Export edition', ''), ('img', 'img/bimnox-edition-nwc.png', 'NWC Bulk Export edition', ''), ('img', 'img/image9.png', 'An earlier version: scheduled model checks', ''), ('img', 'img/image7.png', 'An earlier version: nightly exports', '')], 'aps-raumbuch': [('img', 'img/raumbuch-dashboard.jpg', 'The room book dashboard', 'One offline HTML file. Rendered from the real template with sample data.'), ('imgn', 'img/raumbuch-panel.png', 'The Revit add-in panel', 'Model status, the three steps, export formats and settings.'), ('img', 'img/raumbuch-excel.png', 'Excel export', 'Rooms with their furniture grouped under each room.'), ('img', 'img/raumbuch-pdf-room.png', 'PDF: one page per room', 'General data, the room plan and the furniture list.'), ('img', 'img/raumbuch-web-login.png', 'Web app: sign in or open IFC', 'Autodesk sign-in for ACC, or IFC files with no login.'), ('img', 'img/raumbuch-web-ifc.png', 'Web app: an IFC model', 'The model, the plan panel and the room table side by side.'), ('img', 'img/raumbuch-web-room.png', 'Web app: a selected room', 'Shown from above with its furniture.'), ('img', 'img/raumbuch-web-settings.png', 'Web app: settings', 'Which room parameters and furniture categories go into the exports.')], 'clash-management': [('img', 'img/sortie-zones.png', 'Zones', ''), ('img', 'img/sortie-transfer.png', 'Status transfer', ''), ('img', 'img/sortie-report.png', 'A finished transfer', ''), ('img', 'img/sortie-cleanup.png', 'Clean up', ''), ('img', 'img/sortie-logo.png', 'The SORTIE mark', '')], 'rimacos': [('img', 'img/rimacos-editor.jpg', 'The matrix editor', ''), ('img', 'img/rimacos-tests.jpg', 'The clash tests a rule set produces', ''), ('img', 'img/rimacos-report.jpg', 'The HTML report', '')], 'speckle-llm': [('img', 'img/arvent-card.png', 'The ARVENT mark', ''), ('img', 'img/arvent-01-index.png', 'Reading a model into the local database', ''), ('img', 'img/arvent-query.png', 'A model-wide question', ''), ('img', 'img/arvent-03-query-de.png', 'The same question in German', ''), ('img', 'img/arvent-04-extract.png', 'Rules proposed from a specification', ''), ('img', 'img/arvent-check.png', 'Checking approved rules', ''), ('img', 'img/arvent-ask.png', 'A missing value is reported, never invented', '')], 'qubecta': [('img', 'img/qubecta-tabs.jpg', 'Set up, bill and cost plan', 'Shown with a sample model.'), ('img', 'img/qubecta-suggest-export.jpg', 'Suggestions, measured quantities and export', ''), ('imgn', 'img/qubecta-revit.png', 'Docked in Revit', 'DIN 276 suggestions with their checks on the Snowdon Towers sample.'), ('img', 'img/qubecta-pdf.png', 'PDF bill summary', ''), ('img', 'img/qubecta-pdf-division.png', 'PDF bill by division', ''), ('img', 'img/qubecta-excel.png', 'Excel cost plan by element', ''), ('img', 'img/qubecta-excel-division.png', 'Excel bill by division', ''), ('video', 'video/qubecta-earlier.mp4', 'An earlier version', 'Generating a detailed bill of quantities in Excel.')], 'acc-integrations': [('img', 'img/larbacc-projects.png', 'Projects and weekly schedule', 'Made-up data.'), ('img', 'img/larbacc-folders.png', 'Folder selection', ''), ('img', 'img/larbacc-running.png', 'A backup running', ''), ('img', 'img/larbacc-first-run.png', 'First start', ''), ('imgn', 'img/larbacc-settings.png', 'Settings', '')], 'family-validation': [('img', 'img/family-validation-logo.png', 'The Family Validation mark', ''), ('img', 'img/family-validation-start.png', 'The launcher', ''), ('img', 'img/family-validation-launcher.png', 'A finished check', ''), ('img', 'img/family-validation-standards.png', 'The rules editor', ''), ('img', 'img/family-validation-standards-problem.png', 'The rules editor refusing an invalid rule', '')], 'cloud-revisions': [('img', 'img/cloud-revisions-dashboard.jpg', 'The revision cloud dashboard', ''), ('img', 'img/cloud-revisions-workbook.png', 'The Excel workbook', ''), ('imgn', 'img/cloud-revisions-panel.png', 'The docked panel', ''), ('img', 'img/cloud-revisions-logo.png', 'The Cloud Revisions mark', '')]}
for _p in P:
    if _p['slug'] in MEDIA: _p['media'] = MEDIA[_p['slug']]
    if _p['slug'] == 'bim-analytics': _p['media'] = [('img', 'img/bimperf-overview.jpg', 'Offline rebuild: overview', 'Client project names are blurred.'), ('img', 'img/bimperf-model-health-summary.jpg', 'Offline rebuild: model health', ''), ('img', 'img/bimperf-clash-detection.jpg', 'Offline rebuild: clash detection', '')] + _p['media']
    _p['features'] = FEATURES.get(_p['slug'], [])


# ---------------------------------------------------------------- notes
# Short dated write-ups in my own voice. A string starting with "## " is a heading, anything else a paragraph.
# `related` lists project slugs shown under the note.
NOTES = [
dict(slug="rules-for-ai-on-bim-data", date="2026-11-11",
  title="The rules I follow when I put a language model on BIM data",
  lead="Six rules from building an assistant that answers questions about building models. Most of them are about what the model isn't allowed to do.",
  related=["speckle-llm"],
  body=[
   "Most demos of AI on BIM data look the same. Someone types a question, an answer appears, everyone nods. Nobody asks how you'd know if the answer was wrong.",
   "On a real project that's the only question that matters. A wrong door count goes into a tender. A wrong fire rating goes into a report that someone signs. So when I rebuilt ARVENT in 2026, three years after I first connected Speckle to a language model, I wrote down the rules it had to follow. I use the same ones everywhere now.",
   "## 1. The model never does the arithmetic",
   "Counting, summing and comparing are done by code. A language model asked to count doors is guessing at a number that a query can simply return.",
   "## 2. The model never writes the query",
   "It fills in a structured query plan, and the plan can only use field names that exist in the data. Code checks the plan, repairs what it can and runs it. The model chooses what to ask for. It doesn't get to decide how.",
   "## 3. Every answer shows its working",
   "Each reply includes the exact query and the result it came from, and a link that shows those elements in the model. Anyone can check an answer without having to trust me or the model.",
   "## 4. Missing data is reported, not filled in",
   "If a door has no fire rating, the answer says so. It sounds obvious. It's also the first thing a language model gets wrong when it's left alone, because a plausible value is always available.",
   "## 5. Nothing takes effect until a person approves it",
   "ARVENT can read a specification and propose rules to check the model against. Those rules do nothing until someone approves them. The same goes for anything else AI suggests in my tools: a person signs off.",
   "## 6. Project data stays where it is",
   "ARVENT runs on a local Llama model through Ollama, so model data and project documents never leave the machine. On many projects that decides whether a tool is allowed at all.",
   "## What this leaves for the model",
   "Less than you'd think, and that's fine. It turns a question in plain language into a plan, and it turns a result back into a sentence. Those are the two things it's good at.",
   "What I learned in 2023 still holds. The model was never the hard part. Getting clean, structured data out of the design tools is.",
  ]),
dict(slug="running-with-nobody-watching", date="2026-11-11",
  title="What a BIM tool needs before it can run with nobody watching",
  lead="Seven requirements I now treat as a checklist. Each one comes from a tool that had to run overnight.",
  related=["bimnox", "acc-integrations", "family-validation"],
  body=[
   "Writing a tool that works while you watch it is the easy half. The hard half is the Tuesday night when the network drops, one model hangs, and nobody looks at the result until Thursday.",
   "These are the seven things I build in before I let a tool run on a schedule.",
   "## 1. It knows when not to work",
   "Bimnox skips a model when its source, its settings and its results haven't changed since the last good run. LARBACC links an unchanged document to the previous backup instead of downloading it again. The second run should be the cheap one.",
   "## 2. One bad input doesn't stop the rest",
   "Every model in Bimnox has a time limit. A model that hangs is closed and reported, and the others carry on.",
   "## 3. It doesn't change what it reads",
   "Bimnox opens each model once, runs every task and closes it without saving. Older models are upgraded in memory only. Family Validation copies each original aside before it does anything, and if that copy fails, the family is skipped.",
   "## 4. A half-finished result can't look finished",
   "In LARBACC a run only counts as a backup once its complete file list is written. A crash or a power cut leaves a folder that's labelled as failed, not one that looks complete.",
   "## 5. It retries on its own, and it's careful after a failure",
   "A missed backup runs at the next start. A failed one tries again after 15 minutes, 1 hour and 4 hours. After any run that had failures, nothing old is deleted.",
   "## 6. It leaves a record someone else can read",
   "One output folder. A history workbook. A message in Teams after each run. Skipped models say why they were skipped, and failures say what to fix. The person reading it on Thursday wasn't there on Tuesday.",
   "## 7. There's a way to rehearse",
   "A dry run that writes the full report without changing a file. A test run that downloads nothing. People trust a schedule more once they've seen what it would have done.",
   "None of this is clever. It's what lets people stop thinking about the tool.",
  ]),
]

def nice_date(iso):
    y, m, d = iso.split("-")
    return f"{int(d)} {['January','February','March','April','May','June','July','August','September','October','November','December'][int(m)-1]} {y}"

# Where I've worked: (when, employer, place, role, summary)
JOBS = [
 ("2026 to now", "Sweco", "Munich", "BIM &amp; AI Solutions Architect", "I work on the department's AI roadmap: scoping the automation portfolio, planning the Microsoft Copilot Studio rollout and setting delivery milestones with leadership. I also build the Revit tools and LLM agents myself and take them through internal release."),
 ("2025 to 2026", "Sweco", "Munich", "BIM &amp; AI Specialist (working student)", "Revit add-ins, LLM agents that search technical documentation, Power Automate and Power Apps for project workflows, and Power BI dashboards that show coordination status."),
 ("2024 to 2025", "Obermeyer", "Munich", "BIM Software Developer (working student)", "Scripts that automate model-checking rules in Desite MD, Power Automate flows that sort and name SharePoint files, and Power BI dashboards on model quality."),
 ("2023 to 2024", "Dewan Architects + Engineers", "Dubai, remote", "BIM Software Developer &amp; Data Analyst", "BIM software and data analysis for coordination, model quality and project reporting."),
 ("2022 to 2024", "Freelance", "Remote", "BIM Software Developer &amp; Data Analyst", "18 client projects: Revit automation, Dynamo scripts and Python data pipelines."),
 ("2023", "Solid Construction", "Cairo", "BIM Software Developer", "Revit add-ins and Dynamo scripts for structural modelling, quantities and finishes."),
 ("2021 to 2023", "Pinnacle Misr", "Cairo", "BIM Coordinator / Developer", "Revit plugins and Dynamo workflows on large projects, including the El Alamein Iconic Tower and Kitoko Ministerial City."),
 ("2020 to 2021", "X-Dimension", "Cairo", "BIM Architect", "BIM standards and templates, Dynamo scripts, and Scan-to-BIM (turning laser scans of existing buildings into models)."),
]

# How I build: principles drawn from the projects above.
WAYS = [
 ("People stay in control", "Every action is one undo step. There's a dry run before anything changes. When AI suggests something, a person signs off."),
 ("Boring is a feature", "The best tools run overnight, try again when the network drops, and never leave a half-finished result that looks finished."),
 ("Data stays where it belongs", "AI models that run locally, IFC files read in the browser instead of uploaded, and no passwords or keys baked into a program."),
 ("Open where it counts", "IFC, IDS and BCF wherever they fit, so nobody gets locked into one vendor."),
]

CAPS = [
 ("AEC development","Add-ins and scripts inside the tools designers already use.",
  "Revit API (2022 to 2027) · Navisworks API · Autodesk Model Checker · Dynamo · Grasshopper · RhinoCommon · pyRevit · Desite MD"),
 ("Cloud &amp; interoperability","Getting model data out of one platform and into another, with open standards where possible.",
  "Autodesk Platform Services (Viewer, Model Derivative, Data Management, AEC Data Model) · ACC · BIM 360 · Speckle · IFC / IfcOpenShell / web-ifc · IDS · BCF"),
 ("AI &amp; agents","Language models on top of BIM data, with the numbers computed by code rather than guessed.",
  "Model Context Protocol · Claude API · local LLMs (Ollama, Llama) · constrained query planning · multi-agent orchestration · Azure OpenAI · LLM evaluation"),
 ("Geospatial","Graduate training at TUM in GIS, spatial data mining and remote sensing.",
  "Spatial data mining · distributed GIS &amp; cloud computing · geospatial data harmonisation · photogrammetry &amp; remote sensing · mobile laser scanning · earth-observation data science"),
 ("Software","Desktop, web and back-end work, tested and built for every supported Revit version.",
  "C# .NET (Framework 4.8, .NET 8, .NET 10; WPF / MVVM) · Python · React · Vite · FastAPI · Node.js · GraphQL · SQL · SQLite · xUnit · pytest · Pydantic"),
 ("Data &amp; BI","Dashboards and flows that make project data visible to people who never open the model.",
  "Power BI · Power Automate · Power Apps · SharePoint · pandas · machine learning"),
]

# What I do: (title, plain description, CAPS indices whose tools it lists, project categories it links to)
PILLARS = [
 ("Revit &amp; Navisworks tools", "Add-ins and batch tools that take repetitive model work off people's desks: checks, exports, quantities and clashes.", [0], ["revit", "clash"]),
 ("Cloud &amp; data integration", "Getting model data out of one platform and into another, and into dashboards people who never open the model will actually read.", [1, 5], ["cloud", "data"]),
 ("AI on BIM data", "Language models that answer questions about a building model, with the numbers computed by code rather than guessed.", [2], ["ai"]),
]

CSS = """
/* Modern professional: monochrome zinc neutrals, near-black and white, Inter. No colour accent except the green status dot. Dark navy header and hero in both modes;
   in dark mode the page body is a step lighter than the header. */
:root{--bg:#ffffff;--bg-alt:#fafafa;--card:#ffffff;--line:#e4e4e7;--line-strong:#d4d4d8;
--fg:#18181b;--fg-soft:#52525b;--fg-faint:#71717a;
--accent:#18181b;--accent-2:#52525b;--accent-hi:#e4e4e7;--on-accent:#ffffff;--accent-soft:#f4f4f5;--warm:#18181b;
--ink:#09090b;--ink-2:#18181b;--on-ink:#fafafa;--ink-soft:#a1a1aa;--ink-line:rgba(161,161,170,.16);
--charcoal:var(--ink);--on-charcoal:var(--on-ink);
--shadow:0 1px 2px rgba(9,9,11,.04),0 1px 3px rgba(9,9,11,.06);
--shadow-hi:0 12px 32px -12px rgba(9,9,11,.18),0 2px 6px rgba(9,9,11,.05);
--r:12px;--r-sm:8px;
--sans:"Inter",ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;
--maxw:1120px;--read:760px}
:root[data-theme="dark"]{--bg:#18181b;--bg-alt:#111113;--card:#27272a;--line:#3f3f46;--line-strong:#52525b;
--fg:#f4f4f5;--fg-soft:#d4d4d8;--fg-faint:#a1a1aa;
--accent:#fafafa;--accent-2:#a1a1aa;--accent-hi:#e4e4e7;--on-accent:#18181b;--accent-soft:rgba(255,255,255,.06);--warm:#fafafa;
--shadow:0 1px 2px rgba(0,0,0,.3);--shadow-hi:0 16px 36px -14px rgba(0,0,0,.7)}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%;scroll-behavior:smooth;scroll-padding-top:76px}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}*{transition:none!important}}
body{margin:0;background:var(--bg);color:var(--fg);font-family:var(--sans);font-size:16.5px;
line-height:1.65;-webkit-font-smoothing:antialiased;font-feature-settings:"cv11","ss01"}
::selection{background:#d4d4d8;color:#09090b}
.wrap{max-width:var(--maxw);margin:0 auto;padding:0 24px}
.read{max-width:var(--read)}
a{color:var(--accent);text-decoration:none;text-underline-offset:3px}a:hover{text-decoration:underline}
:focus-visible{outline:2px solid var(--accent-2);outline-offset:3px;border-radius:6px}
.skip{position:absolute;left:-999px;top:8px;background:var(--card);padding:8px 12px;border-radius:var(--r-sm);z-index:30}
.skip:focus{left:12px}
/* dark surfaces: navy with a soft blue glow */
.band,.contact{background-color:var(--ink);
background-image:radial-gradient(900px 420px at 85% -10%,rgba(255,255,255,.07),transparent 60%)}
/* nav */
.nav{position:sticky;top:0;z-index:20;background:rgba(9,9,11,.82);-webkit-backdrop-filter:saturate(1.6) blur(14px);
backdrop-filter:saturate(1.6) blur(14px);color:var(--on-ink);border-bottom:1px solid var(--ink-line)}
.nav .wrap{display:flex;align-items:center;gap:18px;height:64px}
.brand{display:flex;align-items:center;gap:11px;color:var(--on-ink);font-weight:600;letter-spacing:-.01em;margin-right:auto;font-size:15.5px}
.brand:hover{text-decoration:none}
.brand i{width:32px;height:32px;flex:none;border-radius:9px;display:grid;place-items:center;font-style:normal;
font-size:13px;font-weight:700;letter-spacing:-.02em;color:#09090b;background:#fafafa;
box-shadow:inset 0 -1px 0 rgba(0,0,0,.12)}
.nav nav{display:flex;gap:2px}
.nav nav a{color:#d4d4d8;font-size:14.5px;font-weight:500;padding:7px 12px;border-radius:var(--r-sm);transition:color .15s,background-color .15s}
.nav nav a:hover{color:#fff;background:rgba(255,255,255,.07);text-decoration:none}
#tt{width:36px;height:36px;border:1px solid rgba(161,161,170,.25);background:transparent;color:#d4d4d8;border-radius:var(--r-sm);
cursor:pointer;font-size:15px;line-height:1;display:grid;place-items:center;flex:none;transition:color .15s,border-color .15s}
#tt:hover{color:#fff;border-color:rgba(161,161,170,.5)}
@media(max-width:640px){.wrap{padding:0 16px}.brand span{display:none}.nav .wrap{gap:4px}.nav nav a{padding:6px 7px;font-size:13.5px}.nav nav a.hide-sm{display:none}}
/* hero and project headers */
.band{color:var(--on-ink);position:relative}
.band a{color:var(--accent-hi)}
.hero{padding:88px 0 64px}
.hero .hello{display:inline-flex;align-items:center;gap:8px;font-size:13.5px;font-weight:500;color:#e4e4e7;
background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.12);padding:5px 12px;border-radius:999px;margin:0 0 20px}
.hero .hello b{width:7px;height:7px;border-radius:50%;background:#22c55e;box-shadow:0 0 0 3px rgba(34,197,94,.22)}
.hero .role{color:var(--ink-soft)}
.hero .sub{color:#d4d4d8}
.hero .now{background:rgba(255,255,255,.04);border-color:rgba(161,161,170,.2);color:#e4e4e7}
.hero .btn{background:rgba(255,255,255,.04);color:var(--on-ink);border-color:rgba(161,161,170,.28)}
.hero .btn:hover{border-color:rgba(161,161,170,.55);background:rgba(255,255,255,.08);color:#fff}
.hero .btn.primary{background:#fafafa;border-color:#fafafa;color:#09090b}
.hero .btn.primary:hover{background:#e4e4e7;border-color:#e4e4e7;color:#09090b}
.hero .photo{box-shadow:0 0 0 1px rgba(161,161,170,.25),0 0 0 8px rgba(255,255,255,.03),0 24px 60px -24px rgba(0,0,0,.8)}
.band .crumb{color:var(--ink-soft)}.band .crumb:hover{color:#fff}
.band .phead{padding:20px 0 52px}
.band .phead .subtitle{color:#e4e4e7}
.band .tag{background:rgba(255,255,255,.06);border-color:rgba(255,255,255,.14);color:#e4e4e7}
.band .chips li{background:rgba(255,255,255,.05);border-color:rgba(161,161,170,.22);color:#e4e4e7}
.hero .grid{display:grid;grid-template-columns:1fr auto;gap:64px;align-items:center}
.photo{width:220px;height:220px;border-radius:50%;object-fit:cover;display:block;background:#fff}
.hello{font-size:16px;color:var(--warm);margin:0 0 6px;font-weight:500}
h1{font-size:clamp(38px,6vw,60px);line-height:1.05;margin:0 0 12px;letter-spacing:-.035em;font-weight:700}
.role{font-size:clamp(15px,2vw,17px);font-weight:500;margin:0 0 26px}
.lede{font-size:clamp(20px,2.6vw,24px);line-height:1.4;max-width:32ch;margin:0 0 16px;font-weight:600;letter-spacing:-.02em}
.sub{color:var(--fg-soft);max-width:60ch;margin:0 0 26px}
.now{display:inline-flex;align-items:center;gap:10px;font-size:14px;color:var(--fg-soft);background:var(--card);
border:1px solid var(--line);border-radius:999px;padding:6px 14px 6px 12px;margin:0 0 30px}
.now b{width:8px;height:8px;border-radius:50%;background:#22c55e;box-shadow:0 0 0 3px rgba(34,197,94,.2)}
.links{display:flex;flex-wrap:wrap;gap:10px}
.btn{display:inline-flex;align-items:center;padding:10px 18px;border:1px solid var(--line-strong);border-radius:var(--r-sm);font-size:15px;
color:var(--fg);background:var(--card);transition:background-color .15s,border-color .15s,color .15s,box-shadow .15s;font-weight:500}
.btn:hover{border-color:var(--fg-faint);text-decoration:none}
.btn.primary{background:var(--accent);border-color:var(--accent);color:var(--on-accent);box-shadow:none}
.btn.primary:hover{opacity:.88;color:var(--on-accent)}
/* stats */
.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin:64px 0 0}
.stat{padding:18px 20px;border:1px solid rgba(161,161,170,.16);border-radius:var(--r);background:rgba(255,255,255,.03)}
.stat b{display:block;font-size:30px;font-weight:700;letter-spacing:-.03em;line-height:1.15;color:#fff;font-variant-numeric:tabular-nums}
.stat span{font-size:13.5px;color:var(--ink-soft)}
@media(max-width:760px){.hero{padding:52px 0 48px}.hero .grid{grid-template-columns:1fr;gap:28px}
.photo{width:120px;height:120px;order:-1}.stats{grid-template-columns:repeat(2,1fr);margin-top:44px}}
/* sections */
section{padding:96px 0}
section+section{border-top:1px solid var(--line)}
#services,#notes,#about{background:var(--bg-alt)}
.sec-head{margin:0 0 40px;max-width:var(--read)}
.eyebrow{font-size:13px;font-weight:600;letter-spacing:.06em;text-transform:uppercase;color:var(--fg-faint);margin:0 0 10px}
h2{font-size:clamp(28px,3.6vw,38px);line-height:1.15;letter-spacing:-.03em;margin:0 0 12px;font-weight:700;color:var(--fg)}
.sec-head p{color:var(--fg-soft);margin:0 0 10px}
.hint{font-size:14.5px;color:var(--fg-faint)}
/* filters + cards */
.filters{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 28px}
.filters button{font:inherit;font-size:14px;font-weight:500;padding:6px 14px;border-radius:999px;border:1px solid var(--line);
background:var(--card);color:var(--fg-soft);cursor:pointer;transition:border-color .15s,color .15s,background-color .15s}
.filters button:hover{border-color:var(--line-strong);color:var(--fg)}
.filters button[aria-pressed="true"]{background:var(--fg);border-color:var(--fg);color:var(--bg)}
.filters button small{opacity:.55;margin-left:4px;font-size:12.5px;font-variant-numeric:tabular-nums}
.cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(310px,1fr));gap:24px}
.card{display:flex;flex-direction:column;border:1px solid var(--line);border-radius:var(--r);overflow:hidden;
background:var(--card);color:var(--fg);transition:transform .2s ease-out,box-shadow .2s ease-out,border-color .2s;box-shadow:var(--shadow)}
.card[hidden]{display:none}
.card:hover{border-color:var(--line-strong);transform:translateY(-4px);text-decoration:none;box-shadow:var(--shadow-hi)}
.card .thumb{aspect-ratio:16/9;background:var(--bg-alt);overflow:hidden;border-bottom:1px solid var(--line)}
.card .thumb img{width:100%;height:100%;object-fit:cover;object-position:top;display:block;transition:transform .4s ease-out}
.card:hover .thumb img{transform:scale(1.03)}
.glyph{width:100%;height:100%;display:flex;flex-direction:column;justify-content:flex-end;padding:20px 22px;
background:linear-gradient(135deg,#18181b,#3f3f46)}
.glyph b{font-size:24px;line-height:1.15;letter-spacing:-.02em;color:#fff;font-weight:700}
.glyph small{font-size:12.5px;color:#d4d4d8;margin-top:4px}
.card .cbody{padding:20px 22px 22px;display:flex;flex-direction:column;flex:1}
.card h3{font-size:19px;margin:0 0 6px;letter-spacing:-.02em;font-weight:650}
.tag{font-size:12px;font-weight:500;color:var(--fg-soft);background:var(--accent-soft);border:1px solid var(--line);
padding:3px 10px;border-radius:999px;display:inline-block;margin-bottom:12px;align-self:flex-start}
.card p{margin:0;font-size:15px;color:var(--fg-soft);line-height:1.6}
.more{font-size:14px;font-weight:600;color:var(--accent);margin-top:auto;padding-top:18px}
.card:hover .more{text-decoration:underline}
/* timeline */
.timeline{list-style:none;margin:0;padding:0;max-width:860px}
.timeline li{display:grid;grid-template-columns:120px 1fr;gap:28px;position:relative;padding:0 0 36px}
.timeline li:last-child{padding-bottom:0}
.timeline li::before{content:"";position:absolute;left:143px;top:12px;bottom:-12px;width:2px;background:var(--line)}
.timeline li:last-child::before{display:none}
.timeline .when{font-size:13.5px;font-weight:500;color:var(--fg-faint);padding-top:3px;text-align:right;font-variant-numeric:tabular-nums}
.timeline .job{position:relative;padding-left:22px}
.timeline .job::before{content:"";position:absolute;left:-12px;top:7px;width:12px;height:12px;border-radius:50%;
background:var(--bg);border:2px solid var(--line-strong)}
.timeline li:first-child .job::before{background:var(--accent);border-color:var(--accent);box-shadow:0 0 0 4px var(--accent-soft)}
.timeline h3{font-size:18px;margin:0;font-weight:650;letter-spacing:-.015em}
.timeline h3 small{font-size:14px;font-weight:400;color:var(--fg-faint)}
.timeline .jrole{font-size:15px;color:var(--fg);margin:2px 0 6px;font-weight:500}
.timeline p{margin:0 0 6px;font-size:15.5px;color:var(--fg-soft);line-height:1.6}
.jproj{display:flex;flex-wrap:wrap;gap:6px;margin-top:8px!important}
.jproj a{font-size:13px;padding:3px 10px;border-radius:999px;background:var(--accent-soft);color:var(--fg)}
@media(max-width:640px){.timeline li{grid-template-columns:1fr;gap:4px;padding-left:24px}
.timeline li::before{left:5px;top:14px}.timeline .when{text-align:left}
.timeline .job{padding-left:0}.timeline .job::before{left:-24px;top:-22px}}
/* ways */
.ways{display:grid;grid-template-columns:repeat(4,1fr);gap:20px}
@media(max-width:980px){.ways{grid-template-columns:repeat(2,1fr)}}@media(max-width:560px){.ways{grid-template-columns:1fr}}
.way{padding:24px;border:1px solid var(--line);border-radius:var(--r);background:var(--card);box-shadow:var(--shadow)}
.way span{display:grid;place-items:center;width:32px;height:32px;border-radius:9px;background:var(--accent-soft);border:1px solid var(--line);
color:var(--fg);font-size:13px;font-weight:700;font-variant-numeric:tabular-nums}
.way h3{font-size:17px;margin:16px 0 6px;font-weight:650;letter-spacing:-.015em}
.way p{margin:0;font-size:15px;color:var(--fg-soft);line-height:1.6}
/* skills */
.caps{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:20px}
.cap{padding:22px 24px;border:1px solid var(--line);border-radius:var(--r);background:var(--card)}
.cap h3{font-size:17px;margin:0 0 4px;font-weight:650;letter-spacing:-.01em}
.cap p{margin:0 0 12px;font-size:15px;color:var(--fg-soft);line-height:1.6}
.cap small{display:block;font-size:13.5px;line-height:1.75;color:var(--fg-faint);padding-top:12px;border-top:1px solid var(--line)}
/* about */
.about{display:grid;grid-template-columns:1.55fr 1fr;gap:56px}
.about p{margin:0 0 16px;color:var(--fg-soft);max-width:64ch}.about p strong{color:var(--fg);font-weight:600}
.edu{background:var(--card);border:1px solid var(--line);border-radius:var(--r);padding:24px 24px 8px;align-self:start;box-shadow:var(--shadow)}
.edu h3{font-size:13px;font-weight:600;letter-spacing:.06em;text-transform:uppercase;color:var(--fg-faint);margin:0 0 18px}
.edu div{margin-bottom:18px}.edu b{display:block;font-size:15.5px;font-weight:600}
.edu span{display:block;font-size:14.5px;color:var(--fg-soft)}
.edu em{display:block;font-size:13px;color:var(--fg-faint);font-style:normal;margin-top:2px}
@media(max-width:760px){.about{grid-template-columns:1fr;gap:28px}}
/* contact */
#contact{border-top:0;padding-bottom:72px}
.contact{border-radius:20px;padding:56px 52px;margin:0 0 8px;color:var(--on-ink);border:1px solid rgba(161,161,170,.12)}
.contact h2{margin-bottom:10px;color:#fff}
.contact .eyebrow{color:#a1a1aa}
.contact p{color:#d4d4d8;max-width:60ch;margin:0 0 26px}
.contact .btn{background:rgba(255,255,255,.04);color:var(--on-ink);border-color:rgba(161,161,170,.28)}
.contact .btn:hover{border-color:rgba(161,161,170,.55);background:rgba(255,255,255,.08);color:#fff}
.contact .btn.primary{background:#fafafa;border-color:#fafafa;color:#09090b}
.contact .btn.primary:hover{background:#e4e4e7;color:#09090b}
@media(max-width:640px){.contact{padding:32px 24px}}
footer{padding:24px 0 30px;font-size:13.5px;color:var(--ink-soft);background:var(--ink)}
footer .wrap{display:flex;flex-wrap:wrap;gap:6px 18px;justify-content:space-between}
/* project page */
.crumb{display:inline-block;font-size:14px;font-weight:500;margin:36px 0 0;color:var(--fg-soft)}
.crumb:hover{color:var(--accent)}
.phead{padding:22px 0 36px}
.phead h1{margin-bottom:12px}
.phead .subtitle{font-size:clamp(19px,2.6vw,22px);line-height:1.45;color:var(--fg);margin:0 0 24px;font-weight:500;letter-spacing:-.015em}
.chips{display:flex;flex-wrap:wrap;gap:6px;margin:0;padding:0;list-style:none}
.chips li{font-size:13px;font-weight:500;color:var(--fg-soft);background:var(--card);border:1px solid var(--line);border-radius:999px;padding:3px 11px}
.pbody{padding-top:0;padding-bottom:0}
section:has(.pbody){padding:64px 0 80px}
.pbody h2{font-size:23px;margin:44px 0 12px;letter-spacing:-.02em}.pbody h2:first-child{margin-top:0}
.problem{font-size:19px;line-height:1.6;color:var(--fg);margin:0}
.pbody p{color:var(--fg-soft);margin:0 0 14px}
.pbody p strong{color:var(--fg);font-weight:600}
.result{margin:0 0 8px;padding:20px 22px;background:var(--accent-soft);border:1px solid var(--line);
border-radius:var(--r);font-size:16px;color:var(--fg)}
.result span,.plain span{display:block;font-size:13px;font-weight:600;color:var(--fg-faint);letter-spacing:.06em;text-transform:uppercase;margin-bottom:6px}
.features{list-style:none;margin:8px 0 4px;padding:0;display:grid;grid-template-columns:1fr;gap:10px}
.features li{position:relative;padding:0 0 0 30px;color:var(--fg);font-size:15.5px;line-height:1.55}
.features li::before{content:"";position:absolute;left:0;top:2px;width:20px;height:20px;border-radius:50%;background:var(--accent-soft) center/12px no-repeat
url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 12 12'%3E%3Cpath d='M2.5 6.2 5 8.5l4.5-5' fill='none' stroke='%2371717a' stroke-width='1.8' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E")}
.plain{margin:0 0 36px;padding:20px 22px;background:var(--bg-alt);border:1px solid var(--line);border-radius:var(--r)}
.plain p{margin:0;font-size:17px;line-height:1.65}
.gloss{display:grid;grid-template-columns:1fr;gap:0;margin:8px 0 0;border:1px solid var(--line);border-radius:var(--r);background:var(--card);overflow:hidden}
.gloss div{padding:14px 18px;border-top:1px solid var(--line)}.gloss div:first-child{border-top:0}
.gloss dt{font-size:15px;font-weight:600;color:var(--fg)}
.gloss dd{margin:3px 0 0;color:var(--fg-soft);font-size:15px;line-height:1.55}
.pnote{margin-top:18px;font-size:14.5px;color:var(--fg-faint)}
.gallery{display:grid;gap:48px}
figure{margin:0}
figure video,figure img{width:100%;border:1px solid var(--line);border-radius:var(--r);display:block;background:var(--bg-alt);box-shadow:var(--shadow)}
figure.narrow img{width:auto;max-width:min(100%,380px)}
figure a{display:block;cursor:zoom-in}
figcaption{margin-top:12px}
figcaption b{display:block;font-size:15.5px;font-weight:600;margin-bottom:2px}
figcaption span{font-size:14.5px;color:var(--fg-soft);line-height:1.55}
.pn{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.pn a{display:block;background:var(--card);border:1px solid var(--line);border-radius:var(--r);padding:18px 20px;color:var(--fg);transition:border-color .15s,box-shadow .15s}
.pn a:hover{border-color:var(--line-strong);box-shadow:var(--shadow-hi);text-decoration:none}
.pn small{display:block;font-size:13px;font-weight:500;color:var(--fg-faint)}
.pn b{font-size:17px;font-weight:650}
.pn .next{text-align:right}
@media(max-width:560px){.pn{grid-template-columns:1fr}.pn .next{text-align:left}}
/* nav call to action */
.nav nav a.cta{background:#fafafa;color:#09090b;margin-left:6px;font-weight:600}
.nav nav a.cta:hover{background:#e4e4e7;color:#09090b}
/* what I do */
.pillars{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
.pillar{display:flex;flex-direction:column;padding:26px 26px 22px;border:1px solid var(--line);border-radius:var(--r);background:var(--card);box-shadow:var(--shadow)}
.pillar .num{font-size:13px;font-weight:600;color:var(--fg-faint);font-variant-numeric:tabular-nums}
.pillar h3{font-size:20px;letter-spacing:-.02em;font-weight:650;margin:10px 0 8px}
.pillar p{margin:0 0 16px;font-size:15px;color:var(--fg-soft);line-height:1.6}
.pillar ul{list-style:none;margin:0 0 18px;padding:0;display:flex;flex-wrap:wrap;gap:6px}
.pillar li{font-size:12.5px;font-weight:500;color:var(--fg-soft);background:var(--accent-soft);border:1px solid var(--line);border-radius:999px;padding:2px 10px}
.pillar .see{margin-top:auto;padding-top:16px;border-top:1px solid var(--line);font-size:14px;color:var(--fg-faint)}
.pillar .see a{color:var(--fg);font-weight:500}
.also{display:grid;grid-template-columns:auto 1fr;gap:6px 20px;margin:28px 0 0;padding:18px 22px;border:1px dashed var(--line-strong);border-radius:var(--r);font-size:14.5px}
.also dt{font-weight:600;color:var(--fg)}.also dd{margin:0;color:var(--fg-soft)}
@media(max-width:900px){.pillars{grid-template-columns:1fr}}
@media(max-width:560px){.also{grid-template-columns:1fr}.also dd{margin-bottom:8px}}
/* selected work: large horizontal cards */
.featured{display:grid;gap:24px;margin:0 0 72px}
.card.feat{display:grid;grid-template-columns:1.25fr 1fr}
.card.feat .thumb{aspect-ratio:auto;min-height:300px;border-bottom:0;border-right:1px solid var(--line)}
.card.feat .cbody{padding:30px 32px}
.card.feat h3{font-size:26px;margin-bottom:8px}
.card.feat p{font-size:16px}
.card.feat .hl{margin-top:16px;padding:12px 14px;border-radius:var(--r-sm);background:var(--accent-soft);border:1px solid var(--line);font-size:14px;color:var(--fg-soft);line-height:1.55}
.card.feat .hl strong{color:var(--fg)}
@media(max-width:860px){.card.feat{grid-template-columns:1fr}.card.feat .thumb{aspect-ratio:16/9;min-height:0;border-right:0;border-bottom:1px solid var(--line)}.card.feat .cbody{padding:22px}}
.sub-head{display:flex;flex-wrap:wrap;align-items:baseline;justify-content:space-between;gap:12px;margin:0 0 18px}
.sub-head h3{font-size:22px;letter-spacing:-.02em;margin:0;font-weight:650}
.cards.compact{grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:18px}
.cards.compact .cbody{padding:16px 18px 18px}
.cards.compact h3{font-size:17px}
.cards.compact p{font-size:14.5px}
.cards.compact .more{display:none}
/* experience: older roles folded */
.earlier{max-width:860px;margin-top:28px}
.earlier summary{cursor:pointer;display:inline-flex;align-items:center;gap:8px;font-weight:500;font-size:15px;color:var(--fg);
padding:8px 16px;border:1px solid var(--line-strong);border-radius:999px;list-style:none;background:var(--card)}
.earlier summary::-webkit-details-marker{display:none}
.earlier summary::after{content:"+";font-weight:600;color:var(--fg-faint)}
.earlier[open] summary::after{content:"\2212"}
.earlier[open] summary{margin-bottom:28px}
/* about: principles beside the story */
.principles{list-style:none;margin:28px 0 0;padding:0;display:grid;grid-template-columns:1fr 1fr;gap:14px}
.principles li{padding:16px 18px;border:1px solid var(--line);border-radius:var(--r);background:var(--card)}
.principles b{display:block;font-size:15.5px;font-weight:600;margin-bottom:4px;color:var(--fg)}
.principles span{display:block;font-size:14.5px;color:var(--fg-soft);line-height:1.55}
@media(max-width:640px){.principles{grid-template-columns:1fr}}
.side{display:grid;gap:20px;align-self:start}
/* notes */
.notes{display:grid;gap:0;border:1px solid var(--line);border-radius:var(--r);background:var(--card);box-shadow:var(--shadow);overflow:hidden;max-width:920px}
.note{display:grid;grid-template-columns:150px 1fr auto;gap:8px 28px;align-items:baseline;padding:24px 28px;color:var(--fg);border-top:1px solid var(--line);transition:background-color .15s}
.note:first-child{border-top:0}
.note:hover{background:var(--accent-soft);text-decoration:none}
.note time{font-size:13.5px;font-weight:500;color:var(--fg-faint);font-variant-numeric:tabular-nums}
.note h3{font-size:19px;margin:0 0 4px;font-weight:650;letter-spacing:-.02em;line-height:1.3}
.note p{margin:0;font-size:15px;color:var(--fg-soft);line-height:1.6}
.note .go{font-size:14px;font-weight:600;color:var(--fg);white-space:nowrap}
.note:hover .go{text-decoration:underline}
.feed{margin:16px 0 0;font-size:14px;color:var(--fg-faint)}
.feed a{color:var(--fg-soft);text-decoration:underline}
@media(max-width:700px){.note{grid-template-columns:1fr;padding:20px}.note .go{display:none}}
.nbody h2{font-size:21px;margin:36px 0 8px}
.nbody p{font-size:17.5px;line-height:1.7;color:var(--fg-soft);margin:0 0 16px}
.nbody p:first-child{color:var(--fg);font-size:19px}
.related{margin-top:40px;padding-top:22px;border-top:1px solid var(--line);font-size:15px;color:var(--fg-faint)}
.related a{color:var(--fg);font-weight:500;text-decoration:underline}
"""

CSS_VER = None  # set from the CSS content before writing

JS_THEME = """(function(){var r=document.documentElement,t=document.getElementById('tt'),s=null;
try{s=localStorage.getItem('theme')}catch(e){}
if(s)r.setAttribute('data-theme',s);
t.addEventListener('click',function(){var c=r.getAttribute('data-theme');
if(!c)c='light';
var n=c==='dark'?'light':'dark';r.setAttribute('data-theme',n);
try{localStorage.setItem('theme',n)}catch(e){}});})();"""

JS_FILTER = """(function(){var f=document.querySelector('.filters');if(!f)return;f.hidden=false;
var bs=f.querySelectorAll('button'),cs=document.querySelectorAll('.cards.compact .card');
bs.forEach(function(b){b.addEventListener('click',function(){var k=b.getAttribute('data-f');
bs.forEach(function(x){x.setAttribute('aria-pressed',x===b?'true':'false')});
cs.forEach(function(c){c.hidden=k!=='all'&&(' '+c.getAttribute('data-cats')+' ').indexOf(' '+k+' ')<0});});});})();"""

def head(title, desc, root, url, og="og-image.png"):
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
<meta property="og:image" content="{BASE}/{og}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{BASE}/{og}">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><rect width='100' height='100' rx='26' fill='%2309090b'/><text x='50' y='66' text-anchor='middle' font-size='44' font-weight='700' font-family='Inter,Arial,sans-serif' fill='%23fafafa'>MK</text></svg>">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap">
<link rel="alternate" type="application/rss+xml" title="Notes by {NAME}" href="{BASE}/feed.xml">
<link rel="stylesheet" href="{root}style.css?v={CSS_VER}">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="nav"><div class="wrap">
  <a class="brand" href="{root}index.html"><i aria-hidden="true">MK</i><span>{NAME}</span></a>
  <nav aria-label="Main">
    <a class="hide-sm" href="{root}index.html#services">Expertise</a>
    <a href="{root}index.html#work">Work</a>
    <a href="{root}index.html#notes">Notes</a>
    <a class="hide-sm" href="{root}index.html#experience">Experience</a>
    <a href="{root}index.html#about">About</a>
    <a class="cta" href="{root}index.html#contact">Contact</a>
  </nav>
  <button id="tt" type="button" aria-label="Switch between light and dark theme">◐</button>
</div></header>
"""

def contact(root):
    return f"""
<section id="contact"><div class="wrap"><div class="contact">
  <p class="eyebrow">Contact</p>
  <h2>Let's talk</h2>
  <p>If your team loses hours to model checks, exports, sorting clashes or copying data out of Revit by hand,
  I'd like to hear about it. I'm also always up for a conversation about AEC software, openBIM and AI in
  construction.</p>
  <div class="links">
    <a class="btn primary" href="mailto:{EMAIL}">Email me</a>
    <a class="btn" href="{LINKEDIN}" rel="noopener">LinkedIn</a>
    <a class="btn" href="{GITHUB}" rel="noopener">GitHub</a>
  </div>
</div></div></section>
<footer><div class="wrap">
  <span>{NAME} · Munich, Germany</span>
  <span>A small static site. No trackers, no cookies.</span>
</div></footer>"""

def thumb_for(p):
    for kind, src, *_ in p['media']:
        if kind in ('img', 'imgn'):
            return f'<img src="{src}" alt="" loading="lazy">'
    return f'<div class="glyph"><b>{p["title"]}</b></div>'

# ---------------------------------------------------------------- index
def build_index():
    feat = [next(p for p in P if p['slug'] == s) for s in FEATURED]
    rest = [p for p in P if p['slug'] not in FEATURED]
    counts = {k: sum(k in p['cats'].split() for p in rest) for k, _ in CATS}
    chips = f'<button type="button" data-f="all" aria-pressed="true">All <small>{len(rest)}</small></button>' + "".join(
        f'<button type="button" data-f="{k}" aria-pressed="false">{label} <small>{counts[k]}</small></button>'
        for k, label in CATS if counts[k])

    def card(p, cls=""):
        hl = f'<div class="hl">{p["result"]}</div>' if cls and p['result'] else ""
        return f"""
      <a class="card{cls}" href="projects/{p['slug']}.html" data-cats="{p['cats']}">
        <div class="thumb">{thumb_for(p)}</div>
        <div class="cbody">
          <span class="tag">{p['tag']}</span>
          <h3>{p['title']}</h3>
          <p>{p['card']}</p>{hl}
          <span class="more">Read the case study →</span>
        </div>
      </a>"""
    featured = "".join(card(p, " feat") for p in feat)
    cards = "".join(card(p) for p in rest)

    def pillar(i, t, plain, ci, cats):
        tools = [x.strip() for c in ci for x in re.split(r"\s·\s", CAPS[c][2])]
        projs = [p for p in P if set(p['cats'].split()) & set(cats)]
        links = " · ".join(f'<a href="projects/{p["slug"]}.html">{p["title"]}</a>' for p in projs)
        return f"""<div class="pillar"><span class="num">0{i}</span><h3>{t}</h3><p>{plain}</p>
      <ul aria-label="Tools">{"".join(f"<li>{x}</li>" for x in tools)}</ul>
      <p class="see">Projects: {links}</p></div>"""
    pillars = "".join(pillar(i, *x) for i, x in enumerate(PILLARS, 1))
    also = "".join(f"<dt>{CAPS[c][0]}</dt><dd>{CAPS[c][2]}</dd>" for c in (4, 3))

    ways = "".join(f'<li><b>{t}</b><span>{b}</span></li>' for t, b in WAYS)
    def job(when, org, place, role, summary):
        return f"""
    <li><span class="when">{when}</span><div class="job">
      <h3>{org} <small>· {place}</small></h3><p class="jrole">{role}</p><p>{summary}</p>
    </div></li>"""
    note_rows = "".join(f"""
    <a class="note" href="notes/{n['slug']}.html"><time datetime="{n['date']}">{nice_date(n['date'])}</time>
      <div><h3>{n['title']}</h3><p>{n['lead']}</p></div><span class="go">Read →</span></a>""" for n in NOTES)
    recent = "".join(job(*j) for j in JOBS[:4])
    older = "".join(job(*j) for j in JOBS[4:])

    return head(f"{NAME} | BIM &amp; AI Solutions Architect",
                "BIM &amp; AI Solutions Architect in Munich: Revit and Navisworks tools, cloud integrations and AI on top of BIM data.",
                "", BASE, "og-image.png?v=" + hashlib.sha1(open(os.path.join(SITE, "og-image.png"), "rb").read()).hexdigest()[:8]) + f"""
<main id="main">
<div class="hero band"><div class="wrap">
<div class="grid">
  <div>
    <p class="hello"><b aria-hidden="true"></b>Now: BIM &amp; AI Solutions Architect at Sweco, Munich</p>
    <h1>{NAME}</h1>
    <p class="role">{ROLE} · Munich</p>
    <p class="lede">{LEDE}</p>
    <p class="sub">For five years I've written the tools that sit between engineers and their models: add-ins,
    background services and cloud integrations that take repetitive coordination work off people's desks.</p>
    <div class="links">
      <a class="btn primary" href="#work">See selected work</a>
      <a class="btn" href="#contact">Get in touch</a>
    </div>
  </div>
  <img class="photo" src="img/headshot.jpg" alt="Portrait of {NAME}" width="200" height="200">
</div>
  <div class="stats">
    <div class="stat"><b>~20</b><span>tools shipped</span></div>
    <div class="stat"><b>5+</b><span>years in AEC</span></div>
    <div class="stat"><b>6</b><span>organisations</span></div>
    <div class="stat"><b>3</b><span>countries</span></div>
  </div>
</div></div>

<section id="services"><div class="wrap">
  <div class="sec-head">
    <p class="eyebrow">What I do</p>
    <h2>Three things I'm good at</h2>
    <p>Most of my work falls into one of these. Each lists the tools I use and the projects that show it.</p>
  </div>
  <div class="pillars">{pillars}</div>
  <dl class="also">{also}</dl>
</div></section>

<section id="work"><div class="wrap">
  <div class="sec-head">
    <p class="eyebrow">Selected work</p>
    <h2>Things I've built</h2>
    <p>Each case study starts with a plain explanation, then the problem, then what the tool actually does.
    Technical words are explained at the bottom.</p>
  </div>
  <div class="featured">{featured}</div>
  <div class="sub-head"><h3>More projects</h3><span class="hint">Most of the code is private. I'm happy to walk you through any of it.</span></div>
  <div class="filters" role="group" aria-label="Filter projects" hidden>{chips}</div>
  <div class="cards compact">{cards}</div>
</div></section>

<section id="notes"><div class="wrap">
  <div class="sec-head">
    <p class="eyebrow">Notes</p>
    <h2>How I think about this work</h2>
    <p>Short write-ups on the rules and checklists behind the tools above, and what I got wrong on the way.</p>
  </div>
  <div class="notes">{note_rows}</div>
  <p class="feed">New notes also go out by <a href="feed.xml">RSS</a>.</p>
</div></section>

<section id="experience"><div class="wrap">
  <div class="sec-head">
    <p class="eyebrow">Experience</p>
    <h2>Where I've worked</h2>
    <p>Six organisations and a freelance practice, from Cairo to Dubai to Munich.</p>
  </div>
  <ol class="timeline">{recent}</ol>
  <details class="earlier"><summary>Earlier roles, 2020 to 2024</summary><ol class="timeline">{older}</ol></details>
</div></section>

<section id="about"><div class="wrap">
  <div class="sec-head">
    <p class="eyebrow">About</p>
    <h2>A bit about me</h2>
  </div>
  <div class="about">
  <div>
    <p>I trained as an architectural engineer, and the drawings were never the part that hooked me. It was
    the logic behind them. The interesting problems in construction turned out to be data problems: project
    information stuck in disconnected tools and manual routines. I build the systems that connect it.</p>
    <p>That has meant Revit and Navisworks plugins, model-health and clash dashboards, and automation that
    runs on its own, in Cairo, Dubai and now Munich. Along the way I took on <strong>18 freelance client projects</strong> next to my day jobs.</p>
    <p>In 2024 I left a good full-time job to do the ITBE master's at TUM, and I don't regret it for a second.
    It added the half I was missing: GIS, spatial data mining, photogrammetry and remote sensing, next to semantic
    modelling and software engineering.</p>
    <h3 class="eyebrow" style="margin-top:32px">How I build</h3>
    <ul class="principles">{ways}</ul>
  </div>
  <div class="side">
  <div class="edu">
    <h3>Education</h3>
    <div><b>Technical University of Munich</b><span>M.Sc. Information Technologies for the Built Environment</span><em>2024 to 2026</em></div>
    <div><b>Information Technology Institute</b><span>Intensive Code Camp: BIM Automation Development</span><em>2022 · Giza</em></div>
    <div><b>Alexandria University</b><span>B.Sc. Architectural Engineering</span><em>2014 to 2020</em></div>
    <div><b>Autodesk</b><span>Certified Professional, Revit Architecture</span><em>2020</em></div>
  </div>
  <div class="edu">
    <h3>Languages</h3>
    <div><b>Arabic</b><span>Native</span></div>
    <div><b>English</b><span>Professional working (IELTS Academic 6.5)</span></div>
    <div><b>German</b><span>Learning (A2)</span></div>
  </div>
  </div>
  </div>
</div></section>
</main>
{contact("")}
<script>{JS_THEME}
{JS_FILTER}</script>
</body></html>"""

# ---------------------------------------------------------------- link preview images
# One 1200 x 630 card per project page, so a shared link (LinkedIn, Teams, Slack) shows the project
# itself. Needs Pillow and the macOS system fonts; without them the shared og-image.png is used.
def build_og(p):
    try:
        from PIL import Image, ImageDraw, ImageFont
        F = "/System/Library/Fonts/"
        bold = lambda n: ImageFont.truetype(F + "Supplemental/Arial Bold.ttf", n)
        sans = lambda n: ImageFont.truetype(F + "SFNS.ttf", n)
        mono = lambda n: ImageFont.truetype(F + "Menlo.ttc", n)
        bold(10)
    except Exception:
        return False
    W, H, CHARCOAL = 1200, 630, (9, 9, 11)
    im = Image.new("RGB", (W, H), CHARCOAL)
    grid = Image.new("RGBA", (W, H), (0, 0, 0, 0)); g = ImageDraw.Draw(grid)
    for r in range(420, 0, -6):  # soft blue glow top right
        g.ellipse([W - 260 - r, -140 - r, W - 260 + r, -140 + r], fill=(255, 255, 255, max(0, int(2 * (1 - r / 420) ** 1.5 * 10))))
    im.paste(grid, (0, 0), grid)
    d = ImageDraw.Draw(im)
    shot = next((src for kind, src, *_ in p['media'] if kind in ('img', 'imgn')), None)
    tw = 470 if shot else 1000

    def wrap(text, font, width, lines):
        out, cur = [], ""
        for w in text.split():
            t = (cur + " " + w).strip()
            if d.textlength(t, font=font) <= width: cur = t
            else: out.append(cur); cur = w
        out.append(cur)
        if len(out) > lines:
            out = out[:lines]; out[-1] = out[-1].rstrip(".,:;") + "..."
        return out

    x, y = 64, 64
    d.text((x, y), "MOHAMED K. MAHDY", font=mono(19), fill=(161, 161, 170)); y += 52
    title = html.unescape(p['title'])
    for size in (64, 56, 48):
        tl = wrap(title, bold(size), tw, 3)
        if len(tl) <= 2 or size == 48: break
    for line in tl:
        d.text((x, y), line, font=bold(size), fill="white"); y += int(size * 1.12)
    y += 10
    d.text((x, y), html.unescape(p['tag']).upper(), font=mono(19), fill=(212, 212, 216)); y += 48
    for line in wrap(html.unescape(p['card']), sans(26), tw, 6 if shot else 4):
        d.text((x, y), line, font=sans(26), fill=(228, 228, 231)); y += 37
    d.text((x, H - 64), DOMAIN, font=mono(18), fill=(212, 212, 216))

    if shot:
        bx, by, bw, bh = 576, 56, 568, 518
        src = Image.open(os.path.join(SITE, shot)).convert("RGB")
        scale = max(bw / src.width, bh / src.height)
        src = src.resize((round(src.width * scale), round(src.height * scale)), Image.LANCZOS)
        src = src.crop((0, 0, bw, bh))
        shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        ImageDraw.Draw(shadow).rounded_rectangle([bx + 6, by + 10, bx + bw + 6, by + bh + 10], 16, fill=(0, 0, 0, 70))
        im.paste(shadow, (0, 0), shadow)
        mask = Image.new("L", (bw, bh), 0); ImageDraw.Draw(mask).rounded_rectangle([0, 0, bw - 1, bh - 1], 14, fill=255)
        im.paste(src, (bx, by), mask)
        d.rounded_rectangle([bx, by, bx + bw - 1, by + bh - 1], 14, outline=(255, 255, 255), width=2)
    os.makedirs(os.path.join(SITE, 'og'), exist_ok=True)
    im.save(os.path.join(SITE, 'og', p['slug'] + '.png'), optimize=True)
    return True

# ---------------------------------------------------------------- project page
def build_project(i, p):
    gal = ""
    if p['media']:
        items = ""
        for kind, src, cap, *rest in p['media']:
            note = rest[0] if rest else ""
            if kind == 'video':
                el, cls = f'<video src="../{src}" controls muted playsinline preload="metadata"></video>', ''
            else:
                el = f'<a href="../{src}" target="_blank" rel="noopener"><img src="../{src}" alt="{cap}" loading="lazy"></a>'
                cls = ' class="narrow"' if kind == 'imgn' else ''
            items += f'<figure{cls}>{el}<figcaption><b>{cap}</b>{f"<span>{note}</span>" if note else ""}</figcaption></figure>'
        gal = f"""<section><div class="wrap">
  <div class="sec-head"><p class="eyebrow">See it</p><h2>Screenshots &amp; demos</h2></div>
  <div class="gallery">{items}</div>
</div></section>"""

    body = "".join(f"<p>{b}</p>" for b in p['body'])
    plain = f'<div class="plain"><span>In plain words</span><p>{p["plain"]}</p></div>' if p.get('plain') else ""
    text = " ".join([p['title'], p['card'], p.get('plain', ''), p['problem'], p['result']] + p['body'] + p.get('features', []))
    text = re.sub(r"<[^>]+>", " ", text)
    # Everyday words (add-in, family, sheet...) match in any case; acronyms and names only as written.
    terms = [(t, d) for t, rx, d in GLOSSARY if re.search(rx, text, 0 if t.isupper() or " " in t or t in ("Revit", "Navisworks", "Speckle") else re.I)]
    gloss = ('<h2>Terms on this page</h2><dl class="gloss">' + "".join(f"<div><dt>{t}</dt><dd>{d}</dd></div>" for t, d in terms) + '</dl>') if terms else ""
    feats = ('<h2>Features</h2><ul class="features">' + "".join(f"<li>{html.escape(f, quote=False)}</li>" for f in p['features']) + '</ul>') if p.get('features') else ""
    res = f'<div class="result"><span>Result</span>{p["result"]}</div>' if p['result'] else ""
    pnote = f'<p class="pnote">{p["note"]}</p>' if p.get('note') else ""
    chips = "".join(f"<li>{s}</li>" for s in p['stack'])
    prev, nxt = P[i - 1], P[(i + 1) % len(P)]

    # og:url is the address without ".html", the form Cloudflare Pages serves.
    og_file = os.path.join(SITE, 'og', p['slug'] + '.png')
    # The version is the image's content hash, so link previews refresh whenever the image changes.
    og = (f"og/{p['slug']}.png?v={hashlib.sha1(open(og_file, 'rb').read()).hexdigest()[:8]}"
          if os.path.exists(og_file) else "og-image.png")
    return head(f"{p['title']} | {NAME}", html.unescape(p['card']), "../",
                f"{BASE}/projects/{p['slug']}", og) + f"""
<main id="main">
<div class="band"><div class="wrap read">
  <a class="crumb" href="../index.html#work">← All work</a>
  <div class="phead">
    <span class="tag">{p['tag']}</span>
    <h1>{p['title']}</h1>
    <p class="subtitle">{p['head']}</p>
    <ul class="chips" aria-label="Built with">{chips}</ul>
  </div>
</div></div>
<section><div class="wrap read pbody">
  {plain}
  {res}
  <h2>The problem</h2>
  <p class="problem">{p['problem']}</p>
  <h2>What it does</h2>
  {body}
  {feats}
  {gloss}
  {pnote}
</div></section>
{gal}
<section><div class="wrap"><div class="pn">
  <a href="{prev['slug']}.html"><small>← Previous project</small><b>{prev['title']}</b></a>
  <a class="next" href="{nxt['slug']}.html"><small>Next project →</small><b>{nxt['title']}</b></a>
</div></div></section>
</main>
{contact("../")}
<script>{JS_THEME}</script>
</body></html>"""

# ---------------------------------------------------------------- note page
def build_note(n):
    parts = []
    for b in n['body']:
        parts.append(f"<h2>{b[3:]}</h2>" if b.startswith("## ") else f"<p>{b}</p>")
    rel = [p for p in P if p['slug'] in n.get('related', [])]
    related = ('<p class="related">The tools this comes from: ' + " · ".join(
        f'<a href="../projects/{p["slug"]}.html">{p["title"]}</a>' for p in rel) + '</p>') if rel else ""
    # Each note gets its own link-preview card (og/note-<slug>.png), built like the project cards.
    og_file = os.path.join(SITE, 'og', 'note-' + n['slug'] + '.png')
    og = (f"og/note-{n['slug']}.png?v={hashlib.sha1(open(og_file, 'rb').read()).hexdigest()[:8]}"
          if os.path.exists(og_file) else "og-image.png")
    return head(f"{n['title']} | {NAME}", html.escape(n['lead'], quote=True), "../", f"{BASE}/notes/{n['slug']}", og) + f"""
<main id="main">
<div class="band"><div class="wrap read">
  <a class="crumb" href="../index.html#notes">← All notes</a>
  <div class="phead">
    <span class="tag">Note · <time datetime="{n['date']}">{nice_date(n['date'])}</time></span>
    <h1 style="font-size:clamp(30px,4.6vw,44px);line-height:1.12">{n['title']}</h1>
    <p class="subtitle">{n['lead']}</p>
  </div>
</div></div>
<section><div class="wrap read pbody nbody">
  {"".join(parts)}
  {related}
</div></section>
</main>
{contact("../")}
<script>{JS_THEME}</script>
</body></html>"""

def build_feed():
    from email.utils import format_datetime
    from datetime import datetime, timezone
    items = "".join(f"""
  <item><title>{html.escape(n['title'])}</title><link>{BASE}/notes/{n['slug']}</link>
  <guid>{BASE}/notes/{n['slug']}</guid><pubDate>{format_datetime(datetime.fromisoformat(n['date']).replace(hour=8, tzinfo=timezone.utc))}</pubDate>
  <description>{html.escape(n['lead'])}</description></item>""" for n in NOTES)
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0"><channel>
  <title>Notes by {NAME}</title><link>{BASE}/#notes</link>
  <description>Short write-ups on BIM automation and AI on BIM data.</description><language>en</language>{items}
</channel></rss>
"""

# Old page names point to the current ones, so earlier links keep working.
REDIRECTS = {"genq": "qubecta", "interior-finishes": "rifadex", "batch-tools": "bimnox", "model-health": "bimnox", "revit-batch": "bimnox"}

# ---------------------------------------------------------------- write
os.makedirs(OUT_PROJ, exist_ok=True)
open(os.path.join(SITE, "CNAME"), "w").write(DOMAIN + "\n")
CSS_VER = hashlib.sha1(CSS.encode()).hexdigest()[:8]
open(os.path.join(SITE, 'style.css'), 'w').write(CSS)
open(os.path.join(SITE, 'index.html'), 'w').write(build_index())
og_made = [build_og(p) for p in P]
for n in NOTES:
    build_og(dict(slug='note-' + n['slug'], title=n['title'], tag='Note · ' + nice_date(n['date']), card=n['lead'], media=[]))
for i, p in enumerate(P):
    open(os.path.join(OUT_PROJ, p['slug'] + '.html'), 'w').write(build_project(i, p))
OUT_NOTES = os.path.join(SITE, 'notes'); os.makedirs(OUT_NOTES, exist_ok=True)
for n in NOTES:
    open(os.path.join(OUT_NOTES, n['slug'] + '.html'), 'w').write(build_note(n))
open(os.path.join(SITE, 'feed.xml'), 'w').write(build_feed())
for old, new in REDIRECTS.items():
    open(os.path.join(OUT_PROJ, old + '.html'), 'w').write(
        f'<!doctype html><meta charset="utf-8"><title>Moved</title>'
        f'<meta http-equiv="refresh" content="0; url={new}.html"><link rel="canonical" href="{BASE}/projects/{new}">'
        f'<p>This page moved to <a href="{new}.html">{new}.html</a>.</p>')
# Cloudflare Pages answers these with a real 301 before the HTML stubs above are ever served.
open(os.path.join(SITE, '_redirects'), 'w').write("".join(
    f"/projects/{old} /projects/{new} 301\n/projects/{old}.html /projects/{new} 301\n" for old, new in REDIRECTS.items()))
print(f"built: index.html, style.css, {len(P)} project pages, {len(NOTES)} notes, {sum(og_made)} preview images")
for p in P:
    n = len(p['media'])
    print(f"  projects/{p['slug']}.html  ({n} media)" if n else f"  projects/{p['slug']}.html")
