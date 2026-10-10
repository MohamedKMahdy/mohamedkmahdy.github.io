#!/usr/bin/env python3
"""Static site generator for mohamedkmahdy.github.io.
Run: python3 build.py   (from the site/ directory)"""
import os, html, hashlib

SITE = os.path.dirname(os.path.abspath(__file__))
OUT_PROJ = os.path.join(SITE, 'projects')

NAME  = "Mohamed K. Mahdy"
ROLE  = "AEC Solutions Architect &amp; AI Specialist"
LEDE  = "I build the software layer between engineers and their models, and the AI layer above it."
BASE  = "https://mohamedkmahdy.github.io"
EMAIL = "mohamedkmahdy@outlook.com"
LINKEDIN = "https://www.linkedin.com/in/mohamedkmahdy/"
GITHUB = "https://github.com/MohamedKMahdy"

# Filter chips on the index; each project lists the keys it belongs to in `cats`.
CATS = [("revit","Revit"), ("clash","Navisworks &amp; clashes"), ("cloud","Cloud &amp; web"),
        ("data","Data &amp; dashboards")]

# ---------------------------------------------------------------- projects
P = [
dict(slug="revit-batch", title="Revit Batch", tag="Revit 2023 to 2027 · batch", cats="revit cloud",
  card="Model checks, IFC, NWC, PDF and DWG exports, health and change reports over many Revit models, each model opened once.",
  head="Set up a job once, let it run every week.",
  problem="Model checks and deliverable exports are the jobs everyone agrees matter and nobody has time to run by hand on dozens of models every week.",
  stack=["C#", ".NET Framework 4.8 / .NET 8 / .NET 10", "Revit API", "WPF", "Autodesk Platform Services", "Windows Task Scheduler"],
  body=["A desktop program and a headless Revit worker that run seven tasks across many models in one go, now or on a weekly schedule: Autodesk Model Checker, the IFC export, the NWC export for Navisworks, PDF and DWG sheet exports, a model health report and a change report. The program starts the matching installed Revit in the background, opens each model once, runs every chosen task on it and closes it without saving.",
        "<strong>Four kinds of source:</strong> chosen ACC cloud models, an ACC folder, a local or network folder, or a fixed list of files. Folders are read again at every run, so new models are picked up, and exports and reports can be uploaded back to ACC afterwards.",
        "<strong>Repeat runs cost little.</strong> A model whose source, settings and outputs have not changed since the last verified run is skipped. Results land in one output folder with a history workbook for Excel and Power BI, plus an optional Teams message after each run.",
        "<strong>One codebase, four apps.</strong> Besides the combined tool there are three single-task editions for teams that need only one job: <strong>Bulk Model Checker</strong> (Model Checker reports, a history table for Power BI and a Teams message after each run), <strong>IFC Bulk Export</strong> (presets, space boundaries and user-defined property sets) and <strong>NWC Bulk Export</strong>.",
        "It is the current generation of scheduled checking and export services I first built in 2023: nightly model checks feeding Power BI, and nightly NWC and DWG exports, so nothing depended on someone remembering."],
  result="Every Revit version from 2023 to 2027 from <strong>one codebase</strong>, each model routed to the installed Revit that can open it, with a German and English interface and a per-user install that needs no admin rights.",
  media=[("img","img/revit-batch-jobs.png","A weekly job","Models from ACC, the Revit version each one opens in, and the tasks to run. Shown with made-up data."),
         ("img","img/revit-batch-tasks.png","Seven tasks, one pass","Every task chosen here runs on each model while Revit has it open once."),
         ("img","img/revit-batch-results.png","Results per model and task","Unchanged models are skipped and say why; failures say what to fix."),
         ("img","img/revit-batch-output.png","Output, history and schedule","One output folder synced with SharePoint, a history workbook, a Teams message and the weekly time."),
         ("img","img/bmc-finished.png","The Bulk Model Checker edition","A finished weekly run with reports, history and a Teams message. Made-up data."),
         ("img","img/ifc-bulk-acc.png","The IFC Bulk Export edition","Models from Autodesk Docs, IFC settings, property sets and the results of a run."),
         ("img","img/image9.png","An earlier version: scheduled model checks","Projects and check-sets defined once, then run unattended on a nightly cycle."),
         ("img","img/image7.png","An earlier version: nightly exports","")]),

dict(slug="aps-raumbuch", title="Raumbuch", tag="Revit + web", cats="revit cloud",
  card="Room books straight from the BIM model: a Revit add-in, and an ACC-connected web app that also opens IFC files in the browser.",
  head="One room book, two routes to it.",
  problem="A room book lists every room and everything in it. Teams often assemble it by hand from the model, room by room, and start again when the design changes.",
  stack=["C#", "Revit API", "React", "Vite", "FastAPI", "APS Viewer", "Model Derivative API", "web-ifc", "three.js"],
  body=["<strong>Revit add-in</strong> (Revit 2023 to 2027). Assigns every piece of furniture and equipment to the room it stands in, also across linked models, and writes the room number and name into shared parameters. It then creates one cropped plan per room and exports the room book as Excel, as a PDF with one page per room, and as an offline HTML dashboard. The three steps live in one docked panel, in German and English.",
        "<strong>Web app.</strong> Signs in to Autodesk Construction Cloud, browses hubs, projects and folders across all APS regions, and opens a model in the APS Viewer with a plan panel beside the 3D view. Rooms come from the 3D scene, from the Model Derivative API, or from the 2D plan views when neither has them. Furniture from the main model and every linked model is placed in one coordinate system and matched to rooms by parameter, by position, or by the nearest room within 2 m.",
        "Both export a formatted German <em>Raumbuch</em> to Excel, PDF and a single-file HTML dashboard whose charts double as filters."],
  result="Not locked to one vendor: IFC files open <strong>without any login</strong>, are parsed in the browser with web-ifc and never uploaded. Several IFC files form one federated model.",
  media=[("img","img/raumbuch-dashboard.jpg","The room book dashboard","One offline HTML file with KPI tiles, charts that filter and the room table. Rendered from the real template with sample data."),
         ("imgn","img/raumbuch-panel.png","The Revit add-in panel","Model status, the three steps with their state, the export formats and the settings, in one docked panel.")]),

dict(slug="clash-management", title="SORTIE", tag="Navisworks · clash tools", cats="clash",
  card="Clash zones and statuses for Navisworks: group clashes by the zone they sit in, and carry statuses and comments between tests and files.",
  head="4,000 clashes, 200 actual problems.",
  problem="A clash run can report thousands of clashes when the real coordination problems number a few hundred. Sorting them by area, and keeping their statuses when tests are rerun or files change, takes days.",
  stack=["C#", "Navisworks API 2022 to 2027", "WPF", "xUnit"],
  body=["<strong>SORTIE</strong> (Status Organiser, Renamer and Transferrer for Interference Events) is a Navisworks Manage add-in for 2022 to 2027.",
        "<strong>Zones.</strong> It groups clashes by the zone their clash point lies in, one group per zone, or writes the zone in front of each clash name. Zones are any 3D objects: masses, rooms, generic models or a separate zones model, and the real zone shape is used rather than its bounding box. Where zones overlap, the smallest wins.",
        "<strong>Status transfer.</strong> It exports status, assignment, approval, description and comments of clashes and imports them into the same clashes in this or another Navisworks file, also from a Navisworks XML clash report. Clashes are matched by result GUID first and then by the clashing pair.",
        "<strong>Clean up.</strong> It moves clashes out of their groups again, or takes the zones off their names."],
  result="Every action works on the clash tests you check and is <strong>one undo step</strong>, and a clash with two possible counterparts is left alone rather than guessed.",
  media=[("img","img/sortie-zones.png","Grouping clashes by zone","Zones come from any 3D objects; a clash belongs to the zone its clash point lies in."),
         ("img","img/sortie-logo.png","The SORTIE mark","")]),

dict(slug="rimacos", title="Rimacos", tag="openBIM · clash matrices", cats="clash",
  card="Clash detection matrices written as rules instead of cells, with Navisworks, IfcClash, BCF, IDS, Excel and HTML outputs.",
  head="Rules, not cells.",
  problem="A clash matrix grows with the square of the number of clash groups. Maintaining thousands of cells by hand, and turning them into thousands of separate clash tests, does not scale.",
  stack=["Python", "IfcOpenShell / IfcClash", "IDS 1.0", "BCF", "Navisworks XML", "openpyxl", "pytest"],
  body=["<strong>Rimacos</strong> (Rule-based Interference Matrices And Clash tests on Open Standards) turns a short list of rules into a complete clash detection matrix and the files to run it: Navisworks search sets and Clash Detective tests, IfcClash sets with BCF output, a buildingSMART IDS file that checks the models carry what the clash groups select on, and an Excel matrix and HTML report for the BIM execution plan.",
        "A rule says how two references are tested against each other (everything, a discipline, a tag or a single group), and the most specific rule wins. A local browser editor handles the matrix, groups and rules.",
        "Clash groups select by IFC class and predefined type, property filters and classification codes, and models are found by their ISO 19650 container name, so the whole matrix also runs on open tooling."],
  result="A classic 133-group matrix carried <strong>8,778 cells</strong>. Rimacos reproduces every one of them with <strong>4 rules</strong>, and the merged output needs <strong>79 clash tests</strong> instead of 8,778.",
  media=[("img","img/rimacos-editor.jpg","The matrix editor","Discipline matrix, the rule behind each cell, and the group pairs it decides.")]),

dict(slug="speckle-llm", title="ARVENT", tag="Speckle · local LLM", cats="ai cloud",
  card="A BIM assistant in Speckle comment threads, on a local Llama: answers about elements, the whole model and the specification.",
  head="I put an LLM on BIM data before it was a category.",
  problem="Most people on a project never open the model, but they still have questions about it: what this panel's U-value is, how many doors lack a fire rating, whether the latest version still meets the spec.",
  stack=["Python", "FastAPI", "Speckle (GraphQL, webhooks, specklepy)", "Ollama", "Llama 3.1", "SQLite"],
  body=["In 2023 I connected Speckle to a large language model so project teams could ask questions about a 3D model in plain language. <strong>ARVENT</strong> (Assistant for Requirements, Verification and Element Notes in Threads) is the 2026 rebuild. It runs on a <strong>local Llama through Ollama</strong>, so model data and project documents never leave the machine.",
        "It works inside Speckle comment threads. It answers questions about a selected element from its parameters and any attached specification PDF, with page citations. It answers questions about the whole model. And it checks every new model version against rules drawn from the specification, opening one thread per failing rule that isolates the offending elements in the viewer and replying when a later version fixes them.",
        "<strong>The language model never computes and never writes SQL.</strong> It fills a JSON query plan constrained to the index's real field names; code validates and repairs the plan and runs it as parameterised SQL, and every reply shows the exact query and result. Rules from the specification are proposed by the model and only run once a person approves them.",
        "Along the way I also built a custom Speckle-Revit connector for a separate client, extending open interoperability between the two platforms."],
  result="The lesson from 2023 still holds: <strong>the model was never the hard part.</strong> The hard part is getting clean, queryable, structured data out of the authoring tools.",
  media=[("img","img/arvent-card.png","The ARVENT mark",""), ("img","img/arvent-logo.png","The mark on light and dark backgrounds","On white, on the dark header band and as an icon.")]),

dict(slug="qubecta", title="Qubecta", tag="Revit · cost planning", cats="revit",
  card="Priced bills of quantities and elemental cost plans straight from the Revit model, exported to Excel, PDF, CSV or GAEB. Revit 2022 to 2027.",
  head="A priced bill and a cost plan without leaving Revit.",
  problem="Quantity surveyors often re-measure what the model already knows. Qubecta reads the quantities straight from Revit, prices them and turns them into a bill and a cost plan.",
  stack=["C#", "Revit API 2022 to 2027", ".NET Framework 4.8 / .NET 8 / .NET 10", "ClosedXML", "PDFsharp", "GAEB DA XML 3.3", "xUnit"],
  body=["<strong>Qubecta</strong> (QUantities, Bills, Elements, Costs, Tendering and Assembly codes) is an add-in for Revit 2022 to 2027. Tick the element types to price and give each one a unit, a bill section (CSI MasterFormat 2018, RICS NRM2 or your own list), an element for the cost plan (UniFormat, RICS NRM1, DIN 276 or your own list), a rate and a description. <strong>Qubecta suggests all of these</strong> from your earlier projects, Revit keynotes and assembly codes, and each type's name and materials, with the reason for each; you check them before anything changes.",
        "It then measures the model and gives you the bill by trade and the cost plan by element, with cost per m² of gross floor area and additions such as preliminaries, contingency and VAT. Exports go to Excel, PDF and CSV, and to <strong>GAEB DA XML</strong> for German tendering and costing software, validated against the official schemas. Elements are written back into Revit's Assembly Code, so schedules and the IFC export carry them.",
        "Under the hood it measures the model in one pass, filters by phase, design option and level, counts repeated linked models, and matches categories by Revit's built-in ids, so it works in any Revit language. Every third-party library is bundled into one assembly, so Qubecta never clashes with Revit's own copies or other add-ins. Elements are also read from where things are: doors and windows take theirs from the wall or roof they sit in, and walls and floors from their exterior and load-bearing settings."],
  result="Self-tested inside Revit on Autodesk's Snowdon Towers sample: <strong>392 types, 294 suggestions, 136 bill lines</strong>, a cost plan by element, and a GAEB export that validates against the official 3.3 schemas.",
  media=[("img","img/qubecta-tabs.jpg","Set up, bill and cost plan","Three numbered steps in one docked panel, shown with a sample model."),
         ("img","img/qubecta-suggest-export.jpg","Suggestions and export","Each suggestion says why; exports include GAEB X83 and X82."),
         ("imgn","img/qubecta-revit.png","Docked in Revit","DIN 276 suggestions with their checks, from the in-Revit self-test on the Snowdon Towers sample."),
         ("video","video/qubecta-earlier.mp4","An earlier version","Generating a detailed bill of quantities in Excel.")]),

dict(slug="rifadex", title="RIFADEX", tag="Revit · interior finishes", cats="revit",
  card="Room finishes for Revit 2024 to 2027: pick wall, floor, skirting and ceiling finishes per room, then preview, draw and keep them up to date.",
  head="Finish walls, floors, skirting and ceilings that follow the rooms.",
  problem="Modelling interior finishes by hand, room by room, is slow, and every design change leaves finishes that no longer fit the room.",
  stack=["C#", "Revit API 2024 to 2027", ".NET Framework 4.8 / .NET 8 / .NET 10", "WPF", "extensible storage", "no third-party libraries"],
  body=["Lengths are shown and typed in the project's units. Pick a wall, floor, base and ceiling finish for each room, from this model or from a linked architect's model, singly or for many rooms at once. RIFADEX then draws one finish wall per run of room boundary, a floor per room with openings for columns and shafts, skirting that stops at doors, and a ceiling at the room height. Doors and windows of the walls behind are cut through the finish walls.",
        "<strong>Plan, preview, apply.</strong> Every change is shown before anything is drawn, and running it again updates existing finishes in place, keeping their element ids: a new code changes the type, a room that changed shape is redrawn, openings follow moved doors, and a type you changed by hand is kept, so a feature wall survives. The linked model is never touched.",
        "Finish types and materials are managed in a table or round-tripped through Excel, with new rows creating new types and an optional naming convention. One XML settings file holds the company standard, so any template works and nothing has to be added to a project first.",
        "<strong>RIFADEX</strong> (Revit Interior Finishes: Assignment, Drawing and Excel eXchange) is one company-neutral bundle that rebuilds my earlier in-house finishes tools, without any office-specific parameter."],
  result="Tested inside Revit end to end: drawing, redrawing, hand edits, door cuts, a moved and rotated link and an Excel round trip, from <strong>one codebase for Revit 2024 to 2027</strong> with no third-party DLLs.",
  media=[("video","video/finishes-drawer.mp4","An earlier version: drawing finishes","Reads room finishes and draws the wall, floor and wall-base geometry."),
         ("video","video/finishes-manager.mp4","An earlier version: finish types","Finish types exported, edited in Excel and written back to the model."),
         ("video","video/materials-manager.mp4","An earlier version: finish materials","The same round trip for finish materials.")]),

dict(slug="acc-integrations", title="LARBACC", tag="ACC · backups", cats="cloud",
  card="Scheduled local backups of Autodesk Construction Cloud and BIM 360 projects, incremental by hard links.",
  head="Cloud-hosted does not mean backed up.",
  problem="Projects in Autodesk Construction Cloud feel safe because they live in the cloud. A deleted folder or an ended subscription can still take years of work with it.",
  stack=["C#", ".NET 8", "WPF", "Autodesk Platform Services (PKCE)", "Data Management API"],
  body=["<strong>LARBACC</strong> (Local, Automatic, Rotating Backups of Autodesk Construction Cloud) keeps dated local copies of ACC and BIM 360 projects. Pick projects and folders, a destination and a weekly time; LARBACC downloads the latest version of every document and keeps the last few backups. The interface is in German and English.",
        "<strong>Incremental by hard links.</strong> A document unchanged since the previous backup is linked instead of downloaded again, so later runs are fast and five kept backups do not take five times the space. A run only becomes a backup once its manifest is written, so a crash or power cut never leaves a half-finished folder that looks complete.",
        "Sign-in uses PKCE, so no client secret ships with the program. A scheduled backup missed while LARBACC was closed runs at the next start, and a failed one is retried after 15 minutes, 1 hour and 4 hours."],
  result="Open-source roots: LARBACC began as a WPF front end for Stewart Celani's MIT-licensed <a href=\"https://github.com/stewartcelani/autodesk-construction-cloud-backup\" rel=\"noopener\">autodesk-construction-cloud-backup</a>, and keeps that history and credit.",
  media=[("img","img/larbacc-projects.png","Projects and weekly schedule","Shown with made-up data."),
         ("img","img/larbacc-folders.png","Folder selection","Untick a folder to leave it out; new folders follow their parent."),
         ("img","img/larbacc-running.png","A backup running","")]),

dict(slug="family-validation", title="Family Validation", tag="Revit · Content Catalog", cats="revit",
  card="Checks and cleans Revit families before they reach the Autodesk Content Catalog, without the user ever opening Revit.",
  head="Clean families in, clean catalog out.",
  problem="One badly built family, with an embedded CAD import or the wrong category, slows down every project that loads it. Checking hundreds of them by hand does not happen.",
  stack=["C#", "Revit API 2023 to 2027", "WPF", ".NET Framework 4.8 / .NET 8 / .NET 10", "no third-party libraries"],
  body=["A launcher window drives a hidden Revit that opens every family in a folder and checks it: the naming convention (auto-correcting the category prefix when that is unambiguous), embedded CAD imports (removed, while linked CAD is kept), name against category, required parameters, file size limits, and an optional classification code such as DIN 276 or Uniclass.",
        "<strong>Safe by construction.</strong> The original is copied aside before anything else, and a family whose copy fails is skipped, never touched. Cleaned copies go to their own folder, sources are never changed in place, and a dry run writes the full report without changing a file.",
        "A visual rules editor lets non-developers maintain the standard: categories and name patterns are built from blocks instead of regular expressions, and the editor refuses to save a ruleset the run would reject."],
  result="<strong>Zero third-party dependencies:</strong> everything is .NET plus the Revit API, with each worker built for the runtime its Revit version ships.",
  media=[("img","img/family-validation-logo.png","The Family Validation mark","")]),

dict(slug="cloud-revisions", title="Cloud Revisions", tag="Revit add-in", cats="revit data",
  card="Every revision cloud in a model, with its sheet and revision data, exported to Excel or an offline interactive dashboard.",
  head="Where the cloud APIs stop, an add-in starts.",
  problem="Keeping track of which revision clouds sit on which sheets, and under which revision, usually means clicking through the sheets one by one.",
  stack=["C#", "Revit API 2023 to 2027", ".NET Framework 4.8 / .NET 8 / .NET 10", "dependency-free Excel and HTML"],
  body=["Revision clouds are annotation elements. The APS AEC Data Model API does not expose them and the Model Derivative API only inconsistently, so the only complete source is the Revit API itself.",
        "The add-in lists every revision cloud in the active model with its view, the sheet it appears on and the full revision data (sequence, number, date, description, issue status, issued by and to), then exports a formatted Excel workbook or a self-contained HTML dashboard with Power BI style filtering. Everything sits in one docked panel on its own ribbon tab, in German or English.",
        "Version 2.0 has its own name, logo and ribbon tab."],
  result="Neither export needs Excel, a CDN or internet access: both files are written by the add-in itself, so they work behind a <strong>corporate proxy</strong>.",
  media=[("img","img/cloud-revisions-dashboard.jpg","The revision cloud dashboard","Filters by revision, view type, issue status and sheet, with linked charts. Rendered from the real template with sample data."),
         ("img","img/cloud-revisions-logo.png","The Cloud Revisions mark","")]),

dict(slug="revit-automation", title="Revit Automation Suite", tag="4 tools · video", cats="revit",
  card="Production Revit plugins for model management, worksets, element joins and bulk file operations. With demos.",
  head="Small tools for the jobs nobody wants to do by hand.",
  problem="Small, repetitive Revit tasks (worksets, joins, moving types between projects, purging before issue) add up to hours of engineering time every week.",
  stack=["C#", "Revit API", "WPF", "Excel interop"],
  body=["A suite of enterprise Revit add-ins built for architecture and engineering teams, covering model management, worksets, element joins and bulk file operations. Each one replaced a manual process that consumed engineering hours every week.",
        "The quantity and finishes tools from the same years have since grown into products of their own, <a href=\"qubecta.html\">Qubecta</a> and <a href=\"rifadex.html\">RIFADEX</a>, and are shown there. All demos below are recorded against a generic sample model."],
  result="",
  media=[
    ("video","video/revit-transmitter.mp4","Revit-Transmitter","Detaches models with preserve or delete worksets, purges unused elements, and prepares issue-ready files."),
    ("video","video/worksets-manager.mp4","Worksets Manager","Creates standard worksets from Excel or by UNIFORMAT, then assigns every element to the right one."),
    ("video","video/auto-joiner.mp4","Auto Joiner","Joins and unjoins every intersecting element of selected categories in one pass."),
    ("video","video/transfer-types.mp4","Transfer Types","Selects Revit projects from a folder tree and transfers types and families between them in bulk."),
    ("img","img/image54.png","Auto Joiner: interface",""),
  ]),

dict(slug="bim-analytics", title="BIM Analytics", tag="Power BI · 9 dashboards", cats="data",
  card="Model health, clash detection, issues and resourcing: automated reporting pipelines on ACC and BIM 360.",
  head="Making model health visible to people who never open Revit.",
  problem="Model health is invisible to the people who never open Revit, which is most of the people making decisions about a project.",
  stack=["Power BI", "DAX", "SharePoint", "BIM 360 / ACC", "Revizto", "Python"],
  body=["A suite of automated Power BI dashboards and reporting pipelines built for BIM coordination, covering model health, clash detection, open issues, ACC administration, resourcing and team-level assessment.",
        "Each dashboard reads directly from project data and refreshes on a schedule, so coordination status is current without anyone assembling a report. Deployed as project-specific intelligence hubs on SharePoint.",
        "In 2026 I decoded one programme's 52 Power BI files (model health across 376 Revit models, clash trends, issues and account administration) and rebuilt them as <strong>one self-contained HTML page</strong> that opens offline in any browser, without Power BI, and leaves out every personal detail."],
  result="Built and refined across three organisations.",
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

dict(slug="curtain-panels", title="Curtain Panel Suite", tag="Parametric · 4 tools", cats="revit",
  card="Generator → Scheduler → Drawings → Tagger. A facade from parametric definition to annotated documentation.",
  head="Geometry that builds itself.",
  problem="Documenting a complex facade panel by panel, with a schedule, a view and dimensions for every type, is slow and easy to get wrong.",
  stack=["C#", "Revit API", "adaptive families"],
  body=["One tool chain taking a curtain wall facade from parametric definition through to fully annotated documentation.",
        "<strong>Panel Generator</strong> creates and edits curtain panels across the facade. <strong>Panel Scheduler</strong> builds and exports panel schedules. <strong>Panel Drawings</strong> generates a dedicated view for every panel type. <strong>Panel Tagger</strong> tags and dimensions the whole set automatically."],
  result="",
  media=[("img","img/image55.jpeg","Panel Generator",""),
         ("img","img/image56.jpeg","Panel Scheduler",""),
         ("img","img/image57.jpeg","Panel Drawings",""),
         ("img","img/image58.jpeg","Panel Tagger","")]),
]

# Full feature list per project, from each repository's README.
FEATURES = {'revit-batch': ['Seven tasks in one pass: Autodesk Model Checker, IFC export, NWC export for Navisworks, PDF and DWG sheet exports, a model health report and a change report', 'Revit opens each model once for every task of a job and closes it again without saving', 'Four kinds of source: chosen ACC cloud models, an ACC folder, a local or network folder, or a fixed list of .rvt files', 'Folders are read again at every run, so models added later are included', 'Every installed Revit from 2023 to 2027; each model goes to the version that can open it, older models are upgraded in memory only', 'Weekly runs through the Windows Task Scheduler, also while the program is closed', 'ACC both ways: plain .rvt files are downloaded for the run, and IFC, NWC, PDF, DWG files and reports can be uploaded back', 'Skip unchanged: a model whose source, settings and outputs have not changed since the last verified run is left out', 'PDF of every sheet, of a sheet set saved in the model, or of sheets matching a number pattern; one PDF per sheet or per model', 'Model health report per model: warnings, families, CAD, links, views, groups and rooms', "Change report: elements added, deleted and changed since the job's last report", 'A time limit per model; a model that hangs is closed and reported while the others carry on', 'One output folder (a SharePoint library synced with OneDrive works), a history workbook for Excel and Power BI, a Teams message after each run', 'Single-task editions built from the same code: Bulk Model Checker, IFC Bulk Export and NWC Bulk Export', 'German and English interface; per-user install without admin rights'], 'aps-raumbuch': ['Revit add-in for Revit 2023 to 2027, one docked panel with three steps and a highlighted next action, in German and English', 'Assigns every piece of furniture and equipment to the room it stands in, also across linked models, and writes room number and name into shared parameters', 'Creates one cropped floor plan per room, named by room number and name', 'Exports the room book as Excel, as a PDF with a cover and one page per room with its plan and furniture, and as an offline HTML dashboard', 'Settings choose the room parameters in the PDF, the furniture categories and the view template of the room plans', 'Web app: Autodesk sign-in, hubs, projects and folders of all APS regions (US, EMEA, AUS) in one list', 'Web app: APS Viewer with a plan panel; selecting a room tints its furniture and cuts it out with a section box', 'Web app: rooms from the 3D scene, the Model Derivative API or the 2D plan views; furniture from the main model and every linked model in one coordinate system', 'Furniture is matched to rooms by parameter, by position, or by the nearest room within 2 m; leftovers are listed separately', 'Searchable room table with level separators, area totals and furniture grouped by category and type', 'IFC files open in the browser without any login, several files form one federated model, nothing is uploaded', 'Dashboard export: one offline HTML file with KPI tiles, charts that act as filters, a room table with plan images and CSV download'], 'clash-management': ['Group clashes by the zone their clash point lies in, one group per zone, or write the zone in front of each clash name', 'Zones are any 3D objects: masses, rooms, generic models or a separate zones model', 'The real zone shape is used, with the bounding box as a faster option for simple zones', 'Where zones overlap the smallest wins; clashes outside every zone go to a "No zone" group', "Zone name from the object's name or from any property", 'Export status, assignment, approval, description and comments of clashes to a status file', 'Import them into the same clashes in this or another Navisworks file, also from a Navisworks XML clash report', 'Clashes are matched by result GUID first, then by the clashing pair; a clash with two possible counterparts is left alone', 'Clean up: move clashes out of their groups, or take the zones off their names again', 'Every action works on the clash tests you check and is one undo step', 'One add-in for Navisworks Manage 2022 to 2027, with its own ribbon tab, keyboard shortcuts and a per-user install'], 'rimacos': ['Clash rules instead of matrix cells: a rule says how two references are tested, and the most specific rule wins', 'References at four levels: everything, a discipline, a tag or a single clash group', 'Test types hard, hard (conservative), clearance, duplicate and none, each with tolerance and severity', 'Group priorities decide which side is responsible for each clash pair', 'Navisworks output: search sets and Clash Detective tests as XML, ready to import', 'IfcOpenShell output: IfcClash sets that run on IFC models and report as BCF', 'buildingSMART IDS 1.0 file that checks the models carry the classes, classifications and properties the groups filter on', 'Excel matrix for the BIM execution plan, editable and importable again', 'HTML report and CSV test list, optionally with clash counts per test and discipline pair', 'Clash groups select by IFC class and predefined type, property filters, classification codes and Revit categories', 'Models are found by their ISO 19650 container name', 'Local browser editor for the matrix, groups, rules and tests; imports classic matrix workbooks', 'Merged or per-pair test granularity'], 'speckle-llm': ['Answers questions about a selected element from its parameters and any attached specification PDF, with page citations', 'Answers questions about the whole model, such as counts, totals and breakdowns per level', 'Every element of the latest version of each model sits in a local SQLite index', 'The Llama only fills a JSON query plan; code checks and repairs it and runs it as parameterised SQL', 'Each reply shows the exact query and result, plus a link that opens exactly those elements in the Speckle viewer', 'Proposes rules from specification PDFs; a person approves them before they run', 'Checks every new model version and opens one pinned thread per failing rule, isolating the elements in the viewer', 'Replies "Resolved" when a later version fixes the problem', 'Missing values are stated, never invented, and citations are checked against the supplied documents', 'Runs on a local Llama through Ollama, so model data and documents never leave the machine', 'Works with both Speckle data shapes (v2 Revit parameters and v3 properties)', 'Webhook server with signature check and de-duplicated retries; command line for indexing, questions and checks; Docker setup with GPU'], 'qubecta': ['Units, bill sections, cost plan elements, rates and descriptions per element type', 'Code lists: CSI MasterFormat 2018, RICS NRM2 and NRM1, UniFormat II and DIN 276 built in; Uniclass 2015, OmniClass and Revit assembly code files read as they are', "Suggestions from earlier projects, Revit keynotes and assembly codes, and each type's name and materials, each with its reason", 'Elements from where things are: doors and windows from their host, walls and floors from exterior and load-bearing settings', 'Measures count, length, area, volume, perimeter, weight from material density, and one line per material layer', 'Filters by phase, design option and level; counts repeated placements of linked models', 'Bill by trade and cost plan by element, with cost per m² of gross floor area', 'Additions on the running total: preliminaries, overheads and profit, contingency and VAT; waste percentage; items not in the model', 'Exports to Excel, PDF and CSV, and to GAEB DA XML 3.3 (X83 tender, X82 priced estimate) validated against the official schemas', "Writes elements back into Revit's Assembly Code, so schedules and the IFC export carry them", 'Settings and rates are saved in the model; price lists move between projects as Excel files', 'Works in any Revit language; one docked panel for Revit 2022 to 2027'], 'rifadex': ['Choose wall, floor, base (skirting) and ceiling finishes per room, from this model or a linked model', 'Set finishes for many rooms at once, filter by level, search or any room parameter, group rooms by name', 'Draws finish walls against the room boundary, a floor per room with openings, skirting that stops at doors, and a ceiling at the room height', 'Door and window openings are cut through the finish walls from the walls behind, linked or not', 'Plan, preview, apply: every change is shown before anything is drawn', 'Running it again updates existing finishes in place, keeps hand edits, and does not redraw skirting you deleted', "Height and floor offset can be overridden per room; lengths in the project's units", 'Remove drawn finishes per room and surface; a count of what was drawn per room', 'Finish types and materials in a table or round-tripped through Excel; new rows create new types', 'Optional naming convention built from tokens', 'One XML settings file holds the company standard and can live on a server; any template works', 'No shared parameters and no third-party DLLs; Revit 2024 to 2027 from one codebase'], 'acc-integrations': ['Pick ACC and BIM 360 projects, folders and a destination; the latest version of every document is saved under its ACC name', 'One dated folder per project and run, with a report and a manifest of every file and its ACC version', 'Unchanged documents are hard-linked from the previous backup instead of downloaded again', 'Keeps the last backups per project (5 by default); never deletes anything after a run with failures', 'A run only becomes a backup once its manifest is written; failed and cancelled runs are kept and labelled', 'Include or exclude any folder; new folders follow their parent', 'Weekly schedule on any days and time, running from the notification area and optionally with Windows', 'Missed backups are made up at the next start; failed ones are retried after 15 minutes, 1 hour and 4 hours', 'Sign-in with PKCE, no client secret shipped; an optional secret is stored encrypted for the Windows user', 'Parallel downloads (1 to 8), a test run that downloads nothing, daily logs', 'German and English interface'], 'family-validation': ['Checks a whole folder of Revit families without the user opening Revit: a launcher drives a hidden Revit', 'File name against the naming convention, with a safe auto-correction of the category prefix', 'Removes embedded CAD imports, keeps linked CAD, and can scan nested families for CAD', "Checks that each family's category matches its name", 'Required family parameters: present, right binding and storage type, optionally not empty', 'File size warning and error limits', 'Optional classification code check against DIN 276, Uniclass or a custom pattern', 'Originals are copied aside before anything else; cleaned copies go to their own folder; sources are never changed', 'Dry run that writes the full report without changing a file', 'Excel report sorted worst first, plus a log', 'Visual rules editor: name patterns from blocks, refuses rulesets that would fail, keeps backups, imports rulesets from colleagues', 'Revit 2023 to 2027, German and English, no third-party libraries'], 'cloud-revisions': ['Lists every revision cloud in the active model', 'Per cloud: id, view and view type, the sheet it appears on, revision sequence, number, date, description, issue status, issued by and to, comment and mark', 'Filters for revision, clouds on sheets only and issued revisions only', 'Formatted Excel workbook with frozen header and filters', 'Offline HTML dashboard with KPI tiles, filter chips, linked charts and a searchable, sortable table', 'Neither export needs Excel, a CDN or internet access', 'One docked panel on its own ribbon tab, German or English, with an explanation for every option', 'Revit 2023 to 2027, no dependencies'], 'revit-automation': ['Revit-Transmitter: detaches models with worksets kept or discarded, purges unused elements and prepares issue-ready files', 'Worksets Manager: creates standard worksets from Excel or by classification and assigns every element to the right one', 'Auto Joiner: joins and unjoins every intersecting element of selected categories in one pass', 'Transfer Types: transfers types and families between many projects selected from a folder tree'], 'bim-analytics': ['Model health dashboards from Autodesk Model Checker results across every project', 'Clash detection dashboards: trend per report date, discipline-pair matrix and clash tests', 'Issues dashboards from BIM 360 and ACC: causes, companies, status and timelines', 'ACC account administration: staffing load, products, companies, project sizes and model opening times', 'Resourcing and team-level assessment dashboards', 'Project intelligence hubs on SharePoint with scheduled refresh', 'Offline rebuild: 52 Power BI files decoded into one self-contained HTML page with a project picker across every tab, no Power BI needed, personal data left out'], 'curtain-panels': ['Panel Generator: creates and edits curtain panels across the facade', 'Panel Scheduler: builds and exports panel schedules', 'Panel Drawings: generates a dedicated view for every panel type', 'Panel Tagger: tags and dimensions the whole set automatically']}

MEDIA = {'revit-batch': [('img', 'img/revit-batch-jobs.png', 'A weekly job', 'Models, the Revit version each one opens in, and the tasks to run. Made-up data.'), ('img', 'img/revit-batch-07-acc-models.png', 'Choosing models in ACC', ''), ('img', 'img/revit-batch-21b-source-local-folder.png', 'Models from a network folder', ''), ('img', 'img/revit-batch-tasks.png', 'Seven tasks, one pass', ''), ('img', 'img/revit-batch-23h-task-pdf.png', 'PDF export of the sheets', ''), ('img', 'img/revit-batch-23f-task-model-health.png', 'Model health and change reports', ''), ('img', 'img/revit-batch-output.png', 'Output, history and Teams', ''), ('img', 'img/revit-batch-25a-schedule-on.png', 'Weekly schedule', ''), ('img', 'img/revit-batch-results.png', 'Results per model and task', ''), ('img', 'img/revit-batch-26a-results-done.png', 'A finished run', ''), ('img', 'img/bmc-job.png', 'Bulk Model Checker edition', ''), ('img', 'img/bmc-finished.png', 'Bulk Model Checker: a finished weekly run', ''), ('img', 'img/ifc-bulk-acc.png', 'IFC Bulk Export edition', ''), ('img', 'img/nwc-acc-tree.png', 'NWC Bulk Export edition', ''), ('img', 'img/nwc-finished.png', 'NWC Bulk Export: uploads back to ACC', ''), ('img', 'img/image9.png', 'An earlier version: scheduled model checks', ''), ('img', 'img/image7.png', 'An earlier version: nightly exports', '')], 'aps-raumbuch': [('img', 'img/raumbuch-dashboard.jpg', 'The room book dashboard', 'Rendered from the real template with sample data.'), ('imgn', 'img/raumbuch-panel.png', 'The Revit add-in panel', '')], 'clash-management': [('img', 'img/sortie-zones.png', 'Zones', ''), ('img', 'img/sortie-transfer.png', 'Status transfer', ''), ('img', 'img/sortie-report.png', 'A finished transfer', ''), ('img', 'img/sortie-cleanup.png', 'Clean up', ''), ('img', 'img/sortie-logo.png', 'The SORTIE mark', '')], 'rimacos': [('img', 'img/rimacos-editor.jpg', 'The matrix editor', ''), ('img', 'img/rimacos-tests.jpg', 'The clash tests a rule set produces', ''), ('img', 'img/rimacos-report.jpg', 'The HTML report', '')], 'speckle-llm': [('img', 'img/arvent-card.png', 'The ARVENT mark', ''), ('img', 'img/arvent-01-index.png', 'Indexing a model', ''), ('img', 'img/arvent-query.png', 'A model-wide question', ''), ('img', 'img/arvent-03-query-de.png', 'The same question in German', ''), ('img', 'img/arvent-04-extract.png', 'Rules proposed from a specification', ''), ('img', 'img/arvent-check.png', 'Checking approved rules', ''), ('img', 'img/arvent-ask.png', 'A missing value is stated, never invented', '')], 'qubecta': [('img', 'img/qubecta-tabs.jpg', 'Set up, bill and cost plan', 'Shown with a sample model.'), ('img', 'img/qubecta-suggest-export.jpg', 'Suggestions, what is measured, and export', ''), ('imgn', 'img/qubecta-revit.png', 'Docked in Revit', 'DIN 276 suggestions with their checks on the Snowdon Towers sample.'), ('img', 'img/qubecta-pdf.png', 'PDF bill summary', ''), ('img', 'img/qubecta-pdf-division.png', 'PDF bill by division', ''), ('img', 'img/qubecta-excel.png', 'Excel cost plan by element', ''), ('img', 'img/qubecta-excel-division.png', 'Excel bill by division', ''), ('video', 'video/qubecta-earlier.mp4', 'An earlier version', 'Generating a detailed bill of quantities in Excel.')], 'acc-integrations': [('img', 'img/larbacc-projects.png', 'Projects and weekly schedule', 'Made-up data.'), ('img', 'img/larbacc-folders.png', 'Folder selection', ''), ('img', 'img/larbacc-running.png', 'A backup running', ''), ('img', 'img/larbacc-first-run.png', 'First start', ''), ('imgn', 'img/larbacc-settings.png', 'Settings', '')], 'family-validation': [('img', 'img/family-validation-logo.png', 'The Family Validation mark', ''), ('img', 'img/family-validation-start.png', 'The launcher', ''), ('img', 'img/family-validation-launcher.png', 'A finished check', ''), ('img', 'img/family-validation-standards.png', 'The rules editor', ''), ('img', 'img/family-validation-standards-problem.png', 'The rules editor refusing an invalid rule', '')], 'cloud-revisions': [('img', 'img/cloud-revisions-dashboard.jpg', 'The revision cloud dashboard', ''), ('img', 'img/cloud-revisions-workbook.png', 'The Excel workbook', ''), ('imgn', 'img/cloud-revisions-panel.png', 'The docked panel', ''), ('img', 'img/cloud-revisions-logo.png', 'The Cloud Revisions mark', '')]}
for _p in P:
    if _p['slug'] in MEDIA: _p['media'] = MEDIA[_p['slug']]
    if _p['slug'] == 'bim-analytics': _p['media'] = [('img', 'img/bimperf-overview.jpg', 'Offline rebuild: overview', 'Client project names are blurred.'), ('img', 'img/bimperf-model-health-summary.jpg', 'Offline rebuild: model health', ''), ('img', 'img/bimperf-clash-detection.jpg', 'Offline rebuild: clash detection', '')] + _p['media']
    _p['features'] = FEATURES.get(_p['slug'], [])

# Where I've worked: (when, employer, place, role, summary)
JOBS = [
 ("2025 to now", "Sweco", "Munich", "Werkstudent, AI &amp; Automation Specialist (BIM + Data Science)",
  "I own the AI and automation roadmap for the BIM + Data Science department: scoping the automation portfolio, building Revit tools and LLM agents, and taking tools through internal release."),
 ("2024 to 2025", "Obermeyer", "Munich", "BIM Software Developer",
  "Model-checking rules in Desite MD, Power Automate flows for SharePoint data management, and Power BI reporting on model quality."),
 ("2023 to 2024", "Dewan Architects + Engineers", "Dubai, remote", "BIM Software Developer &amp; Data Analyst",
  "BIM software development and data analytics for coordination, model quality and project reporting."),
 ("2022 to 2024", "Freelance (Upwork)", "Remote", "BIM Software Developer &amp; Data Analyst",
  "18 client engagements across 895 billable hours with a 5.0 average rating: Revit automation, Dynamo and Python pipelines."),
 ("2023", "Solid Construction", "Cairo", "BIM Software Developer",
  "Revit add-ins and Dynamo workflows for structural, quantity and finishes work."),
 ("2021 to 2023", "Pinnacle Misr", "Cairo", "BIM Coordinator / Developer",
  "Revit plugins and Dynamo workflows on large projects, including the El Alamein Iconic Tower and Kitoko Ministerial City."),
 ("2020 to 2021", "X-Dimension", "Cairo", "BIM Architect",
  "BIM standards and templates, Dynamo workflows, and Scan-to-BIM."),
]

# How I build: principles drawn from the projects above.
WAYS = [
 ("People stay in control", "Every action is one undo step, a dry run comes before anything changes, and when AI proposes something, a person approves it."),
 ("Boring is a feature", "Tools that run overnight on their own, retry when the network drops, and never leave a half-finished result that looks complete."),
 ("Data stays where it belongs", "Local language models, IFC files read in the browser, and no secrets baked into a program."),
 ("Open where it counts", "IFC, IDS and BCF wherever they fit, so a workflow is not locked to one vendor."),
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

CSS = """
:root{--bg:#F2F2F2;--bg-alt:#E6E6E6;--fg:#111111;--fg-soft:#575656;--fg-faint:#6b6b6b;
--accent:#3C6E28;--accent-2:#538840;--on-accent:#fff;--accent-soft:#E6F2DE;--warm:#3C6E28;--line:#e2e2e2;--card:#fff;
--charcoal:#444444;--on-charcoal:#ffffff;--charcoal-soft:#B2B2B2;--amber:#E0A800;
--shadow:0 1px 2px rgba(0,0,0,.04),0 6px 18px rgba(0,0,0,.05);
--mono:"Cascadia Mono",ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;
--sans:"Segoe UI",-apple-system,BlinkMacSystemFont,Calibri,Arial,sans-serif;--maxw:1060px;--read:760px}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#1e1e1e;--bg-alt:#2a2a2a;--fg:#F2F2F2;
--fg-soft:#cfcfcf;--fg-faint:#B2B2B2;--accent:#A9C99A;--accent-2:#7BA85F;--on-accent:#111;--accent-soft:#2c3a25;--warm:#A9C99A;
--line:#3a3a3a;--card:#2a2a2a;--charcoal:#333333;--shadow:0 1px 2px rgba(0,0,0,.3)}}
:root[data-theme="dark"]{--bg:#1e1e1e;--bg-alt:#2a2a2a;--fg:#F2F2F2;--fg-soft:#cfcfcf;--fg-faint:#B2B2B2;
--accent:#A9C99A;--accent-2:#7BA85F;--on-accent:#111;--accent-soft:#2c3a25;--warm:#A9C99A;--line:#3a3a3a;--card:#2a2a2a;
--charcoal:#333333;--shadow:0 1px 2px rgba(0,0,0,.3)}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%;scroll-behavior:smooth;scroll-padding-top:76px}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}*{transition:none!important}}
body{margin:0;background:var(--bg);color:var(--fg);font-family:var(--sans);font-size:17px;
line-height:1.65;-webkit-font-smoothing:antialiased}
.wrap{max-width:var(--maxw);margin:0 auto;padding:0 24px}
.read{max-width:var(--read)}
a{color:var(--accent);text-decoration:none}a:hover{text-decoration:underline}
:focus-visible{outline:2px solid var(--accent);outline-offset:3px;border-radius:6px}
.skip{position:absolute;left:-999px;top:8px;background:var(--card);padding:8px 12px;border-radius:8px;z-index:30}
.skip:focus{left:12px}
/* nav */
.nav{position:sticky;top:0;z-index:20;background:var(--charcoal);color:var(--on-charcoal)}
.nav .wrap{display:flex;align-items:center;gap:18px;height:60px}
.brand{display:flex;align-items:center;gap:10px;color:#fff;font-weight:640;letter-spacing:-.01em;margin-right:auto}
.brand:hover{text-decoration:none}
.brand i{width:30px;height:30px;border-radius:6px;background:#538840;color:#fff;display:grid;
place-items:center;font:600 15px/1 var(--mono);font-style:normal}
.nav nav{display:flex;gap:4px}
.nav nav a{color:#e6e6e6;font-size:14.5px;padding:6px 10px;border-radius:6px}
.nav nav a:hover{color:#fff;background:rgba(255,255,255,.12);text-decoration:none}
#tt{width:34px;height:34px;border:1px solid rgba(255,255,255,.3);background:transparent;color:#e6e6e6;border-radius:6px;
cursor:pointer;font-size:15px;line-height:1;display:grid;place-items:center;flex:none}
#tt:hover{color:#fff;border-color:#A9C99A}
@media(max-width:640px){.brand span{display:none}.nav .wrap{gap:8px}.nav nav a{padding:6px 7px;font-size:14px}}
/* hero */
.band{background:var(--charcoal);color:#fff}
.band a{color:#A9C99A}
.hero{padding:64px 0 52px}
.hero .hello,.hero .role{color:#A9C99A}
.hero .sub{color:#dcdcdc}
.hero .now{background:rgba(255,255,255,.08);border-color:rgba(255,255,255,.2);color:#e6e6e6}
.hero .btn{background:transparent;color:#fff;border-color:rgba(255,255,255,.45)}
.hero .btn:hover{border-color:#A9C99A;color:#fff}
.hero .btn.primary{background:#538840;border-color:#538840;color:#fff;font-weight:600}
.hero .btn.primary:hover{background:#3C6E28;border-color:#3C6E28;opacity:1}
.hero .stat{background:#fff;color:#111}.hero .stat b{color:#3C6E28}.hero .stat span{color:#575656}
.hero .photo{box-shadow:0 0 0 5px rgba(255,255,255,.15)}
.band .crumb{color:#cfcfcf}.band .crumb:hover{color:#fff}
.band .phead{padding:18px 0 40px}
.band .phead .subtitle{color:#e6e6e6}
.band .tag{background:transparent;border:1px solid #7BA85F;color:#A9C99A}
.band .chips li{background:rgba(255,255,255,.08);border-color:rgba(255,255,255,.2);color:#e6e6e6}
.hero .grid{display:grid;grid-template-columns:1fr auto;gap:48px;align-items:center}
.photo{width:200px;height:200px;border-radius:50%;object-fit:cover;display:block;background:#fff;
box-shadow:0 0 0 6px var(--card),0 0 0 7px var(--line),var(--shadow)}
.hello{font-size:18px;color:var(--warm);margin:0 0 6px;font-weight:560}
h1{font-size:clamp(34px,5.6vw,52px);line-height:1.08;margin:0 0 10px;letter-spacing:-.025em;font-weight:680}
.role{font-family:var(--mono);font-size:clamp(12px,2vw,14px);color:var(--accent);letter-spacing:.04em;margin:0 0 24px}
.lede{font-size:clamp(19px,2.6vw,23px);line-height:1.45;max-width:30ch;margin:0 0 16px;font-weight:520;letter-spacing:-.01em}
.sub{color:var(--fg-soft);max-width:62ch;margin:0 0 22px}
.now{display:inline-flex;align-items:center;gap:9px;font-size:14px;color:var(--fg-soft);background:var(--card);
border:1px solid var(--line);border-radius:999px;padding:6px 14px 6px 12px;margin:0 0 26px}
.now b{width:8px;height:8px;border-radius:50%;background:#538840;box-shadow:0 0 0 3px rgba(83,136,64,.2)}
.links{display:flex;flex-wrap:wrap;gap:10px}
.btn{display:inline-block;padding:10px 16px;border:1px solid var(--line);border-radius:10px;font-size:15px;
color:var(--fg);background:var(--card);transition:.15s;font-weight:520}
.btn:hover{border-color:var(--accent);color:var(--accent);text-decoration:none}
.btn.primary{background:var(--accent);border-color:var(--accent);color:var(--on-accent)}
.btn.primary:hover{opacity:.9;color:var(--on-accent)}
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:14px;margin:48px 0 0}
.stat{background:var(--card);border:1px solid var(--line);border-left:4px solid var(--accent-2);border-radius:8px;padding:16px 18px 14px}
.stat b{display:block;font-size:28px;font-weight:700;letter-spacing:-.02em;line-height:1.15;color:var(--accent)}
.stat span{font-size:14px;color:var(--fg-soft)}
@media(max-width:760px){.hero{padding:44px 0 40px}.hero .grid{grid-template-columns:1fr;gap:26px}
.photo{width:120px;height:120px;order:-1}}
/* sections */
section{padding:72px 0;border-top:1px solid var(--line)}
.sec-head{margin:0 0 34px;max-width:var(--read)}
.eyebrow{font-size:12px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--accent-2);margin:0 0 8px}
h2{font-size:clamp(26px,3.6vw,34px);line-height:1.2;letter-spacing:-.01em;margin:0 0 12px;font-weight:700;color:var(--accent)}
.sec-head p{color:var(--fg-soft);margin:0 0 10px}
.hint{font-size:14.5px;color:var(--fg-faint)}
/* filters + cards */
.filters{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 26px}
.filters button{font:inherit;font-size:14.5px;padding:6px 14px;border-radius:999px;border:1px solid var(--accent-2);
background:var(--card);color:var(--fg-soft);cursor:pointer}
.filters button:hover{border-color:var(--accent);color:var(--accent)}
.filters button[aria-pressed="true"]{background:var(--accent);border-color:var(--accent);color:var(--on-accent)}
.filters button small{opacity:.7;margin-left:4px;font-size:12.5px}
.cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:20px}
.card{display:flex;flex-direction:column;border:1px solid var(--line);border-radius:10px;overflow:hidden;background:var(--card);
color:var(--fg);transition:.18s;box-shadow:var(--shadow)}
.card[hidden]{display:none}
.card:hover{border-color:var(--accent);transform:translateY(-3px);text-decoration:none}
.card .thumb{aspect-ratio:16/9;background:var(--bg-alt);overflow:hidden;border-bottom:1px solid var(--line)}
.card .thumb img{width:100%;height:100%;object-fit:cover;object-position:top;display:block;transition:.3s}
.card:hover .thumb img{transform:scale(1.03)}
.glyph{width:100%;height:100%;display:flex;flex-direction:column;justify-content:flex-end;padding:18px 20px;
background:linear-gradient(var(--line) 1px,transparent 1px) 0 0/28px 28px,linear-gradient(90deg,var(--line) 1px,transparent 1px) 0 0/28px 28px,var(--accent-soft)}
.glyph b{font-size:24px;line-height:1.15;letter-spacing:-.02em;color:var(--accent);font-weight:680}
.glyph small{font-family:var(--mono);font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:var(--fg-soft);margin-top:4px}
.card .cbody{padding:18px 20px 20px;display:flex;flex-direction:column;flex:1}
.card h3{font-size:19px;margin:0 0 6px;letter-spacing:-.015em;font-weight:650}
.tag{font-family:var(--sans);font-weight:600;font-size:11px;letter-spacing:.06em;text-transform:uppercase;
color:var(--accent);background:var(--accent-soft);padding:3px 8px;border-radius:6px;display:inline-block;margin-bottom:10px;align-self:flex-start}
.card p{margin:0;font-size:15px;color:var(--fg-soft);line-height:1.55}
.more{font-size:14px;font-weight:560;color:var(--accent);margin-top:auto;padding-top:14px}
.card:hover .more{text-decoration:underline}
/* timeline */
.timeline{list-style:none;margin:0;padding:0;max-width:820px}
.timeline li{display:grid;grid-template-columns:130px 1fr;gap:24px;position:relative;padding:0 0 30px}
.timeline li:last-child{padding-bottom:0}
.timeline li::before{content:"";position:absolute;left:150px;top:8px;bottom:-8px;width:1px;background:var(--line)}
.timeline li:last-child::before{display:none}
.timeline .when{font-family:var(--mono);font-size:13px;color:var(--fg-faint);padding-top:3px;text-align:right}
.timeline .job{position:relative;padding-left:20px}
.timeline .job::before{content:"";position:absolute;left:-10px;top:8px;width:11px;height:11px;border-radius:50%;
background:var(--bg);border:2px solid var(--accent)}
.timeline li:first-child .job::before{background:var(--accent)}
.timeline h3{font-size:18px;margin:0;font-weight:650;letter-spacing:-.01em}
.timeline h3 small{font-size:14px;font-weight:450;color:var(--fg-faint)}
.timeline .jrole{font-size:14.5px;color:var(--accent);margin:2px 0 6px}
.timeline p{margin:0 0 6px;font-size:15.5px;color:var(--fg-soft);line-height:1.55}
.jproj{display:flex;flex-wrap:wrap;gap:6px;margin-top:8px!important}
.jproj a{font-size:13px;padding:3px 10px;border-radius:999px;background:var(--accent-soft);color:var(--accent)}
.jproj a:hover{text-decoration:none;filter:brightness(.97)}
@media(max-width:640px){.timeline li{grid-template-columns:1fr;gap:4px;padding-left:22px}
.timeline li::before{left:5px;top:10px}.timeline .when{text-align:left}
.timeline .job{padding-left:0}.timeline .job::before{left:-22px;top:-20px}}
/* ways */
.ways{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:16px}
.way{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:20px}
.way span{font-family:var(--mono);font-size:12px;color:var(--warm)}
.way h3{font-size:17px;margin:6px 0 6px;font-weight:650;letter-spacing:-.01em}
.way p{margin:0;font-size:15px;color:var(--fg-soft);line-height:1.55}
/* skills */
.caps{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:28px 32px}
.cap h3{font-size:17px;margin:0 0 4px;font-weight:650}
.cap p{margin:0 0 8px;font-size:15px;color:var(--fg-soft);line-height:1.55}
.cap small{display:block;font-size:13px;color:var(--fg-faint);line-height:1.7}
/* about */
.about{display:grid;grid-template-columns:1.55fr 1fr;gap:48px}
.about p{margin:0 0 15px;color:var(--fg-soft);max-width:64ch}.about p strong{color:var(--fg)}
.edu{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:22px 22px 6px;align-self:start}
.edu h3{font-size:13px;font-family:var(--mono);letter-spacing:.12em;text-transform:uppercase;color:var(--fg-faint);margin:0 0 16px;font-weight:500}
.edu div{margin-bottom:18px}.edu b{display:block;font-size:15px;font-weight:620}
.edu span{display:block;font-size:14px;color:var(--fg-soft)}
.edu em{display:block;font-size:13px;color:var(--fg-faint);font-style:normal;margin-top:2px}
@media(max-width:760px){.about{grid-template-columns:1fr;gap:28px}}
/* contact */
.contact{background:var(--accent-soft);border-radius:20px;padding:40px 36px;margin:0 0 8px}
.contact h2{margin-bottom:10px}
.contact p{color:var(--fg-soft);max-width:60ch;margin:0 0 22px}
@media(max-width:640px){.contact{padding:28px 22px}}
footer{padding:24px 0 30px;font-size:13.5px;color:#cfcfcf;background:var(--charcoal)}
footer .wrap{display:flex;flex-wrap:wrap;gap:6px 18px;justify-content:space-between}
/* project page */
.crumb{display:inline-block;font-size:14.5px;margin:30px 0 0;color:var(--fg-soft)}
.crumb:hover{color:var(--accent)}
.phead{padding:22px 0 36px}
.phead h1{margin-bottom:12px}
.phead .subtitle{font-size:clamp(19px,2.6vw,23px);line-height:1.45;color:var(--fg);margin:0 0 22px;font-weight:520;letter-spacing:-.01em}
.chips{display:flex;flex-wrap:wrap;gap:6px;margin:0;padding:0;list-style:none}
.chips li{font-size:13px;color:var(--fg-soft);background:var(--card);border:1px solid var(--line);border-radius:999px;padding:3px 11px}
.pbody{padding:40px 0 48px}
.pbody h2{font-size:22px;margin:34px 0 10px}.pbody h2:first-child{margin-top:0}
.problem{font-size:19px;line-height:1.6;color:var(--fg);margin:0}
.pbody p{color:var(--fg-soft);margin:0 0 14px}
.pbody p strong{color:var(--fg);font-weight:620}
.result{margin-top:28px;padding:18px 20px;background:var(--accent-soft);border:1px solid var(--line);border-left:4px solid var(--accent-2);
border-radius:12px;font-size:16px;color:var(--fg)}
.result span{display:block;font-family:var(--mono);font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:var(--warm);margin-bottom:6px}
.features{list-style:none;margin:6px 0 4px;padding:0;display:grid;grid-template-columns:1fr;gap:9px}
.features li{position:relative;padding:10px 14px 10px 40px;background:var(--card);border:1px solid var(--line);border-radius:8px;
color:var(--fg);font-size:15.5px;line-height:1.5}
.features li::before{content:"";position:absolute;left:14px;top:14px;width:14px;height:14px;border-radius:50%;background:var(--accent-2);
}
.features li::after{content:"";position:absolute;left:18.5px;top:17px;width:4px;height:7px;border:solid #fff;border-width:0 2px 2px 0;transform:rotate(45deg)}
.pnote{margin-top:18px;font-size:14.5px;color:var(--fg-faint)}
.gallery{display:grid;gap:40px}
figure{margin:0}
figure video,figure img{width:100%;border:1px solid var(--line);border-radius:12px;display:block;background:var(--bg-alt)}
figure.narrow img{width:auto;max-width:min(100%,380px)}
figure a{display:block;cursor:zoom-in}
figcaption{margin-top:10px}
figcaption b{display:block;font-size:15.5px;font-weight:640;margin-bottom:2px}
figcaption span{font-size:14.5px;color:var(--fg-soft);line-height:1.55}
.pn{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.pn a{display:block;background:var(--card);border:1px solid var(--line);border-radius:14px;padding:16px 18px;color:var(--fg)}
.pn a:hover{border-color:var(--accent);text-decoration:none}
.pn small{display:block;font-size:13px;color:var(--fg-faint)}
.pn b{font-size:17px;font-weight:640}
.pn .next{text-align:right}
@media(max-width:560px){.pn{grid-template-columns:1fr}.pn .next{text-align:left}}
"""

CSS_VER = None  # set from the CSS content before writing

JS_THEME = """(function(){var r=document.documentElement,t=document.getElementById('tt'),s=null;
try{s=localStorage.getItem('theme')}catch(e){}
if(s)r.setAttribute('data-theme',s);
t.addEventListener('click',function(){var c=r.getAttribute('data-theme');
if(!c)c=window.matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light';
var n=c==='dark'?'light':'dark';r.setAttribute('data-theme',n);
try{localStorage.setItem('theme',n)}catch(e){}});})();"""

JS_FILTER = """(function(){var f=document.querySelector('.filters');if(!f)return;f.hidden=false;
var bs=f.querySelectorAll('button'),cs=document.querySelectorAll('.card');
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
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><rect width='100' height='100' rx='18' fill='%233C6E28'/><text y='.9em' x='50' text-anchor='middle' font-size='62' font-family='monospace' fill='white'>M</text></svg>">
<link rel="stylesheet" href="{root}style.css?v={CSS_VER}">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="nav"><div class="wrap">
  <a class="brand" href="{root}index.html"><i>M</i><span>{NAME}</span></a>
  <nav aria-label="Main">
    <a href="{root}index.html#work">Work</a>
    <a href="{root}index.html#experience">Experience</a>
    <a href="{root}index.html#about">About</a>
    <a href="{root}index.html#contact">Contact</a>
  </nav>
  <button id="tt" type="button" aria-label="Switch between light and dark theme">◐</button>
</div></header>
"""

def contact(root):
    return f"""
<section id="contact"><div class="wrap"><div class="contact">
  <p class="eyebrow">Contact</p>
  <h2>Let's talk</h2>
  <p>If your team loses hours to model checks, exports, clash triage or data copied out of Revit by hand,
  I would like to hear about it. I am also always up for a conversation about AEC software, openBIM
  tooling and AI in the built environment.</p>
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
    counts = {k: sum(k in p['cats'].split() for p in P) for k, _ in CATS}
    chips = f'<button type="button" data-f="all" aria-pressed="true">All <small>{len(P)}</small></button>' + "".join(
        f'<button type="button" data-f="{k}" aria-pressed="false">{label} <small>{counts[k]}</small></button>'
        for k, label in CATS)

    cards = "".join(f"""
      <a class="card" href="projects/{p['slug']}.html" data-cats="{p['cats']}">
        <div class="thumb">{thumb_for(p)}</div>
        <div class="cbody">
          <span class="tag">{p['tag']}</span>
          <h3>{p['title']}</h3>
          <p>{p['card']}</p>
          <span class="more">Read the story →</span>
        </div>
      </a>""" for p in P)

    ways = "".join(f'<div class="way"><span>0{i}</span><h3>{t}</h3><p>{b}</p></div>'
                   for i, (t, b) in enumerate(WAYS, 1))
    caps = "".join(f'<div class="cap"><h3>{t}</h3><p>{plain}</p><small>{tools}</small></div>'
                   for t, plain, tools in CAPS)
    jobs = "".join(f"""
    <li><span class="when">{when}</span><div class="job">
      <h3>{org} <small>· {place}</small></h3><p class="jrole">{role}</p><p>{summary}</p>
    </div></li>""" for when, org, place, role, summary in JOBS)

    return head(f"{NAME} | AEC Solutions Architect &amp; AI Specialist",
                "Revit &amp; Navisworks tooling, Autodesk Platform Services, and AI over BIM data. Munich.",
                "", BASE, "og-image.png?v=" + hashlib.sha1(open(os.path.join(SITE, "og-image.png"), "rb").read()).hexdigest()[:8]) + f"""
<main id="main">
<div class="hero band"><div class="wrap"><div class="grid">
  <div>
    <p class="hello">Hi, I'm</p>
    <h1>{NAME}</h1>
    <p class="role">{ROLE} · Munich</p>
    <p class="lede">{LEDE}</p>
    <p class="sub">For five years I have been building tools for architects and engineers: Revit and
    Navisworks add-ins, scheduled services and cloud integrations that take repetitive coordination work off
    people's desks and run overnight on their own.</p>
    <p class="now"><b aria-hidden="true"></b>Now: AI &amp; automation for BIM&nbsp;+&nbsp;Data Science at Sweco, and an M.Sc. at TUM</p>
    <div class="links">
      <a class="btn primary" href="#work">See my work</a>
      <a class="btn" href="mailto:{EMAIL}">Get in touch</a>
      <a class="btn" href="{LINKEDIN}" rel="noopener">LinkedIn</a>
    </div>
  </div>
  <img class="photo" src="img/headshot.jpg" alt="Portrait of {NAME}" width="200" height="200">
</div>
  <div class="stats">
    <div class="stat"><b>~20</b><span>tools shipped</span></div>
    <div class="stat"><b>5+</b><span>years in AEC</span></div>
    <div class="stat"><b>6</b><span>organisations</span></div>
    <div class="stat"><b>895</b><span>consulting hours</span></div>
  </div>
</div></div>

<section id="work"><div class="wrap">
  <div class="sec-head">
    <p class="eyebrow">Work</p>
    <h2>Things I've built</h2>
    <p>Tools for architects, engineers and BIM coordinators, from small Revit add-ins to services that run
    unattended every night. Each project page starts with the problem it solves.</p>
    <p class="hint">Most of the code lives in private repositories. I am happy to walk you through any of it.</p>
  </div>
  <div class="filters" role="group" aria-label="Filter projects" hidden>{chips}</div>
  <div class="cards">{cards}</div>
</div></section>

<section id="experience"><div class="wrap">
  <div class="sec-head">
    <p class="eyebrow">Experience</p>
    <h2>Where I've worked</h2>
    <p>Six organisations and a freelance practice, from Cairo to Dubai to Munich.</p>
  </div>
  <ol class="timeline">{jobs}</ol>
</div></section>

<section id="how"><div class="wrap">
  <div class="sec-head">
    <p class="eyebrow">How I build</p>
    <h2>A few things I care about</h2>
    <p>The same handful of rules shows up in almost everything above.</p>
  </div>
  <div class="ways">{ways}</div>
</div></section>

<section id="skills"><div class="wrap">
  <div class="sec-head">
    <p class="eyebrow">Skills</p>
    <h2>What I work with</h2>
  </div>
  <div class="caps">{caps}</div>
</div></section>

<section id="about"><div class="wrap">
  <div class="sec-head">
    <p class="eyebrow">About</p>
    <h2>A bit about me</h2>
  </div>
  <div class="about">
  <div>
    <p>I trained as an architectural engineer and moved into software because the interesting problems in
    construction are data problems. Most firms are sitting on valuable project data trapped in disconnected
    tools and manual workflows. I build the systems that connect it.</p>
    <p>That has meant Revit and Navisworks plugins, model-health and clash-analytics platforms, and
    enterprise automation, across Cairo, Dubai and Munich. Along the way I delivered <strong>18 independent client
    engagements across 895 billable hours</strong> with a 5.0 average rating, doubling my rate over the period.</p>
    <p>My M.Sc. at TUM added the half I was missing: graduate work in geospatial information science, spatial
    data mining, photogrammetry and remote sensing alongside semantic modelling and software engineering.
    <strong>BIM, GIS and AI are converging, and very few people work across all three.</strong></p>
    <p>I speak Arabic natively, English at a professional working level (IELTS Academic 6.5), and I am
    learning German (A2).</p>
  </div>
  <div class="edu">
    <h3>Education</h3>
    <div><b>Technical University of Munich</b><span>M.Sc. Information Technologies for the Built Environment</span><em>Expected 2026</em></div>
    <div><b>Information Technology Institute</b><span>Intensive Code Camp: BIM Automation Development</span><em>2022 · Giza</em></div>
    <div><b>Alexandria University</b><span>B.Sc. Architectural Engineering</span><em>2014 to 2020</em></div>
    <div><b>Autodesk</b><span>Certified Professional, Revit Architecture</span><em>2020</em></div>
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
    W, H, CHARCOAL = 1200, 630, (68, 68, 68)
    im = Image.new("RGB", (W, H), CHARCOAL)
    grid = Image.new("RGBA", (W, H), (0, 0, 0, 0)); g = ImageDraw.Draw(grid)
    for x in range(0, W, 60): g.line([(x, 0), (x, H)], fill=(255, 255, 255, 16))
    for y in range(0, H, 60): g.line([(0, y), (W, y)], fill=(255, 255, 255, 16))
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
    d.text((x, y), "MOHAMED K. MAHDY", font=mono(19), fill=(178, 178, 178)); y += 52
    title = html.unescape(p['title'])
    for size in (64, 56, 48):
        tl = wrap(title, bold(size), tw, 3)
        if len(tl) <= 2 or size == 48: break
    for line in tl:
        d.text((x, y), line, font=bold(size), fill="white"); y += int(size * 1.12)
    y += 10
    d.text((x, y), html.unescape(p['tag']).upper(), font=mono(19), fill=(169, 201, 154)); y += 48
    for line in wrap(html.unescape(p['card']), sans(26), tw, 6 if shot else 4):
        d.text((x, y), line, font=sans(26), fill=(236, 236, 236)); y += 37
    d.text((x, H - 64), "mohamedkmahdy.github.io", font=mono(18), fill=(169, 201, 154))

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
    feats = ('<h2>Features</h2><ul class="features">' + "".join(f"<li>{html.escape(f, quote=False)}</li>" for f in p['features']) + '</ul>') if p.get('features') else ""
    res = f'<div class="result"><span>Highlight</span>{p["result"]}</div>' if p['result'] else ""
    pnote = f'<p class="pnote">{p["note"]}</p>' if p.get('note') else ""
    chips = "".join(f"<li>{s}</li>" for s in p['stack'])
    prev, nxt = P[i - 1], P[(i + 1) % len(P)]

    og_file = os.path.join(SITE, 'og', p['slug'] + '.png')
    # The version is the image's content hash, so link previews refresh whenever the image changes.
    og = (f"og/{p['slug']}.png?v={hashlib.sha1(open(og_file, 'rb').read()).hexdigest()[:8]}"
          if os.path.exists(og_file) else "og-image.png")
    return head(f"{p['title']} | {NAME}", html.unescape(p['card']), "../",
                f"{BASE}/projects/{p['slug']}.html", og) + f"""
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
  <h2>The problem</h2>
  <p class="problem">{p['problem']}</p>
  <h2>What it does</h2>
  {body}
  {feats}
  {res}
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

# Old page names point to the current ones, so earlier links keep working.
REDIRECTS = {"genq": "qubecta", "interior-finishes": "rifadex", "batch-tools": "revit-batch", "model-health": "revit-batch"}

# ---------------------------------------------------------------- write
os.makedirs(OUT_PROJ, exist_ok=True)
CSS_VER = hashlib.sha1(CSS.encode()).hexdigest()[:8]
open(os.path.join(SITE, 'style.css'), 'w').write(CSS)
open(os.path.join(SITE, 'index.html'), 'w').write(build_index())
og_made = [build_og(p) for p in P]
for i, p in enumerate(P):
    open(os.path.join(OUT_PROJ, p['slug'] + '.html'), 'w').write(build_project(i, p))
for old, new in REDIRECTS.items():
    open(os.path.join(OUT_PROJ, old + '.html'), 'w').write(
        f'<!doctype html><meta charset="utf-8"><title>Moved</title>'
        f'<meta http-equiv="refresh" content="0; url={new}.html"><link rel="canonical" href="{BASE}/projects/{new}.html">'
        f'<p>This page moved to <a href="{new}.html">{new}.html</a>.</p>')
print(f"built: index.html, style.css, {len(P)} project pages, {sum(og_made)} preview images")
for p in P:
    n = len(p['media'])
    print(f"  projects/{p['slug']}.html  ({n} media)" if n else f"  projects/{p['slug']}.html")
