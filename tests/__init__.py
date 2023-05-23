import subprocess
from dataclasses import dataclass


@dataclass
class GenerateTeamsMeeting:

    exe_path: str = r'C:\Users\evgenyp\vision\core\repo_test\_tools\TeamsUsersSimulator\TeamsUsersSimulator.exe'

    def meeting_call(self) -> None:
        process = subprocess.Popen(self.exe_path, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        if process.returncode != 0:
            print('Error:', error.decode('utf-8'))
        else:
            print('Output:', output.decode('utf-8'))


generate = GenerateTeamsMeeting()
if __name__ == '__main__':
    generate.meeting_call()
