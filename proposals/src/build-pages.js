// Builds a phone-width PDF where each <section> is one page sized to its content,
// plus a PNG preview per page.
// Usage: node build-pages.js <file.html>   (run from proposals/src)
const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');
const { chromium } = require('playwright');

(async () => {
  const src = path.resolve(process.argv[2]);
  const base = path.basename(src, '.html');
  const outDir = path.join(path.dirname(src), '..');
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 416, height: 800 }, deviceScaleFactor: 2 });
  await page.goto('file://' + src, { waitUntil: 'load' });
  await page.evaluate(() => document.fonts.ready);
  const n = await page.evaluate(() => document.querySelectorAll('section').length);
  const parts = [];
  for (let i = 0; i < n; i++) {
    const h = await page.evaluate(i => {
      const s = [...document.querySelectorAll('section')];
      s.forEach((el, j) => { el.style.display = j === i ? 'block' : 'none'; });
      return Math.ceil(document.body.getBoundingClientRect().height);
    }, i);
    const part = path.join(outDir, `.part${i}.pdf`);
    await page.pdf({ path: part, width: '110mm', height: `${h + 2}px`, printBackground: true, pageRanges: '1' });
    await page.setViewportSize({ width: 416, height: h });
    await page.screenshot({ path: path.join(outDir, `${base}_p${i + 1}.png`), fullPage: true });
    parts.push(part);
  }
  await browser.close();
  const out = path.join(outDir, `${base}.pdf`);
  execFileSync('python3', ['-c', `
import sys
from pypdf import PdfReader, PdfWriter
w = PdfWriter()
for p in sys.argv[2:]:
    w.add_page(PdfReader(p).pages[0])
w.write(sys.argv[1])
`, out, ...parts]);
  parts.forEach(p => fs.unlinkSync(p));
  console.log('built', path.relative(process.cwd(), out), n, 'pages');
})();
