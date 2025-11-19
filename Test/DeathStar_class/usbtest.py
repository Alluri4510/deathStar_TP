import serial
import sys
import platform

def send_file_over_com_port(filename, baudrate=12000000):
    com_port = "COM3"
    try:
        with serial.Serial(com_port, baudrate, timeout=1) as ser:
            with open(filename, 'rb') as file:
                data = file.read()
                ser.write(data)
                print(f"Successfully transmitted {len(data)} bytes over {com_port}.")
    except serial.SerialException as e:
        print(f"Error opening {com_port}: {e}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Example usage
send_file_over_com_port('message.txt')
