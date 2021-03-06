'''record audio frames
send audio frames (callback which just sticks into play)
play audio frames on callback

pysoundcard


server which forwards all udp packets from one ip, port to everyone connected to it via udp


erasure codes later if time permits
'''

from pysoundcard import InputStream, OutputStream, continue_flag
import time

"""Loop back five seconds of audio data."""

output = OutputStream(samplerate=44100, blocksize=16)
output.start()

def callback(in_data, time_info, status):
    output.write(in_data*4)
    return continue_flag

s = InputStream(samplerate=44100, blocksize=16, callback=callback)

s.start()
time.sleep(5)
s.stop()
output.stop()

