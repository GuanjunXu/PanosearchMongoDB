# -*- coding: utf-8 -*-

from uiautomator import device as d
import time
import os

def swipeUp():
    d.swipe(550, 1500, 450, 800, steps=15)

def launchPano():
    d.press('home')
    time.sleep(1)
    swipeUp()
    time.sleep(3)

def exitPano():
    os.popen("adb shell am force-stop com.letv.android.quicksearchbox")

def launchSlideUp():
    launchPano()

def actSlideUp():
    launchPano()

def slideDownRefresh():
    d.swipe(550, 700, 550, 1500,steps=10)

def backspaceOnInputBox():
    inputText('a')
    d.press('delete') # Delete a

def launchHoldHomekey():
    longPressHome()

def longPressHome():
    os.popen('adb shell sendevent /dev/input/event13 1 172 1')
    os.popen('adb shell sendevent /dev/input/event13 0 0 0')
    time.sleep(1)
    os.popen('adb shell sendevent /dev/input/event13 1 172 0')
    os.popen('adb shell sendevent /dev/input/event13 0 0 0')
    time.sleep(3)

def actHoldHomeKey():
    d.press('home')
    longPressHome()
    # if d(resourceId = 'com.android.settings:id/step_next').exists() and d(resourceId = 'com.android.settings:id/step_last').exists():
    #     d(text = u'万象搜索').click()
    #     d.press('back')
    # longPressHome()

def inputText(ttt):
    searchbox = 'com.letv.android.quicksearchbox:id/search_src_text'
    d(resourceId = searchbox).click()
    d(resourceId = searchbox).set_text(ttt) # Input a
    time.sleep(1)

def clearInputBox():
    inputText('a')
    d(resourceId = 'com.letv.android.quicksearchbox:id/delete').click()

def backFromThirdApp():
    while d(text = u'院线热映').wait.gone(timeout = 3000):
        d.swipe(700, 1700, 700, 1000, steps = 30)
    d(resourceId='com.letv.android.quicksearchbox:id/image').click()
    time.sleep(2)
    d.press('back')

def backFromResult():
    inputText('a')
    d.press('back')

def backFromEditsWidget():
    while d(text = u'编辑我的订阅').wait.gone(timeout = 3000):
        d.swipe(700, 1700, 700, 1000, steps = 30)
    d(text = u'编辑我的订阅').click()
    d.press('back')

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
    time.sleep(3)

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
    time.sleep(3)

def exitViaCancel():
    launchSlideUp()
    d(text = u'取消').click()

def exitViaMenu():
    launchSlideUp()
    d.press('menu')
    d.swipe(550, 900, 1000, 900, steps = 10)
    time.sleep(2)
    d.press('back')

def exitViaBack():
    launchSlideUp()
    d.press('back')

def exitViaDoubleBack():
    launchSlideUp()
    d.press('back')
    d.press('back')

def actFromSlideUp():
    launchPano()
    d.press('home')
    launchPano()

def actFromHoldHome():
    launchPano()
    d.press('home')
    longPressHome()

def actFromSysSettings():
    launchPano()
    d.press('home')
    launchFromSysSettings()

def actFromWallet():
    launchPano()
    d.press('home')
    launchFromWallet()

def actEndViaHome():
    launchPano()
    d.press('home')

def actEndViaBack():
    launchPano()
    d.press('back')

def actEndViaThrdParty():
    launchPano()
    p = 0
    while d(text = u'短视频').wait.gone():
        p += 1
        swipeUp()
        if p > 4:
            break
    d(text=u'短视频').down(resourceId='com.letv.android.quicksearchbox:id/template_item').click()
    time.sleep(5)

def actEndViaCancel():
    launchPano()
    d(text = u'取消').click()

def invokeLaunchSlideUp():
    launchPano()

def invokeLaunchHoldHomekey():
    launchHoldHomekey()

def invokeLaunchSysSettings():
    launchFromSysSettings()

def invokeLaunchThrdParty():
    launchFromWallet()

def exposeLaunchSlideUp():
    launchPano()

def exposeRefreshSlideDown():
    launchPano()
    slideDownRefresh()
    
def exposeDelSearchBar():
    launchPano()
    backspaceOnInputBox()

def exposeLaunchHoldHome():
    launchHoldHomekey()

def exposeClearSearchBar():
    launchPano()
    clearInputBox()

def exposeWallet():
    launchFromWallet()

def exposeBackFromResult():
    inputText('a')
    d.pres('back')

def exposeBackFromEditsWidget():
    pass

def exposeBackFromWidgetList():
    pass

def exposeBackFromScreenLock():
    launchPano()
    d.press('power')
    time.sleep(3)
    d.press('power')
    swipeUp()

def clickSearchHomePage():
    launchPano()
    inputText('')

def clickSearchResult():
    launchPano()
    inputText('a')
    time.sleep(1)
    inputText('z')

def clickCancelHomePage():
    launchPano()
    d(text = u'取消').click()

def clickCancelResult():
    launchPano()
    inputText('a')
    d(text = u'取消').click()

def clickClearButton():
    clearInputBox()

def exposeSERPHistory():
    launchPano()
    inputText('a')
    d(resourceId = 'com.letv.android.quicksearchbox:id/group_title').click()
    exitPano()
    launchPano()
    d(text = u'搜索历史').down(text = 'a').click()

def exposeSERPHot():
    launchPano()
    p = 0
    while d(text = u'大家都在搜').wait.gone():
        p += 1
        swipeUp()
        if p > 10:
            break
    d(text = u'大家都在搜').down(resourceId = 'com.letv.android.quicksearchbox:id/content').click()

def exposeSERPInput():
    launchPano()
    inputText('a')

def exposeSERPHome():
    launchPano()
    inputText('a')
    time.sleep(3)
    launchPano()

def clickMoreButton(card_name = None):
    if card_name != None:
        d(text = u'%s'%card_name).right(resourceId = 'com.letv.android.quicksearchbox:id/group_search').click()
    else:
        d(resourceId = 'com.letv.android.quicksearchbox:id/group_search').click()

def clickMoreSERP():
    launchPano()
    inputText('a')
    clickMoreButton()
    time.sleep(2)

def clickEpisode():
    launchPano()
    inputText('a')
    d(resourceId = 'com.letv.android.quicksearchbox:id/txt_episode').click()
    time.sleep(2)

def clickMoreEpisode():
    launchPano()
    inputText('a')
    d(text = u'更多', resourceId = 'com.letv.android.quicksearchbox:id/txt_episode').click()
    time.sleep(2)

def clickShowOnWeb():
    launchPano()
    inputText('a')
    p = 0
    while d(text = u'搜索网页').wait.gone():
        p += 1
        swipeUp()
        if p > 10:
            break
    d(text = u'搜索网页').click()
    time.sleep(2)

def clickHotOpus():
    pass

def exposeNoResult():
    launchPano()
    inputText('pppppppppppppppppppppppppp')
    time.sleep(2)

def clickFollow():
    pass

def clickFollowed():
    pass

def clickSendSMS():
    launchPano()
    inputText('gao')
    d(resouceId = 'com.letv.android.quicksearchbox:id/message_image').click()
    time.sleep(2)

def clickCallOut():
    launchPano()
    inputText('gao')
    d(resouceId = 'com.letv.android.quicksearchbox:id/call_image').click()
    time.sleep(2)

def clickCallTheCar():
    launchPano()
    inputText('soho')
    d(text = u'去叫车').click()
    time.sleep(2)

def clickInstallApp():
    launchPano()
    inputText('shipin')
    p = 0
    while d(text = u'安装').wait.gone():
        p += 1
        swipeUp()
        if p > 10:
            break
    d(text = u'安装').click()
    time.sleep(2)
    d(text = u'暂停').click()

def clickUpgradeApp():
    # launchPano()
    # inputText('shipin')
    # p = 0
    # while d(text = u'更新').wait.gone():
    #     p += 1
    #     swipeUp()
    #     if p > 10:
    #         break
    # d(text = u'更新').click()
    pass

def clickOpenApp():
    launchPano()
    inputText('shipin')
    p = 0
    while d(text = u'安装').wait.gone():
        p += 1
        swipeUp()
        if p > 10:
            break
    d(text = u'安装').click()
    time.sleep(120)
    d(text = u'打开').click()

def clickPlayNow():
    launchPano()
    inputText('shipin')
    p = 0
    while d(text = u'立即播放').wait.gone():
        p += 1
        swipeUp()
        if p > 10:
            break
    d(text = u'立即播放').click()
    time.sleep(2)

def clickContactListSMS():
    clickSendSMS()
    d(resourceId = 'com.letv.android.quicksearchbox:id/number').click()

def expseContactListSMS():
    clickContactListSMS()

def clickCancelContactList():
    clickSendSMS()
    d(text = u'取消').click()

def clickContactListCall():
    clickCallOut()
    d(resourceId = 'com.letv.android.quicksearchbox:id/number').click()

def expseContactListCall():
    clickContactListCall()

def clickCancelContactListCall():
    clickCallOut()
    d(text = u'取消').click()