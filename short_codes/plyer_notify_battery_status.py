import time
from plyer import battery
from plyer import notification

b_state = battery.get_state()

isCharging = b_state["isCharging"]
percentage = b_state["percentage"]

msg = f"Is charging: {isCharging},\n"
msg = msg + f"Percentage: {percentage}%"

notification.notify(
    title = "Battery status!",
    message = msg,
    timeout = 10,
    # app_icon = "/home/usman/Desktop/media/usman.jpg"
)