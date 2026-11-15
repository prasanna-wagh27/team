// Builds a landscape 1280x720 slide PDF (one .slide per page) plus PNG previews.
// Usage: node build-slides.js <file.html>   (run from proposals/src)
const path = require('path');
const fs = require('fs');
const { chromium } = require('playwright');

(async () => {
  const src = path.resolve(process.argv[2]);
  const base = path.basename(src, '.html');
  const outDir = path.join(path.dirname(src), '..');
  const prevDir = path.join(outDir, 'previews');
  fs.mkdirSync(prevDir, { recursive: true });
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1280, height: 720 }, deviceScaleFactor: 1 });
  await page.goto('file://' + src, { waitUntil: 'load' });
  await page.evaluate(() => document.fonts.ready);
  await page.pdf({ path: path.join(outDir, `${base}.pdf`), width: '1280px', height: '720px', printBackground: true, preferCSSPageSize: true });
  const slides = await page.$$('.slide');
  for (let i = 0; i < slides.length; i++) {
    await slides[i].screenshot({ path: path.join(prevDir, `${base}_s${i + 1}.png`) });
  }
  await browser.close();
  console.log('built', base + '.pdf', slides.length, 'slides');
})();
