#!/usr/bin/env python3

import subprocess

def run_command(command):
    print(f"Running command: {command}")
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    while True:
        output = process.stdout.readline()
        error = process.stderr.readline()
        if output == b'' and error == b'' and process.poll() is not None:
            break
        if output:
            print(output.decode('utf-8').strip())
        if error:
            print(error.decode('utf-8').strip())

    return process.returncode

def install_spark():
    # Update package lists
    run_command("sudo apt-get update -qq")

    # Install OpenJDK
    result = run_command("sudo apt install -y openjdk-8-jdk-headless")
    if result != 0:
        print("Error installing OpenJDK. Exiting.")
        return

    # Download and extract Spark
    run_command("sudo wget -q http://archive.apache.org/dist/spark/spark-3.1.1/spark-3.1.1-bin-hadoop3.2.tgz")
    run_command("sudo tar xf spark-3.1.1-bin-hadoop3.2.tgz")

    # Install findspark
    run_command("sudo pip install -q findspark")

if __name__ == "__main__":
    install_spark()
