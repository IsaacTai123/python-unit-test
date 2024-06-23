# Usage

1. Create a folder for the certificate and name it after the doorbell's ThingName. Use the following command to get the ThingName from the doorbell JSON file:

    ```
    # Run this command on the doorbell to get the ThingName from the JSON file
    cat /data/aws/aws-iot-device.json | jq -r '.IOT.ThingName'

    # Run this command on your project path
    mkdir ./certification/<thing_name>

    ```

2. Copy the certification files from the doorbell the /tmp directory:

    ```
    scp camera@<camear_ip>:/tmp/privkey /tmp/rootca /tmp/cert ./certification/<thing_name>
    ```

3. Modify the `config/setting.yml` file:
    rename setting_example.yml to setting.yml, then make some changes

    ```yml
    thingName: <thing_name>
    ...
    certificates:
    rootca: "certificates/<thing_name>/rootca"
    cert_path: "certificates/<thing_name>/cert"
    private_key: "certificates/<thing_name>/privkey"
    ```

4. Execute 
    Run singal command: python main.py "Set Spotlight Off"
    Run all command: python main.py