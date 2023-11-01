import numpy as np
import pycuda.driver as cuda
import pycuda.autoinit
import sys

def generate_vram_load():
    # Retrieve parameters from the request
    vram_load = int(sys.argv[1])
    duration = int(sys.argv[2])
    
    # Calculate the number of bytes to allocate based on the VRAM load percentage
    vram_bytes = int(vram_load / 100.0 * cuda.mem_get_info()[0])
    
    # Create a NumPy array and copy it to the GPU to consume VRAM
    vram_buffer = np.zeros(vram_bytes, dtype=np.uint8)
    gpu_vram_buffer = cuda.mem_alloc(vram_buffer.nbytes)
    cuda.memcpy_htod(gpu_vram_buffer, vram_buffer)
    
    # Specify the number of iterations based on the desired duration
    num_iterations = int(duration)
    
    for i in range(num_iterations):
        # Access the VRAM by reading and writing to the GPU buffer (can be a no-op)
        # You can perform a no-op operation or simply access the data
        # Access the GPU data using gpu_vram_buffer
        print(f"Iteration {i + 1} (VRAM Load)")

generate_vram_load()