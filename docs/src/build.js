// Builds every src/NN_*.html fragment into two PDFs:
//   ../NN_*.pdf          phone-sized (primary, for reading on mobile)
//   ../print/NN_*_A4.pdf A4 (for printing)
// Usage: node build.js   (run from docs/src)
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

const SRC = __dirname;
const OUT = path.resolve(SRC, '..');
const PRINT = path.join(OUT, 'print');

const variants = [
  { name: 'mobile', css: ['style.css', 'mobile.css'], dir: OUT, suffix: '', pad: '7mm', font: '8px' },
  { name: 'a4', css: ['style.css'], dir: PRINT, suffix: '_A4', pad: '17mm', font: '7px' },
];

(async () => {
  fs.mkdirSync(PRINT, { recursive: true });
  const browser = await chromium.launch();
  const page = await browser.newPage();
  // Optional: node build.js <file.html> <outDir>  -> builds only that file, phone-sized only
  const only = process.argv[2];
  const onlyOut = process.argv[3] ? path.resolve(process.argv[3]) : null;
  const files = only ? [path.basename(only)] : fs.readdirSync(SRC).filter(f => /^\d\d_.*\.html$/.test(f)).sort();
  const runVariants = only ? [{ ...variants[0], dir: onlyOut || OUT }] : variants;
  if (onlyOut) fs.mkdirSync(onlyOut, { recursive: true });
  for (const v of runVariants) {
    for (const f of files) {
      const body = fs.readFileSync(only ? path.resolve(only) : path.join(SRC, f), 'utf8');
      const title = (body.match(/<!--\s*title:\s*(.*?)\s*-->/) || [, f])[1];
      const links = v.css.map(c => `<link rel="stylesheet" href="${c}">`).join('');
      const html = `<!doctype html><html lang="en" class="${v.name}"><head><meta charset="utf-8"><title>${title}</title>${links}</head><body>${body}</body></html>`;
      const tmp = path.join(SRC, `.tmp_${f}`);
      fs.writeFileSync(tmp, html);
      await page.goto('file://' + tmp, { waitUntil: 'load' });
      await page.evaluate(() => {
        // Label each cell with its column header so stacked mobile cards stay readable.
        document.querySelectorAll('table').forEach(t => {
          const first = t.rows[0];
          if (!first || !first.querySelector('th')) return;
          first.classList.add('head');
          const labels = [...first.cells].map(c => c.textContent.trim());
          [...t.rows].slice(1).forEach(r => [...r.cells].forEach((c, i) => {
            if (i > 0 && labels[i]) c.dataset.label = labels[i];
          }));
        });
        return document.fonts.ready;
      });
      const out = path.join(v.dir, f.replace(/\.html$/, `${v.suffix}.pdf`));
      await page.pdf({
        path: out, printBackground: true, preferCSSPageSize: true,
        displayHeaderFooter: true,
        headerTemplate: '<span></span>',
        footerTemplate: `<div style="width:100%;font-family:Helvetica,Arial,sans-serif;font-size:${v.font};color:#5b6170;padding:0 ${v.pad};display:flex;justify-content:space-between">
          <span>Outgrid Labs · ${title}</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>`,
      });
      fs.unlinkSync(tmp);
      console.log('built', path.relative(OUT, out));
    }
  }
  await browser.close();
})();
