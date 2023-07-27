from playwright.sync_api import Playwright, sync_playwright

import time

def run(playwright: Playwright) -> None:
    
    try:
        pagina_base = 'https://stellar.mlsmatrix.com/Matrix/Default.aspx?c=AAEAAAD*****AQAAAAAAAAARAQAAAEQAAAAGAgAAAAQ2MDcwDUAGAwAAAAUGwqJpHg0CCw))&f='
        #Creacion del contexto de la pag web
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        # MarHusKim1!
        #entrando a la pagina web
        #wait_until ='networkidle'
        page.goto(pagina_base, wait_until ='networkidle')

        #page.click('#loginId')

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
        #page.click('#btn-login')



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
        time.sleep(2)

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
        print('listo para enviar')
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
        time.sleep(3)
        context.close()
        browser.close()
        
    except Exception as e:
        print('fallo -> '+str(e))
            
with sync_playwright() as playwright:
    run(playwright)