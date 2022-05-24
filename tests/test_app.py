from dash.testing.application_runners import import_app
import time
from selenium import webdriver

driver = webdriver.Chrome('C:/DevTools/chromedriver.exe')

# 1. give each testcase a tcid, and pass the fixture as a function argument, less boilerplate
# mmffddd => module + file + three digits
def test_uoaa001(dash_duo):
    # 2. define your app inside the test function
    app = import_app('tests.app')

    # 3. host the app locally in a thread, all dash server configs could be passed after the first app argument
    dash_duo.start_server(app)

    # 4. use wait_for_* if your target element is the result of a callback,
    # keep in mind even the initial rendering can trigger callbacks
    dash_duo.wait_for_text_to_equal('h1', 'Pink', timeout=10)

    # 5. to make the checkpoint more readable, you can describe the
    # acceptance criterion as an assert message after the comma.
    assert dash_duo.get_logs() == [], "browser console should contain no error"

    # 8. visual testing with percy snapshot
    dash_duo.percy_snapshot("bsly001-layout")


