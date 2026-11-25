"""Pruebas por ID de aceptación. No ejecuta Gherkin como intérprete.
Instalar requirements-tests.txt y ejecutar playwright install chromium.
"""
from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib, http.server, json, math, os, platform, shutil, subprocess, threading, time, traceback
from functools import partial

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'evidencias'/'ejecucion_actual'
OUT.mkdir(parents=True,exist_ok=True)
rows=[]
def result(case,status,environment,observed,evidence=''):
    rows.append(dict(caso=case,estado=status,entorno=environment,observado=observed,evidencia=evidence))
def run(case,env,fn):
    try:fn();result(case,'APROBADO',env,'Se cumplieron las aserciones de la prueba automatizada.')
    except Exception as e:result(case,'FALLIDO',env,str(e));print(case,env,traceback.format_exc())
def ensure(value,message='No se cumplió la comprobación'):
    if not value:raise AssertionError(message)

class Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self,*args):pass
server=http.server.ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(ROOT/'docs')))
threading.Thread(target=server.serve_forever,daemon=True).start()
url=f'http://127.0.0.1:{server.server_port}/index.html'
environment={'fecha_academica':'2026-11-25','timestamp_sistema_utc':datetime.now(timezone.utc).isoformat(),'sistema':platform.platform(),'python':platform.python_version(),'version_mvp':'1.0.1-mvp','servidor':'HTTP local por loopback; sin red externa','cache':'Recursos estáticos precargados; interacciones en memoria; sin limitación artificial de CPU o red','operador':'Ejecución técnica automatizada asistida; no participación atribuida a un estudiante'}

node=os.environ.get('CODEX_PRIMARY_RUNTIME_NODE') or shutil.which('node')
if node:
    proc=subprocess.run([node,'--test',str(ROOT/'tests/model.test.cjs')],capture_output=True,text=True)
    (OUT/'unitarias.txt').write_text(proc.stdout+proc.stderr)
    environment['unitarias_exit_code']=proc.returncode
else:environment['unitarias_exit_code']='Node no instalado'

def suite(page,env):
    def fresh():
        page.goto(url);page.evaluate('window.prisma.reset()')
    def filters(theme='océanos',approach='científico'):
        page.locator('#open-selector').click();page.locator('#theme').select_option(theme);page.locator('#approach').select_option(approach);page.get_by_role('button',name='Aplicar filtros',exact=True).click()
    def ids():return page.locator('#results article').evaluate_all('(xs)=>xs.map(x=>x.dataset.id)')
    def route(name):page.locator(f'header button[data-route="{name}"]').click()
    def account(a):page.locator('#account').select_option(a);route('subscription')
    def view_amount():return page.locator('#plan-amount').inner_text()
    def confirm():page.locator('#confirm-action').click()
    def case_01():
        fresh();filters();ensure(ids()==['D01'],str(ids()))
    def case_02():
        fresh();page.locator('#explore-all').click();ensure(ids()==['D01','D02','D03','D05']);page.locator('[data-title="D01"]').click();ensure(page.locator('#detail').is_visible())
    def case_03():
        fresh();page.locator('[data-title="D01"]').click();t=page.locator('#detail').inner_text();ensure(all(v in t for v in ['océanos','científico','Estudio de ecosistemas marinos','Ficha editorial sintética D01']))
    def case_04():
        fresh();page.locator('[data-title="D05"]').click();ensure(page.locator('#detail-approach').inner_text()=='Enfoque no disponible')
    def case_05():
        fresh();filters('océanos','histórico');ensure(ids()==[]);ensure(page.locator('#status').inner_text()=='No encontramos coincidencias');ensure(page.locator('#modify-filters').is_visible())
    def case_06():
        fresh();filters('océanos','histórico');page.locator('#remove-approach').click();ensure(ids()==['D01','D02']);ensure(page.locator('#active-filters').inner_text()=='océanos')
    def case_07():
        fresh();page.locator('[data-title="D01"]').click();ensure(page.locator('#detail').is_visible());ensure(not page.locator('#selector').is_visible())
    def case_08():
        fresh();page.locator('#open-selector').click();page.locator('#theme').select_option('océanos');page.locator('#close-selector').click();s=page.evaluate('window.prisma.snapshot()');ensure(not s['filters']['theme'] and not s['prefs']);ensure(ids()==['D01','D02','D03','D05'])
    def case_09():
        fresh();account('C01');ensure(page.locator('#plan-name').inner_text()=='Plan prueba A');ensure(page.locator('#plan-limit').inner_text()=='2')
    def case_10():
        fresh();account('C04');ensure(page.locator('#plan-limit').inner_text()=='Límite no disponible')
    def case_11():
        fresh();account('C01');ensure(view_amount()=='29.90');ensure(page.locator('#plan-currency').inner_text()=='PEN');ensure('Datos sintéticos' in page.locator('#subscription').inner_text())
    def case_12():
        fresh();route('subscription');before=page.evaluate('window.prisma.snapshot().account');page.locator('#manage-subscription').click();ensure(page.locator('#management').is_visible());ensure(before==page.evaluate('window.prisma.snapshot().account'))
    def case_13(code,amount,currency,limit):
        fresh();account(code);ensure(view_amount()==amount);ensure(page.locator('#plan-currency').inner_text()==currency);ensure(page.locator('#plan-limit').inner_text()==limit)
    def case_14():
        fresh();account('C01');ensure(view_amount()=='29.90');account('C04');ensure(view_amount()=='No disponible')
    def case_15(save):
        fresh();filters('océanos','');route('preferences');page.locator('#save-preference').click()
        if save:confirm()
        else:page.locator('#cancel-action').click()
        text=page.locator('#saved-preference').inner_text();ensure(('océanos' in text)==save)
        page.reload();route('preferences');ensure(('océanos' in page.locator('#saved-preference').inner_text())==save)
    def case_16():
        fresh();filters('océanos','');route('preferences');page.locator('#save-preference').click();confirm();page.locator('#delete-preference').click();confirm();route('catalog');ensure(ids()==['D01','D02','D03','D05']);route('preferences');ensure(page.locator('#saved-preference').inner_text()=='No tienes preferencias guardadas')
    def case_17():
        fresh()
        def tab_to(selector):
            target=page.locator(selector)
            for _ in range(60):
                if target.evaluate('(e)=>e===document.activeElement'):return
                page.keyboard.press('Tab')
            raise AssertionError('No se pudo alcanzar con Tab: '+selector)
        tab_to('#open-selector');page.keyboard.press('Enter');ensure(page.locator('#selector').is_visible())
        ensure(page.locator('#theme').evaluate('(e)=>e===document.activeElement'),'El diálogo debe enfocar el primer campo')
        page.keyboard.press('ArrowDown');page.keyboard.press('Tab');ensure(page.locator('#approach').evaluate('(e)=>e===document.activeElement'))
        page.keyboard.press('ArrowDown');page.keyboard.press('Tab');page.keyboard.press('Enter');page.wait_for_timeout(50)
        ensure(not page.locator('#selector').is_visible());ensure(page.locator('#open-selector').evaluate('(e)=>e===document.activeElement'))
        ensure(ids()==['D01'])
        tab_to('[data-title="D01"]');ensure(page.locator('[data-title="D01"]').evaluate('(e)=>getComputedStyle(e).outlineWidth')=='3px')
        page.keyboard.press('Enter');ensure(page.locator('#detail').is_visible())
        tab_to('#detail [data-route="catalog"]');page.keyboard.press('Enter');ensure(page.locator('#catalog').is_visible())
        tab_to('header button[data-route="subscription"]');page.keyboard.press('Enter');ensure(page.locator('#subscription').is_visible())
        tab_to('header button[data-route="balance"]');page.keyboard.press('Enter');ensure(page.locator('#balance').is_visible())
    def case_21():
        fresh();route('balance');ensure('D01' in page.locator('#seen-list').inner_text());ensure('D02' in page.locator('#pending-list').inner_text());ensure('D02' not in page.locator('#seen-list').inner_text())
    def case_22():
        fresh();route('balance');page.locator('#clear-pending').click();confirm();ensure(page.locator('#pending-list').inner_text()=='No hay títulos en esta categoría');page.locator('#balance [data-route="catalog"]').click();ensure(page.locator('#catalog').is_visible())
    cases=[('AT01',case_01),('AT02',case_02),('AT03',case_03),('AT04',case_04),('AT05',case_05),('AT06',case_06),('AT07',case_07),('AT08',case_08),('AT09',case_09),('AT10',case_10),('AT11',case_11),('AT12',case_12),('AT13-C01',lambda:case_13('C01','29.90','PEN','2')),('AT13-C02',lambda:case_13('C02','45.90','PEN','4')),('AT13-C03',lambda:case_13('C03','9.90','USD','1')),('AT14',case_14),('AT15-confirmar',lambda:case_15(True)),('AT15-cancelar',lambda:case_15(False)),('AT16',case_16),('AT17',case_17),('AT21',case_21),('AT22',case_22)]
    for case,fn in cases:run(case,env,fn)
    fresh();page.screenshot(path=str(OUT/f'catalogo-{env}.png'),full_page=True)
    if env=='escritorio':
        case_03();page.screenshot(path=str(OUT/'ficha-D01.png'),full_page=True)
        case_05();page.screenshot(path=str(OUT/'sin-coincidencias.png'),full_page=True)
        account('C04');page.screenshot(path=str(OUT/'plan-sin-datos.png'),full_page=True)
        fresh();account('C01');page.screenshot(path=str(OUT/'suscripcion-C01.png'),full_page=True)
        fresh();route('balance');page.screenshot(path=str(OUT/'balance.png'),full_page=True)

browser_error=None
try:
    from playwright.sync_api import sync_playwright
    with sync_playwright() as pw:
        options={'headless':True}
        if os.environ.get('PRISMA_BROWSER'):options['executable_path']=os.environ['PRISMA_BROWSER']
        browser=pw.chromium.launch(**options)
        environment['navegador']='Chromium '+browser.version
        for env,size in [('escritorio',{'width':1365,'height':900}),('movil-emulado',{'width':390,'height':844})]:
            ctx=browser.new_context(viewport=size,reduced_motion='reduce');page=ctx.new_page();suite(page,env)
            ensure(page.evaluate('document.documentElement.scrollWidth<=window.innerWidth'),'Desbordamiento horizontal')
            ctx.close()
        ctx=browser.new_context(viewport={'width':1365,'height':900});page=ctx.new_page();page.goto(url);page.evaluate('window.prisma.reset()')
        snapshot=page.locator('body').aria_snapshot();(OUT/'estructura-accesible.txt').write_text(snapshot)
        live=page.locator('#status').get_attribute('aria-live')=='polite'
        result('AT18','PARCIAL','estructura DOM/árbol accesible','Etiquetas semánticas y región viva presentes: '+str(live)+'. No se ha ejecutado un lector de pantalla real.','estructura-accesible.txt')
        samples=[]
        for route in ['resultados','ficha']:
            action="window.prisma.applyFilters({theme:'océanos',approach:'científico'})" if route=='resultados' else "window.prisma.openTitle('D01')"
            for n in range(105):
                measurement=page.evaluate('async()=>{const start=performance.now();let error=null;try{await '+action+';}catch(e){error=String(e);}return {ms:performance.now()-start,error};}')
                if n>=5:samples.append({'ruta':route,'muestra':n-4,**measurement})
        with (OUT/'rendimiento.csv').open('w',newline='') as f:
            w=csv.DictWriter(f,fieldnames=['ruta','muestra','ms','error']);w.writeheader();w.writerows(samples)
        perf={}
        for route in ['resultados','ficha']:
            subset=[s for s in samples if s['ruta']==route];valid=sorted(s['ms'] for s in subset if not s['error'])
            perf[route]={'muestras':len(subset),'errores':sum(bool(s['error']) for s in subset),'p95_ms':valid[math.ceil(.95*len(valid))-1] if valid else None,'min_ms':min(valid) if valid else None,'max_ms':max(valid) if valid else None}
        environment['rendimiento']=perf
        result('AT19','APROBADO' if all(v['muestras']==100 and not v['errores'] for v in perf.values()) else 'FALLIDO','HTTP local escritorio',json.dumps(perf,ensure_ascii=False),'rendimiento.csv')
        baseline_path=ROOT/'evidencias/linea_base/entorno.json'
        baseline=json.loads(baseline_path.read_text()) if baseline_path.exists() else None
        target_ok=baseline is not None and all(v['p95_ms'] is not None and v['p95_ms']<=2000 and not v['errores'] for v in perf.values())
        comparison={'meta_tecnica_provisional_ms':2000,'version_base':baseline.get('version_mvp') if baseline else None,'version_actual':environment['version_mvp'],'base':baseline.get('rendimiento') if baseline else None,'actual':perf,'ajuste':'Evitar reemplazar el DOM de resultados cuando su contenido no cambió; preservar los nodos y el foco.','alcance':'Meta adoptada para el MVP; no es un SLA comercial ni aprobación documentada del equipo. No se afirma mejora estadística a partir de dos series.'}
        (OUT/'comparacion-rendimiento.json').write_text(json.dumps(comparison,ensure_ascii=False,indent=2))
        result('AT20','APROBADO' if target_ok else 'BLOQUEADO','HTTP local escritorio',json.dumps(comparison,ensure_ascii=False),'comparacion-rendimiento.json')
        ctx.close();browser.close()
except Exception as e:
    browser_error=str(e);environment['error_navegador']=browser_error
    for n in range(1,23):
        if not any(r['caso'].split('-')[0]==f'AT{n:02}' for r in rows):result(f'AT{n:02}','BLOQUEADO','entorno local','No se pudo iniciar el navegador de pruebas. Consultar entorno.json y repetir en GitHub Actions.')
finally:server.shutdown()
environment['sha256_archivos']={str(f.relative_to(ROOT)):hashlib.sha256(f.read_bytes()).hexdigest() for f in sorted((ROOT/'docs').glob('*')) if f.is_file()}
(OUT/'entorno.json').write_text(json.dumps(environment,ensure_ascii=False,indent=2))
(OUT/'resultados.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2))
with (OUT/'resultados.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['caso','estado','entorno','observado','evidencia']);w.writeheader();w.writerows(rows)
print(json.dumps({'registros':len(rows),'estados':{s:sum(r['estado']==s for r in rows) for s in set(r['estado'] for r in rows)},'navegador':environment.get('navegador'),'error_navegador':browser_error},ensure_ascii=False))
if browser_error or any(r['estado']=='FALLIDO' for r in rows):raise SystemExit(1)
