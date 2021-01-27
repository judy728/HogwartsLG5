from appium_frame2.base_page import BasePage
from appium_frame2.page.search_page import SearchPage


class MarketPage(BasePage):
    # 点击搜索
    def goto_search(self):
        self.run_steps("../page/market_page.yml", "goto_search")

        # self.find_and_click((By.XPATH,"//*[@resource-id='com.xueqiu.android:id/action_search']"))
        return SearchPage(self.driver)