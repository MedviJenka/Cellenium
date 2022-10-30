import jenkins
from datetime import datetime
import numpy as np
import sys, getopt
import matplotlib as plt
from dataclasses import dataclass


@dataclass 
class DurationMetrics:

    username: str = "medvijenia"
    password: str = "008195qzx5dS#@jenkins"
    server = None

    def connect_to_jenkins(self) -> None:
        self.server = jenkins.Jenkins('http://localhost:8080', self.username, self.password)
        user = self.server.get_whoami()
        version = self.server.get_version()
        print(f"hello {user['full_name']} from jenkins, version: {version}")


def main(argv: sys) -> None:
    username = ''
    password = ''
    
    try:
        opts, args = getopt.getopt(argv, "hu:p:", ["username=", "password="])
    except getopt.GetoptError:
        print("error")
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            username = arg
        elif opt == '-p':
            password = arg

    duration_metrics = DurationMetrics(username, password)
    duration_metrics.connect_to_jenkins()


if __name__ == "__main__":
    main(sys.argv[1:])
