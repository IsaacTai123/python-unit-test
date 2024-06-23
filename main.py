# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
from awscrt import io, mqtt
from awsiot import mqtt_connection_builder
import sys
import time
import json
import csv
import datetime
import inspect
import re 
from pub_payload import *
from schema import *
from common import *
from jsonschema import validate
from jsonschema.exceptions import ValidationError

pub_topic = config["publish_topic"] % (config["thingName"])
sub_request_topic = config["subcribe_request_topic"] % (config["thingName"])
sub_event_topic = config["subcrib_event_topic"] % (config["thingName"])


timeout_functions =[]
had_response = True
one_command = False
published_payloads = {}
event_function_name = ""

formatted_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
report_path = f"test_result_{formatted_datetime}.csv"
# report_path = f"test_result.csv"

def replace_csv_row(new_row):
    
    function_name = new_row['Auc Function']
    if function_name == "Set Stop Streaming":
        return
    
    # Read the CSV file into a list of dictionaries
    rows = []
    
    if os.path.isfile(report_path):
        with open(report_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                rows.append(row)
    
    existed = False
    # Find the row with the specified search key in the "Auc Function" column
    for i, row in enumerate(rows):
        if row['Auc Function'] == function_name:
            # Replace the row with the new data
            rows[i] = new_row
            existed = True
            break
        
    if not existed:
        rows.append(new_row)
    
    # Write the updated rows back to the CSV file
    fieldnames = rows[0].keys()
    with open(report_path, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
 
def compare_event(sub_payload):
    resource = sub_payload["resource"]
    op = sub_payload["event"]["op"]
    
    if op == "n+d":
        if resource == "/chime":
            # log_message("{:<60}".format(f"Received message with [{event_function_name}] function"),True)
            validate(instance=sub_payload["event"]["cn"],
                    schema=aws_r_kvs_video_event)
        elif resource == "/aiSensor":
            # log_message("{:<60}".format(f"Received message with [AI_ML Event] function"),True)
            validate(instance=sub_payload["event"]["cn"],
                    schema=aws_r_ai_sensor)
        elif resource == "/pirSensor":
            # log_message("{:<60}".format(f"Received message with [PIR Event] function"),True)
            validate(instance=sub_payload["event"]["cn"],
                    schema=aws_r_kvs_video_event)
        elif resource == "/video_interval":
          
            validate(instance=sub_payload["event"]["cn"],
                    schema=aws_r_videointerval)
        elif resource == "/ir_sensor":
            validate(instance=sub_payload["event"]["cn"],
                     schema=aws_r_autoLight)
        else:
            raise ValueError(
                "the'resource' is not present in the current test case.")
        
def compare_command(pub_payload, sub_payload):

    resource = pub_payload["resource"]
    op = pub_payload["command"]["op"]

    assert pub_payload["resource"] == sub_payload[
        "resource"], f"{resource} 'resource' is mismatch"
    assert sub_payload["format"] == "OCF", f"{resource} 'format' is mismatch"

    if op == "r":
        assert sub_payload["response"][
            "ri"] == "request-1", f"{resource} 'ri' is mismatch"
        assert sub_payload["response"][
            "rs"] == "200", f"{resource} 'rs' is mismatch"

        if resource == "/ir_sensor":
            validate(instance=sub_payload["response"]["cn"],
                     schema=aws_r_autoLight)

        elif resource == "/maintenance/settings":
            validate(instance=sub_payload["response"]["cn"],
                     schema=aws_r_settings_camera)

        elif resource == "/hdr":
            validate(instance=sub_payload["response"]["cn"],
                     schema=oic_r_switch_binary)

        elif resource == "/audio_volume":
            validate(instance=sub_payload["response"]["cn"],
                     schema=oic_r_audio)

        elif resource == "/maintenance/info":
            validate(instance=sub_payload["response"]["cn"],
                     schema=aws_r_info_camera)

        elif resource == "/maintenance/processing":
            validate(instance=sub_payload["response"]["cn"],
                     schema=oic_r_switch_binary)

        elif resource == "/maintenance/video_settings":
            validate(instance=sub_payload["response"]["cn"],
                     schema=aws_r_settings_video)

        elif resource == "/audio_recording":
            validate(instance=sub_payload["response"]["cn"],
                     schema=oic_r_switch_binary)

        elif resource == "/spotlight":
            validate(instance=sub_payload["response"]["cn"],
                     schema=aws_r_autoLight)

        elif resource == "/maintenance/event_trigger_settings":
            validate(instance=sub_payload["response"]["cn"],
                     schema=aws_r_settings_eventTrigger)

        elif resource == "/chime":
            validate(instance=sub_payload["response"]["cn"],
                     schema=aws_r_kvs_video_event)

        elif resource == "/siren":
            validate(instance=sub_payload["response"]["cn"],
                     schema=oic_r_switch_binary)

        elif resource == "/audio_playback":
            validate(instance=sub_payload["response"]["cn"],
                     schema=aws_r_audio_state)    
        elif resource == "/video":
            validate(instance=sub_payload["response"]["cn"],
                     schema=aws_r_kvsstream)

        else:
            raise ValueError(
                "the 'resource' is not present in the current test case.")

    elif op == "u":
        assert sub_payload["response"][
            "ri"] == "request-1", f"{resource} 'ri' is mismatch"
        assert sub_payload["response"]["rs"] in [
            "200", "204"
        ], f"{resource} 'rs' is mismatch"

        if resource == "/ir_sensor":
            validate(instance=sub_payload["response"]["cn"],
                     schema=aws_r_autoLight)
            validate(instance=pub_payload["command"]["cn"],
                     schema=aws_r_autoLight)

        elif resource == "/maintenance/settings":
            validate(instance=sub_payload["response"]["cn"],
                     schema=aws_r_settings_camera)
            validate(instance=pub_payload["command"]["cn"],
                     schema=aws_r_settings_camera)

        elif resource == "/hdr":
            validate(instance=sub_payload["response"]["cn"],
                     schema=oic_r_switch_binary)
            validate(instance=pub_payload["command"]["cn"],
                     schema=oic_r_switch_binary)

        elif resource == "/audio_volume":
            validate(instance=sub_payload["response"]["cn"],
                     schema=oic_r_audio)
            validate(instance=pub_payload["command"]["cn"], schema=oic_r_audio)

        elif resource == "/audio_playback":
            validate(instance=sub_payload["response"]["cn"],
                     schema=aws_r_audio_state)
            validate(instance=pub_payload["command"]["cn"],
                     schema=aws_r_audio_state)

        elif resource == "/maintenance/processing":
            validate(instance=sub_payload["response"]["cn"],
                     schema=oic_r_switch_binary)
            validate(instance=pub_payload["command"]["cn"],
                     schema=oic_r_switch_binary)

        elif resource == "/video":
            validate(instance=sub_payload["response"]["cn"],
                     schema=aws_r_kvsstream)
            validate(instance=pub_payload["command"]["cn"],
                     schema=aws_r_kvsstream)

        elif resource == "/maintenance/video_settings":
            validate(instance=sub_payload["response"]["cn"],
                     schema=aws_r_settings_video)
            validate(instance=pub_payload["command"]["cn"],
                     schema=aws_r_settings_video)

        elif resource == "/audio_recording":
            validate(instance=sub_payload["response"]["cn"],
                     schema=oic_r_switch_binary)
            validate(instance=pub_payload["command"]["cn"],
                     schema=oic_r_switch_binary)

        elif resource == "/maintenance/reboot":
            validate(instance=sub_payload["response"]["cn"],
                     schema=oic_r_switch_binary)
            validate(instance=pub_payload["command"]["cn"],
                     schema=oic_r_switch_binary)

        elif resource == "/spotlight":
            validate(instance=sub_payload["response"]["cn"],
                     schema=aws_r_autoLight)
            validate(instance=pub_payload["command"]["cn"],
                     schema=aws_r_autoLight)

        elif resource == "/maintenance/deRegistration":
            validate(instance=sub_payload["response"]["cn"],
                     schema=aws_r_deRegistration)
            validate(instance=pub_payload["command"]["cn"],
                     schema=aws_r_deRegistration)

        elif resource == "/siren":
            validate(instance=sub_payload["response"]["cn"],
                     schema=oic_r_switch_binary)
            validate(instance=pub_payload["command"]["cn"],
                     schema=oic_r_switch_binary)

        elif resource == "/maintenance/event_trigger_settings":
            validate(instance=pub_payload["command"]["cn"],
                     schema=aws_r_settings_eventTrigger)

        elif resource == "/maintenance/deRegistration":
            validate(instance=sub_payload["response"]["cn"],
                     schema=aws_r_deRegistration)
            validate(instance=pub_payload["command"]["cn"],
                     schema=aws_r_deRegistration)
        # didn't define schema
        elif resource == "/audio_files_download":
            pass
        elif resource == "/face_group_vectors_download":
            pass
        elif resource == "/activity_zones":
            pass
        # only for internal force stop recording streaming
        elif resource == "/sop_streaming":
            pass
        else:
            raise ValueError(
                "the 'resource' is not present in the current test case.")

    elif op == "c":
        assert sub_payload["response"][
            "ri"] == "request-1", f"{resource} 'ri' is mismatch"
        assert sub_payload["response"]["rs"] in [
            "200", "204"
        ], f"{resource} 'rs' is mismatch"
        
        if resource == "/video":
            validate(instance=sub_payload["response"]["cn"],
                     schema=aws_r_kvsstream)
            validate(instance=pub_payload["command"]["cn"],
                     schema=aws_r_kvsstream)
        elif resource == "/onboard":
            validate(instance=pub_payload["command"]["cn"],
                     schema=aws_r_onboard)
            pass
        else:
            raise ValueError(
                "the 'resource' is not present in the current test case.")
    else:
        raise ValueError("the 'op' is not present in the current test case.")

# Callback when connection is accidentally lost.
def on_connection_interrupted(connection, error, **kwargs):
    log_error(f"Connection interrupted. error: {error}", True)

# Callback when an interrupted connection is re-established.
def on_connection_resumed(connection, return_code, session_present, **kwargs):
    print(
        f"Connection resumed. return_code: {return_code} session_present: {session_present}"
    )

    if return_code == mqtt.ConnectReturnCode.ACCEPTED and not session_present:
        print("Session did not persist. Resubscribing to existing topics...")
        resubscribe_future, _ = connection.resubscribe_existing_topics()

        # Cannot synchronously wait for resubscribe result because we're on the connection's event-loop thread,
        # evaluate result with a callback instead.
        resubscribe_future.add_done_callback(on_resubscribe_complete)

def on_resubscribe_complete(resubscribe_future):
    resubscribe_results = resubscribe_future.result()
    print(f"Resubscribe results: {resubscribe_results}")

    for topic, qos in resubscribe_results['topics']:
        if qos is None:
            sys.exit(f"Server rejected resubscribe to topic: {topic}")

# Callback when the subscribed topic receives a message
def on_message_received(topic, payload, dup, qos, retain, **kwargs):

    sub_payload = json.loads(payload.decode('utf-8'))
    resource = sub_payload["resource"]
    test_result = ""
    error_message = ""
    function = ""
    
    if topic == sub_event_topic:
       
        if  sub_payload["resource"] == "/video_interval":
            mode = (sub_payload["event"]["cn"]["mode"]).capitalize()
            function = f"{event_function_name} Video Interval - {mode}"
        elif  sub_payload["resource"] == "/ir_sensor":
            function = "IR Event"
        else:
            function = event_function_name
        
        if function != "IR Event":
            log_message("{:<60}".format(f"Received message with [{function}] function"),True)
            
        try:
            compare_event(sub_payload)
            test_result = "pass"
        except (AssertionError, ValueError, ValidationError) as error:
            test_result = "fail"
            error_message = error
        replace_csv_row({'Auc Function': function, 'Test Result': test_result, 'Error Message': error_message, 'Publish Payload': "", 'Subscribe Payload':  json.dumps(sub_payload)})
           
    # Only the requested command needs to be compared for correctness.
    elif topic == sub_request_topic:
        if resource not in published_payloads:
            return
        pub_payload = published_payloads[resource]["content"]
        function = published_payloads[resource]["function"]

        log_message("{:<60}".format(f"Received message with [{function}] function"),True)
        
        try:
            compare_command(pub_payload, sub_payload)
            test_result = "pass"
        except (AssertionError, ValueError, ValidationError) as error:
            test_result = "fail"
            error_message = error

        global timeout_functions
        if function in timeout_functions:
            timeout_functions.remove(function)
        else:
            replace_csv_row({'Auc Function': function, 'Test Result': test_result, 'Error Message': error_message, 'Publish Payload':  json.dumps(pub_payload), 'Subscribe Payload':  json.dumps(sub_payload)})
           
        global had_response
        had_response = True
        del published_payloads[resource]

def setup_connection():
    # Spin up resources
    event_loop_group = io.EventLoopGroup(1)
    host_resolver = io.DefaultHostResolver(event_loop_group)
    client_bootstrap = io.ClientBootstrap(event_loop_group, host_resolver)
    proxy_options = None

    mqtt_connection = mqtt_connection_builder.mtls_from_path(
        endpoint=config["endpoint"],
        port=8883,
        cert_filepath=config["certificates"]['cert_path'],
        pri_key_filepath=config["certificates"]['private_key'],
        client_bootstrap=client_bootstrap,
        ca_filepath=config["certificates"]['rootca'],
        on_connection_interrupted=on_connection_interrupted,
        on_connection_resumed=on_connection_resumed,
        client_id=f'{config["thingName"]}-pc',
        clean_session=False,
        keep_alive_secs=5,
        http_proxy_options=proxy_options)

    print(
        f"Connecting to {config['endpoint']} with client ID '{config['thingName']}'..."
    )

    #Connect to the gateway
    while True:
        try:
            connect_future = mqtt_connection.connect()
            # Future.result() waits until a result is available
            connect_future.result()
        except Exception as e:
            print("Connection to IoT Core failed...  retrying in 5s.")
            log_error(e, True)
            time.sleep(5)
            continue
        else:
            print("Connected!")
            break
    return mqtt_connection

def subscribe_topic(mqtt_connection,topic):
    # Subscribe topic
    # topics = [sub_request_topic, sub_event_topic]
 
    subscribe_future, packet_id = mqtt_connection.subscribe(topic=topic,qos=mqtt.QoS.AT_LEAST_ONCE,callback=on_message_received)
    subscribe_result = subscribe_future.result()
    print(f"Subscribed '{topic}' with qos {subscribe_result['qos']}")

def run_one_command(function_name):
    for filename in os.listdir(os.getcwd()):
        if not filename.endswith('.csv'):
            continue
    
    max_timestamp = 0
    global report_path
    match = re.search(r'test_result_(\d{8}_\d{6})\.csv', filename)
    if match:
        timestamp = int(match.group(1))
        print(timestamp)
        if timestamp > max_timestamp:
            max_timestamp = timestamp
            report_path = filename
    
    exists_command = False
    published_data = ""
    
    for command in all_commands:
        variable_name = next((name for name, value in globals().items()
                              if value is command and name != 'command'), None)
        command = globals()[variable_name]
    
        if command["function"] == function_name:
            message_json = json.dumps(command["content"])
            published_payloads[command["content"]["resource"]] = command

            log_message(
                f'Publishing message with [{command["function"]}] function.',
                True)
            mqtt_connection.publish(topic=pub_topic,
                                    payload=message_json,
                                    qos=mqtt.QoS.AT_MOST_ONCE)
            exists_command = True
            published_data = command
            

    if not exists_command:
        raise ValueError(
            f"The command [{function_name}] is not present in the current test case."
        )
    wait_one_response(published_data)

def wait_one_response(published_data):
    
    wait_seconds = 1
    global had_response
    global timeout_functions
    global one_command 
    
    function_name = published_data['function']
    if function_name in timeout_functions:
        timeout_functions.remove(function_name)
    
    one_command = True
    had_response = False
    while not had_response:
        time.sleep(1)
        print(
            f"waitting [{published_data['function']}] testcase response with {wait_seconds} seconds...."
        )
        wait_seconds += 1
        if wait_seconds > 10:
            timeout_functions.append(published_data['function'])
            replace_csv_row({'Auc Function': published_data['function'], 'Test Result': 'fail', 'Error Message': 'Response Timeout: Please check your network connection', 'Publish Payload': published_data["content"], 'Subscribe Payload': ''})
            
            break

def wait_responses(commands_list,index):
    # Waiting for the previously published MQTT response.
    wait_seconds = 1
    global had_response
    global timeout_functions
    
    while not had_response:
        time.sleep(1)
        published_data = commands_list[index - 1]
        function_name = published_data['function']
        if function_name  in timeout_functions:
            timeout_functions.remove(function_name)
        print(f"waitting [{published_data['function']}] testcase response with {wait_seconds} seconds....")
        wait_seconds += 1
        if wait_seconds > 10:
            timeout_functions.append(function_name)
            replace_csv_row({'Auc Function': published_data['function'], 'Test Result': 'fail', 'Error Message': 'Response Timeout: Please check your network connection', 'Publish Payload': published_data["content"], 'Subscribe Payload': ''})
            
            break

    had_response = False

def run_all_commands(commands_list):
    if os.path.isfile(report_path):
        os.remove(report_path)


    for index, data in enumerate(commands_list):
        if data["function"] == "Set All Event Trigger":
            continue

        wait_responses(commands_list,index)

        payload = data["content"]
        payload["ts"] = int(time.time())
        resource = payload["resource"]
        published_payloads[resource] = data

        log_message(
            "{:<60}".format(
                f'Published message with [{data["function"]}] function'), True)

        message_json = json.dumps(payload)
        mqtt_connection.publish(topic=pub_topic,
                                payload=message_json,
                                qos=mqtt.QoS.AT_MOST_ONCE)

    wait_responses(commands_list,len(commands_list))
    
    
def enable_event_trigger(event_trigger):
    
    chime_enable = 0
    pir_enable = 0
    ai_enable = 0
    
    if event_trigger == "ChimeButton":
         chime_enable = 1
    elif event_trigger == "PIR":
        pir_enable = 1 
    elif event_trigger == "AI_ML":
        ai_enable = 1
    else:
        raise ValueError("Your event trigger is not supported. Please check your event trigger.")
        
    trigger_json = set_event_trigger
    enable_trigger = trigger_json["content"]["command"]["cn"]
    enable_trigger["Common"]["CloudRecord-CoolingDurationTime"] = 10
    
    trigger_values = {
        "AI_ML": ai_enable,
        "ChimeButton": chime_enable,
        "PIR": pir_enable
    }

    for trigger_ai in ["Animal","Body","Package","Vehicle"]:
        enable_trigger["AI_ML"][trigger_ai]["Action-CloudRecord-PostRollTime"] = 10
        enable_trigger["AI_ML"][trigger_ai]["Action-CloudRecord-PreRollTim"]  = 10
        enable_trigger["AI_ML"][trigger_ai]["Action-CloudRecord-Time"]  = 20
        enable_trigger["AI_ML"][trigger_ai]["Action-CloudRecord-MaxTime"]  = 30
        
        for action_key in ["Action-CloudRecord-Enable", "Action-Always", "Action-Enable","Action-MQTT"]:
            enable_trigger["AI_ML"][trigger_ai][action_key] = trigger_values["AI_ML"]
        enable_trigger["AI_ML"][trigger_ai]["Action-CloudRecord-RecordingType"] = 0
        
    for other_trigger in ["ChimeButton","PIR"]:
        enable_trigger[other_trigger]["Action-CloudRecord-PostRollTime"] = 10
        enable_trigger[other_trigger]["Action-CloudRecord-PreRollTim"]  = 10
        enable_trigger[other_trigger]["Action-CloudRecord-Time"]  = 20
        enable_trigger[other_trigger]["Action-CloudRecord-MaxTime"]  = 30
        enable_setting = trigger_values[other_trigger]
        for action_key in ["Action-CloudRecord-Enable", "Action-Always", "Action-Enable","Action-MQTT"]:
            enable_trigger[other_trigger][action_key] = enable_setting
        
    return  json.dumps(trigger_json["content"]) 

def run_event_testing(command):
    log_message("{:<60}".format(f'Starting test [{command}] function'), True)
    global event_function_name
    event_function_name = command
    subscribe_topic(mqtt_connection, sub_event_topic)
    
    mqtt_connection.publish(topic=pub_topic,
                            payload=set_stop_streaming["content"],
                            qos=mqtt.QoS.AT_MOST_ONCE)
    
    mqtt_connection.publish(topic=pub_topic,
                            payload=enable_event_trigger(command.split()[0]),
                            qos=mqtt.QoS.AT_MOST_ONCE)
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("stopping event testing...")


if __name__ == "__main__":
    mqtt_connection = setup_connection()
    event_command_lists = ["AI_ML Event","ChimeButton Event", "PIR Event"]


    command = sys.argv[1] if len(sys.argv) > 1 else None

    if command:
        if command in event_command_lists:
            run_event_testing(command)
        else:
            subscribe_topic(mqtt_connection, sub_request_topic)
            run_one_command(command)
    else:
        subscribe_topic(mqtt_connection, sub_request_topic)
        run_all_commands(all_commands)
        for command in event_command_lists:
            run_event_testing(command)

        # run_all_commands(reboot_and_deRegistration_command)


