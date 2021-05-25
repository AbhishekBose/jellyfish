import requests
import jenkins
server = jenkins.Jenkins('https://jenkins.nayan.co', username='nayan', password='11794b43899ef5e78ef6cfce9b18e91d74')

class Trigger:

    @staticmethod
    def trigger_job(**kwargs):
        print(kwargs)
        BUILD_NAME = 'Testing-Api'
        server.build_job(BUILD_NAME, kwargs)
        return 