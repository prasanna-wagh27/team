// Builds a branded, phone-sized proposal PDF (cover page without footer).
// Usage: node build.js <file.html>   -> ../<file>.pdf
const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');
const { chromium } = require('playwright');

(async () => {
  const src = path.resolve(process.argv[2]);
  const out = path.join(path.dirname(src), '..', path.basename(src).replace(/\.html$/, '.pdf'));
  const noFooter = out.replace(/\.pdf$/, '.cover.tmp.pdf');
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + src, { waitUntil: 'load' });
  await page.evaluate(() => document.fonts.ready);
  const base = { printBackground: true, preferCSSPageSize: true };
  await page.pdf({
    ...base, path: out, displayHeaderFooter: true,
    headerTemplate: '<span></span>',
    footerTemplate: `<div style="width:100%;font-family:Helvetica,Arial,sans-serif;font-size:7.5px;color:#6b7280;padding:0 8mm;display:flex;justify-content:space-between">
      <span><b style="color:#0B0D12">Outgrid</b> Labs · outgridlabs.com</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>`,
  });
  await page.pdf({ ...base, path: noFooter, pageRanges: '1' });
  await browser.close();
  // Swap in the footer-free cover.
  execFileSync('python3', ['-c', `
import sys
from pypdf import PdfReader, PdfWriter
out, cover = sys.argv[1], sys.argv[2]
r, c, w = PdfReader(out), PdfReader(cover), PdfWriter()
w.add_page(c.pages[0])
for p in r.pages[1:]: w.add_page(p)
w.write(out)
`, out, noFooter]);
  fs.unlinkSync(noFooter);
  console.log('built', path.relative(process.cwd(), out));
})();
