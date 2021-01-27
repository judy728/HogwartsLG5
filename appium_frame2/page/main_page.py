from appium_frame2.base_page import BasePage
from appium_frame2.page.market_page import MarketPage


class MainPage(BasePage):
    # 点击行情时出现的弹窗或者黑名单--例：发表评论弹窗，取消弹窗，再点击行情tab
    def goto_market_page(self):
        self.run_steps("../page/main_page.yml" , "goto_market_page")

        #点击行情时出现的弹窗或者黑名单--例：发表评论弹窗
        # self.find_and_click((By.XPATH, "//*[@resource-id='com.xueqiu.android:id/post_status']"))
        # #点击行情tab
        # self.find_and_click((By.XPATH, "//*[@text='行情']"))
        return MarketPage(self.driver)

    def goto_mine(self):
        self.run_steps("../page/main_page.yml","goto_mine")