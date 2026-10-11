import os
import subprocess

current_dir = os.path.dirname(os.path.abspath(__file__))
exe_path = os.path.join(current_dir, 'manager', 'snos_manager.exe')

subprocess.Popen(exe_path)
