#!/usr/bin/env python3
#Import additional code to complete our task
import shutil
import os

# Move into working directory
os.chdir("/home/student/mycode/")

# Copy the FileA to FileB
shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

#Copy the entire directoryA to directoryB
shutil.copytree("5g_research/", "5g_research_backup/")

