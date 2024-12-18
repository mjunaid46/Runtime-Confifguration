import os
import subprocess
import sys
# Define the container name and the path to the new config file
CONTAINER_NAME = "test-dynamic_config_app-1"
UPDATED_CONFIG_PATH = "./new_config2.ini"
DEST_PATH = "/app/config2.ini"  # Path inside the container
def find_container(container_name):
    """Check if the container with the given name is running."""
    try:
        # Use docker ps to find the container ID
        result = subprocess.run(
            ["docker", "ps", "--filter", f"name={container_name}", "--format", "{{.ID}}"],
            capture_output=True,
            text=True,
            check=True
        )
        container_id = result.stdout.strip()
        if not container_id:
            print(f"Error: No running container found with name '{container_name}'")
            sys.exit(1)
        return container_id
    except subprocess.CalledProcessError as e:
        print(f"Error while finding container: {e}")
        sys.exit(1)
def copy_file_to_container(container_id, source_path, dest_path):
    """Copy a file from the host to the container."""
    try:
        # Use docker cp to copy the file
        subprocess.run(
            ["docker", "cp", source_path, f"{container_id}:{dest_path}"],
            check=True
        )
        print(f"File '{source_path}' copied to '{dest_path}' in container {container_id}.")
    except subprocess.CalledProcessError as e:
        print(f"Error while copying file: {e}")
        sys.exit(1)
def main():
    # Check if the updated config file exists on the host
    if not os.path.exists(UPDATED_CONFIG_PATH):
        print(f"Error: The file '{UPDATED_CONFIG_PATH}' does not exist.")
        sys.exit(1)
    # Find the container ID
    container_id = find_container(CONTAINER_NAME)
    # Copy the updated config file to the container
    copy_file_to_container(container_id, UPDATED_CONFIG_PATH, DEST_PATH)
if __name__ == "__main__":
    main()