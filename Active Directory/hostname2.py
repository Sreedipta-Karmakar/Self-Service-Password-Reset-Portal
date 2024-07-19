import csv
import socket

# Function to load device mappings from CSV
def load_device_mappings(csv_file):
    device_mappings = {}
    try:
        with open(csv_file, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                username = row['username'].strip().lower()  # Strip whitespace and convert to lower case
                hostname = row['hostname'].strip().lower()  # Strip whitespace and convert to lower case
                device_mappings[username] = hostname
        #print(f"Loaded device mappings from '{csv_file}' successfully.")
    except FileNotFoundError:
        print(f"Error: File '{csv_file}' not found.")
    except Exception as e:
        print(f"Error loading '{csv_file}': {e}")
    return device_mappings

# Function to fetch current system hostname
def get_system_hostname():
    hostname = socket.gethostname().lower()  # Convert to lower case
    #print(f"Current system hostname: {hostname}")
    return hostname

# Function to check if hostname matches for given username
def is_hostname_match(username, device_mappings):
    system_hostname = get_system_hostname()
    mapped_hostname = device_mappings.get(username)
    #print(f"Checking hostname match for user '{username}': system_hostname='{system_hostname}', mapped_hostname='{mapped_hostname}'")
    if mapped_hostname:
        return system_hostname == mapped_hostname  # Case insensitive comparison
    else:
        return False

# Main function to handle password reset process
def handle_password_reset(username, csv_file='dataset.csv'):
    device_mappings = load_device_mappings(csv_file)
    # Normalize username input to handle potential case sensitivity and whitespace issues
    normalized_username = username.strip().lower()  # Strip whitespace and convert to lower case
    #print(f"Normalized username: {normalized_username}")
    if normalized_username in device_mappings:
        if is_hostname_match(normalized_username, device_mappings):
            print(f"Hostname match for user '{username}'. Proceeding with password reset.")
            # Add code here to proceed with password reset
        else:
            print(f"Hostname mismatch for user '{username}'. Closing process.")
            # Add code here to close the process
    else:
        print(f"User '{username}' not found in the dataset. Closing process.")
        # Add code here to handle the case where username is not found

# Example usage
if __name__ == "__main__":
    username_to_reset = input("Enter the username to reset password: ")
    handle_password_reset(username_to_reset)
