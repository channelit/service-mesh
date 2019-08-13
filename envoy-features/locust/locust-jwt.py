from locust import HttpLocust, TaskSet, task
from locust.clients import HttpSession
import os
import json


class SubscriberTasks(TaskSet):

    def __init__(self, parent):
        super().__init__(parent)
        self.auth_token = ""

    def on_start(self):
        self.login()

    def login(self):
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
        client = HttpSession(base_url=os.environ.get("JWT_URL", "http://localhost:8080"))
        response = client.post('/auth/realms/envoy/protocol/openid-connect/token',
                               payload,
                               headers=headers)
        self.auth_token = "Bearer " + json.loads(response.text)['access_token']

    @task(1)
    def call_client(self):
        self.client.get("/client", headers={'Authorization': self.auth_token})

    @task(2)
    def call_status(self):
        self.client.get("/status", headers={'Authorization': self.auth_token})


class ServiceUser(HttpLocust):
    URL_HOST = os.environ.get('URL_HOST', '127.0.0.1')
    URL_PORT = os.environ.get('URL_PORT', '8090')
    URL_ENDPOINT = os.environ.get('URL_ENDPOINT', '')
    host = "http://" + URL_HOST + ":" + URL_PORT + "/" + URL_ENDPOINT
    min_wait = 2000
    max_wait = 5000
    task_set = SubscriberTasks


if __name__ == '__main__':
    ServiceUser().run()
