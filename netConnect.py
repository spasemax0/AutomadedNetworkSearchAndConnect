#Author: spasemax0
import subprocess
import time

def scan_and_connect():
    log_file = 'connection_log.txt'  # Specify the path and filename for the log file

    while True:
        # Scan for available networks
        subprocess.run(['nmcli', 'device', 'wifi', 'rescan'])

        # Retrieve network information
        result = subprocess.run(['nmcli', '-t', '-f', 'SECURITY,SSID', 'device', 'wifi', 'list'], capture_output=True, text=True)
        output = result.stdout

        # Process network information
        networks = [line.split(':')[1] for line in output.splitlines()]
        open_networks = [network for network in networks if network.startswith('none')]

        if open_networks:
            # Connect to the first open network found
            network_name = open_networks[0].split(':')[1]
            subprocess.run(['nmcli', 'device', 'wifi', 'connect', network_name])

            # Delay to allow time for connection to establish
            time.sleep(10)

            # Check if the connection was successful
            result = subprocess.run(['nmcli', 'connection', 'show'], capture_output=True, text=True)
            output = result.stdout

            if network_name in output:
                # Connection successful, break the loop
                break
            else:
                # Log the failed connection attempt
                with open(Desktop/netscan_logz.txt, 'a') as f:
                    f.write(f'Failed to connect to network: {network_name}\n')

        # Delay between each scan
        time.sleep(5)

# Run the scan_and_connect function
scan_and_connect()
