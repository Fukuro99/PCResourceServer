import psutil
import subprocess

DEFAULT_ATTRIBUTES = (
    'index',
    'uuid',
    'name',
    'timestamp',
    'memory.total',
    'memory.free',
    'memory.used',
    'utilization.gpu',
    'utilization.memory',
    'temperature.gpu'
)


def get_gpu_info(nvidia_smi_path='nvidia-smi', keys=DEFAULT_ATTRIBUTES, no_units=True):
    nu_opt = '' if not no_units else ',nounits'
    cmd = f'%s --query-gpu=%s --format=csv,noheader%s' % (nvidia_smi_path, ','.join(keys), nu_opt)
    output = subprocess.check_output(cmd, shell=True)
    lines = output.decode().split('\n')
    lines = [ line.strip() for line in lines if line.strip() != '' ]
    return [ { k: v for k, v in zip(keys, line.split(', ')) } for line in lines ]

def get_resource():
    mem = psutil.virtual_memory().percent
    cpu = psutil.cpu_percent(interval=1)
    gpu_info = get_gpu_info()
    gpu_mem = gpu_info[0]["memory.used"]
    gpu_temp = gpu_info[0]["temperature.gpu"]
    return f"cpu:{cpu},mem:{mem},gpu_mem:{gpu_mem},gpu_temp:{gpu_temp}"