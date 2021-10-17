from git_automation import Git
from projects import Directories
from process import Process
import os



git = Git("path to the project folder where .git file is located")
directories = Directories(git=git)
process = Process(git=git, directories=directories)
process.run_process()

