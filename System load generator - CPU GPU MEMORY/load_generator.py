import psutil
import time
import math 
import multiprocessing
import subprocess
import threading

from flask import Flask, request, jsonify

app = Flask(__name__)

def generate_gpu_load():
    command = f'/bin/python3.9 /home/ubuntu/gpu_load.py 70 10'
    # print(command)
    subprocess.run(command, shell=True)

def generate_cpu_load():
    start_time = time.time()
    for i in range(int(duration),0,-1):
        while time.time()-start_time < cpu_load/100.0:
            a = math.sqrt(64*64*64*64*64*64*64)
        print(str(i))
        time.sleep(1-cpu_load/100.0)
        start_time += 1

def generate_memory_load():
    memory_usage = (memory_load / 100) * psutil.virtual_memory().total
    b'\x00' * int(memory_usage)
    for i in range(int(duration),0,-1):
        print(str(i))

@app.route('/load', methods=['POST'])
def generate_load():
    global cpu_load, memory_load, duration, cores, vram_load
    data = request.get_json()
    if 'cpu_load' in data.keys() and 'cores' in data.keys():
        cpu_load = data['cpu_load']
        cores = data['cores']
        duration = data['duration']
        processes = []
        for _ in range(int(data['cores'])):
            p = multiprocessing.Process(target =generate_cpu_load)
            p.start()
            processes.append(p)
        # for process in processes:
        #     process.join()  
    if 'memory_load' in data.keys():
        memory_load = data['memory_load']
        duration = data['duration']
        # generate_memory_load()
        a = threading.Thread(target=generate_memory_load)
        a.start()
    if 'vram_load' in data.keys():
        # generate_gpu_load()
        b = threading.Thread(target=generate_gpu_load)
        b.start()
    return jsonify({"message": "Load generated successfully."})

if __name__ == '__main__':
    app.run()