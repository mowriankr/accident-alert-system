import smbus2
import math
import time

# MPU6050 address
MPU_ADDR = 0x68

# I2C bus
bus = smbus2.SMBus(1)

# Wake MPU6050
bus.write_byte_data(MPU_ADDR, 0x6B, 0)

print("MPU6050 initialized")
print("Monitoring for accidents...")


def read_word_2c(register):
    high = bus.read_byte_data(MPU_ADDR, register)
    low = bus.read_byte_data(MPU_ADDR, register + 1)

    value = (high << 8) | low

    if value >= 32768:
        value -= 65536

    return value


def read_acceleration():

    acc_x = read_word_2c(0x3B)
    acc_y = read_word_2c(0x3D)
    acc_z = read_word_2c(0x3F)

    x = acc_x / 16384.0
    y = acc_y / 16384.0
    z = acc_z / 16384.0

    total = math.sqrt(x*x + y*y + z*z)

    return total


# Adjust this after testing
ACCIDENT_THRESHOLD = 2.0

while True:

    try:

        acceleration = read_acceleration()

        print("Acceleration:", round(acceleration, 2), "g")

        if acceleration > ACCIDENT_THRESHOLD:

            print("🚨 ACCIDENT DETECTED!")

            # Later we will call GPS + Telegram here

            time.sleep(5)

        time.sleep(1)

    except KeyboardInterrupt:

        print("\nMonitoring stopped.")
        break

    except Exception as e:

        print("Error:", e)
        time.sleep(2)
