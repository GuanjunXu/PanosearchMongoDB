# -*- coding: utf-8 -*-

from uiautomator import device as d
import time
import os

def launchPano():
    d.press('home')
    time.sleep(1)
    d.swipe(550, 1500, 450, 800, steps=15)

def exitPano():
    os.popen("adb shell am force-stop com.letv.android.quicksearchbox")

def launchSlideUp():
    launchPano()

def actSlideUp():
    launchPano()

def slideDownRefresh():
    d.swipe(700, 700, 700, 1500,steps=10)

def backspaceOnInputBox():
    searchbox = 'com.letv.android.quicksearchbox:id/search_src_text'
    d(resourceId = searchbox).click()
    d(resourceId = searchbox).set_text('a') # Input a
    time.sleep(1)
    d.press('delete') # Delete a

def launchHoldHomekey():
    longPressHome()

def actHoldHomeKey():
    d.press('home')
    longPressHome()
    # if d(resourceId = 'com.android.settings:id/step_next').exists() and d(resourceId = 'com.android.settings:id/step_last').exists():
    #     d(text = u'万象搜索').click()
    #     d.press('back')
    # longPressHome()

def clearInputBox():
    searchbox = 'com.letv.android.quicksearchbox:id/search_src_text'
    d(resourceId = searchbox).click()
    d(resourceId = searchbox).set_text('a') # Input a
    time.sleep(1)
    d(resourceId = 'com.letv.android.quicksearchbox:id/delete').click()

def backFromThirdApp():
    while d(text = u'院线热映').wait.gone(timeout = 3000):
        d.swipe(700, 1700, 700, 1000, steps = 30)
    d(resourceId='com.letv.android.quicksearchbox:id/image').click()
    time.sleep(2)
    d.press('back')

def backFromResult():
    searchbox = 'com.letv.android.quicksearchbox:id/search_src_text'
    d(resourceId = searchbox).click()
    d(resourceId = searchbox).set_text('a') # Input a
    time.sleep(1)
    d.press('back')

def backFromEditsWidget():
    while d(text = u'编辑我的订阅').wait.gone(timeout = 3000):
        d.swipe(700, 1700, 700, 1000, steps = 30)
    d(text = u'编辑我的订阅').click()
    d.press('back')

# def backFromAllWidget():
#     while d(text = u'展开全部订阅').wait.gone(timeout = 3000):
#         d.swipe(700, 1700, 700, 1000, steps = 30)
#     d(text = u'展开全部订阅').click()
#     d.press('back')

def unlockScreen():
    d.press('power')
    time.sleep(1)
    d.press('power')
    d.swipe(700, 1700, 700, 500)

def launchFromSysSettings():
    d.press('home')
    d(text = u'设置').click()
    while d(text = u'万象搜索').wait.gone(timeout = 3000):
        d.swipe(600, 1700, 600, 500)
    d(text = u'万象搜索').click()

def actFromSysSettings():
    launchPano()
    d.press('home')
    d(text = u'设置').click()
    while d(text = u'万象搜索').wait.gone(timeout = 3000):
        d.swipe(600, 1700, 600, 500)
    d(text = u'万象搜索').click()

def launchWallet():
    os.popen('adb shell am force-stop com.letv.walletbiz')
    os.popen('adb shell am start -n com.letv.walletbiz/com.letv.walletbiz.MainActivity')

def launchFromWallet():
    launchWallet()
    d(resourceId = 'com.letv.walletbiz:id/icon', instance = 1).click()
    d(text = u'电影票', resourceId = 'com.letv.walletbiz:id/service_name').click()
    d(resourceId = 'com.letv.walletbiz:id/action_search').click()














def longPressHome():
    os.popen('adb shell sendevent /dev/input/event13 1 172 1')
    os.popen('adb shell sendevent /dev/input/event13 0 0 0')
    time.sleep(1)
    os.popen('adb shell sendevent /dev/input/event13 1 172 0')
    os.popen('adb shell sendevent /dev/input/event13 0 0 0')

