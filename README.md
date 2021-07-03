# rpi4ad9850

AD9850 controlled by Raspberry Pi in Python 3.

## usage:

1. Connect AD9850 to Raspberry PI.

2. In the current directory, open Python 3 in Your Raspbian on Rasberry PI:

```> python3```

3. In Python, issue the following command to load the necessary script:

```> exec(open("ad9850ctl.py").read())```

4. Then, initialize AD9850:

```> ad9850ctl.initialize()```

5. From now on, set a required frequency [Hz] as per Your needs, whenever You want:

```> ad9850ctl.set_freq(2000000)```
