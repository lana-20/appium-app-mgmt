from appium import webdriver
from appium.options.common import AppiumOptions
from pprint import pprint

APP = "https://github.com/webdriverio/native-demo-app/releases/download/v1.0.8/android.wdio.native.app.v1.0.8.apk"
APPIUM = 'http://localhost:4723'

CAPS = {
    "platformName": "Android",
    "appium:options": {
        "platformVersion": "14.0",  # optional
        "deviceName": "Android Emulator",
        "automationName": "UiAutomator2",
        "app": APP
    }
}

OPTIONS = AppiumOptions().load_capabilities(CAPS)

driver = webdriver.Remote(
    command_executor=APPIUM,
    options=OPTIONS
)

try:
    app = "https://github.com/appium/android-apidemos/releases/download/v3.1.0/ApiDemos-debug.apk"
    app_id = 'io.appium.android.apis'

    # Get the app strings from the device for the specified language.
    print("The app strings are:")
    pprint(driver.execute_script("mobile: getAppStrings", {"app": app, "language": "en"}))

    # Remove the specified app from the device.
    driver.execute_script("mobile: removeApp", {"appId": app_id})

    # Install the app found at `app_path` on the device.
    driver.execute_script("mobile: installApp", {"appPath": app})

    # Check whether the app specified by `app_id` is installed on the device.
    print("Is app installed?:", driver.execute_script("mobile: isAppInstalled", {"appId": app_id}))

    # Activate the app if it is not running or is running in the background.
    driver.execute_script("mobile: activateApp", {"appId": app_id})

    # Query the state of the app.
    print("The app state is:", driver.execute_script("mobile: queryAppState", {"appId": app_id}))

    # Terminate the app if it is running.
    driver.execute_script("mobile: terminateApp", {"appId": app_id})

    # Remove the specified app from the device.
    driver.execute_script("mobile: removeApp", {"appId": app_id})
finally:
    if driver:
        driver.quit()