import re
from locustio.common_utils import init_logger, jira_measure, run_as_specific_user  # noqa F401

logger = init_logger(app_type='jira')

def fetch_static_content(locust):
    locust.get('/download/resources/io.bloompeak.jira-sumup-pro:react-js/static/js/vendors.dd8eba93d87e0e9265d8.js', catch_response=True)
    locust.get('/download/resources/io.bloompeak.jira-sumup-pro:react-js/static/js/main.1d8f6ead150afb50f1c3.js', catch_response=True)
    locust.get('/download/resources/io.bloompeak.jira-sumup-pro:react-js/static/css/main.72f5bcb468e7e5c4545e.css', catch_response=True)
    locust.get('/download/resources/io.bloompeak.jira-sumup-pro:react-js/static/css/vendors.73741ca1b298ea5908d1.css', catch_response=True)

@jira_measure("locust_app_specific_action")
# WebSudo is a feature that enhances security by requiring administrators to re-authenticate before
# accessing administrative functions within Atlassian applications.
# do_websudo=True requires user administrative rights, otherwise requests fail.
#@run_as_specific_user(username='admin', password='admin', do_websudo=False)  # run as specific user
def app_specific_action(locust):
    content = locust.get('/plugins/servlet/io-bloompeak-sumup/mainservlet/chart?dashboardId=10100&itemId=10100', headers={'content-type': 'text/html;charset=UTF-8'}, catch_response=True).content.decode('utf-8')
    assertionString = 'bloompeak-sumup-root'
    if assertionString not in content:
        logger.error(f"'{assertionString}' was not found in {content}")
    assert assertionString in content  # assert specific string in response content

    
    headers = {'content-type': 'application/json'}
    locust.get('/rest/api/2/field', headers=headers, catch_response=True).content.decode('utf-8')
    
    # locust.get('/rest/api/2/dashboard/10100/items/10100/properties/report', headers=headers, catch_response=False)#.content.decode('utf-8')
    
    body="""{"expand":[],"jql":"(project IN (10000)) AND (created >= -360d)","maxResults":100,"fields":["status"],"startAt":0}"""
    locust.post('/rest/api/2/search', body, headers=headers, catch_response=True).content.decode('utf-8')

    fetch_static_content(locust)
