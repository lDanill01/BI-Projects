const fs = require('fs');
const assert = require('assert');

const html = fs.readFileSync(__dirname + '/index.html', 'utf8');

assert.match(html, /cdn\.jsdelivr\.net\/npm\/chart\.js@4\.4\.7\/dist\/chart\.umd\.min\.js/);
assert.match(html, /new Chart\(/);
assert.strictEqual((html.match(/function lineChart\s*\(/g) || []).length, 1);
assert.strictEqual((html.match(/function horizontal\s*\(/g) || []).length, 1);
assert.match(html, /maintainAspectRatio:\s*false/);

console.log('Dashboard Chart.js: verificações estruturais aprovadas.');
