from pyrtcm import RTCMReader

def read_file(filename, rtcm):
    stream = open(filename, 'rb')
    rtr = RTCMReader(stream)
    for (raw_data, parsed_data) in rtr:
        print(parsed_data)
        rtcm.append(parsed_data)
        print("")
        break
    stream.close()

def read_socket():
    pass

def read_serial():
    pass