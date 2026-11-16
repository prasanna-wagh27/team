# Builds final screens: parts/X.html with <!--PACKS--> <!--ICONS--> <!--SB--> markers -> X.html
import glob, os
packs = open('parts/packs.svg').read(); icons = open('parts/icons.svg').read(); kit = open('parts/kit.css').read()
sb = '''<div class="sb"><span>9:41</span><span class="r">
<svg width="18" height="12" viewBox="0 0 18 12"><rect x="0" y="8" width="3" height="4" rx="1"/><rect x="5" y="5.5" width="3" height="6.5" rx="1"/><rect x="10" y="3" width="3" height="9" rx="1"/><rect x="15" y="0" width="3" height="12" rx="1"/></svg>
<svg width="16" height="12" viewBox="0 0 16 12"><path d="M8 11.5 5.6 9a3.4 3.4 0 0 1 4.8 0Z"/><path d="M3.4 6.8a6.5 6.5 0 0 1 9.2 0l-1.4 1.4a4.5 4.5 0 0 0-6.4 0Z"/><path d="M1.2 4.6a9.6 9.6 0 0 1 13.6 0l-1.4 1.4a7.6 7.6 0 0 0-10.8 0Z"/></svg>
<svg width="27" height="13" viewBox="0 0 27 13"><rect x=".5" y=".5" width="23" height="12" rx="3.5" fill="none" stroke="currentColor" opacity=".45"/><rect x="2.5" y="2.5" width="17" height="8" rx="2"/><path d="M25 4.5v4a2 2 0 0 0 0-4Z" opacity=".45"/></svg>
</span></div><div class="island"></div>'''
for f in sorted(glob.glob('parts/*.html')):
    s = open(f).read().replace('<!--PACKS-->', packs).replace('<!--ICONS-->', icons).replace('<!--SB-->', sb).replace('<!--KIT-->', kit)
    open(os.path.basename(f), 'w').write(s); print('built', os.path.basename(f))
