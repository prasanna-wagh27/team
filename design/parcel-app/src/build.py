# Builds new screens from parts/<name>.html into full pages with shared status bar, icons and home bar.
# Usage: python3 build.py   (writes NN_name.html next to this file)
import glob, os
HERE = os.path.dirname(os.path.abspath(__file__))
icons = open(os.path.join(HERE, 'icons.svg.part')).read()
icons += '''
  <symbol id="send" viewBox="0 0 24 24"><path d="M21 3 10 14"/><path d="M21 3 14 21l-4-7-7-4Z"/></symbol>
  <symbol id="mic" viewBox="0 0 24 24"><rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5 11a7 7 0 0 0 14 0M12 18v3"/></symbol>
  <symbol id="image" viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="16" rx="2.5"/><circle cx="9" cy="10" r="1.8"/><path d="m21 16-5-5-9 9"/></symbol>
  <symbol id="more" viewBox="0 0 24 24"><circle cx="5" cy="12" r="1.3"/><circle cx="12" cy="12" r="1.3"/><circle cx="19" cy="12" r="1.3"/></symbol>
  <symbol id="staro" viewBox="0 0 24 24"><path d="m12 2.5 2.9 6 6.6.9-4.8 4.6 1.2 6.5L12 17.4l-5.9 3.1 1.2-6.5L2.5 9.4l6.6-.9Z"/></symbol>
  <symbol id="flag" viewBox="0 0 24 24"><path d="M5 21V4M5 4h11l-2 4 2 4H5"/></symbol>
  <symbol id="receipt" viewBox="0 0 24 24"><path d="M5 3h14v18l-3-2-2 2-2-2-2 2-2-2-3 2Z"/><path d="M9 8h6M9 12h6"/></symbol>
  <symbol id="bank" viewBox="0 0 24 24"><path d="M3 10 12 4l9 6M5 10v8M9.5 10v8M14.5 10v8M19 10v8M3 20h18"/></symbol>
  <symbol id="up" viewBox="0 0 24 24"><path d="M4 16l6-6 4 4 6-6"/><path d="M15 8h5v5"/></symbol>
  <symbol id="info" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M12 11v6"/><circle cx="12" cy="7.8" r=".7"/></symbol>
  <symbol id="nav" viewBox="0 0 24 24"><path d="M3 11 21 3l-8 18-2-8Z"/></symbol>
  <symbol id="route" viewBox="0 0 24 24"><circle cx="6" cy="19" r="2.5"/><circle cx="18" cy="5" r="2.5"/><path d="M8.5 19H17a3.5 3.5 0 0 0 0-7H7a3.5 3.5 0 0 1 0-7h8.5"/></symbol>
  <symbol id="logo" viewBox="0 0 24 24"><path d="M4 17c3-9 13-9 16-6" /><circle cx="4.5" cy="17.5" r="2" fill="currentColor" stroke="none"/><path d="M17 8l3 3-3.5 2"/></symbol>
'''
SB = '''    <div class="sb%s">
      <span>9:41</span>
      <span class="sbr">
        <svg width="18" height="12" viewBox="0 0 18 12"><rect x="0" y="8" width="3" height="4" rx="1"/><rect x="5" y="5.5" width="3" height="6.5" rx="1"/><rect x="10" y="3" width="3" height="9" rx="1"/><rect x="15" y="0" width="3" height="12" rx="1"/></svg>
        <svg width="16" height="12" viewBox="0 0 16 12"><path d="M8 11.5 5.6 9a3.4 3.4 0 0 1 4.8 0Z"/><path d="M3.4 6.8a6.5 6.5 0 0 1 9.2 0l-1.4 1.4a4.5 4.5 0 0 0-6.4 0Z"/><path d="M1.2 4.6a9.6 9.6 0 0 1 13.6 0l-1.4 1.4a7.6 7.6 0 0 0-10.8 0Z"/></svg>
        <svg width="27" height="13" viewBox="0 0 27 13"><rect x=".5" y=".5" width="23" height="12" rx="3.5" fill="none" stroke="currentColor" opacity=".4"/><rect x="2.5" y="2.5" width="17" height="8" rx="2"/><path d="M25 4.5v4a2 2 0 0 0 0-4Z" opacity=".4"/></svg>
      </span>
    </div>
    <div class="island"></div>
'''
for part in sorted(glob.glob(os.path.join(HERE, 'parts', '*.html'))):
    name = os.path.basename(part)[:-5]
    src = open(part).read()
    first, body = src.split('\n', 1)          # first line: <!-- title | light|dark -->
    title, mode = [x.strip() for x in first.strip('<!-> \n').split('|')]
    page = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Parcel app · {title}</title>
<link rel="stylesheet" href="app.css">
</head>
<body>
<div class="screen{' dark' if mode=='dark' else ''}">
{SB % (' light' if mode=='dark' else '')}{body}  <div class="homebar"></div>
</div>
<svg width="0" height="0" style="position:absolute"><defs>
{icons}
</defs></svg>
</body>
</html>
'''
    open(os.path.join(HERE, name + '.html'), 'w').write(page)
    print('built', name)
