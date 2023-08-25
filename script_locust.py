from locust import task, between
from locust.contrib.fasthttp import FastHttpUser
import requests

class MyUser(FastHttpUser):
    wait_time = between(0.5, 1)

    @task
    def download_file(self):
        url = "URL_OF_YOUR_FILE"
        response = requests.get(url)