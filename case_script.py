# -*- coding: utf-8 -*-

import time
import os
import sys
# from uiautomator import device as d
from uiautomator import Device

reload(sys)
sys.setdefaultencoding('gbk')

d = Device('910019c9')

yuanxianreying = u"反转人生"

w = 1080
h = 1920
w_m = w/2
h_m = h/2

def slideUp(speed = 15):
    d.swipe(w_m, h-500, w_m-100, h/2, steps = speed)
    time.sleep(2)

def slideDown(speed = 15):
    d.swipe(w_m, h/3, w_m, h, steps = speed)

def launchPano():
    d.press('home')
    time.sleep(1)
    slideUp()
    time.sleep(3)

def exitPano():
    os.popen("adb shell am force-stop com.letv.android.quicksearchbox")

def launchSlideUp():
    launchPano()

def actSlideUp():
    launchPano()

def slideDownRefresh():
    slideDown(10)

def backspaceOnInputBox():
    inputText('a')
    searchbox = 'com.letv.android.quicksearchbox:id/search_src_text'
    d(resourceId = searchbox).click()
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
    time.sleep(2)
    try:
        d(resourceId = 'com.letv.android.quicksearchbox:id/group_title').click()
    except:
        pass

def clearInputBox():
    inputText('a')
    d(resourceId = 'com.letv.android.quicksearchbox:id/delete').click()

def backFromThirdApp():
    while d(text = u'院线热映').wait.gone(timeout = 3000):
        slideUp()
    d(resourceId='com.letv.android.quicksearchbox:id/image').click()
    time.sleep(2)
    d.press('back')

def backFromResult():
    inputText('a')
    d.press('back')

def backFromEditsWidget():
    while d(text = u'编辑我的订阅').wait.gone(timeout = 3000):
        slideUp()
    d(text = u'编辑我的订阅').click()
    d.press('back')

def unlockScreen():
    d.press('power')
    time.sleep(1)
    d.press('power')
    slideUp()

def launchFromSysSettings():
    d.press('home')
    d(text = u'设置').click()
    while d(text = u'万象搜索').wait.gone(timeout = 3000):
        slideUp()
    d(text = u'万象搜索').click()
    time.sleep(3)

def actFromSysSettings():
    launchPano()
    d.press('home')
    d(text = u'设置').click()
    while d(text = u'万象搜索').wait.gone(timeout = 3000):
        slideUp()
    d(text = u'万象搜索').click()

def launchWallet():
    os.popen('adb shell am force-stop com.letv.walletbiz')
    os.popen('adb shell am start -n com.letv.walletbiz/com.letv.walletbiz.MainActivity')
    if d(textContains = u'稍后').wait.exists():
        d(textContains = u'稍后').click()

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
    d.press('recent')
    time.sleep(2)
    d.swipe(w_m, h/2, w, h/2, steps = 5)
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
    swipeToFindText(txt = u'院线热映')
    slideUp()
    d(text = u'您的附近正在上映').click()

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
    launchPano()
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
    time.sleep(3)
    slideUp()

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
    launchPano()
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
    swipeToFindText(txt = u'大家都在搜')
    slideUp()
    d(text = u'大家都在搜').down(resourceId = 'com.letv.android.quicksearchbox:id/content').click()

def exposeSERPInput():
    launchPano()
    inputText('a')

def exposeSERPHome():
    launchPano()
    inputText('a')
    time.sleep(3)
    d.press('home')
    time.sleep(3)
    slideUp()

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
    inputText('zhz')
    d(resourceId = 'com.letv.android.quicksearchbox:id/txt_episode').click()
    time.sleep(2)

def clickMoreEpisode():
    launchPano()
    inputText('p')
    time.sleep(1)
    swipeToFindText(txt = u'更多')
    slideUp()
    d(text = u'更多', resourceId = 'com.letv.android.quicksearchbox:id/txt_episode').click()
    time.sleep(2)

def clickShowOnWeb():
    launchPano()
    inputText('a')
    swipeToFindText(txt = u'搜索网页')
    slideUp()
    d(text = u'搜索网页').click()

def clickHotOpus():
    pass

def exposeNoResult():
    launchPano()
    inputText('pppppppppppppppppppppppppp')
    d(text = u'搜索网页').click()
    time.sleep(2)
    d.press('back')

def clickFollow():
    launchPano()
    inputText('syst')
    swipeToFindText(txt = u'关注广场')
    slideUp()
    d(text = u'关注').click()

def clickFollowed():
    launchPano()
    inputText('syst')
    swipeToFindText(txt = u'关注广场')
    slideUp()
    d(text = u'已关注').click()
    d(text = u'确定').click()

def clickSendSMS():
    launchPano()
    inputText('gao')
    d(resourceId = 'com.letv.android.quicksearchbox:id/message_image').click()
    time.sleep(2)

def clickCallOut():
    launchPano()
    inputText('gao')
    d(resourceId = 'com.letv.android.quicksearchbox:id/call_image').click()
    time.sleep(2)

def clickCallTheCar():
    launchPano()
    inputText('soho')
    d(text = u'去叫车').click()
    time.sleep(2)

def clickInstallApp():
    launchPano()
    inputText(u'崩坏')
    swipeToFindText(txt = u'安装')
    slideUp()
    d(text = u'安装').click()
    time.sleep(5)
    d(text = u'暂停').click()

def clickUpgradeApp():
    launchPano()
    inputText('live')
    swipeToFindText(txt = u'更新')
    d(text = u'更新').click()

def clickOpenApp():
    launchPano()
    inputText('shipin')
    swipeToFindText(txt = u'安装')
    d(text = u'安装').click()
    time.sleep(120)
    d(text = u'打开').click()

def clickPlayNow():
    launchPano()
    inputText('shipin')
    swipeToFindText(txt = u'立即播放')
    slideUp()
    d(text = u'立即播放').click()
    time.sleep(2)

def clickContactListSMS():
    clickSendSMS()
    d(resourceId = 'com.letv.android.quicksearchbox:id/number').click()

def expseContactListSMS():
    clickContactListSMS()

def clickCancelContactListSMS():
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

def clickNextPage():
    launchPano()
    # nextPage = 'com.letv.android.quicksearchbox:id/flush'
    # p = 0
    # while d(resourceId = nextPage).wait.gone():
    #     p += 1
    #     slideUp()
    #     if p > 10:
    #         break
    # d(resourceId = nextPage).click()
    swipeToFindText(u'换一换')
    d(text = u'换一换').click()
    time.sleep(2)

def exposePanoSettingsFromSysSettings():
    actFromSysSettings()

def exposePanoSettingsFromPersonalSettings():
    actFromSysSettings()
    d(resourceId = 'com.letv.android.quicksearchbox:id/home_page_setting').click()
    d(resourceId = 'com.letv.android.quicksearchbox:id/home_page_switch').click()
    time.sleep(2)
    d.press('back')

def exposePanoSettingsFromFeedback():
    actFromSysSettings()
    d(text = u'用户反馈').click()
    time.sleep(2)
    d.press('back')

def exposePanoSettingsFromCardEdit():
    pass

def exposePanoSettingsFromUnlockScreen():
    actFromSysSettings()
    lockThenUnlock()

def exposePanoSettingsFromMenulist():
    actFromSysSettings()
    d.press('recent')
    time.sleep(2)
    d.press('back')

def exposePersonalSettingsFromScreenlock():
    actFromSysSettings()
    d(resourceId = 'com.letv.android.quicksearchbox:id/home_page_setting').click()
    lockThenUnlock()

def exposePersonalSettingsFromTask():
    actFromSysSettings()
    d(resourceId = 'com.letv.android.quicksearchbox:id/home_page_setting').click()
    d.press('recent')
    time.sleep(2)
    d.press('back')

def exposePersonalSettingsFromHomepage():
    launchPano()
    swipeToFindText(txt = u'进入个性化设置')
    d(text = u'进入个性化设置').click()
    d(resourceId = 'com.letv.android.quicksearchbox:id/home_page_switch').click()
    time.sleep(2)
    d.press('back')

def lockThenUnlock():
    d.press('power')
    time.sleep(3)
    d.press('power')
    time.sleep(3)
    # slideUp()
    d.swipe(w_m, h_m, w_m, 0, steps=10)
    d.swipe(w_m, h_m, w_m, 0, steps=10)

def exposeFeedbackFromScreenLock():
    actFromSysSettings()
    d(text = u'用户反馈').click()
    lockThenUnlock()

def exposeFeedbackFromTask():
    actFromSysSettings()
    d(text = u'用户反馈').click()
    d.press('recent')
    time.sleep(2)
    d.press('back')

def exposeFeedbackFromHomepage():
    actFromSysSettings()
    d(text = u'用户反馈').click()

def clickSwitchOn():
    actFromSysSettings()
    d(resourceId = 'com.letv.android.quicksearchbox:id/home_page_setting').click()
    # d(resourceId = 'com.letv.android.quicksearchbox:id/home_page_switch').click()
    d(text = u'院线热映').click()
    time.sleep(2)
    d.press('back')

def clickSwitchOff():
    actFromSysSettings()
    d(resourceId = 'com.letv.android.quicksearchbox:id/home_page_setting').click()
    # d(resourceId = 'com.letv.android.quicksearchbox:id/home_page_switch').click()
    d(text = u'院线热映').click()
    time.sleep(2)
    d(resourceId = 'com.letv.android.quicksearchbox:id/back').click()

def clickTogoLIVEinSERP():
    launchPano()
    inputText(u'卫视')
    swipeToFindText(txt = u'直播中')
    slideUp()
    d(text = u'直播中').click()

def clickSubscribeLIVEinSERP():
    launchPano()
    inputText('zhibo')
    swipeToFindText(txt = u'去预约')
    slideUp()
    d(text = u'去预约').click()

def clickPreloadinSERP():
    launchPano()
    inputText('dianshiju')
    swipeToFindText(txt = u'缓存')
    slideUp()
    d(text = u'缓存').click()

def clickGoinSERP():
    launchPano()
    inputText('baidu')
    swipeToFindText(txt = u'直达')
    slideUp()
    d(text = u'直达').click()

def clickRecentFilminSERP():
    launchPano()
    inputText('yingyuan')
    swipeToFindText(txt = u'近期上映')
    slideUp()
    d(text = u'近期上映').click()

def clickNavigationinSERP():
    launchPano()
    inputText('yingyuan')
    swipeToFindText(txt = u'导航')
    slideUp()
    d(text = u'导航').click()

def swipeToFindText(txt):
    p = 0
    while d(text = u'%s'%txt).wait.gone():
        p += 1
        slideUp()
        if p > 10:
            break

def clickCallCarinSERP():
    launchPano()
    inputText('yingyuan')
    swipeToFindText(txt = u'叫车')
    slideUp()
    d(text = u'叫车').click()

def clickFilminSERP():
    clickRecentFilminSERP()
    slideUp()
    d(resourceId = 'com.letv.android.quicksearchbox:id/movie_name').click()

def clickCancelInstallinSERP():
    clickInstallApp()

def clickContinueInstallinSERP():
    clickInstallApp()
    d(text = u'继续').click()
    time.sleep(5)
    d(text = u'暂停').click()

def clickHotWords():
    launchPano()
    searchbox = 'com.letv.android.quicksearchbox:id/search_src_text'
    d(resourceId = searchbox).click()
    d.press('enter')

def exposeQVSERP():
    launchPano()
    inputText('a')
    time.sleep(2)

def clickBuyTicket():
    launchPano()
    # swipeToFindText(txt = u'院线热映')
    # swipeToFindText(txt = u'叫车')
    inputText(yuanxianreying)
    swipeToFindText(txt = u'购票')
    # while d(text = u'购票').wait.gone():
    #     d(text = u'院线热映').right(resourceId = 'com.letv.android.quicksearchbox:id/flush').click()
    #     time.sleep(2)
    d(text = u'购票').click()

def clickSwitchSort():
    launchPano()
    swipeToFindText(txt = u'进入个性化设置')
    slideUp()
    d(text = u'进入个性化设置').click()
    d(text = u'卡片智能化排序').click()
    d(resourceId = 'com.letv.android.quicksearchbox:id/back').click()

def exposeEachCard():
    launchPano()
    time.sleep(2)
    slideUp(30)
    time.sleep(1)
    slideUp(30)

def clickEachCard():
    clickBuyTicket()

def searchResEachCard():
    launchPano()
    inputText('a')
    time.sleep(5)
    swipeToFindText(txt = u'立即播放')
    slideUp()
    d(text = u'立即播放').click()
    # d(resourceId = 'com.letv.android.quicksearchbox:id/imgposter').click()

def exposeSERP():
    launchPano()
    inputText('a')
    time.sleep(5)
    slideUp(30)
    time.sleep(2)

def exposeHomepageEachCard():
    exposeEachCard()

def captureScreenAndPull(f_name, pc_dir):
    f_name = f_name[:-4]
    os.popen('adb shell mkdir sdcard/pano_fail_png')
    os.popen('adb shell /system/bin/screencap -p /sdcard/pano_fail_png/%s.png'%f_name)
    os.popen('adb pull /sdcard/pano_fail_png/%s.png %s'%(f_name, pc_dir))
    time.sleep(2)
    os.popen('adb shell rm /sdcard/pano_fail_png/%s.png'%f_name)

def taskClear():
    d.press('recent')
    time.sleep(2)
    d.swipe(w_m, h/2, w, h/2, steps = 5)
    time.sleep(3)
    d.press('home')