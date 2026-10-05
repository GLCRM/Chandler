// Impression HTML -> PDF lettre portrait, avec numéro de page en pied (Chromium via Playwright).
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
(async () => {
  const [,, entree, sortie] = process.argv;
  const navigateur = await chromium.launch();
  const page = await navigateur.newPage();
  await page.goto('file://' + entree, { waitUntil: 'load' });
  await page.pdf({
    path: sortie, format: 'Letter', printBackground: true,
    margin: { top: '20mm', bottom: '20mm', left: '22mm', right: '22mm' },
    displayHeaderFooter: true,
    headerTemplate: '<span></span>',
    footerTemplate: '<div style="width:100%;font-family:Liberation Sans,Arial,sans-serif;font-size:8.5pt;color:#555;padding:0 22mm;display:flex;justify-content:space-between">'
      + '<span>Hôpital de Chandler — R-657-24 · rapports d\'analyse, version lisible · document de travail</span>'
      + '<span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>',
  });
  await navigateur.close();
  console.log('ok', sortie);
})().catch(e => { console.error(e); process.exit(1); });
