// Builds a branded, phone-sized proposal PDF.
// Usage: node build.js <file.html>   -> ../<file>.pdf
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

(async () => {
  const src = path.resolve(process.argv[2]);
  const out = path.join(path.dirname(src), '..', path.basename(src).replace(/\.html$/, '.pdf'));
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + src, { waitUntil: 'load' });
  await page.evaluate(() => document.fonts.ready);
  await page.pdf({
    path: out, printBackground: true, preferCSSPageSize: true, displayHeaderFooter: true,
    headerTemplate: '<span></span>',
    footerTemplate: `<div style="width:100%;font-family:Inter,Helvetica,Arial,sans-serif;font-size:7.5px;color:#6b7280;padding:0 8mm;display:flex;justify-content:space-between">
      <span><b style="color:#0B0D12">Outgrid</b> Labs · outgridlabs.com</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>`,
  });
  await browser.close();
  console.log('built', path.relative(process.cwd(), out));
})();
