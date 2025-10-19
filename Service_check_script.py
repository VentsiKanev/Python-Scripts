
import subprocess

svc = input("Enter the service name to check: ")

service_check = subprocess.call(["ps", "-C", svc])

if service_check == 0:
    print("The service is running")
else:
    print("The service is stopped.")
