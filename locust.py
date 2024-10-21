from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 5)  # Time (in seconds) to wait between tasks

    @task
    def load_test(self):
        self.client.get("/")  # Replace "/" with your target endpoint

if __name__ == "__main__":
    import os
    os.system("locust -f locustfile.py")
