import requests

class Trigger:

    @staticmethod
    def trigger_job(**kwargs):
        #curl -v -X POST 34.71.54.148:31554/job/Testing-Api/build --user nayan:11794b43899ef5e78ef6cfce9b18e91d74 --data-urlencode json='{"parameter":[{"name":"user","value":"34"},{"name":"job_id","value":"102"}]}' -H "Accept: application/json"
        print(kwargs)
        return 