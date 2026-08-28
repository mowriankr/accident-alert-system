import serial
import time

gps = serial.Serial(
    "/dev/serial0",
    baudrate=9600,
    timeout=1
)


def convert_to_decimal(raw, direction):

    if not raw:
        return None

    value = float(raw)

    degrees = int(value / 100)

    minutes = value - (degrees * 100)

    decimal = degrees + minutes / 60

    if direction in ["S", "W"]:
        decimal = -decimal

    return decimal


print("Waiting for GPS data...")

while True:

    try:

        line = gps.readline().decode(
            "utf-8",
            errors="ignore"
        ).strip()

        if line.startswith("$GPGGA") or line.startswith("$GNGGA"):

            parts = line.split(",")

            if len(parts) > 5:

                raw_lat = parts[2]
                lat_direction = parts[3]

                raw_lon = parts[4]
                lon_direction = parts[5]

                if raw_lat and raw_lon:

                    latitude = convert_to_decimal(
                        raw_lat,
                        lat_direction
                    )

                    longitude = convert_to_decimal(
                        raw_lon,
                        lon_direction
                    )

                    print(
                        "Latitude:",
                        latitude,
                        "Longitude:",
                        longitude
                    )

        time.sleep(0.1)

    except KeyboardInterrupt:

        print("\nGPS test stopped.")
        break

    except Exception as e:

        print("GPS Error:", e)
