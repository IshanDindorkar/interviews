import yaml


def read_config(file_path):
    with open(file_path, 'r') as file:
        config = yaml.safe_load(file)
    return config


def main():
    file_path = "utils/config.yaml"
    config = read_config(file_path=file_path)

    # Access the configuration values
    db_host = config['database']['host']
    db_port = config['database']['port']
    db_username = config['database']['username']
    db_password = config['database']['password']

    app_debug = config['app']['debug']
    app_log_file = config['app']['log_file']

    # Use the configuration values in your application logic
    print(f"Database Host: {db_host}")
    print(f"Database Port: {db_port}")
    print(f"Database Username: {db_username}")
    print(f"Database Password: {db_password}")
    print(f"App Debug Mode: {app_debug}")
    print(f"App Log File: {app_log_file}")


if __name__ == "__main__":
    main()

# EOF
