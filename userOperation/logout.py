# -*- encoding: utf-8 -*-
from random import uniform
from time import sleep


def logout(browser):
    browser.get('https://www.xuexi.cn/')
    sleep(round(uniform(1, 2), 2))
    logoutBtn = browser.find_element_by_xpath('//*[@id="root"]/div/header/div[2]/div[2]/span/a')
    logoutBtn.click()
