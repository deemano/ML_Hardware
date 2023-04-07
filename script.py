#!/bin/python3
import subprocess

def stopMLs():
    # Stop the depthnet process before starting imagenet
    try:
        subprocess.run(['pkill', '-f', '-2', 'depthnet csi://'])
        subprocess.run(['pkill', '-f', '-2', 'imagenet csi://'])
        subprocess.run(['pkill', '-f', '-2', 'detectnet csi://'])
        subprocess.run(['pkill', '-f', '-2', 'segnet csi://'])
        subprocess.run(['pkill', '-f', '-2', 'posenet csi://'])
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while sending SIGINT to depthnet: {e}")
# ========================================================================

def imagenet():
    # Stop any previous ML models
    try:
        stopMLs()
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while sending SIGINT to depthnet: {e}")

    # Start ML process
    command = "imagenet csi://0 rtp://192.168.0.196:8554"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        print(f"Error executing script: {stderr.decode('utf-8')}")
    else:
        print(f"ML model was stopped: {stdout.decode('utf-8')}")
	#ubprocess.run('ml11.py')#etwork=ssd-inception-v2 csi://0 rtp://192.168.0.197:8554')
#/usr/local/bin/networks/MonoDepth-FCN-Mobilenet/monodepth_fcn_mobilenet.onnx
# ========================================================================

def detectnet():
    # Stop any previous ML models
    try:
        stopMLs()
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while sending SIGINT to depthnet: {e}")

    # Start ML process
    command = "detectnet csi://0 rtp://192.168.0.196:8554"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        print(f"Error executing script: {stderr.decode('utf-8')}")
    else:
        print(f"ML model was stopped: {stdout.decode('utf-8')}")
# ========================================================================

def segnet():
    # Stop any previous ML models
    try:
        stopMLs()
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while sending SIGINT to depthnet: {e}")

    # Start ML process
    command = "segnet csi://0 rtp://192.168.0.196:8554"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        print(f"Error executing script: {stderr.decode('utf-8')}")
    else:
        print(f"ML model was stopped: {stdout.decode('utf-8')}")
# ========================================================================

def posenet():
    # Stop any previous ML models
    try:
        stopMLs()
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while sending SIGINT to depthnet: {e}")

    # Start ML process
    command = "posenet csi://0 rtp://192.168.0.196:8554"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        print(f"Error executing script: {stderr.decode('utf-8')}")
    else:
        print(f"ML model was stopped: {stdout.decode('utf-8')}")

# ========================================================================

def depthnet():
    # Stop any previous ML models
    try:
        stopMLs()
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while sending SIGINT to depthnet: {e}")

    # Start ML process
    command = "depthnet csi://0 rtp://192.168.0.196:8554"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        print(f"Error executing script: {stderr.decode('utf-8')}")
    else:
        print(f"ML model was stopped: {stdout.decode('utf-8')}")


