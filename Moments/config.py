
# 微信手机号密码
PHONE_NUMBER = ''
PASSWD = ''

# 配置Appium启动项
DESIRED_CAPS = {
    # 系统版本(ios或者android)
    'platformName': 'Android',
    # 手机型号
    "deviceName": 'OPPO_A57',
    # App包名
    "appPackage": "com.tencent.mm",
    # App入口
    "appActivity": "com.tencent.mm.ui.LauncherUI",
    # Android版本
    "platformVersion": "6.0.1",
    # 默认appium执行完之后会清除app应用数据，这里设置为True之后不会清除应用程序数据。
    "noReset": True,
    # 如果Appium无法定位元素，请使用uiautomator2引擎
    "automationName": "uiautomator2"
}

# Appium服务器地址
DRIVER_SERVER = 'http://localhost:4723/wd/hub'

# 等待元素加载时间
TIMEOUT = 5

MONGO_URI = 'mongodb://localhost:27017/'
MONGO_DB = 'wechat'
MONGO_COLLECTION = 'moments'
