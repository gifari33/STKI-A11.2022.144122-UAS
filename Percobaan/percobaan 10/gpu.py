import numpy as np
import pyopencl as cl

# Membuat konteks OpenCL
platform = cl.get_platforms()[0]
device = platform.get_devices()[0]
context = cl.Context([device])
queue = cl.CommandQueue(context)

# Mengompilasi kernel OpenCL
kernel_code = """
__kernel void matmul(const int N, __global float* a, __global float* b, __global float* c) {
    int row = get_global_id(0);
    int col = get_global_id(1);
    float sum = 0.0;

    for (int k = 0; k < N; k++) {
        sum += a[row * N + k] * b[k * N + col];
    }

    c[row * N + col] = sum;
}
"""

program = cl.Program(context, kernel_code).build()

# Inisialisasi matriks
N = 1000
a = np.random.rand(N, N).astype(np.float32)
b = np.random.rand(N, N).astype(np.float32)
c = np.zeros((N, N), dtype=np.float32)

# Membuat buffer OpenCL
a_buf = cl.Buffer(context, cl.mem_flags.READ_ONLY | cl.mem_flags.COPY_HOST_PTR, hostbuf=a)
b_buf = cl.Buffer(context, cl.mem_flags.READ_ONLY | cl.mem_flags.COPY_HOST_PTR, hostbuf=b)
c_buf = cl.Buffer(context, cl.mem_flags.WRITE_ONLY, c.nbytes)

# Menjalankan kernel OpenCL
global_size = (N, N)
local_size = None
program.matmul(queue, global_size, local_size, np.int32(N), a_buf, b_buf, c_buf)

# Membaca hasil dari buffer
cl.enqueue_copy(queue, c, c_buf)
queue.finish()

# Memeriksa hasil
print(c)

