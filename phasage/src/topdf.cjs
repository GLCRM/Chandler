const { chromium } = require('/opt/node22/lib/node_modules/playwright');
(async () => {
  const [,, inPath, outPath] = process.argv;
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + inPath, { waitUntil: 'load' });
    await page.waitForTimeout(500);
  await page.pdf({ path: outPath, preferCSSPageSize: true, printBackground: true });
  await browser.close();
  console.log('ok', outPath);
})().catch(e => { console.error(e); process.exit(1); });
