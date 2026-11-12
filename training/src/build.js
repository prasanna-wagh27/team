// Builds every src/NN_*.html fragment into ../NN_*.pdf
// Usage: node build.js   (run from training/src)
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

const SRC = __dirname;
const OUT = path.resolve(SRC, '..');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  const files = fs.readdirSync(SRC).filter(f => /^\d\d_.*\.html$/.test(f)).sort();
  for (const f of files) {
    const body = fs.readFileSync(path.join(SRC, f), 'utf8');
    const title = (body.match(/<!--\s*title:\s*(.*?)\s*-->/) || [, f])[1];
    const html = `<!doctype html><html lang="en"><head><meta charset="utf-8"><title>${title}</title>
<link rel="stylesheet" href="style.css"></head><body>${body}</body></html>`;
    const tmp = path.join(SRC, `.tmp_${f}`);
    fs.writeFileSync(tmp, html);
    await page.goto('file://' + tmp, { waitUntil: 'load' });
    await page.evaluate(() => document.fonts.ready);
    const out = path.join(OUT, f.replace(/\.html$/, '.pdf'));
    await page.pdf({
      path: out, format: 'A4', printBackground: true, preferCSSPageSize: true,
      displayHeaderFooter: true,
      headerTemplate: '<span></span>',
      footerTemplate: `<div style="width:100%;font-family:Helvetica,Arial,sans-serif;font-size:7px;color:#5b6170;padding:0 17mm;display:flex;justify-content:space-between">
        <span>Outgrid Labs · ${title}</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>`,
    });
    fs.unlinkSync(tmp);
    console.log('built', path.basename(out));
  }
  await browser.close();
})();
