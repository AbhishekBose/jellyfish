import jenkins

server = jenkins.Jenkins('https://jenkins.nayan.co', username='nayan', password='11794b43899ef5e78ef6cfce9b18e91d74')
user = server.get_whoami()
version = server.get_version()
print('Hello %s from Jenkins %s' % (user['fullName'], version))
print(server.jobs_count())
jobs = server.get_jobs()
# print(jobs)
my_job = server.get_job_config('Testing-Api')
# print(my_job)

server.build_job('Testing-Api', {'user': 1, 'job_id': 20})