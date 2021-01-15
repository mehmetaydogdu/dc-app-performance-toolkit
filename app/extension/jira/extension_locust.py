import random
import re
from locustio.common_utils import init_logger, jira_measure
from locustio.common_utils import RESOURCE_HEADERS

from locustio.jira.requests_params import jira_datasets

logger = init_logger(app_type='jira')

jira_dataset = jira_datasets()

def fetch_static_content(locust):
    locust.get('/download/resources/io.bloompeak.status-time:react-css/2.4fb28a4f.chunk.css', catch_response=True)
    locust.get('/download/resources/io.bloompeak.status-time:react-css/main.aea6ee88.chunk.css', catch_response=True)
    locust.get('/download/resources/io.bloompeak.status-time:react-js/2.e8c4c6a4.chunk.js', catch_response=True)
    locust.get('/download/resources/io.bloompeak.status-time:react-js/main.8a70e262.chunk.js', catch_response=True)
    locust.get('/download/resources/io.bloompeak.status-time:react-js/runtime-main.b43b082e.js', catch_response=True)
    locust.get('/download/resources/io.bloompeak.status-time:i18n/en.json', catch_response=True)
    locust.get('/download/resources/io.bloompeak.status-time:i18n/en-US.json', catch_response=True)

@jira_measure
def app_specific_action_report_page(locust):
    r = locust.get('/plugins/servlet/bloompeak-st/mainservlet/st-report', catch_response=True)  # call app-specific GET endpoint
    content = r.content.decode('utf-8')   # decode response content

    # token_pattern_example = '"token":"(.+?)"'
    # id_pattern_example = '"id":"(.+?)"'
    # token = re.findall(token_pattern_example, content)  # get TOKEN from response using regexp
    # id = re.findall(id_pattern_example, content)    # get ID from response using regexp

    # logger.locust_info(f'token: {token}, id: {id}')  # log information for debug when verbose is true in confluence.yml file
    assertString='<div id="bloompeak-root" class="ac-content"></div>'
    if assertString not in content:
        logger.error(f"{assertString} was not found in {content}")
    assert assertString in content  # assert specific string in response content
    
    # fetch_static_content(locust)
    
    headers = {'content-type': 'application/json'}
    calendarsResponse = locust.get('/rest/io.bloomp/1.0/calendars', headers=headers, catch_response=True).content.decode('utf-8')
    assertStringCalendar='workingIntervals'
    if assertStringCalendar not in calendarsResponse:
        logger.error(f"{assertStringCalendar} was not found in {calendarsResponse}")
    assert assertStringCalendar in calendarsResponse  # assert specific string in response content

    locust.get('/rest/api/2/status', headers=headers, catch_response=True).content.decode('utf-8')
    locust.get('/rest/api/2/field', headers=headers, catch_response=True).content.decode('utf-8')

    # locust.get('/rest/api/2/issue/${issueKey}?expand=changelog&fields=*all', headers=headers, catch_response=True).content.decode('utf-8')

    body="""{
        "expand": [
            "changelog",
            "names"
          ],
        "jql": "status != Closed order by key",
        "maxResults": 50,
        "fields": ["created", "status"],
        "startAt": 0
        }"""
    # locust.post('/rest/api/2/search', body, headers, catch_response=True)  # call app-specific POST endpoint
    

    # body = {"id": id, "token": token}  # include parsed variables to POST request body
    # headers = {'content-type': 'application/json'}
    # r = locust.post('/app/post_endpoint', body, headers, catch_response=True)  # call app-specific POST endpoint
    # content = r.content.decode('utf-8')
    # if 'assertion string after successful POST request' not in content:
    #     logger.error(f"'assertion string after successful POST request' was not found in {content}")
    # assert 'assertion string after successful POST request' in content  # assertion after POST request

@jira_measure
def app_specific_action_issue_view(locust):
    issue_key = random.choice(jira_dataset['issues'])[0]
    headers = {'content-type': 'application/json'}
    locust.get(f"/plugins/servlet/bloompeak-st/mainservlet/st-issue-view?issueKey={issue_key}", catch_response=True)
    
    # fetch_static_content(locust)

    calendarsResponse = locust.get('/rest/io.bloompeak.st/1.0/calendars', headers=headers, catch_response=True).content.decode('utf-8')
    assertStringCalendar='workingIntervals'
    if assertStringCalendar not in calendarsResponse:
        logger.error(f"{assertStringCalendar} was not found in {calendarsResponse}")
    assert assertStringCalendar in calendarsResponse

    locust.get('/rest/api/2/status', headers=headers, catch_response=True)
    locust.get('/rest/api/2/myself', headers=headers, catch_response=True)
    locust.get(f"/rest/api/2/issue/{issue_key}?expand=changelog&fields=*all", headers=headers, catch_response=True)