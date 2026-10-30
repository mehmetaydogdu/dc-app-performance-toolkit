import re
from locustio.common_utils import init_logger, jira_measure, run_as_specific_user  # noqa F401

logger = init_logger(app_type='jira')

def fetch_static_content(locust):
    locust.get('/s/d/_/download/resources/io.bloompeak.jira-reports-pro:react-js/static/js/vendors.af65ae203e62b69c3152.js', catch_response=True)
    locust.get('/s/d/_/download/resources/io.bloompeak.jira-reports-pro:react-js/static/js/main.b2b5b0baff7344aaa049.js', catch_response=True)
    locust.get('/s/d/_/download/resources/io.bloompeak.jira-reports-pro:react-js/static/css/main.afe5bc87ffdce7428cb1.css', catch_response=True)
    locust.get('/s/d/_/download/resources/io.bloompeak.jira-reports-pro:react-js/static/css/vendors.2b1d239ab17c006fca64.css', catch_response=True)

@jira_measure("locust_app_specific_action")
# @run_as_specific_user(username='admin', password='admin')  # run as specific user
def app_specific_action(locust):
    content = locust.get('/plugins/servlet/bloompeak-jr/mainservlet/chart?dashboardId=10100&itemId=10101', headers={'content-type': 'text/html;charset=UTF-8'}, catch_response=True).content.decode('utf-8')
    assertionString = 'bloompeak-jr-root'
    if assertionString not in content:
        logger.error(f"'{assertionString}' was not found in {content}")
    assert assertionString in content  # assert specific string in response content

    
    headers = {'content-type': 'application/json'}
    locust.get('/rest/api/2/field', headers=headers, catch_response=True).content.decode('utf-8')
    
    # locust.get('/rest/api/2/dashboard/10100/items/10100/properties/report', headers=headers, catch_response=False)#.content.decode('utf-8')
    
    body="""{"expand":[],"jql":"(project IN (10396)) AND (created >= -90d)","maxResults":100,"fields":["status"],"startAt":0}"""
    locust.post('/rest/api/2/search', body, headers=headers, catch_response=True).content.decode('utf-8')

    fetch_static_content(locust)