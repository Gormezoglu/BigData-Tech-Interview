#!/usr/bin/env python3

import subprocess

def run_command(command):
    subprocess.run(command, shell=True, check=True)

def install_spark():
    # Install OpenJDK
    run_command("sudo apt-get install openjdk-8-jdk-headless -qq > /dev/null")

    # Download and extract Spark
    run_command("sudo wget -q http://archive.apache.org/dist/spark/spark-3.1.1/spark-3.1.1-bin-hadoop3.2.tgz")
    run_command("sudo tar xf spark-3.1.1-bin-hadoop3.2.tgz")

    # Install findspark
    run_command("sudo pip install -q findspark")

if __name__ == "__main__":
    install_spark()
