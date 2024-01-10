from appium import webdriver
from appium.options.common import AppiumOptions

APP = "/Users/lanabegunova/PycharmProjects/sel_appium_testing/mobile/other_apps/TestApp3.app"
APPIUM = 'http://localhost:4723'

CAPS = {
    "platformName": "iOS",
    "appium:options": {
        "platformVersion": "17.2",
        "deviceName": "iPhone 15 Pro Max",
        "automationName": "XCUITest",
        "app": APP
    }
}

OPTIONS = AppiumOptions().load_capabilities(CAPS)

driver = webdriver.Remote(
    command_executor=APPIUM,
    options=OPTIONS
)

try:
    app = "https://github.com/webdriverio/native-demo-app/releases/download/v1.0.8/ios.simulator.wdio.native.app.v1.0.8.zip"
    app_id = "org.reactjs.native.example.wdiodemoapp"

    # Get all defined Strings from an app for the specified language and strings filename.
    print("The app strings are:", driver.app_strings("en"))

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

    # Terminate the app if it is running.
    driver.terminate_app(app_id)

    # Remove the specified app from the device.
    driver.remove_app(app_id)
finally:
    if driver:
        driver.quit()