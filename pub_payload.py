import time
import random
import datetime
from common import config

set_schedule_manual_vedio ={
    "function":"Set Schudule Manual Video",
    "content":{
        "thingName": "IP_CAMERA_THING",
        "resource": "/video",
        "ri": "request-1",
        "format": "OCF",
        "command": {
            "uri": "auc://IP_CAMERA_THING/video",
            "op": "c",
            "cn": {
                "rt": ["aws.r.kvsstream"],
                "if": ["oic.if.a","oic.if.baseline"],
                "modes": "start",
                "media":
                {
                    "datetime": (datetime.datetime.utcnow() + datetime.timedelta(seconds=10)).strftime("%Y-%m-%dT%H:%M:%SZ"), 
                    "duration": 10, 
                    "destination": "manual" 
                }
            }
        },
        "ts": int(time.time()),
    }
}


set_manual_vedio ={
    "function":"Set Manual Video",
    "content":{
        "thingName": "IP_CAMERA_THING",
        "resource": "/video",
        "ri": "request-1",
        "format": "OCF",
        "command": {
            "uri": "auc://IP_CAMERA_THING/video",
            "op": "c",
            "cn": {
                "rt": ["aws.r.kvsstream"],
                "if": ["oic.if.a","oic.if.baseline"],
                "modes": "start",
                "media":
                {
                    "datetime": "", 
                    "duration": 10, 
                    "destination": "manual" 
                }
            }
        },
        "ts": int(time.time()),
    }
}

get_chime ={
    "function":"Get Chime",
    "content":{
        "thingName": "IP_CAMERA_THING",
        "resource": "/chime",
        "format": "OCF",
        "ts": int(time.time()),
        "ri": "request-1",
        "command": {
            "uri": "auc://IP_CAMERA_THING_NAME/chime",
            "ri": "request-1",
            "op": "r"
        }
    }
}

get_device_info = {
    "function":"Get Device Info",
    "content":{
        "thingName": "IP_CAMERA_THING",
        "resource": "/maintenance/info",
        "format": "OCF",
        "ts": int(time.time()),
        "ri": "request-1",
        "command": {
            "uri": "auc://IP_CAMERA_THING_NAME/maintenance/info",
            "ri": "request-1",
            "op": "r"
        }
    }
}

set_privacy_mode_on ={
    "function":"Set Privacy Mode On",
    "content":{
        "thingName": "IP_CAMERA_THING",
        "resource": "/maintenance/processing",
        "format": "OCF",
        "ts": int(time.time()),
        "ri": "request-1",
        "command": {
            "uri": "auc://IP_CAMERA_THING_NAME/maintenance/processing",
            "ri": "request-1",
            "op": "u",
            "cn": {
                "rt": ["oic.r.switch.binary"],
                "if": ["oic.if.a","oic.if.baseline"],
                "value": True
            }
        }
    }
}

get_privacy_mode = {
    "function":"Get Privacy Mode",
    "content":{
        "thingName": "IP_CAMERA_THING",
        "resource": "/maintenance/processing",
        "format": "OCF",
        "ts": int(time.time()),
        "ri": "request-1",
        "command": {
            "uri": "auc://IP_CAMERA_THING_NAME/maintenance/processing",
            "ri": "request-1",
            "op": "r"
        }
    }
}

set_privacy_mode_off ={
    "function":"Set Privacy Mode Off",
    "content":{
        "thingName": "IP_CAMERA_THING",
        "resource": "/maintenance/processing",
        "format": "OCF",
        "ts": int(time.time()),
        "ri": "request-1",
        "command": {
            "uri": "auc://IP_CAMERA_THING_NAME/maintenance/processing",
            "ri": "request-1",
            "op": "u",
            "cn": {
                "rt": ["oic.r.switch.binary"],
                "if": ["oic.if.a","oic.if.baseline"],
                "value": False
            }
        }
    }
}


set_night_mode_message = {
    "function":"Set Night Mode",
    "content":{
        "thingName": "IP_CAMERA_THING",
        "resource": "/ir_sensor",
        "format": "OCF",
        "ts": int(time.time()),
        "ri": "request-1",
        "command": {
            "uri": "auc://IP_CAMERA_THING_NAME/ir_sensor",
            "ri": "request-1",
            "op": "u",
            "cn": {
                "rt": [ "aws.r.autoLight" ],
                "if": [ "oic.if.a","oic.if.baseline"],
                "supportedModes": ["auto", "on", "off"],
                "mode": random.choice(["auto", "on", "off"])
            }
        }
    }
}

get_night_mode_message ={
    "function":"Get Night Mode",
    "content":{
        "thingName": "IP_CAMERA_THING",
        "resource": "/ir_sensor",
        "format": "OCF",
        "ts": int(time.time()),
        "ri": "request-1",
        "command": {
            "uri": "auc://IP_CAMERA_THING_NAME/ir",
            "ri": "request-1",
            "op": "r"
        }
    }
}

set_video_config = {
    "function":"Set Video Config",
    "content":{
        "thingName": "IP_CAMERA_THING",
        "resource": "/maintenance/settings",
        "format": "OCF",
        "ts": int(time.time()),
        "ri": "request-1",
        "command": {
            "uri": "auc://IP_CAMERA_THING_NAME/maintenance/settings",
            "ri": "request-1",
            "op": "u",
            "cn": {
                "rt": ["aws.r.settings.camera"],
                "if": ["oic.if.rw","oic.if.baseline"],
                # "h265Encoding": random.choice([True,False]),
                "irThreshold":  random.randint(1, 99),
                "aiDetectionLED": random.choice([True,False]),
                "timeZone": "UTC",
                "pirSensitivity": random.choice([1,3]),
                "chimeType":random.randint(0, 2),
                "imageRotate": random.choice([0,3])
            }
        }
    }
}

get_video_config = {
    "function":"Get Video Config",
    "content":{
        "thingName": "IP_CAMERA_THING",
        "resource": "/maintenance/settings",
        "format": "OCF",
        "ts": int(time.time()),
        "ri": "request-1",
        "command": {
            "uri": "auc://IP_CAMERA_THING_NAME/maintenance/settings",
            "ri": "request-1",
            "op": "r"
        }
    }
}

set_auto_HDR_config ={
    "function":"Set Auto HDR Config",
    "content":{
        "thingName": "IP_CAMERA_THING",
        "resource": "/hdr",
        "format": "OCF",
        "ts": int(time.time()),
        "ri": "request-1",
        "command": {
            "uri": "auc://IP_CAMERA_THING_NAME/hdr",
            "ri": "request-1",
            "op": "u",
            "cn": {
                "rt": [
                    "oic.r.switch.binary"
                ],
                "if": [
                    "oic.if.a","oic.if.baseline"
                ],
                "value": random.choice([True, False])
            }
        }
    }
}

get_auto_HDR_config ={
    "function":"Get Auto HDR Config",
    "content":{
        "thingName": "IP_CAMERA_THING",
        "resource": "/hdr",
        "format": "OCF",
        "ts": int(time.time()),
        "ri": "request-1",
        "command": {
            "uri": "auc://IP_CAMERA_THING_NAME/hdr",
            "ri": "request-1",
            "op": "r"
        }
    }
}

set_speaker_volume = {
    "function":"Set Speaker Volume",
    "content":{
        "thingName": "IP_CAMERA_THING",
        "resource": "/audio_volume",
        "format": "OCF",
        "ts": int(time.time()),
        "ri": "request-1",
        "command": {
            "uri": "auc://IP_CAMERA_THING_NAME/audio_volume",
            "ri": "request-1",
            "op": "u",
            "cn": {
                "rt": ["oic.r.audio"],
                "if": ["oic.if.a","oic.if.baseline"],
                "volume": random.choice([0,1,2,3]),
                "mute":  random.choice([True,False])
            }
        }
    }
}
  
get_speaker_volume = {
    "function":"Get Speaker Volume",
    "content":{
        "thingName": "IP_CAMERA_THING",
        "resource": "/audio_volume",
        "format": "OCF",
        "ts": int(time.time()),
        "ri": "request-1",
        "command": {
            "uri": "auc://IP_CAMERA_THING_NAME/audio_volume",
            "ri": "request-1",
            "op": "r"
        }
    }
}

set_play_audio_file = {
    "function":"Set Play Audio File",
    "content":{
        "thingName": "IP_CAMERA_THING",
        "resource": "/audio_playback",
        "format": "OCF",
        "ts": int(time.time()),
        "ri": "request-1",
        "command": {
            "uri": "auc://IP_CAMERA_THING_NAME/audio_playback",
            "ri": "request-1",
            "op": "u",
            "cn": {
                "rt": [ "aws.r.audio.state" ],
                "if": [ "oic.if.a","oic.if.baseline" ],
                "jobStates": ["playing", "stopped"],
                "language": "",
                "selectedFile": f"file://m1.mp3",
                "currentJobState":"playing"
            }
        }
    }
}

get_play_audio_file = {
    "function":"Get Play Audio file",
    "content":{
        "thingName": "IP_CAMERA_THING",
        "resource": "/audio_playback",
        "format": "OCF",
        "ts": int(time.time()),
        "ri": "request-1",
        "command": {
            "uri": "auc://IP_CAMERA_THING_NAME/audio_playback",
            "ri": "request-1",
            "op": "r"
        }
    }
}

set_stop_audio_file = {
    "function":"Set Stop Audio File",
    "content":{
        "thingName": "IP_CAMERA_THING",
        "resource": "/audio_playback",
        "format": "OCF",
        "ts": int(time.time()),
        "ri": "request-1",
        "command": {
            "uri": "auc://IP_CAMERA_THING_NAME/audio_playback",
            "ri": "request-1",
            "op": "u",
            "cn": {
                "rt": [ "aws.r.audio.state" ],
                "if": [ "oic.if.a","oic.if.baseline" ],
                "jobStates": ["playing", "stopped"],
                "language": "",
                "selectedFile": f"file://m1.mp3",
                "currentJobState":"stopped"
            }
        }
    }
}


get_video_upload =  {
    "function":"Get Video Upload",
    "content":{
        "thingName": "IP_CAMERA_THING",
        "resource": "/video",
        "format": "OCF",
        "ts": int(time.time()),
        "ri": "request-1",
        "command": {
            "uri": "auc://IP_CAMERA_THING/video",
            "ri": "request-1",
            "op": "r"
        }
    }
}

set_video_setting = {
    "function":"Set Video Setting",
    "content":{
        "thingName": "IP_CAMERA_THING",
        "resource": "/maintenance/video_settings",
        "format": "OCF",
        "ts": int(time.time()),
        "ri": "request-1",
        "command": {
            "uri": "auc://IP_CAMERA_THING_NAME/maintenance/video_settings",
            "ri": "request-1",
            "op": "u",
            "cn": {
                "rt": ["aws.r.settings.video"],
                "if": ["oic.if.rw","oic.if.baseline"],
                "videoQuality": random.choice([1920,1440,960,480]),
                "h265Encoding": random.choice([True,False]),
                "frameRate": random.choice([1, 5, 10, 15, 20, 25, 30]),
                "bitrateMode": random.choice([0,1]),
                "bitrateMin": random.randint(64000,1000000),
                # "bitrateMax": random.randint(512000,4000000),
                "bitrateMax": random.randint(1100000,4000000),
            }
        }
    }

}

get_video_setting = {
    "function":"Get Video Setting",
    "content":{
        "thingName": "IP_CAMERA_THING",
        "resource": "/maintenance/video_settings",
        "format": "OCF",
        "ts": int(time.time()),
        "ri": "request-1",
        "command": {
            "uri": "auc://IP_CAMERA_THING_NAME/maintenance/video_settings",
            "ri": "request-1",
            "op": "r"
        }
    }
}

set_audio_recoding = {
    "function":"Set Audio Recoding",
    "content":{
        "thingName": "IP_CAMERA_THING_NAME",
        "resource": "/audio_recording",
        "format": "OCF",
        "ts": int(time.time()),
        "ri": "request-1",
        "command": {
            "uri":"auc://IP_CAMERA_THING_NAME/audio_recording",
            "ri": "request-1",
            "op": "u",
            "cn": {
                "rt": ["oic.r.switch.binary"],
                "if": ["oic.if.a","oic.if.baseline"],    
                "value": random.choice([True,False])
            }
        }
    }
}

get_audio_recording = {
    "function":"Get Audio Recording",
    "content":{
        "thingName": "IP_CAMERA_THING",
        "resource": "/audio_recording",
        "format": "OCF",
        "ts":  int(time.time()),
        "ri": "request-1",
        "command": {
            "uri": "auc://IP_CAMERA_THING_NAME/audio_recording",
            "ri": "request-1",
            "op": "r"
        }
    }
}

set_spotlight_on = {
    "function":"Set Spotlight On",
    "content":{
        "thingName": "IP_CAMERA_THING_NAME",
        "resource": "/spotlight",
        "format": "OCF",
        "ts": int(time.time()),
        "ri": "request-1",
        "command": {
            "uri":"auc://IP_CAMERA_THING_NAME/spotlight",
            "ri": "request-1",
            "op": "u",
            "cn": {
                "rt": ["aws.r.autoLight"],
                "if": ["oic.if.a"],
                "mode": "on"
            }
        }
    }
 }
 
get_spotlight = {
    "function":"Get Spotlight",
    "content":{
            "thingName": "IP_CAMERA_THING",
            "resource": "/spotlight",
            "format": "OCF",
            "ts": int(time.time()),
            "ri": "request-1",
            "command": {
                "uri":"auc://IP_CAMERA_THING_NAME/spotlight",
                "ri": "request-1",
                "op": "r"
            }
    }
}
 
set_spotlight_off = {
    "function":"Set Spotlight Off",
    "content":{
    "thingName": "IP_CAMERA_THING_NAME",
    "resource": "/spotlight",
    "format": "OCF",
    "ts":int(time.time()),
    "ri": "request-1",
    "command": {
        "uri":"auc://IP_CAMERA_THING_NAME/spotlight",
        "ri": "request-1",
        "op": "u",
        "cn": {
            "rt": ["aws.r.autoLight"],
            "if": ["oic.if.a"],
            "mode": "off"
        }
    }
}

 }


set_siren_on ={
    "function":"Set Siren On",
    "content":{
        "thingName": "IP_CAMERA_THING_NAME",
        "resource": "/siren",
        "format": "OCF",
        "ts": int(time.time()),
        "ri": "request-1",
        "command" :{
            "uri": "auc://IP_CAMERA_THING_NAME/siren",
            "ri": "request-1",
            "op": "u",
            "cn": {
                "rt": ["oic.r.switch.binary"],
                "if": ["oic.if.a","oic.if.baseline"],
                "value": True   
            }
        }
    }
}

set_siren_off ={
    "function":"Set Siren Off",
    "content":{
        "thingName": "IP_CAMERA_THING_NAME",
        "resource": "/siren",
        "format": "OCF",
        "ts": int(time.time()),
        "ri": "request-1",
        "command" :{
            "uri": "auc://IP_CAMERA_THING_NAME/siren",
            "ri": "request-1",
            "op": "u",
            "cn": {
                "rt": ["oic.r.switch.binary"],
                "if": ["oic.if.a","oic.if.baseline"],
                "value": False   
            }
        }
    }
}

get_siren = {
    "function":"Get Siren",
    "content":{
        "thingName": "IP_CAMERA_THING",
        "resource": "/siren",
        "format": "OCF",
        "ts": int(time.time()),
        "ri": "request-1",
        "command": {
            "uri": "auc://IP_CAMERA_THING_NAME/siren",
            "ri": "request-1",
            "op": "r"
        }
    }
}

set_event_trigger ={
    "function": "Set Event Trigger",
    "content": {
        "thingName": "IP_CAMERA_THING_NAME",
        "resource": "/maintenance/event_trigger_settings",
        "format": "OCF",
        "ts": int(time.time()),
        "ri": "request-1",
        "command": {
            "uri": "auc://IP_CAMERA_THING_NAME/maintenance/event_trigger_settings",
            "ri": "request-1",
            "op": "u",
            "cn": {
                "rt": ["aws.r.settings.eventTrigger"],
                "if": ["oic.if.rw","oic.if.baseline"],
                "version": 4,
                "AI_ML": {
                    "Animal": {
                        "Action-CloudRecord-Enable":  random.choice([0,1]),
                        "Action-CloudRecord-MaxTime": random.randint(0, 2147483647),
                        "Action-CloudRecord-PostRollTime": random.randint(0, 2147483647),
                        "Action-CloudRecord-PreRollTime": random.randint(0, 10),
                        "Action-CloudRecord-RecordingType": random.choice([0,1]),
                        "Action-CloudRecord-Time": random.randint(0, 2147483647),
                        "Action-MQTT": random.choice([0,1]),
                        "Action-Always": random.choice([0,1]),
                        "Action-Enable": 0,
                        "Action-OnDay": [random.choice([0,1]), random.choice([0,1]), random.choice([0,1]), random.choice([0,1]), random.choice([0,1]), random.choice([0,1]), random.choice([0,1])]
                    },
                    "Body": {
                        "Action-CloudRecord-Enable": random.choice([0,1]),
                        "Action-CloudRecord-MaxTime": random.randint(0, 2147483647),
                        "Action-CloudRecord-PostRollTime": random.randint(0, 2147483647),
                        "Action-CloudRecord-PreRollTime": random.randint(0, 10),
                        "Action-CloudRecord-RecordingType": random.choice([0,1]),
                        "Action-CloudRecord-Time": random.randint(0, 2147483647),
                        "Action-MQTT": random.choice([0,1]),
                        "Action-Always": random.choice([0,1]),
                        "Action-Enable": 0,
                        "Action-OnDay":  [random.choice([0,1]), random.choice([0,1]), random.choice([0,1]), random.choice([0,1]), random.choice([0,1]), random.choice([0,1]), random.choice([0,1])]
                    },
                    "Package": {
                        "Action-CloudRecord-Enable": random.choice([0,1]),
                        "Action-CloudRecord-MaxTime": random.randint(0, 2147483647),
                        "Action-CloudRecord-PostRollTime": random.randint(0, 2147483647),
                        "Action-CloudRecord-PreRollTime": random.randint(0, 10),
                        "Action-CloudRecord-RecordingType": random.choice([0,1]),
                        "Action-CloudRecord-Time": random.randint(0, 2147483647),
                        "Action-MQTT": random.choice([0,1]),
                        "Action-Always": random.choice([0,1]),
                        "Action-Enable": 0,
                        "Action-OnDay":  [random.choice([0,1]), random.choice([0,1]), random.choice([0,1]), random.choice([0,1]), random.choice([0,1]), random.choice([0,1]), random.choice([0,1])]
                    },
                    "Vehicle": {
                        "Action-CloudRecord-Enable": random.choice([0,1]),
                        "Action-CloudRecord-MaxTime": random.randint(0, 2147483647),
                        "Action-CloudRecord-PostRollTime": random.randint(0, 2147483647),
                        "Action-CloudRecord-PreRollTime": random.randint(0, 10),
                        "Action-CloudRecord-RecordingType": random.choice([0,1]),
                        "Action-CloudRecord-Time": random.randint(0, 2147483647),
                        "Action-MQTT": random.choice([0,1]),
                        "Action-Always": random.choice([0,1]),
                        "Action-Enable": 0,
                        "Action-OnDay":  [random.choice([0,1]), random.choice([0,1]), random.choice([0,1]), random.choice([0,1]), random.choice([0,1]), random.choice([0,1]), random.choice([0,1])]
                    }
                },
                "ChimeButton": {
                    "Action-CloudRecord-Enable": random.choice([0,1]),
                    "Action-CloudRecord-MaxTime": random.randint(0, 2147483647),
                    "Action-CloudRecord-PostRollTime": random.randint(0, 2147483647),
                    "Action-CloudRecord-PreRollTime": random.randint(0, 10),
                    "Action-CloudRecord-RecordingType": random.choice([0,1]),
                    "Action-CloudRecord-Time": random.randint(0, 2147483647),
                    "Action-MQTT": random.choice([0,1]),
                    "Action-Always": random.choice([0,1]),
                    "Action-Enable": 0,
                    "Action-OnDay":  [random.choice([0,1]), random.choice([0,1]), random.choice([0,1]), random.choice([0,1]), random.choice([0,1]), random.choice([0,1]), random.choice([0,1])]
                },
                "Common": {
                    "CloudRecord-CoolingDurationTime": random.randint(0, 2147483647)
                },
                "PIR": {
                    "Action-CloudRecord-Enable": random.choice([0,1]),
                    "Action-CloudRecord-PreRollTime": random.randint(0, 10),
                    "Action-CloudRecord-RecordingType": random.choice([0,1]),
                    "Action-CloudRecord-Time": random.randint(0, 2147483647),
                    "Action-MQTT": random.choice([0,1]),
                    "Action-Always": random.choice([0,1]),
                    "Action-Enable": 0,
                    "Action-OnDay": [random.choice([0,1]), random.choice([0,1]), random.choice([0,1]), random.choice([0,1]), random.choice([0,1]), random.choice([0,1]), random.choice([0,1])]
                },
                "SCHEDULE": {
                    "Enable": 0,
                    "OnDay":  [random.choice([0,1]), random.choice([0,1]), random.choice([0,1]), random.choice([0,1]), random.choice([0,1]), random.choice([0,1]), random.choice([0,1])]
                }
            }
        }
    }
}

get_event_trigger = {
    "function":"Get Event Trigger",
    "content":{
            "thingName": "IP_CAMERA_THING",
            "resource": "/maintenance/event_trigger_settings",
            "format": "OCF",
            "ts": int(time.time()),
            "ri": "request-1",
            "command": {
                "uri":"auc://IP_CAMERA_THING_NAME/maintenance/event_trigger_settings",
                "ri": "request-1",
                "op": "r"
            }
    }
}

set_stop_streaming = {
    "function":"Set Stop Streaming",
    "content":{
        "thingName": "IP_CAMERA_THING_NAME",
        "resource": "/sop_streaming",
        "format": "OCF",
        "ts": int(time.time()),
        "ri": "request-1",
        "command" :{
            "uri": "auc://IP_CAMERA_THING_NAME/siren",
            "ri": "request-1",
            "op": "u",
            "cn": {
                "rt": ["oic.r.switch.binary"],
                "if": ["oic.if.a","oic.if.baseline"],
                "value": True   
            }
        }
    }
}

set_videoOnboard = {
    "function": "Set Video Onboard",
    "content": {
        "thingName": "IP_CAMERA_THING",
        "resource": "/onboard",
        "ri": "request-1",
        "format": "OCF",
        "ts": int(time.time()),
        "command": {
            "uri": "auc://IP_CAMERA_THING/onboard",
            "op": "c",
            "cn": {
                "rt": ["aws.r.onboard"],
                "if": ["oic.if.rw"],
                "kvsBundle": {
                    "event": { 
                        "name": f'SH20-eventStream-{config["thingName"]}',
                        "arn": "arn:aws:kinesisvideo:ca-central-1:123456789012:stream/SH20-eventStream-device01/1234567890123"
                    },
                    "manual": {
                        "name": f'SH20-manualStream-{config["thingName"]}',
                        "arn": "arn:aws:kinesisvideo:ca-central-1:123456789012:stream/SH20-manualStream-device01/1234567890123"
                    },
                    "device": {
                        "name": f'SH20-deviceStream-{config["thingName"]}',
                        "arn": "arn:aws:kinesisvideo:ca-central-1:123456789012:stream/SH20-deviceStream-device01/1234567890123"
                    },
                    "live": { 
                        "name": f'SH20-liveChannel-{config["thingName"]}',
                        "arn": "arn:aws:kinesisvideo:ca-central-1:123456789012:channel/SH20-liveChannel-device01/1234567890123"
                    },
                },
                "iotBundle": {
                    "region": "ca-central-1",
                    "iotEndpoint": "abc08n9hm6123-ats.iot.ca-central-1.amazonaws.com",
                    "credential": {
                        "credentialEndpoint": "abc3tl3g6q123.credentials.iot.ca-central-1.amazonaws.com",
                        "roleAlias": "kvsAccessRoleAlias"
                    }
                }
            }
        }
    }
}  

set_activity_zones = {
    "function": "Set Activity Zones",
    "content": {
        "thingName": "IP_CAMERA_THING_NAME",
        "resource": "/activity_zones",
        "format": "OCF",
        "ts": int(time.time()),
        "ri": "request-1",
        "command": {
            "uri": "auc://IP_CAMERA_THING_NAME/activity_zones",
            "ri": "request-1",
            "op": "u",
            "cn": {
                "rt": ["aws.r.ai.zones"],
                "if": ["oic.if.rw"],
                # "payload": '{"BodyVA_zone":[[[0,0],[320,0],[320,240],[0,240]]],"AnimalVA_zone":[[[0,0],[320,0],[320,240],[0,240]]],"VehicleVA_zone":[[[0,0],[320,0],[320,240],[0,240]]],"PackageVA_zone":[[[0,0],[320,0],[320,240],[0,240]]]}',
                #default value 
                "payload": '{"AnimalVA_zone":[[[0,0],[640,0],[640,480],[0,480]]],"BodyVA_zone":[[[0,0],[640,0],[640,480],[0,480]]],"PackageVA_zone":[[[0,0],[640,0],[640,480],[0,480]]],"VehicleVA_zone":[[[0,0],[640,0],[640,480],[0,480]]]}',
            }
        }
    }
}

# The Url will expire
audio_download = {
    "function": "Audio File Download",
    "content": {
        "thingName": "IP_CAMERA_THING",
        "resource": "/audio_files_download",
        "format": "OCF",
        "ts": int(time.time()),
        "ri": "request-1",
        "command": {
            "uri": "auc://IP_CAMERA_THING_NAME/audio_files_download",
            "ri": "request-1",
            "op": "u",
            "cn": {
                "rt": ["aws.r.s3Download"],
                "if": ["oic.if.r"],
                "language": "NA_English",
                "files": [
                    {
                        "location":"https://fxn-ota-verification-bucket-ca-central-1.s3.ca-central-1.amazonaws.com/OTA/otaFile/testModel/AUDIO_FILE/v0.0.1/smooth-ac-guitar-loop-93bpm-137706_9af12089daea259fc346c0099e97e1ad.wav?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaDmFwLW5vcnRoZWFzdC0yIkYwRAIgNzeCUJsptAWkSBQnH8k70lZgvjK4jhJRKTyCi94U%2FJ8CIHzadw7NkUfAtBvgvHO6zM5kVK09noivUe6uIFIBXYHfKvQDCOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNTM0NjA3NDM2ODY0Igz0BfVPqIYU6gRsuU4qyAMKkfGU4oKDGz1nTRRVdrXZ7t9t3qf1PUIrjS56jPqC8jjeOWADgeTrHzjDIoA3XqeUpdMZJ4VElkyc37AskORaxDFWOMZlhu17%2BZ0n5T3R103R8dXne3%2Bw24hqeoyx1ZBzz0v7QsXnmrnzULxu1Fp0nzzTFSJFcNluuxPFMD4m2nzQnritvgGtj3QgmykcNVGaHZwljv1YMZOshnMa1eT2VTgPgUaLZqQ8Zo4oOJVZDYvP5P1m8GvKIwObrMVl4ufsR%2BqFY4sgY%2B7wwTA4juPm9O%2FvZRcKgwwBfqZeradKSKSWqmMGzsZPsSIOekx4LGjJJhp1JRNaYff2BwbTti77A8IL8tg1CeJEPIhfsN%2BqZohj%2ByYVAKIeHmiqK%2BE2wM35acrmwLF3c6BFH3B8Vs%2BWwD51M8m6JKruBdc0aaABIgobfCgjG0NNauYayYeV0au5OiI%2Fmk4LMkGa%2BApTwJNpc%2BpMhZWU0%2FDCKNe%2BYD1OAJyHbyuXxREbalrAn7jxNFDC7Y%2BbTYREE%2BZeYxCDWK64glxVxInkt%2FS%2Fppij8rqJJqEl%2BsetX1mocrb1S3yNUDP4g6jqjFM7EH5wWGFFcnWhq4v%2BaMapp9MwrqzcrQY6lQJXMrzJuHV0NW%2Bvzp65GHEVGicJTMyMfkgpbXW0L8ysdOBCu7s82CXog5sEcljM9aSp36h9F6fsrOeExzS3kF4PsYX1X%2FBXzJky%2F%2BKYkqo%2Ff6rEaebrrXqQh%2BS79lG9Et5Ao21OBvqgJh937Oyj5%2B79VtMPVs%2BDAzkjpr2N16w4bCN1j%2B65DfjCsGOu3JokvCggUCyWYU8jCPntc602%2BkgBi0X7wy4H4kxpt1bt7ORJN%2FtcbiX4eQWb%2F4AAxx4eB9aU6NwZsDuJ%2FODRNkhHQDsQOgFuSavl55MCGzhcXuWZ0P2TOKNlZBrDA6ZQeJqOw0RajiOvRhLo1IaEE5zShbdXUGDwUXdb9PK04G%2FtaVDbazHxDel5&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20240129T030706Z&X-Amz-SignedHeaders=host&X-Amz-Expires=43200&X-Amz-Credential=ASIAXY6IWDRAGMJA3BM7%2F20240129%2Fca-central-1%2Fs3%2Faws4_request&X-Amz-Signature=5d02c9a0839ee83be623c8c7d7358a0f5ff7a972d5939e14fe794815ee562443",
                    },				
                ]
            }
        }
    }
}

face_vector_download = {
    "function": "Face Vector File Download",
    "content": {
        "thingName": "IP_CAMERA_THING",
        "resource": "/face_group_vectors_download",
        "format": "OCF",
         "ts": int(time.time()),
        "ri": "request-1",
        "command": {
            "uri": "auc://IP_CAMERA_THING_NAME/face_group_vectors_download",
            "ri": "request-1",
            "op": "u",
            "cn": {
                "rt": ["aws.r.s3Download"],
                "if": ["oic.if.rw"],
                "files": [
                    {
                        "location":"https://fxn-ota-verification-bucket-ca-central-1.s3.ca-central-1.amazonaws.com/OTA/otaFile/testModel/FACE_VECOTR/v0.0.1/20240125-083843_FaceVector_02.jsonl?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aDmFwLW5vcnRoZWFzdC0xIkgwRgIhAJDnAfsZ6lFf44O39I5XiYoVSJswov29hqtTD9sz3SCRAiEA85ZtzFppCquiuyMJY1XyTFUAQ%2BVBleGJmbMzzwCNi9Mq9AMI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw1MzQ2MDc0MzY4NjQiDAybLsF0%2Fa%2FSv0gtwCrIA59aNSk5yH7B8ugx2bnnu%2FDzJKiL3v9xTfTU1RU1LB61VKAAAyBUG1DbKr6ZXLRMcG5D0LsXpCmvA4F%2BadfEWxHgAVNrl7Qql%2FJvRbAQ5A%2BlFgV47A1D4Dinvj1IrOBkHNdnqcod8yKK8OCf5U5HvINxRHMaw2BHNzkC91v3hvkjX3UmNTttLCpg6zTc7XQbuetia1ITPE7qSSmkdMXaH7JvjX83R9G30KUilyl1gbDsnQHkNT4TaSD%2FwvWG1eYpLcUPKXnh7ZbYnh%2FQWgQJ1aA9Vj2AsVg1Pg6IzFLZwmxxeY9iVRFeW%2Fa%2FqVeZVamPP3%2B1JRujZNCFNyIN3aY4ehUOCG1VNsCyKMez6p5L8K%2BsiDyTyDS3fT8OJ2Z7d4r%2FfQI%2FXhH3QL3XVNjJxD%2FL1Nye9U%2BUvdfZheUOyP5RqBqGeRax54KU45PdkJf6WU520ClmT%2Bp8913DS90CoOcdv2jsF2UiJTEcp%2B137KFueqIqxIllf%2BqIc7zc%2FLHkNQr2G4ZSaQJ1QV2VSwTOaafgJedyfsUnzrbsHsSKI2duj7mfWtRCB%2FRm9jW1y08BXzbgfAHlTnX2wyU2ENhufeMp2HXoI9HTG1z%2FvTCi%2FNytBjqTAt7COsZwJdhgjQwOq5Z6Ln3ee4%2FyVf0GnuJA69Hxy%2BVOzhP8TDbGLm5Ni4Z0LIFCJKZ7Q3fSg4hQgjlhMDTZ%2BXE6JwqXk6xq6ycJLObVgA9XH9oYO7frtBEZEviBLGTzx011jjrAUuG1okPk616540rcW597RM3IWIPlAbtdwjOpRDDfmgNkRsva2b38hg27Gr6j1LltTz1MAgCAHouLrBhDgy3a1nsMb029sLy9zTV05JqT3X0MuQBqd2sE077q0nwVrIUJPvNI2SAO6MIEM6VzPzRBRR%2FgAM7e1%2BdlyJtzJK1qsmqxPXGWAzdwaDSPcNS2We6k5ThKsz06abXvh7zh9hRjwMoc8XDL60NXbmk1p1tt&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20240129T055730Z&X-Amz-SignedHeaders=host&X-Amz-Expires=43200&X-Amz-Credential=ASIAXY6IWDRAJ43E445T%2F20240129%2Fca-central-1%2Fs3%2Faws4_request&X-Amz-Signature=378ae457253a8442669caeb66c2499affa96cc5e431bbe78adf481b73f9d473b",
                    },				
                ]
            }
        }
    }
}

set_all_event_trigger ={
    "function": "Set All Event Trigger",
    "content": {
        "thingName": "IP_CAMERA_THING_NAME",
        "resource": "/maintenance/event_trigger_settings",
        "format": "OCF",
        "ts": int(time.time()),
        "ri": "request-1",
        "command": {
            "uri": "auc://IP_CAMERA_THING_NAME/maintenance/event_trigger_settings",
            "ri": "request-1",
            "op": "u",
            "cn": {
                "rt": ["aws.r.settings.eventTrigger"],
                "if": ["oic.if.rw","oic.if.baseline"],
                "version": 4,
                "AI_ML": {
                    "Animal": {
                        "Action-CloudRecord-Enable":  random.choice([0,1]),
                        "Action-CloudRecord-MaxTime": 30,
                        "Action-CloudRecord-PostRollTime":10,
                        "Action-CloudRecord-PreRollTime": 10,
                        "Action-CloudRecord-RecordingType": 1,
                        "Action-CloudRecord-Time": 20,
                        "Action-MQTT": 1,
                        "Action-Always": 1,
                        "Action-Enable": 1,
                        "Action-OnDay": [random.choice([0,1]), random.choice([0,1]), random.choice([0,1]), random.choice([0,1]), random.choice([0,1]), random.choice([0,1]), random.choice([0,1])]
                    },
                    "Body": {
                        "Action-CloudRecord-Enable": 1,
                        "Action-CloudRecord-MaxTime": 30,
                        "Action-CloudRecord-PostRollTime":10,
                        "Action-CloudRecord-PreRollTime": 10,
                        "Action-CloudRecord-RecordingType": 1,
                        "Action-CloudRecord-Time": 20,
                        "Action-MQTT": 1,
                        "Action-Always": 1,
                         "Action-Enable":1,
                        "Action-OnDay":  [random.choice([0,1]), random.choice([0,1]), random.choice([0,1]), random.choice([0,1]), random.choice([0,1]), random.choice([0,1]), random.choice([0,1])]
                    },
                    "Package": {
                        "Action-CloudRecord-Enable": 1,
                        "Action-CloudRecord-MaxTime": 30,
                        "Action-CloudRecord-PostRollTime":10,
                        "Action-CloudRecord-PreRollTime": 10,
                        "Action-CloudRecord-RecordingType": 1,
                        "Action-CloudRecord-Time": 20,
                        "Action-MQTT": 1,
                        "Action-Always": 1,
                         "Action-Enable":1,
                        "Action-OnDay":  [random.choice([0,1]), random.choice([0,1]), random.choice([0,1]), random.choice([0,1]), random.choice([0,1]), random.choice([0,1]), random.choice([0,1])]
                    },
                    "Vehicle": {
                        "Action-CloudRecord-Enable": 1,
                        "Action-CloudRecord-MaxTime": 30,
                        "Action-CloudRecord-PostRollTime":10,
                        "Action-CloudRecord-PreRollTime": 10,
                        "Action-CloudRecord-RecordingType": 1,
                        "Action-CloudRecord-Time": 20,
                        "Action-MQTT": 1,
                        "Action-Always": 1,
                         "Action-Enable":1,
                        "Action-OnDay":  [random.choice([0,1]), random.choice([0,1]), random.choice([0,1]), random.choice([0,1]), random.choice([0,1]), random.choice([0,1]), random.choice([0,1])]
                    }
                },
                "ChimeButton": {
                    "Action-CloudRecord-Enable": 1,
                    "Action-CloudRecord-MaxTime": 30,
                    "Action-CloudRecord-PostRollTime":10,
                    "Action-CloudRecord-PreRollTime": 10,
                    "Action-CloudRecord-RecordingType": 1,
                    "Action-CloudRecord-Time": 20,
                    "Action-MQTT": 1,
                    "Action-Always": 0,
                     "Action-Enable":1,
                    "Action-OnDay":  [random.choice([0,1]), random.choice([0,1]), random.choice([0,1]), random.choice([0,1]), random.choice([0,1]), random.choice([0,1]), random.choice([0,1])]
                },
                "Common": {
                    "CloudRecord-CoolingDurationTime": 10,
                },
                "PIR": {
                    "Action-CloudRecord-Enable": 1,
                    "Action-CloudRecord-PreRollTime": 10,
                    "Action-CloudRecord-RecordingType": 1,
                    "Action-CloudRecord-Time": 20,
                    "Action-MQTT": 1,
                    "Action-Always": 1,
                    "Action-Enable":1,
                    "Action-OnDay": [random.choice([0,1]), random.choice([0,1]), random.choice([0,1]), random.choice([0,1]), random.choice([0,1]), random.choice([0,1]), random.choice([0,1])]
                },
                "SCHEDULE": {
                    "Enable": 0,
                    "OnDay":  [random.choice([0,1]), random.choice([0,1]), random.choice([0,1]), random.choice([0,1]), random.choice([0,1]), random.choice([0,1]), random.choice([0,1])]
                }
            }
        }
    }
}

set_manual_vedio ={
    "function":"Set Manual Video",
    "content":{
        "thingName": "IP_CAMERA_THING",
        "resource": "/video",
        "ri": "request-1",
        "format": "OCF",
        "command": {
            "uri": "auc://IP_CAMERA_THING/video",
            "op": "c",
            "cn": {
                "rt": ["aws.r.kvsstream"],
                "if": ["oic.if.a","oic.if.baseline"],
                "modes": "start",
                "media":
                {
                    "datetime": "", 
                    "duration": 10, 
                    "destination": "manual" 
                }
            }
        },
        "ts": int(time.time()),
    }
}



all_commands = [set_schedule_manual_vedio,set_privacy_mode_on,get_privacy_mode,
                set_privacy_mode_off,set_event_trigger,get_chime,
                set_night_mode_message,get_night_mode_message,
                set_video_config,get_video_config,set_auto_HDR_config, 
                get_auto_HDR_config,set_speaker_volume,get_speaker_volume,
                get_device_info,get_play_audio_file,set_play_audio_file, 
                set_stop_audio_file,get_video_setting,get_video_upload,
                set_video_setting,get_audio_recording, set_audio_recoding,
                get_spotlight,set_spotlight_on,set_spotlight_off,get_siren,
                set_siren_on,set_siren_off,get_event_trigger,set_videoOnboard, 
                set_activity_zones,audio_download, face_vector_download, 
                set_stop_streaming,set_all_event_trigger,set_manual_vedio]





set_reboot = {
    "function":"Set Reboot",
    "content":{
        "thingName": "IP_CAMERA_THING",
        "resource": "/maintenance/reboot",
        "format": "OCF",
        "ts": int(time.time()),
        "ri": "request-1",
        "command": {
            "uri": "auc://IP_CAMERA_THING_NAME/maintenance/reboot",
            "ri": "request-1",
            "op": "u",
            "cn": {
                "rt": ["oic.r.switch.binary"],
                "if": ["oic.if.a","oic.if.baseline"],
                "value": False   
            }
        }
    }
}

set_deRegistration ={
    "function": "Set deRegistration",
    "content": {
        "thingName": "IP_CAMERA_THING_NAME",
        "resource": "/maintenance/deRegistration",
        "format": "OCF",
        "ts": int(time.time()),
        "ri": "request-1",
        "command": {
            "uri": "auc://IP_CAMERA_THING_NAME/maintenance/deRegistration",
            "ri": "request-1",
            "op": "u",
            "cn": {
                "rt": ["aws.r.deRegistration"],
                "if": ["oic.if.a"],
                "value": f"deRegister {config['thingName']}"
            }
        }
    }
}    

reboot_and_deRegistration_command = [set_reboot,set_deRegistration]

