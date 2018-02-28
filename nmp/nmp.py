import time


def num():
  curtim = time.time()
  time.sleep(0.1)
  murtim = time.time()
  lurtim = time.time() + (time.time() * murtim) % murtim
  return lurtim
