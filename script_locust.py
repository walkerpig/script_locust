from locust import task, between
from locust.contrib.fasthttp import FastHttpUser
import requests

class MyUser(FastHttpUser):
    wait_time = between(2, 5)

    def on_start(self):
        self.host = "YOUR_HOST_URL" 

    @task
    def download_file(self):
        url = f"{self.host}"
        print(url)
        response = requests.get(url)