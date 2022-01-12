from playwright.sync_api import sync_playwright
def quit(page):
    page.query_selector('[class="no_separator"]').click()
    page.wait_for_selector('[class="bootstrap-dialog-button-icon glyphicon glyphicon-ok-sign"]').click()
def parse(bool):
    with sync_playwright() as p:
        login_ira = 'ПлискоИВ'
        login_lena = 'ПлискоЕВ'
        pw_ira = '3130312'
        pw_lena = '7221364'
        lg =''
        pw =''
        if(bool):
            lg = login_ira
            pw = pw_ira
        else:
            lg = login_lena
            pw = pw_lena
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://sgo.tomedu.ru")
        page.wait_for_timeout(2000)
        seelect_school = page.query_selector('[id="schools"]')
        seelect_school.select_option(label = "МБОУ Академический лицей им. Г.А.Псахье")#jepa выбираем учреждение
        login = page.query_selector('[name="UN"]')
        login.fill(lg)
        password = page.query_selector('[name="PW"]')
        password.fill(pw)
        enter = page.query_selector('[class="button-login-title"]')
        enter.click()
        page.wait_for_url('https://sgo.tomedu.ru/asp/SecurityWarning.asp')
        if(page.url =='https://sgo.tomedu.ru/asp/SecurityWarning.asp'):
            contin =page.query_selector('[title="Продолжить"]')
            contin.click()
            page.wait_for_url('https://sgo.tomedu.ru/angular/school/main/')
        else:
            page.wait_for_url('https://sgo.tomedu.ru/angular/school/main/')
        page.wait_for_selector('[id="11"]').click()
        page.wait_for_url('https://sgo.tomedu.ru/angular/school/reports/studenttotal')
        page.wait_for_selector('[title="Сформировать"]').click()
        #page.wait_for_selector('[title="Экспорт"]').click()                          #не работает скачивание файла пока(
        #page.wait_for_selector('[class="bootstrap-dialog-button-icon glyphicon glyphicon-ok-sign"]').click()
        lessons= []
        temp = page.wait_for_selector('[class="cell-text"]')
        sheet = page.query_selector_all('[class="cell-text"]')
        for i in sheet:
            lessons.append(i.inner_text())
        sheet = page.query_selector_all('[class="cell-num"]')
        marks =[]
        for i in sheet:
            marks.append(i.inner_text())
        ans =[]
        for i in range(0,len(lessons)*2,2):
            ans.append(lessons[i//2])
            ans.append(marks[i//2])
        quit(page)
        browser.close()
        return ans        