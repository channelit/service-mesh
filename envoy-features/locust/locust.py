from locust import HttpLocust, TaskSet, task
import os
import json

def index(l):
    l.client.get("/")

def stats(l):
    l.client.get("/stats/requests")

class MultipleHostsLocust(HttpLocust):
    abstract = True
    
    def __init__(self, *args, **kwargs):
        super(MultipleHostsLocust, self).__init__(*args, **kwargs)
        self.jwt_client = HttpSession(base_url=os.environ.get("JWT_URL", "http://localhost:8080"))

class UserTasks(TaskSet):

    tasks = [index, stats]
    
    def on_start(self):
        self.login()

    def login(self)
        conn = http.client.HTTPConnection("localhost")
        payload = "username=user&password=user&grant_type=password&client_id=envoy"
        headers = {
            'Content-Type': "application/x-www-form-urlencoded",
            'User-Agent': "PostmanRuntime/7.15.2",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Host': "localhost:8080",
            'Accept-Encoding': "gzip, deflate",
            'Content-Length': "63",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
            }
        response = self.jwt_client.post('/auth/realms/envoy/protocol/openid-connect/token',
                         payload, 
                         headers=headers)

    @task
    def page404(self):
        self.client.get("/does_not_exist")
    
class WebsiteUser(MultipleHostsLocust):
    URL_HOST = os.environ.get('URL_HOST', '127.0.0.1')
    URL_PORT = os.environ.get('URL_PORT', '8089')
    URL_ENDPOINT = os.environ.get('URL_ENDPOINT', 'client')
    host = "http://" + URL_HOST + ":" + URL_PORT + "/" + URL_ENDPOINT
    min_wait = 2000
    max_wait = 5000
    task_set =  UserTasks