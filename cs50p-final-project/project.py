import subprocess

# Execute the "pip --version" command and print the output
result = subprocess.run(['pip', '--version'], capture_output=True, text=True)
print(result.stdout)

# Execute the "bash --login -x" command and print the output
result = subprocess.run(['bash', '--login', '-x'], capture_output=True, text=True)
print(result.stdout)
