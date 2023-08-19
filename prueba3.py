import os
#m_wm_w5_m_dl_ctrl2_lnkRun
#m_wm_w5_m_dl_ctrl1_lnkRun
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

SPREADSHEET_ID ="10E8p8wXZl85mzL5q2yb62m4TAjJq1iXSTa3l9PC1zqw"

def main_api():
    credenciales =None
    if os.path.exists("token.json"):
        credenciales = Credentials.from_authorized_user_file("token.json",SCOPES)
    if not credenciales or not credenciales.valid:
        if credenciales and credenciales.expired and credenciales.refresh_token:
            credenciales.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credenciales.json",SCOPES)
            credenciales = flow.run_local_server(port=0)
        with open("token.json","w") as token:
            token.write(credenciales.to_json())
    try:
        service = build("sheets","v4", credentials=credenciales)
        sheets = service.spreadsheets()
    except HttpError as e:
        print("error: ",e)

from playwright.sync_api import Playwright, sync_playwright,expect

import time





def run(playwright: Playwright) -> None:
    
    try:
        pagina_base = 'https://stellar.mlsmatrix.com/Matrix/MyMatrix/MyListings'
        #Creacion del contexto de la pag web
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        # MarHusKim1!
        #entrando a la pagina web
        #wait_until ='networkidle'
        page.goto(pagina_base, wait_until ='networkidle')
        print('entro a la pagina web')
        #page.click('#loginId')
        print('ingresando las credenciales')
        page.get_by_label("MLS ID/NRDS ID Number:").click()
        page.get_by_label("MLS ID/NRDS ID Number:").fill("272562015")
        page.get_by_label("Password").click()
        page.get_by_label("Password").fill("MarleyHuskyKim1972!")
        #page.get_by_role("button", name="Sign In").click()
        #page.fill('#loginId','272562015')
        #page.fill('#password','MarHusKim1!')
        print('lleno los datos')
        page.click('body > div > div > div.row-container > div.auth-container__section')
        
        page.click('#btn-login')
        #page.click('#btn-login') # Opens a new tab
        print('presiono el boton')

        page.wait_for_load_state('networkidle', timeout=60000)
        page.wait_for_url("https://central.stellarmls.com/pages/home-30", timeout=60000)
        page.goto("https://central.stellarmls.com/pages/home-30", wait_until= 'load')
        print('entro a la pagina')

        page.goto("https://stellar.mlsmatrix.com/Matrix/MyMatrix/MyListings",timeout=60000)
        print('entro directo')
        
        #page.wait_for_load_state('networkidle')
        page.get_by_role("link", name=" Home").click()
        page.wait_for_url("https://central.stellarmls.com/pages/home-30")
        page.get_by_role("link", name=" Products & Services").click()
        page.wait_for_url("https://central.stellarmls.com/pages/products-services-31")
        print('entro a la pagina recursos')
        time.sleep(2)

        with page.expect_popup() as popup_info:
            page.get_by_role("link", name="Matrix™ MLS system").click()
        #pagina de los contactos
        page1 = popup_info.value
        print('** entro para seleccionar los links **')
        
        time.sleep(2)
        #añadir locator al botones de regresar en las apgiasn de enviar correo (cancel) y (return to my listenings)

        #m_ucDisplay_m_tdPagingSummary > b:nth-child(4)
        
        #m_ucDisplay_m_tdPagingSummary > b:nth-child(3) este es mas seguro
        page1.locator('#m_ucDisplay_m_tdPagingSummary > b:nth-child(3)')

        cantidad = page1.locator('#m_ucDisplay_m_tdPagingSummary > b:nth-child(3)').inner_text()
        int_cantidad = int(cantidad)
        reverse_prospect_lista = [0,1,2,3,4,5]

        #anotando los ML #
        # tr.DisplayAltRow:nth-child(x) > td:nth-child(10) > span:nth-child(1) > a:nth-child(1) , x es el que varia (1 - xx)
        matriz_indices = []
        
        for indice in range(1,int_cantidad+1):
            if indice % 2 != 0 or indice==1:    
                #para los impares
                elemento_locator = 'tr.DisplayRegRow:nth-child'
            else:
                # tr.DisplayAltRow:nth-child
                #para los pares
                elemento_locator = 'tr.DisplayAltRow:nth-child'
            ml=page1.locator(f'{elemento_locator}({indice}) > td:nth-child(10) > span:nth-child(1) > a:nth-child(1)').inner_text()
            matriz_indices.append(ml)

        for numero in range(1,int_cantidad+1):
            matriz_agentes = []
            print(numero)
            #page1.reload()
            #tr.DisplayAltRow:nth-child(x) > td:nth-child(1) > span:nth-child(1) > input:nth-child(2), x es el que varia (1 - xx)
            #page1.wait_for_selector(f'tr.DisplayRegRow:nth-child({numero}) > td:nth-child(1) > span:nth-child(1) > input:nth-child(2)')
            #if numero==1 or numero==3 or numero==5:#hacer para ver si el numero es impar
            if numero % 2 != 0 or numero==1:    
                #para los impares
                elemento_locator = 'tr.DisplayRegRow:nth-child'
            else:
                # tr.DisplayAltRow:nth-child
                #para los pares
                elemento_locator = 'tr.DisplayAltRow:nth-child'
            elemento = page1.locator(f'{elemento_locator}({numero}) > td:nth-child(1) > span:nth-child(1) > input:nth-child(2)')
            print(f'¿El elemento está habilitado?: {elemento.is_enabled()}')
            print(f'¿El elemento está visible?: {elemento.is_visible()}')

            page1.wait_for_selector(f'{elemento_locator}({numero}) > td:nth-child(1) > span:nth-child(1) > input:nth-child(2)',state='attached')
            print('se espero al check')
            #expect(page1.locator(f'tr.DisplayRegRow:nth-child({numero}) > td:nth-child(1) > span:nth-child(1) > input:nth-child(2)')).to_be_visible()

            page1.locator(f'{elemento_locator}({numero}) > td:nth-child(1) > span:nth-child(1) > input:nth-child(2)').click()
            #page1.get_by_role('checkbox',name='CHB_697519542').check()
            print('presiono el check')

            page1.locator('.icon_agent').click()
            print('presiono Reverse prospect')
            #page1.locator(f'tr.DisplayAltRow:nth-child(1) > td:nth-child(10) > span:nth-child(1) > a:nth-child(1)')
            #print('detecto la fila ',1)
            #page1.locator(f'tr.DisplayAltRow:nth-child(1) > td:nth-child(10) > span:nth-child(1) > a:nth-child(1)').click()
            #print('detecto el link')
            time.sleep(2)
            #m_extraColumns_ctlxx_lbEmail, donde xx es del rango [00,99]
            for lista_prospect in reverse_prospect_lista:
                print(lista_prospect)
                #m_extraColumns_ctl00_lbEmail
                agente = page1.locator(f'#m_extraColumns_ctl0{lista_prospect}_lbEmail').inner_text()
                matriz_agentes.append(agente)

                #telefono
                #tr.DisplayRegRow:nth-child(x) > td:nth-child(8) > div:nth-child(1) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(3) > span:nth-child(1)
                #x va de [2;infinito]
                #impares > DisplayAltRow // pares > DisplayRegRow

                #para ubicar los marcados con corazon
                '''try:
                    print('entrando al try de buscar los corazones')
                    page1.locator(f'tr.DisplayAltRow:nth-child({lista_prospect+2}) > td:nth-child(7) > span:nth-child(1)')
                    print('ubico el corazon')
                except:
                    print('entrando al except de buscar los corazones')
                    page1.locator(f'tr.DisplayRegRow:nth-child({lista_prospect+2}) > td:nth-child(7) > span:nth-child(1)')
                    print('no tiene corazon')'''
                # tr.DisplayAltRow:nth-child(x) > td:nth-child(7) > span:nth-child(1), donde x va de [2,xx]
                #en caso no hay corazon
                # tr.DisplayRegRow:nth-child(x) > td:nth-child(7) > span:nth-child(1), donde x va de [2,xx]
                page1.locator(f'#m_extraColumns_ctl0{lista_prospect}_lbEmail').click()
                print('ingreso a la persona para mandar correo')

                #lista de nombres en el reverse prospect
                #m_extraColumns_ctl00_lbEmail
                #m_extraColumns_ctl01_lbEmail
                
                page1.locator('.icon_emailSend')
                print('listo para enviar')
                #page1.locator('.icon_emailSend').click()

                page1.locator('#m_lbCancel > span:nth-child(1)')
                print('ubico el boton de cancelar')
                page1.locator('#m_lbCancel > span:nth-child(1)').click()
                #m_lbCancel > span:nth-child(1)
                print('regreso a la lista de Prospect reverse')
            print('lista de agentes guardados ',matriz_agentes)
            page1.locator('.linkIcon')
            print('ubico el boton para regresar a la lista de listenings')
            page1.locator('.linkIcon').click()
            print('regreso a la lista de Listenings')

            #para desmcarcar el check
            page1.wait_for_selector(f'{elemento_locator}({numero}) > td:nth-child(1) > span:nth-child(1) > input:nth-child(2)')
            print('se espero al check')

            # tr.j-DisplayCore-item:nth-child(x) > td:nth-child(1) > span:nth-child(1) > input:nth-child(2), donde x es el que varia
            page1.locator(f'tr.j-DisplayCore-item:nth-child({numero}) > td:nth-child(1) > span:nth-child(1) > input:nth-child(2)').click()
            #page1.get_by_role('checkbox',name='CHB_697519542').check()
            print('Desmarco el check')
            print('acabo el bucle N° ',numero)
            time.sleep(3)

        time.sleep(10)

        #tr.DisplayRegRow:nth-child(1) > td:nth-child(1) > span:nth-child(1) > input:nth-child(2)
        #tr.DisplayAltRow:nth-child(2) > td:nth-child(1) > span:nth-child(1) > input:nth-child(2)
        context.close()
        browser.close()

        #page.click('#btn-login')


        '''
        page.wait_for_load_state('networkidle', timeout=60000)
        page.wait_for_url("https://central.stellarmls.com/pages/home-30", timeout=60000)
        page.goto("https://central.stellarmls.com/pages/home-30", wait_until= 'load')
        print('entro a la pagina')

        page.goto("https://stellar.mlsmatrix.com/Matrix/MyMatrix/MyListings",timeout=60000)
        print('entro directo')
        
        #page.wait_for_load_state('networkidle')
        page.get_by_role("link", name=" Home").click()
        page.wait_for_url("https://central.stellarmls.com/pages/home-30")
        page.get_by_role("link", name=" Products & Services").click()
        page.wait_for_url("https://central.stellarmls.com/pages/products-services-31")
        print('entro a la pagina recursos')
        time.sleep(2)

        with page.expect_popup() as popup_info:
            page.get_by_role("link", name="Matrix™ MLS system").click()
        #pagina de los contactos
        page1 = popup_info.value
        print('****')
        page1.locator('#m_ucDisplay_m_pnlDisplay > table > thead > tr > th.Fixed.NoPrint.checkboxTableHeader > span > analyticscontainer > input[type=checkbox]').click()
        page1.locator("#m_ucDisplay_m_ucDisplayPicker_m_ddlPageSize").select_option("100")

        print('eligio mostrar 100')
        #selector = '#m_ucDisplay_m_tdPagingSummary > b:nth-child(4)'
        #page1.get_by_role("cell", name="My Listings (12)").click()
        #m_wm_w5_m_dl_ctrl0_lnkRun


        #cantidad = page1.locator("document.querySelector('#m_ucDisplay_m_tdPagingSummary > b:nth-child(4)')").inner_text
        #cantidad =page1.query_selector('#m_ucDisplay_m_tdPagingSummary > b:nth-child(4)').text_content
        #print(cantidad)

        #page1.locator('#m_ucDisplay_m_tdPagingSummary > b:nth-child(4)')

        #tr.DisplayRegRow:nth-child(1) > td:nth-child(1) > span:nth-child(1) > input:nth-child(2)
        time.sleep(2)
        page1.locator(f'tr.DisplayAltRow:nth-child(1) > td:nth-child(10) > span:nth-child(1) > a:nth-child(1)')
        print('detecto la fila ',1)
        page1.locator(f'tr.DisplayAltRow:nth-child(1) > td:nth-child(10) > span:nth-child(1) > a:nth-child(1)').click()
        print('detecto el link')
        time.sleep(2)
        #page1.locator("tr.DisplayRegRow:nth-child(1) > td:nth-child(1) > span:nth-child(1) > input:nth-child(2)")
        #print('ubico el check')
        #page1.locator("tr.DisplayRegRow:nth-child(1) > td:nth-child(1) > span:nth-child(1) > input:nth-child(2)").check()
        #page1.locator('input[name=\"CHB_697519542\"]').check()
        
        page1.get_by_role("link", name="Reverse Prospect").click()
        page1.get_by_role("link", name="Macson Petit-Jean").click()
        page1.locator("#m_tbxMessage_m_tbxMessage").click()
        page1.locator("#m_tbxMessage_m_tbxMessage").fill("hola mundo")
        page1.get_by_role("link", name="Send")
        time.sleep(2)'''

        '''i=1
        page1.locator(f'tr.DisplayAltRow:nth-child({i}) > td:nth-child(10) > span:nth-child(1) > a:nth-child(1)')
        print('detecto la fila ',i)
        page1.locator(f'tr.DisplayAltRow:nth-child({i}) > td:nth-child(10) > span:nth-child(1) > a:nth-child(1)').click()


        page1.locator('.icon_agent').click()
        j=1
        if(j<10):
            page1.locator(f'#m_extraColumns_ctl0{j}_lbEmail').click()
        else:
            page1.locator(f'#m_extraColumns_ctl{j}_lbEmail').click()
        page1.locator('.icon_emailSend')'''
        #print('listo para enviar')
        #page1.locator('.icon_emailSend').click()
        
        #m_extraColumns_ctl00_lbEmail
        #m_extraColumns_ctl01_lbEmail
        #m_extraColumns_ctl02_lbEmail

        #primer elemento
        #tr.DisplayAltRow:nth-child(2) > td:nth-child(10) > span:nth-child(1) > a:nth-child(1)
        #segundo elemento
        #tr.DisplayAltRow:nth-child(2) > td:nth-child(10) > span:nth-child(1) > a:nth-child(1)
        
        #tr.DisplayRegRow:nth-child(3) > td:nth-child(10) > span:nth-child(1) > a:nth-child(1)
        #tr.DisplayAltRow:nth-child(4) > td:nth-child(10) > span:nth-child(1) > a:nth-child(1)

        #seleccionar el numero de filas
        ##m_ucDisplay_m_tdPagingSummary > b:nth-child(4)

        '''
        page.wait_for_load_state('networkidle', timeout=60000)
        page.wait_for_url("https://stellar.mlsmatrix.com/Matrix/Default.aspx?c=AAEAAAD*****AQAAAAAAAAARAQAAAEQAAAAGAgAAAAQ1MzAyDUAGAwAAAAVzWMOGcw0CCw))&f=", timeout=60000)
        page.goto("https://stellar.mlsmatrix.com/Matrix/Default.aspx?c=AAEAAAD*****AQAAAAAAAAARAQAAAEQAAAAGAgAAAAQ1MzAyDUAGAwAAAAVzWMOGcw0CCw))&f=", wait_until='load')
        print('entro a la pagina del pop up')
        #para desaparecer el pop up
        page1.get_by_text("I've Read This").click()
        page1.get_by_text("I've Read This").click()
        page1.get_by_text("I've Read This").click()
        #para desaparecer el pop up'''

        '''page1.get_by_role("link", name="My Listings").click()
        page1.wait_for_url("https://stellar.mlsmatrix.com/Matrix/MyMatrix/MyListings")
        page1.locator(".col-xs-1").click()'''
        # ---------------------
        
        
    except Exception as e:
        print('fallo -> '+str(e))
            
with sync_playwright() as playwright:
    run(playwright)