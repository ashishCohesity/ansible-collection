import os
import subprocess

# Define the base directory and protoc command options
base_dir = "/home/cohesity/workspace/main/"
protoc_command = [
    "python",
    "-m",
    "grpc_tools.protoc",
    f"-I{base_dir}",
    "--python_out=.",
    "--pyi_out=.",
    "--grpc_python_out=.",
]

# Walk through the directory structure
for root, _, files in os.walk(base_dir):
    for file in files:
        if file.endswith(".proto"):
            proto_file_path = os.path.join(root, file)
            # Construct and run the command for each .proto file
            command = protoc_command + [proto_file_path]
            subprocess.run(command)
