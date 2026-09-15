// Impression HTML -> PDF (Chromium via Playwright) + rapport des débordements de boîtes.
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
(async () => {
  const [,, inPath, outPath, reportPath] = process.argv;
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + inPath, { waitUntil: 'load' });
  await page.waitForTimeout(500);
  const report = await page.evaluate(() => {
    const out = [];
    document.querySelectorAll('.planche').forEach((pl, pi) => {
      pl.querySelectorAll('.box, .cap, .hdr, .ftr, .seq, table.t').forEach(el => {
        const dh = el.scrollHeight - el.clientHeight, dw = el.scrollWidth - el.clientWidth;
        if (dh > 1 || dw > 1) out.push({ planche: pi + 1, type: 'debordement', cls: el.className, id: el.id || '', title: (el.querySelector('.bt') || {}).textContent || el.textContent.slice(0, 50), dh, dw });
      });
      // chevauchements : pied de page contre les boîtes ; légendes (.cap) contre les boîtes et le plan ; boîtes entre elles
      const P = pl.getBoundingClientRect();
      const rect = el => { const r = el.getBoundingClientRect(); return { l: r.left - P.left, t: r.top - P.top, r: r.right - P.left, b: r.bottom - P.top }; };
      const items = [...pl.querySelectorAll('.box, .cap, .plan, .ftr, .hdr')].map(el => ({ el, r: rect(el), name: (el.className.split(' ')[0]) + ':' + (el.id || (el.querySelector('.bt') || {}).textContent || el.textContent.slice(0, 40)) }));
      for (let i = 0; i < items.length; i++) for (let j = i + 1; j < items.length; j++) {
        const A = items[i].r, B = items[j].r;
        const ox = Math.min(A.r, B.r) - Math.max(A.l, B.l), oy = Math.min(A.b, B.b) - Math.max(A.t, B.t);
        if (ox > 1 && oy > 1) out.push({ planche: pi + 1, type: 'chevauchement', a: items[i].name, b: items[j].name, ox: Math.round(ox), oy: Math.round(oy) });
      }
    });
    return out;
  });
  require('fs').writeFileSync(reportPath || '/dev/null', JSON.stringify(report, null, 1));
  await page.pdf({ path: outPath, preferCSSPageSize: true, printBackground: true });
  await browser.close();
  console.log('ok', outPath, 'débordements :', report.length);
})().catch(e => { console.error(e); process.exit(1); });
