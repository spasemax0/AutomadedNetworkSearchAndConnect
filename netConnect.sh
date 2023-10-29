# Author: spasemax0
log_file="User/Desktop/netscan_logz.txt" # Specify log path, change as needed

scan_and_connect() {
  while true; do
    # Scan for available networks
    nmcli device wifi rescan
    sleep 2

    # Retrieve list of available networks
    open_networks=$(nmcli -t -f SECURITY,SSID device wifi list | grep '^none' | cut -d ':' -f 2)

    # Make connection attempts to each available network
    for network_name in $open_networks; do
      echo "Trying to connect to network: $network_name"
      nmcli device wifi connect "$network_name"
      sleep 10

      # Check if connected
      if nmcli connection show --active | grep -q "$network_name"; then
        echo "Successfully connected to network: $network_name"
        exit 0
      else
        echo "Failed to connect to network: $network_name" >> "$log_file" 
      fi
    done

    # Delay between each scan
    sleep 5
  done
}

# Run the scan_and_connect function
scan_and_connect
