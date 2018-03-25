from ctypes import *
msvcrt = cdll.msvcrt
message_string = "Hello world!\n"
msvcrt.wprintf("Testing:%s",message_string)