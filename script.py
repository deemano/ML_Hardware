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
        subprocess.run(['pkill', '-f', '-2', 'imagenet --model=/home/deeman/jetson-inference/python/training/classification/models/kiwi2/resnet18.onnx --input_blob=input_0 --output_blob=output_0 --labels=/home/deeman/jetson-inference/python/training/classification/data/kiwi2/labels.txt csi://0 rtp://192.168.0.196:8554'])
        subprocess.run(['pkill', '-f', '-2', 'actionnet csi://'])
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while sending SIGINT to the model: {e}")
# ========================================================================

def imagenet():
    # Stop any previous ML models
    try:
        stopMLs()
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while sending SIGINT ML: {e}")

    # Start ML process
    command = "imagenet csi://0 rtp://192.168.0.196:8554"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        print(f"Error executing script: {stderr.decode('utf-8')}")
    else:
        print(f"ML model was stopped: {stdout.decode('utf-8')}")

# ========================================================================

def detectnet():
    # Stop any previous ML models
    try:
        stopMLs()
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while sending SIGINT to model: {e}")

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
        print(f"Error occurred while sending SIGINT to model: {e}")

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
        print(f"Error occurred while sending SIGINT to model: {e}")

    # Start ML process
    command = "posenet csi://0 rtp://192.168.0.196:8554"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        print(f"Error executing script: {stderr.decode('utf-8')}")
    else:
        print(f"ML model was stopped: {stdout.decode('utf-8')}")

# ========================================================================

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

# ========================================================================

def kiwi():
    # Stop any previous ML models
    try:
        stopMLs()
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while sending SIGINT to depthnet: {e}")

    # Start ML process
    # This trained CNN cannot run outside Jetson container
    # Here is an attempt to start container and run model and stream it + kill it
    command = "imagenet --model=/home/deeman/jetson-inference/python/training/classification/models/kiwi2/resnet18.onnx --input_blob=input_0 --output_blob=output_0 --labels=/home/deeman/jetson-inference/python/training/classification/data/kiwi2/labels.txt csi://0 rtp://192.168.0.196:8554"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        print(f"Error executing Kiwi_noKiwi script: {stderr.decode('utf-8')}")
    else:
        print(f"ML model was stopped: {stdout.decode('utf-8')}")

# ==============================================================

def action():
    print("Starting action() function...")# Stop any previous ML models
    try:
        print("Trying to stop previous ML models...")
        stopMLs()
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while sending SIGINT to actionnetnet: {e}")

# Run action3.sh script
    action3_sh_path = "/home/deeman/jetson-inference/action3.sh"
    process_action3 = subprocess.Popen(action3_sh_path, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)#, cwd="/home/deeman/jetson-inference")
    logger.info(f"action3.sh process started with PID: {process_action3.pid}")
    print(f"action3.sh process started with PID: {process_action3.pid}")  # Print the process ID

    # Wait for the action3.sh script to finish
    #while process_action3.poll() is None:
        #stdout_line = process_action3.stdout.readline().decode('utf-8')
        #if stdout_line:
            #logger.info(f"action3.sh output: {stdout_line}") #print(f"action3.sh output: {stdout_line}")

    stdout, stderr = process_action3.communicate()
    if process_action3.returncode != 0:
        print(f"Error executing action3.sh: {stderr.decode('utf-8')}")
        return

    # Stop the Docker container when the user changes the model or chooses to close
    try:
        print("Stopping the Docker container...")
        stopMLs()
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while sending SIGINT to depthnet: {e}")
    else:
        print(f"ML model was stopped: {stdout.decode('utf-8')}")
