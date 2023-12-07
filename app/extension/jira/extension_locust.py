import re
from locustio.common_utils import init_logger, jira_measure, run_as_specific_user  # noqa F401

logger = init_logger(app_type='jira')

def fetch_static_content(locust):
    locust.get('/download/resources/io.bloompeak.jira-reports-pro:react-css/main.cad863dd.css', catch_response=True)
    locust.get('/download/resources/io.bloompeak.jira-reports-pro:react-js/522.a6bc323f.chunk.js', catch_response=True)
    locust.get('/download/resources/io.bloompeak.jira-reports-pro:react-js/async-jql-editor.b78ab4f7.chunk.js', catch_response=True)
    locust.get('/download/resources/io.bloompeak.jira-reports-pro:react-js/main.57671c25.js', catch_response=True)

@jira_measure("locust_app_specific_action")
# @run_as_specific_user(username='admin', password='admin')  # run as specific user
def app_specific_action(locust):
    content = locust.get('/plugins/servlet/bloompeak-jr/mainservlet/chart?dashboardId=10100&itemId=10100', headers={'content-type': 'text/html;charset=UTF-8'}, catch_response=True).content.decode('utf-8')
    assertionString = 'bloompeak-jr-root'
    if assertionString not in content:
        logger.error(f"'{assertionString}' was not found in {content}")
    assert assertionString in content  # assert specific string in response content

    
    headers = {'content-type': 'application/json'}
    locust.get('/rest/api/2/field', headers=headers, catch_response=True).content.decode('utf-8')
    locust.get('/rest/api/2/myself', headers=headers, catch_response=True).content.decode('utf-8')
    
    # locust.get('/rest/api/2/dashboard/10100/items/10100/properties/report', headers=headers, catch_response=False)#.content.decode('utf-8')
    
    body="""{"expand":[],"jql":"(project IN (10000)) AND (created >= -360d)","maxResults":100,"fields":["status"],"startAt":0}"""
    locust.post('/rest/api/2/search', body, headers=headers, catch_response=True).content.decode('utf-8')

    fetch_static_content(locust)
    
    """ r = locust.get('/app/get_endpoint', catch_response=True)  # call app-specific GET endpoint
    content = r.content.decode('utf-8')   # decode response content

    token_pattern_example = '"token":"(.+?)"'
    id_pattern_example = '"id":"(.+?)"'
    token = re.findall(token_pattern_example, content)  # get TOKEN from response using regexp
    id = re.findall(id_pattern_example, content)    # get ID from response using regexp

    logger.locust_info(f'token: {token}, id: {id}')  # log info for debug when verbose is true in jira.yml file
    if 'assertion string' not in content:
        logger.error(f"'assertion string' was not found in {content}")
    assert 'assertion string' in content  # assert specific string in response content

    body = {"id": id, "token": token}  # include parsed variables to POST request body
    headers = {'content-type': 'application/json'}
    r = locust.post('/app/post_endpoint', body, headers, catch_response=True)  # call app-specific POST endpoint
    content = r.content.decode('utf-8')
    if 'assertion string after successful POST request' not in content:
        logger.error(f"'assertion string after successful POST request' was not found in {content}")
    assert 'assertion string after successful POST request' in content  # assertion after POST request """
