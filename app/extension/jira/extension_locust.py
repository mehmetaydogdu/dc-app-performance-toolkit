import re
from locustio.common_utils import init_logger, jira_measure, run_as_specific_user  # noqa F401

logger = init_logger(app_type='jira')


@jira_measure("locust_app_specific_action")
# @run_as_specific_user(username='admin', password='admin')  # run as specific user
def app_specific_action(locust):
    r = locust.get('/plugins/servlet/bloompeak-stf/mainservlet/st-report', catch_response=True)  # call app-specific GET endpoint
    content = r.content.decode('utf-8')   # decode response content
    assert '<div id="bloompeak-root" class="ac-content"></div>' in content

    r = locust.get('/download/resources/io.bloompeak.status-time-free:ui-i18n/en.json', catch_response=True)  # call app-specific GET endpoint
    content = r.content.decode('utf-8')   # decode response content
    assert '"Search": "Search",' in content

    locust.get('/download/resources/io.bloompeak.status-time-free:ui-i18n/en-US.json', catch_response=False)
    locust.get('/rest/api/2/myself', catch_response=False)
    locust.get('/rest/api/2/field', catch_response=False)
    locust.get('/rest/api/2/filter/favourite', catch_response=False)
    locust.get('/rest/io.bloompeak.stf/1.0/status', catch_response=False)
    locust.get('/rest/io.bloompeak.stf/1.0/calendars', catch_response=False)
    locust.get('/rest/io.bloompeak.stf/1.0/reports', catch_response=False)
    
    locust.get('/download/resources/io.bloompeak.status-time-free:react-css/2.81e8548a.chunk.css', catch_response=False)
    locust.get('/download/resources/io.bloompeak.status-time-free:react-css/main.afa36abd.chunk.css', catch_response=False)

    locust.get('/download/resources/io.bloompeak.status-time-free:react-js/2.7bc545d9.chunk.js', catch_response=False)
    locust.get('/download/resources/io.bloompeak.status-time-free:react-js/3.ff963ffd.chunk.js', catch_response=False)
    locust.get('/download/resources/io.bloompeak.status-time-free:react-js/main.5f65c7c0.chunk.js', catch_response=False)
    locust.get('/download/resources/io.bloompeak.status-time-free:react-js/runtime-main.b057ef5a.js', catch_response=False)
