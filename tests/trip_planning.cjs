const fs=require('node:fs'), vm=require('node:vm'), assert=require('node:assert/strict');
const path=require('node:path');
const root=process.argv[2]||path.resolve(__dirname,'..');
const html=fs.readFileSync(path.join(root,'src/hang_or_stake.html'),'utf8');
new vm.Script(html.match(/<script>\s*([\s\S]*?)<\/script>/)[1]);
const context=vm.createContext({console,URL,Intl,Date,Map,AbortController,setTimeout,clearTimeout});
const data=html.slice(html.indexOf('const SITES='),html.indexOf('const PARKS='));
// Evaluate only the literal site table, not unrelated page initialization.
vm.runInContext(data,context);
vm.runInContext('const PARK_LOCATIONS='+fs.readFileSync(path.join(root,'data/park_locations.json'),'utf8')+';function esc(v){return String(v).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/"/g,"&quot;");}',context);
vm.runInContext(html.slice(html.indexOf('// Forecast and booking helpers.'),html.indexOf('function detail(s){')),context);
assert.equal(vm.runInContext('SITES.every(s=>BOOKING[s[0]] && planningPanel(s).includes("7-day forecast"))',context),true);
assert.match(vm.runInContext('planningPanel(["Lake Maria","B1"])',context),/Check B1 closure/);
assert.match(vm.runInContext('planningPanel(["MN Valley SRA","historical"])',context),/not confirmed open/);
const now=Date.now();
context.sample={properties:{updateTime:new Date(now).toISOString(),periods:[{name:'Tonight',endTime:new Date(now+3600000).toISOString(),temperature:0,temperatureUnit:'F',shortForecast:'<script>bad</script>',probabilityOfPrecipitation:{value:null}}]}};
const result=vm.runInContext('forecastHTML(sample)',context);
assert.match(result,/0°F/);assert.match(result,/Precipitation unknown/);assert.ok(!result.includes('<script>'));
context.sample.properties.updateTime=new Date(now-172800000).toISOString();
assert.throws(()=>vm.runInContext('forecastHTML(sample)',context),/stale/);
context.sample.properties.updateTime=new Date(now).toISOString();context.sample.properties.periods=[];
assert.throws(()=>vm.runInContext('forecastHTML(sample)',context),/stale/);
console.log('Passed: every campsite has booking/weather, closures, zero temperatures, missing precipitation, escaping, stale and empty forecasts.');

// A rejected network request must retain a retry path and release its loading guard.
context.fetch=async()=>{throw Error('offline');};
context.box={textContent:''};
context.panel={dataset:{lat:'45.317411',lon:'-93.931667'},querySelector:()=>context.box};
vm.runInContext('loadForecast(panel)',context).then(()=>{
 assert.match(context.box.textContent,/Forecast unavailable/);
 assert.equal(context.panel.dataset.loading,undefined);
 console.log('Passed: offline forecast fallback and retry guard.');
});
