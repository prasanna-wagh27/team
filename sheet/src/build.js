// Builds the one-page sales sheet: a single tall, phone-width PDF page + a PNG preview.
// Usage: node build.js   (run from sheet/src)
const path = require('path');
const { chromium } = require('playwright');

(async () => {
  const src = path.join(__dirname, 'Outgrid_Sales_Sheet.html');
  const outPdf = path.join(__dirname, '..', 'Outgrid_Sales_Sheet.pdf');
  const outPng = path.join(__dirname, '..', 'Outgrid_Sales_Sheet.png');
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 416, height: 800 }, deviceScaleFactor: 2 });
  await page.goto('file://' + src, { waitUntil: 'load' });
  await page.evaluate(() => document.fonts.ready);
  const h = await page.evaluate(() => Math.ceil(document.body.getBoundingClientRect().height));
  await page.pdf({ path: outPdf, width: '110mm', height: `${h + 2}px`, printBackground: true, pageRanges: '1' });
  await page.screenshot({ path: outPng, fullPage: true });
  await browser.close();
  console.log('built sheet, height', h, 'px');
})();
