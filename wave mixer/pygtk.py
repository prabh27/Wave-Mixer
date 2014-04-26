#! /usr/bin/env python
# -*- Mode: python; c-basic-offset: 4 -*-

import os
import signal
import sys
import socket, select
from code import InteractiveInterpreter, InteractiveConsole

import gtk
import gobject
import struct


GDK_INPUT_READ = 1

class Mainloop(Interactive Interpreter):
    def __init__(self, read_fd, sock):
        InteractiveInterpreter.__init__(self)
        self._rfd = os.fdopen(read_fd, 'r')
        self._sock = sock
        gobject.io_add_watch(read_fd, GDK_INPUT_READ, self.input_func)

