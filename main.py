from picamera2 import Picamera2, Preview
import time

# Create camera objects
picam0 = Picamera2(0)
picam1 = Picamera2(1)

# Create preview configurations
config0 = picam0.create_preview_configuration()
config1 = picam1.create_preview_configuration()

# Configure cameras
picam0.configure(config0)
picam1.configure(config1)

# Start previews - position them side by side
picam0.start_preview(Preview.QTGL, x=0, y=0, width=800, height=600)
picam1.start_preview(Preview.QTGL, x=800, y=0, width=800, height=600)

# Start cameras
picam0.start()
picam1.start()

try:
    # Run until Ctrl+C is pressed
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Stopping cameras...")
finally:
    # Clean up
    picam0.stop()
    picam1.stop()