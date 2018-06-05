from selenium import webdriver

def before_all(self):
	chromedriver = 'features/chromedriver'
	options = webdriver.ChromeOptions()
	options.add_argument('headless')
	self.browser = webdriver.Chrome(executable_path=chromedriver,chrome_options=options)
	#self.browser = webdriver.Chrome('/home/rizkimp/Downloads/chromedriver')
	self.browser.maximize_window()
	self.browser.implicitly_wait(5)

def after_all(self):
    self.browser.quit()
