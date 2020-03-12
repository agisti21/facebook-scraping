from selenium import webdriver
import time
from getlink import link
import pymysql.cursors

db = pymysql.connect("localhost", "root", "", "scraping")
cur = db.cursor()

browser = webdriver.Chrome()
browser.get("https://m.facebook.com/")

browser.find_element_by_name('email').send_keys('agistisetiawan@gmail.com')
browser.find_element_by_name('pass').send_keys('085624557007')
browser.find_element_by_name('login').click()

time.sleep(2)
url = "https://m.facebook.com/detikcom/"
browser.get(url)
browser.execute_script("window.open('');")
lin = link()
hasil = []

for l in lin:
    time.sleep(2)
    browser.switch_to.window(browser.window_handles[1])
    browser.get(l)

    deskripsi = (
    [symbol.text for symbol in browser.find_elements_by_xpath('//*[@id="u_0_s"]/div[1]/div[1]/p[1]') if symbol.text])
    print("Deskripsi :", deskripsi)
    deskripsi = deskripsi[0] if len(deskripsi) > 0 else ""

    suka = ([symbol.text for symbol in browser.find_elements_by_class_name('_1g06') if symbol.text])
    print("Like :", suka)
    suka = suka[0] if len(suka) > 0 else ""

    komen = ([symbol.text for symbol in browser.find_elements_by_class_name('_333v') if symbol.text])
    print("Komentar :", komen)
    komen = komen[0] if len(komen) > 0 else ""

    url = ([l])
    print("Link : ", url)
    url = url[0] if len(url) > 0 else ""

    cur.execute("INSERT INTO fb (desk,suka,komen,url) VALUES (%s,%s,%s,%s)", (deskripsi, suka, komen, url))
    cur.connection.commit()