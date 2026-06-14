from logger import listener

print("Keyboard Event Logger Started")
print("Press ESC to stop")

listener.start()
listener.join()

print("Logger Stopped")