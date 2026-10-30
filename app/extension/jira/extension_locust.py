import re
from locustio.common_utils import init_logger, jira_measure, run_as_specific_user  # noqa F401

logger = init_logger(app_type='jira')


@jira_measure("locust_app_specific_action")
# @run_as_specific_user(username='admin', password='admin')  # run as specific user
def app_specific_action(locust):
    r = locust.get('/plugins/servlet/bloompeak-stf/mainservlet/st-report', catch_response=True)  # call app-specific GET endpoint
    content = r.content.decode('utf-8')   # decode response content
    assert '<div id="root" class="ac-content"></div>' in content

    locust.get('/rest/api/2/field', catch_response=False)
    locust.get('/rest/io.bloompeak.stf/1.0/status', catch_response=False)
    locust.get('/rest/io.bloompeak.stf/1.0/calendars', catch_response=False)
    locust.get('/rest/io.bloompeak.stf/1.0/reports', catch_response=False)
    
    locust.get('/s/d/_/download/resources/io.bloompeak.status-time-free:react-js/static/css/vendors.04221176ec4a04c4018a.css', catch_response=False)

    locust.get('/s/d/_/download/resources/io.bloompeak.status-time-free:react-js/static/js/vendors.18220b1deab5b4378929.js', catch_response=False)
    locust.get('/s/d/_/download/resources/io.bloompeak.status-time-free:react-js/static/js/main.626303a2ab8d96d05350.js', catch_response=False)
