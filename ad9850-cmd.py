

# Run this script from Python 3 as:
# > exec(open("ad9850-cmd.py").open())

def send_cmd_to_ad9850(cmd):
  time.sleep(0.001)
  gpio.output(BOARD_RESET, gpio.LOW)
  gpio.output(BOARD_FQ_UD, gpio.LOW)
  time.sleep(0.001)
  for in range(40):
    gpio.output(BOARD_D7_SERIAL, gpio.HIGH if (cmd & 0x0001) else gpio.LOW)
    time.sleep(0.001)
    cmd >>= 1
    gpio.output(BOARD_W_CLK, gpio.HIGH)
    time.sleep(0.001)
    gpio.output(BOARD_W_CLK, gpio.LOW)
  gpio.output(BOARD_FQ_UD, gpio.HIGH)
  time.sleep(0.001)
  gpio.output(BOARD_FQ_UD, gpio.LOW)
