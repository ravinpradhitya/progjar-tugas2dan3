import socket
import logging
from concurrent.futures import ThreadPoolExecutor

def send_data(nama="kosong"):
    logging.warning(f"thread {nama}")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logging.warning("membuka socket")

    server_address = ('172.16.16.101', 45000)
    logging.warning(f"opening socket {server_address}")
    sock.connect(server_address)

    try:
        # Send data
        message = 'TIME\r\n'
        logging.warning(f"[CLIENT] sending {message}")
        sock.sendall(message.encode('utf-8'))
        # Look for the response
        data = sock.recv(1024).decode('utf-8')
        logging.warning(f"[DITERIMA DARI SERVER] {data}")
    finally:
        logging.warning("closing")
        sock.close()
    return


if __name__=='__main__':
    executor = ThreadPoolExecutor(max_workers=10)

    for i in range(100):
        executor.submit(send_data, nama=f"{i}")

    executor.shutdown(wait=True)