import re
from locustio.common_utils import init_logger, jira_measure, run_as_specific_user  # noqa F401

logger = init_logger(app_type='jira')


@jira_measure("locust_app_specific_action")
# @run_as_specific_user(username='admin', password='admin')  # run as specific user
def app_specific_action(locust):
    r = locust.get('/plugins/servlet/bloompeak-st/mainservlet/st-report', catch_response=True)  # call app-specific GET endpoint
    content = r.content.decode('utf-8')   # decode response content
    assert '<div id="bloompeak-root" class="ac-content"></div>' in content

    r = locust.get('/download/resources/io.bloompeak.status-time:ui-i18n/en.json', catch_response=True)  # call app-specific GET endpoint
    content = r.content.decode('utf-8')   # decode response content
    assert '"Search": "Search",' in content

    locust.get('/download/resources/io.bloompeak.status-time:ui-i18n/en-US.json', catch_response=False)
    locust.get('/rest/api/2/myself', catch_response=False)
    locust.get('/rest/api/2/field', catch_response=False)
    locust.get('/rest/api/2/status', catch_response=False)
    locust.get('/rest/api/2/filter/favourite', catch_response=False)
    locust.get('/rest/io.bloompeak.st/1.0/calendars', catch_response=False)
    locust.get('/rest/io.bloompeak.st/1.0/reports', catch_response=False)
    
    locust.get('/download/resources/io.bloompeak.status-time:react-css/2.81e8548a.chunk.css', catch_response=False)
    locust.get('/download/resources/io.bloompeak.status-time:react-css/main.afa36abd.chunk.css', catch_response=False)

    locust.get('/download/resources/io.bloompeak.status-time:react-js/2.9213ffcd.chunk.js', catch_response=False)
    locust.get('/download/resources/io.bloompeak.status-time:react-js/3.bbb8287f.chunk.js', catch_response=False)
    locust.get('/download/resources/io.bloompeak.status-time:react-js/main.83b38437.chunk.js', catch_response=False)
    locust.get('/download/resources/io.bloompeak.status-time:react-js/runtime-main.0ed2a896.js', catch_response=False)
