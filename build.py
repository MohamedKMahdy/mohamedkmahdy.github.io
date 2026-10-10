#!/usr/bin/env python3
"""Static site generator for mohamedkmahdy.github.io.
Run: python3 build.py   (from the site/ directory)"""
import os, re, html, hashlib

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
dict(slug="bimnox", title="Bimnox", tag="Revit 2023 to 2027 · batch", cats="revit cloud",
  card="Runs model checks and exports on many Revit models at once, overnight or every week, without anyone sitting at the computer.",
  plain="Architects and engineers keep their building designs in Revit models. Every week someone has to open dozens of these models, check them for errors and save copies in the formats other teams need. Bimnox does that job on its own: you choose the models and the tasks once, and it runs them on a schedule and collects the results in one folder.",
  head="Set up a job once, let it run every week.",
  problem="Checking models and exporting deliverables are jobs everyone agrees matter, but nobody has time to do them by hand for dozens of models every week.",
  stack=["C#", ".NET Framework 4.8 / .NET 8 / .NET 10", "Revit API", "WPF", "Autodesk Platform Services", "Windows Task Scheduler"],
  body=["<strong>Bimnox</strong> (BIM Nightly Orchestration and eXport) is a desktop program with a helper that works inside Revit without opening a window. It runs up to seven tasks on many models in one go, either now or on a weekly schedule: an Autodesk Model Checker check, an IFC export, an NWC export for Navisworks, PDF and DWG exports of the drawing sheets, a model health report and a report of what changed. It starts the right installed version of Revit in the background, opens each model once, runs every chosen task on it and closes it again without saving.",
        "<strong>Models can come from four places:</strong> selected models in Autodesk Construction Cloud (ACC), a whole ACC folder, a folder on your computer or network, or a fixed list of files. Folders are read again at every run, so new models are picked up automatically, and the results can be uploaded back to ACC.",
        "<strong>Repeat runs are quick.</strong> A model that has not changed since the last successful run is skipped. All results go into one output folder, together with a history workbook for Excel and Power BI, and an optional Microsoft Teams message after each run.",
        "<strong>One codebase, four apps.</strong> Besides Bimnox itself, the same code builds three single-task versions for teams that need only one job, each with its own name and icon: <strong>Bulk Model Checker</strong>, <strong>IFC Bulk Export</strong> and <strong>NWC Bulk Export</strong>.",
        "It is the latest generation of the scheduled checking and export services I first built in 2023, so that nothing depends on someone remembering to do it."],
  result="<strong>One codebase</strong> supports every Revit version from 2023 to 2027 and sends each model to an installed Revit that can open it. The interface is in German and English, and it installs per user without admin rights.",
  media=[]),  # screenshots in MEDIA below

dict(slug="aps-raumbuch", title="Raumbuch", tag="Revit + web", cats="revit cloud",
  card="Creates a room book, a list of every room and everything in it, straight from the building model. Works as a Revit add-in and as a web app.",
  plain="A room book (Raumbuch in German) lists every room in a building with its size, finishes and furniture. It is usually typed up by hand. Raumbuch builds it automatically from the 3D building model and exports it to Excel, PDF and an interactive web page.",
  head="One room book, two routes to it.",
  problem="A room book lists every room and everything in it. Teams often put it together by hand from the model, room by room, and have to start again when the design changes.",
  stack=["C#", "Revit API", "React", "Vite", "FastAPI", "APS Viewer", "Model Derivative API", "web-ifc", "three.js"],
  body=["<strong>Revit add-in</strong> (Revit 2023 to 2027). It finds the room that each piece of furniture and equipment stands in, also in linked models, and writes the room number and name onto the item. It then creates one cropped floor plan per room and exports the room book as an Excel file, a PDF with one page per room, and an interactive HTML page that works offline. The three steps sit in one panel inside Revit, in German and English.",
        "<strong>Web app.</strong> It signs in to Autodesk Construction Cloud, lets you browse hubs, projects and folders in every Autodesk data region, and opens a model in the browser with a floor plan next to the 3D view. It reads the rooms from the 3D model, from Autodesk's model data service, or from the 2D plans when neither has them. Furniture from the main model and every linked model is placed in one coordinate system and matched to a room by its room parameter, by its position, or by the nearest room within 2 m.",
        "Both versions export a formatted German <em>Raumbuch</em> to Excel, PDF and a single-file HTML dashboard whose charts also work as filters."],
  result="Not tied to one vendor: IFC files open <strong>without any login</strong>, are read in the browser and are never uploaded. Several IFC files can be combined into one model.",
  media=[("img","img/raumbuch-dashboard.jpg","The room book dashboard","One offline HTML file with summary tiles, charts that filter and the room table. Rendered from the real template with sample data."),
         ("imgn","img/raumbuch-panel.png","The Revit add-in panel","Model status, the three steps, the export formats and the settings, in one panel.")]),

dict(slug="clash-management", title="SORTIE", tag="Navisworks · clash tools", cats="clash",
  card="Sorts the thousands of clashes found in a Navisworks clash check by building zone, and keeps their status and comments when the check is run again.",
  plain="Before a building is built, designers combine the models from every discipline and let software look for places where things collide, such as a pipe running through a beam. These are called clashes, and one check can find thousands. SORTIE groups them by area of the building so each team can see its share, and it carries notes and decisions over when the check is repeated.",
  head="4,000 clashes, 200 actual problems.",
  problem="A clash check can report thousands of clashes when the real coordination problems number only a few hundred. Sorting them by area, and keeping their status when the checks are rerun or the files change, takes days.",
  stack=["C#", "Navisworks API 2022 to 2027", "WPF", "xUnit"],
  body=["<strong>SORTIE</strong> (Status Organiser, Renamer and Transferrer for Interference Events) is an add-in for Navisworks Manage 2022 to 2027.",
        "<strong>Zones.</strong> It groups clashes by the zone of the building they sit in, one group per zone, or adds the zone name in front of each clash name. A zone can be any 3D object, such as a mass, a room or a separate zones model, and its real shape is used rather than a simple box around it. Where zones overlap, the smallest one wins.",
        "<strong>Status transfer.</strong> It saves each clash's status, assignee, approval, description and comments, and loads them back onto the same clashes in this file or another Navisworks file, also from a Navisworks XML clash report. Clashes are matched by their unique ID first and then by the pair of elements involved.",
        "<strong>Clean up.</strong> It moves clashes back out of their groups, or removes the zone names again."],
  result="Every action works only on the clash tests you tick and can be undone in <strong>one step</strong>. A clash that could match two others is left alone rather than guessed.",
  media=[("img","img/sortie-zones.png","Grouping clashes by zone","Zones come from any 3D objects; a clash belongs to the zone its clash point lies in."),
         ("img","img/sortie-logo.png","The SORTIE mark","")]),

dict(slug="rimacos", title="Rimacos", tag="openBIM · clash matrices", cats="clash",
  card="Replaces a huge hand-filled clash table with a few rules, and turns them into ready-to-run clash checks for several programs.",
  plain="A clash matrix is a big table that says which parts of a building should be checked against which, for example pipes against beams. On large projects it has thousands of cells that someone fills in by hand. Rimacos replaces the table with a few rules and produces the checks, reports and files that several programs need, including open formats any software can read.",
  head="Rules, not cells.",
  problem="A clash matrix grows with the square of the number of element groups. Filling in thousands of cells by hand, and turning them into thousands of separate clash tests, does not scale.",
  stack=["Python", "IfcOpenShell / IfcClash", "IDS 1.0", "BCF", "Navisworks XML", "openpyxl", "pytest"],
  body=["<strong>Rimacos</strong> (Rule-based Interference Matrices And Clash tests on Open Standards) turns a short list of rules into a complete clash matrix and the files to run it: search sets and clash tests for Navisworks, clash sets for the open-source IfcClash tool with results in BCF, an IDS file that checks the models contain the information the groups depend on, and an Excel matrix and HTML report for the project's BIM execution plan.",
        "A rule says how two sets of elements are tested against each other. Each side can be everything, a discipline, a tag or a single group, and the most specific rule wins. A local browser editor handles the matrix, the groups and the rules.",
        "Groups select elements by IFC class and type, by property filters and by classification codes, and models are found by their ISO 19650 file names, so the whole matrix also runs on open, free tools."],
  result="A classic 133-group matrix had <strong>8,778 cells</strong>. Rimacos reproduces every one of them with <strong>4 rules</strong>, and the merged output needs <strong>79 clash tests</strong> instead of 8,778.",
  media=[("img","img/rimacos-editor.jpg","The matrix editor","Discipline matrix, the rule behind each cell, and the group pairs it decides.")]),

dict(slug="speckle-llm", title="ARVENT", tag="Speckle · local AI", cats="ai cloud",
  card="Answers questions about a 3D building model in plain language, right in the model's comment threads. It runs on a local AI model, so no data leaves the machine.",
  plain="Most people on a building project never open the 3D model, but they still have questions about it. ARVENT lets them ask in a comment, for example how many doors have no fire rating, and replies with the answer, the exact data behind it and a link that shows those parts in the model. It also checks each new version of the model against the project's written requirements.",
  head="I connected AI to building models before it was a trend.",
  problem="Most people on a project never open the model, but they still have questions about it: what this panel's insulation value is, how many doors have no fire rating, whether the latest version still meets the specification.",
  stack=["Python", "FastAPI", "Speckle (GraphQL, webhooks, specklepy)", "Ollama", "Llama 3.1", "SQLite"],
  body=["In 2023 I connected Speckle, an open platform for sharing 3D building models, to a large language model, so project teams could ask questions about a model in plain language. <strong>ARVENT</strong> (Assistant for Requirements, Verification and Element Notes in Threads) is the 2026 rebuild. It runs on a <strong>local Llama model through Ollama</strong>, so model data and project documents never leave the machine.",
        "It works inside Speckle's comment threads. It answers questions about a selected element from its properties and any attached specification PDF, with page references. It answers questions about the whole model. And it checks every new model version against rules taken from the specification: for each rule that fails, it opens a thread that highlights the elements involved, and it replies when a later version fixes them.",
        "<strong>The language model never calculates anything and never writes database queries.</strong> It only fills in a structured query plan limited to the real field names; code checks and corrects that plan and runs it, and every reply shows the exact query and result. Rules from the specification are proposed by the model and run only after a person approves them.",
        "Along the way I also built a custom connector between Speckle and Revit for a separate client, so the two platforms could exchange data more openly."],
  result="The lesson from 2023 still holds: <strong>the AI was never the hard part.</strong> The hard part is getting clean, structured data out of the design tools.",
  media=[("img","img/arvent-card.png","The ARVENT mark",""), ("img","img/arvent-logo.png","The mark on light and dark backgrounds","On white, on the dark header band and as an icon.")]),

dict(slug="qubecta", title="Qubecta", tag="Revit · cost planning", cats="revit",
  card="Turns the quantities in a Revit model into a priced bill of quantities and a cost plan, and exports them to Excel, PDF or the German GAEB tender format.",
  plain="To estimate what a building will cost, quantity surveyors measure how much of each material and component it needs, then price it. Much of that information is already in the 3D model. Qubecta reads it from the model, suggests prices and categories, and produces the cost documents in the formats that estimators and tender software use.",
  head="A priced bill and a cost plan without leaving Revit.",
  problem="Quantity surveyors often measure again what the model already knows. Qubecta reads the quantities straight from Revit, prices them and turns them into a bill of quantities and a cost plan.",
  stack=["C#", "Revit API 2022 to 2027", ".NET Framework 4.8 / .NET 8 / .NET 10", "ClosedXML", "PDFsharp", "GAEB DA XML 3.3", "xUnit"],
  body=["<strong>Qubecta</strong> (QUantities, Bills, Elements, Costs, Tendering and Assembly codes) is an add-in for Revit 2022 to 2027. You tick the element types to price and give each one a unit, a section in the bill (CSI MasterFormat 2018, RICS NRM2 or your own list), a group in the cost plan (UniFormat, RICS NRM1, DIN 276 or your own list), a rate and a description. <strong>Qubecta suggests all of these</strong> from your earlier projects, from codes already in the model, and from each type's name and materials, and it gives the reason for each suggestion. You check them before anything changes.",
        "It then measures the model and produces the bill by trade and the cost plan by building element, with the cost per m² of floor area and additions such as site overheads, contingency and VAT. Exports go to Excel, PDF and CSV, and to <strong>GAEB DA XML</strong>, the standard format of German tendering and costing software, checked against the official schemas. The cost codes are also written back into the model, so Revit schedules and IFC exports carry them.",
        "It measures the whole model in one pass, filters by construction phase, design option and floor, and counts linked models that are placed more than once. It recognises categories by Revit's internal IDs, so it works in any Revit language. Doors and windows can take their cost group from the wall or roof they sit in, and walls and floors from whether they are external or load-bearing."],
  result="Tested inside Revit on Autodesk's Snowdon Towers sample model: <strong>392 types, 294 suggestions, 136 bill lines</strong>, a cost plan by element, and a GAEB export that passes the official 3.3 schemas.",
  media=[("img","img/qubecta-tabs.jpg","Set up, bill and cost plan","Three numbered steps in one panel, shown with a sample model."),
         ("img","img/qubecta-suggest-export.jpg","Suggestions and export","Each suggestion says why; exports include GAEB X83 and X82."),
         ("imgn","img/qubecta-revit.png","Docked in Revit","DIN 276 suggestions with their checks, from the in-Revit test on the Snowdon Towers sample."),
         ("video","video/qubecta-earlier.mp4","An earlier version","Generating a detailed bill of quantities in Excel.")]),

dict(slug="rifadex", title="RIFADEX", tag="Revit · interior finishes", cats="revit",
  card="Draws the wall, floor, skirting and ceiling finishes of every room in a Revit model, and keeps them up to date when the design changes.",
  plain="Every room in a building gets finishes: plaster or tiles on the walls, a floor covering, skirting boards and a ceiling. In a 3D model each one has to be drawn by hand, and redrawn whenever a room changes. RIFADEX lets you pick the finishes per room, then draws and updates them automatically.",
  head="Finish walls, floors, skirting and ceilings that follow the rooms.",
  problem="Modelling interior finishes by hand, room by room, is slow, and every design change leaves finishes that no longer fit the room.",
  stack=["C#", "Revit API 2024 to 2027", ".NET Framework 4.8 / .NET 8 / .NET 10", "WPF", "extensible storage", "no third-party libraries"],
  body=["You pick a wall, floor, skirting and ceiling finish for each room, one room at a time or many at once, in this model or in a linked architect's model. RIFADEX then draws a finish wall along each side of the room, a floor with cut-outs for columns and shafts, skirting that stops at doors, and a ceiling at the room height. Door and window openings in the walls behind are cut through the finish walls. Lengths are shown and entered in the project's own units.",
        "<strong>Plan, preview, apply.</strong> Every change is shown before anything is drawn. Running it again updates the existing finishes instead of drawing new ones, so their tags and schedules keep working: a new finish code changes the type, a room that changed shape is redrawn, openings follow moved doors, and a wall moved by up to 500 mm takes its finish with it. A type you changed by hand is kept, so a feature wall survives. The linked model is never changed.",
        "Finish types and materials are edited in a table or in Excel, where a new row creates a new type, with an optional naming convention. One settings file holds the company standard, so any project template works and nothing has to be added to a project first.",
        "<strong>RIFADEX</strong> (Revit Interior Finishes: Assignment, Drawing and Excel eXchange) is a single, company-neutral package that rebuilds my earlier in-house finishes tools."],
  result="Tested inside Revit from start to finish with 57 checks in Revit 2026: drawing, redrawing, hand edits, door openings, a moved and rotated linked model and an Excel round trip. <strong>One codebase for Revit 2024 to 2027</strong>, with no third-party libraries.",
  media=[("img","img/rifadex-room-finishes.png","Room Finishes","Codes per room from a linked model, then save and draw. Captured in Revit 2026."),
         ("imgn","img/rifadex-ribbon.png","The RIFADEX ribbon panel","Four tools: Room Finishes, Finish Types, Finish Materials and Settings."),
         ("img","img/rifadex-finish-types.png","Finish Types","Edit types here or in Excel; a row marked NEW creates a new type."),
         ("img","img/rifadex-materials.png","Finish Materials","The same table and Excel round trip for materials."),
         ("img","img/rifadex-settings.png","Settings","The company standard: finish parameters, types, materials, naming and Excel."),
         ("video","video/finishes-drawer.mp4","An earlier version: drawing finishes","Reads room finishes and draws the walls, floors and skirting."),
         ("video","video/finishes-manager.mp4","An earlier version: finish types","Finish types exported, edited in Excel and written back to the model."),
         ("video","video/materials-manager.mp4","An earlier version: finish materials","The same round trip for finish materials.")]),

dict(slug="acc-integrations", title="LARBACC", tag="ACC · backups", cats="cloud",
  card="Makes regular, automatic backup copies of Autodesk Construction Cloud projects on your own drive, downloading only what changed.",
  plain="Many construction teams keep all their project files in Autodesk Construction Cloud, an online file platform. If a folder is deleted there or a subscription ends, the files can be lost. LARBACC copies the projects you choose to your own drive every week and keeps the last few copies.",
  head="Stored in the cloud is not the same as backed up.",
  problem="Projects in Autodesk Construction Cloud feel safe because they live in the cloud. A deleted folder or an ended subscription can still take years of work with it.",
  stack=["C#", ".NET 8", "WPF", "Autodesk Platform Services (PKCE)", "Data Management API"],
  body=["<strong>LARBACC</strong> (Local, Automatic, Rotating Backups of Autodesk Construction Cloud) keeps dated copies of ACC and BIM 360 projects on a local or network drive. You choose projects and folders, a destination and a weekly time; LARBACC downloads the latest version of every document and keeps the last few backups. The interface is in German and English.",
        "<strong>Only changes are downloaded.</strong> A document that has not changed since the previous backup is linked to the earlier copy instead of downloaded again (a file-system feature called a hard link), so later runs are fast and five backups do not take five times the space. A run only counts as a backup once its complete file list is written, so a crash or power cut never leaves a half-finished folder that looks complete.",
        "Sign-in uses a secure method (PKCE) that needs no secret key inside the program. A backup missed while LARBACC was closed runs at the next start, and a failed one is retried after 15 minutes, 1 hour and 4 hours."],
  result="Open-source roots: LARBACC began as a desktop interface for Stewart Celani's MIT-licensed <a href=\"https://github.com/stewartcelani/autodesk-construction-cloud-backup\" rel=\"noopener\">autodesk-construction-cloud-backup</a>, and keeps that history and credit.",
  media=[]),  # screenshots in MEDIA below

dict(slug="family-validation", title="Family Validation", tag="Revit · content library", cats="revit",
  card="Checks and cleans whole folders of Revit components (families) against a company standard, without anyone opening Revit.",
  plain="Revit models are built from reusable components called families, such as a door, a chair or a light fitting. Companies keep libraries of hundreds of them, and one badly made family can slow down every project that uses it. Family Validation checks a whole folder of families against the company's rules, fixes what it safely can, and writes a report.",
  head="Clean families in, clean library out.",
  problem="One badly built family, for example one with an imported CAD drawing inside it or in the wrong category, slows down every project that loads it. Nobody checks hundreds of them by hand.",
  stack=["C#", "Revit API 2023 to 2027", "WPF", ".NET Framework 4.8 / .NET 8 / .NET 10", "no third-party libraries"],
  body=["A small launcher program runs Revit in the background, opens every family in a folder and checks it: the file name against the naming rules (correcting the category prefix when that is safe), imported CAD drawings inside the family (removed, while linked CAD files are kept), whether the name matches the category, required parameters, file size limits, and an optional classification code such as DIN 276 or Uniclass. The checked families are then ready for the company library or the Autodesk Content Catalog.",
        "<strong>Safe by design.</strong> The original file is copied aside before anything else, and a family that cannot be copied is skipped, never touched. Cleaned copies go to their own folder, the original files are never changed, and a dry run writes the full report without changing anything.",
        "A visual rules editor lets people who do not write code maintain the standard: categories and name patterns are built from simple blocks, and the editor refuses to save a set of rules that the check would reject."],
  result="<strong>No third-party libraries:</strong> everything is built on .NET and the Revit API, with a separate build for the .NET version that each Revit release uses.",
  media=[("img","img/family-validation-logo.png","The Family Validation mark","")]),

dict(slug="cloud-revisions", title="Cloud Revisions", tag="Revit add-in", cats="revit data",
  card="Lists every revision cloud in a Revit model with its drawing sheet and revision details, and exports the list to Excel or an interactive offline dashboard.",
  plain="When a drawing changes, designers mark the change with a revision cloud, a wavy outline with a revision number next to it. On a big project there are hundreds of them spread over many drawing sheets. Cloud Revisions collects them all into one list, so anyone can see what changed, where, and in which revision.",
  head="One list of every change marked on the drawings.",
  problem="Keeping track of which revision clouds are on which sheets, and under which revision, usually means clicking through the sheets one by one.",
  stack=["C#", "Revit API 2023 to 2027", ".NET Framework 4.8 / .NET 8 / .NET 10", "dependency-free Excel and HTML"],
  body=["Revision clouds are notes drawn on the drawings, and Autodesk's online data services either do not provide them or provide them only in part. The only complete source is Revit itself, so this is a Revit add-in.",
        "It lists every revision cloud in the open model with its view, the sheet it appears on and all its revision details: sequence, number, date, description, whether it has been issued, and by and to whom. It then exports a formatted Excel workbook or a single-file HTML dashboard with filters similar to Power BI. Everything sits in one panel on its own Revit tab, in German or English."],
  result="Neither export needs Excel, any online service or internet access. The add-in writes both files itself, so they also work on locked-down <strong>company networks</strong>.",
  media=[("img","img/cloud-revisions-dashboard.jpg","The revision cloud dashboard","Filters by revision, view type, issue status and sheet, with linked charts. Rendered from the real template with sample data."),
         ("img","img/cloud-revisions-logo.png","The Cloud Revisions mark","")]),

dict(slug="revit-automation", title="Revit Automation Suite", tag="4 tools · video", cats="revit",
  card="Four Revit tools that take over repetitive model tasks: preparing files for issue, organising worksets, joining elements and copying types between projects.",
  plain="In Revit, many routine jobs mean clicking through the same steps again and again, such as cleaning up a model before sending it out or copying standard settings into each project. Each of these four tools does one such job automatically, across a whole model or many projects at once.",
  head="Small tools for the jobs nobody wants to do by hand.",
  problem="Small, repetitive Revit tasks, such as setting up worksets, joining elements, copying types between projects and cleaning models before issue, add up to hours of engineering time every week.",
  stack=["C#", "Revit API", "WPF", "Excel interop"],
  body=["A set of Revit add-ins built for architecture and engineering teams, covering model management, worksets, element joins and bulk file operations. Each one replaced a manual routine that cost engineering hours every week.",
        "The quantity and finishes tools from the same years have since grown into products of their own, <a href=\"qubecta.html\">Qubecta</a> and <a href=\"rifadex.html\">RIFADEX</a>, and are shown there. All demos below use a generic sample model."],
  result="",
  media=[
    ("video","video/revit-transmitter.mp4","Revit-Transmitter","Detaches models with worksets kept or removed, purges unused elements and prepares files ready for issue."),
    ("video","video/worksets-manager.mp4","Worksets Manager","Creates standard worksets from Excel or by UniFormat code, then puts every element in the right one."),
    ("video","video/auto-joiner.mp4","Auto Joiner","Joins and unjoins every overlapping element of the chosen categories in one pass."),
    ("video","video/transfer-types.mp4","Transfer Types","Choose Revit projects from a folder tree and copy types and families between them in bulk."),
    ("img","img/image54.png","Auto Joiner: interface",""),
  ]),

dict(slug="bim-analytics", title="BIM Analytics", tag="Power BI · 9 dashboards", cats="data",
  card="Power BI dashboards that show the health of building models, open clashes, issues and team workload to people who never open the models.",
  plain="Project managers need to know whether the 3D models are in good shape, how many design conflicts are still open and who is working on what. That information sits inside model files and cloud platforms they rarely open. These dashboards pull it out automatically and show it in charts that update on their own.",
  head="Making model health visible to people who never open Revit.",
  problem="Model health is invisible to the people who never open Revit, and they are most of the people making decisions about a project.",
  stack=["Power BI", "DAX", "SharePoint", "BIM 360 / ACC", "Revizto", "Python"],
  body=["A set of automated Power BI dashboards and reporting pipelines for BIM coordination, covering model health, clash detection, open issues, ACC account administration, resourcing and team assessment.",
        "Each dashboard reads directly from project data and refreshes on a schedule, so the coordination status is always current without anyone putting a report together. They are published as project information hubs on SharePoint.",
        "In 2026 I decoded one programme's 52 Power BI files (model health across 376 Revit models, clash trends, issues and account administration) and rebuilt them as <strong>one self-contained HTML page</strong> that opens offline in any browser, without Power BI, and leaves out every personal detail."],
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

# Where I've worked: (when, employer, place, role, summary)
JOBS = [
 ("2025 to now", "Sweco", "Munich", "Working Student, AI &amp; Automation Specialist (BIM + Data Science)",
  "I own the AI and automation roadmap for the BIM + Data Science department: scoping the automation portfolio, building Revit tools and LLM agents, and taking tools through internal release."),
 ("2024 to 2025", "Obermeyer", "Munich", "BIM Software Developer",
  "Model-checking rules in Desite MD, Power Automate flows for managing SharePoint data, and Power BI reports on model quality."),
 ("2023 to 2024", "Dewan Architects + Engineers", "Dubai, remote", "BIM Software Developer &amp; Data Analyst",
  "BIM software development and data analytics for coordination, model quality and project reporting."),
 ("2022 to 2024", "Freelance (Upwork)", "Remote", "BIM Software Developer &amp; Data Analyst",
  "18 client projects over 895 billable hours with a 5.0 average rating: Revit automation, Dynamo scripts and Python data pipelines."),
 ("2023", "Solid Construction", "Cairo", "BIM Software Developer",
  "Revit add-ins and Dynamo workflows for structural, quantity and finishes work."),
 ("2021 to 2023", "Pinnacle Misr", "Cairo", "BIM Coordinator / Developer",
  "Revit plugins and Dynamo workflows on large projects, including the El Alamein Iconic Tower and Kitoko Ministerial City."),
 ("2020 to 2021", "X-Dimension", "Cairo", "BIM Architect",
  "BIM standards and templates, Dynamo workflows, and Scan-to-BIM (turning laser scans of existing buildings into models)."),
]

# How I build: principles drawn from the projects above.
WAYS = [
 ("People stay in control", "Every action is one undo step, a dry run comes before anything changes, and when AI proposes something, a person approves it."),
 ("Boring is a feature", "Tools that run overnight on their own, try again when the network drops, and never leave a half-finished result that looks complete."),
 ("Data stays where it belongs", "AI models that run locally, IFC files read in the browser instead of uploaded, and no passwords or keys built into a program."),
 ("Open where it counts", "Open file formats such as IFC, IDS and BCF wherever they fit, so a workflow is not locked to one vendor."),
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
--charcoal:#1e1e1e;--on-charcoal:#ffffff;--charcoal-soft:#B2B2B2;--amber:#E0A800;
--shadow:0 1px 2px rgba(0,0,0,.04),0 6px 18px rgba(0,0,0,.05);
--mono:"Cascadia Mono",ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;
--sans:"Segoe UI",-apple-system,BlinkMacSystemFont,Calibri,Arial,sans-serif;--maxw:1060px;--read:760px}
:root[data-theme="dark"]{--bg:#3d3d3d;--bg-alt:#464646;--fg:#F2F2F2;--fg-soft:#cfcfcf;--fg-faint:#B2B2B2;
--accent:#A9C99A;--accent-2:#7BA85F;--on-accent:#111;--accent-soft:#3f4f37;--warm:#A9C99A;--line:#5a5a5a;--card:#4a4a4a;
--shadow:0 1px 2px rgba(0,0,0,.3)}
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
.pbody{padding-top:40px;padding-bottom:48px}
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
.plain{margin:0 0 30px;padding:18px 20px;background:var(--card);border:1px solid var(--line);border-left:4px solid var(--accent-2);border-radius:10px}
.plain span{display:block;font-family:var(--mono);font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:var(--accent-2);margin-bottom:6px}
.plain p{margin:0;font-size:17.5px;line-height:1.6}
.gloss{display:grid;grid-template-columns:1fr;gap:8px;margin:8px 0 0}
.gloss div{padding:10px 14px;border:1px solid var(--line);border-radius:8px;background:var(--card)}
.gloss dt{font-weight:700;color:var(--accent)}
.gloss dd{margin:2px 0 0;color:var(--fg-soft);font-size:15.5px;line-height:1.55}
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
if(!c)c='light';
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
  <p>If your team loses hours to model checks, exports, sorting clashes or copying data out of Revit by hand,
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
    on their own every night. Each project page starts with a short explanation in plain words, then the
    problem the tool solves, and it explains the technical terms it uses.</p>
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
    <p>I trained as an architectural engineer and moved into software because the most interesting problems in
    construction are data problems. Most firms have valuable project data trapped in disconnected tools and
    manual workflows. I build the systems that connect it.</p>
    <p>That has meant Revit and Navisworks plugins, model-health and clash-analytics platforms, and
    enterprise automation, across Cairo, Dubai and Munich. Along the way I completed <strong>18 freelance client
    projects over 895 billable hours</strong> with a 5.0 average rating, and doubled my rate over that time.</p>
    <p>My M.Sc. at TUM added the half I was missing: graduate courses in geographic information science, spatial
    data mining, photogrammetry and remote sensing, alongside semantic modelling and software engineering.
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
    plain = f'<div class="plain"><span>In plain words</span><p>{p["plain"]}</p></div>' if p.get('plain') else ""
    text = " ".join([p['title'], p['card'], p.get('plain', ''), p['problem'], p['result']] + p['body'] + p.get('features', []))
    text = re.sub(r"<[^>]+>", " ", text)
    # Everyday words (add-in, family, sheet...) match in any case; acronyms and names only as written.
    terms = [(t, d) for t, rx, d in GLOSSARY if re.search(rx, text, 0 if t.isupper() or " " in t or t in ("Revit", "Navisworks", "Speckle") else re.I)]
    gloss = ('<h2>Terms on this page</h2><dl class="gloss">' + "".join(f"<div><dt>{t}</dt><dd>{d}</dd></div>" for t, d in terms) + '</dl>') if terms else ""
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
  {plain}
  <h2>The problem</h2>
  <p class="problem">{p['problem']}</p>
  <h2>What it does</h2>
  {body}
  {feats}
  {res}
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

# Old page names point to the current ones, so earlier links keep working.
REDIRECTS = {"genq": "qubecta", "interior-finishes": "rifadex", "batch-tools": "bimnox", "model-health": "bimnox", "revit-batch": "bimnox"}

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
