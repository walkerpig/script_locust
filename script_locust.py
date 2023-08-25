from locust import task, between
from locust.contrib.fasthttp import FastHttpUser

class MyUser(FastHttpUser):
    wait_time = between(0.5, 1)

    @task
    def index(self):
        response = self.client.get("/")