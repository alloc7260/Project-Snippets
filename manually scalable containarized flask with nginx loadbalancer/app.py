from flask import Flask
import socket

app = Flask(__name__)

def get_container_id():
    try:
        with open('/proc/self/cgroup', 'r') as f:
            for line in f:
                if 'docker' in line:
                    return line.split('/')[-1].strip()
    except Exception as e:
        return str(e)

@app.route('/')
def get_hostname():
    host = socket.gethostname()
    return f'Hostname: {host}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
