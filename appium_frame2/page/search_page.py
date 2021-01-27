from appium_frame2.base_page import BasePage


class SearchPage(BasePage):
    #定义搜索页面,并输入内容进行搜索
    def search(self):
        self.run_steps("../page/search_page.yml", "search")

        # self.send((By.XPATH, "//*[@resource-id='com.xueqiu.android:id/search_input_text']"),"阿里巴巴")
        # self.find_and_click((By.XPATH,'//*[@text="阿里巴巴-SW"]'))
        return True