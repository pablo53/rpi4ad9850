#!/usr/bin/python3

import RPi.GPIO as gpio
import time


class ad9850:
    def __init__(self, pin_fq_ud, pin_w_clk, pin_d7, pin_reset, clk_freq):
        self.pin_fq_ud = pin_fq_ud
        self.pin_w_clk = pin_w_clk
        self.pin_d7 = pin_d7
        self.pin_reset = pin_reset
        self.clk_freq = clk_freq
        self.freq = 0
    def sig_w_clk(self):
        gpio.output(self.pin_w_clk, gpio.HIGH)
        time.sleep(0.00001)
        gpio.output(self.pin_w_clk, gpio.LOW)
        time.sleep(0.00001)
    def sig_fq_ud(self):
        gpio.output(self.pin_fq_ud, gpio.HIGH)
        time.sleep(0.0001)
        gpio.output(self.pin_fq_ud, gpio.LOW)
        time.sleep(0.0001)
    def sig_reset(self):
        gpio.output(self.pin_reset, gpio.HIGH)
        time.sleep(0.00001)
        gpio.output(self.pin_reset, gpio.LOW)
        time.sleep(0.00001)
    def initialize(self):
        self.down()
        self.sig_reset()
        self.sig_w_clk()
        self.sig_fq_ud()
        self.set_freq(1000000)
        self.set_freq(1000000)
    def down(self):
        gpio.output(self.pin_fq_ud, gpio.LOW)
        gpio.output(self.pin_w_clk, gpio.LOW)
        gpio.output(self.pin_d7, gpio.LOW)
        gpio.output(self.pin_reset, gpio.LOW)
    def set_freq(self, freq):
        dphase = round(freq * (2 ** 32) / self.clk_freq) & 0xffffffff
        self.freq = dphase * self.clk_freq / (2 ** 32)
        for b in range(0, 32):
            gpio.output(self.pin_d7, gpio.HIGH if (dphase & 1) else gpio.LOW)
            dphase >>= 1
            time.sleep(0.00001)
            self.sig_w_clk()
        for b in range(0, 8):
            gpio.output(self.pin_d7, gpio.LOW)
            time.sleep(0.00001)
            self.sig_w_clk()
        self.sig_fq_ud()
        self.down()



BOARD_FQ_UD = 15
BOARD_W_CLK = 11
BOARD_D7_SERIAL = 12
BOARD_RESET = 16

gpio.setmode(gpio.BOARD)
gpio.setup(BOARD_FQ_UD, gpio.OUT)
gpio.setup(BOARD_W_CLK, gpio.OUT)
gpio.setup(BOARD_D7_SERIAL, gpio.OUT)
gpio.setup(BOARD_RESET, gpio.OUT)

ad9850ctl = ad9850(BOARD_FQ_UD, BOARD_W_CLK, BOARD_D7_SERIAL, BOARD_RESET, 125000000)



