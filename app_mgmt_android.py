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

    # Remove the specified app from the device.
    driver.remove_app(app_id)

    # Install the app found at `app_path` on the device.
    driver.install_app(app)

    # Check whether the app specified by `app_id` is installed on the device.
    print("Is app installed?:", driver.is_app_installed(app_id))

    # Activate the app if it is not running or is running in the background.
    driver.activate_app(app_id)

    # Query the state of the app.
    print("The app state is:", driver.query_app_state(app_id))

    # Get the app strings from the device for the specified language.
    print("The app strings are:")
    pprint(driver.app_strings("en"))

    # Terminate the app if it is running.
    driver.terminate_app(app_id)

    # Remove the specified app from the device.
    driver.remove_app(app_id)
finally:
    if driver:
        driver.quit()
