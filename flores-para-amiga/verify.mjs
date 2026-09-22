import { readFileSync, existsSync } from 'node:fs';
import { resolve, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
const root=resolve(dirname(fileURLToPath(import.meta.url)),'dist');
const files=['index.html','css/style.css','js/main.js'];
const missing=[];
let checked=0;
for(const file of files){
  const source=readFileSync(resolve(root,file),'utf8');
  const patterns=file.endsWith('.css') ? [/url\(['"]?([^)'"\s]+)['"]?\)/g] : [/(?:src|href)=["']([^"']+)["']/g, /['"](assets\/[^'"\s]+\.(?:webp|wav|svg))['"]/g];
  for(const pattern of patterns)for(const match of source.matchAll(pattern)){
    const ref=match[1];
    if(ref.startsWith('#')||ref.startsWith('%23')||ref.startsWith('data:')||ref.startsWith('http')||ref.includes('${'))continue;
    checked++;
    if(!existsSync(resolve(dirname(resolve(root,file)),file.endsWith('.css')?ref:ref.startsWith('assets/')&&file.endsWith('.js')?'../'+ref:ref)))missing.push(`${file}: ${ref}`);
  }
}
if(missing.length){console.error(missing);process.exit(1);}
console.log(`OK: ${checked} referencias locales, sin rutas ausentes.`);
