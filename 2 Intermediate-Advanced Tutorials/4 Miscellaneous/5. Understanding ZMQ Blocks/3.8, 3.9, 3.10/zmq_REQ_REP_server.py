#!/usr/bin/python3
# -*- coding: utf-8 -*-

# zmq_REQ_REP_server.py

# This server program capitalizes received strings and returns them.
# NOTES:
#   1) To comply with the GNU Radio view, messages are received on the REQ socket and sent on the REP socket.
#   2) The REQ and REP messages must be on separate port numbers.

import pmt
import zmq

_debug = 0          # set to zero to turn off diagnostics

# create a REQ socket
_PROTOCOL = "tcp://"
_SERVER = "127.0.0.1"          # localhost
_REQ_PORT = ":50246"
_REQ_ADDR = _PROTOCOL + _SERVER + _REQ_PORT
if (_debug):
    print ("'zmq_REQ_REP_server' version 20056.1 connecting to:", _REQ_ADDR)
req_context = zmq.Context()
if (_debug):
    assert (req_context)
req_sock = req_context.socket (zmq.REQ)
if (_debug):
    assert (req_sock)
rc = req_sock.connect (_REQ_ADDR)
if (_debug):
    assert (rc == None)

# create a REP socket
_PROTOCOL = "tcp://"
_SERVER = "127.0.0.1"          # localhost
_REP_PORT = ":50247"
_REP_ADDR = _PROTOCOL + _SERVER + _REP_PORT
if (_debug):
    print ("'zmq_REQ_REP_server' version 20056.1 binding to:", _REP_ADDR)
rep_context = zmq.Context()
if (_debug):
    assert (rep_context)
rep_sock = rep_context.socket (zmq.REP)
if (_debug):
    assert (rep_sock)
rc = rep_sock.bind (_REP_ADDR)
if (_debug):
    assert (rc == None)

while True:
    #  Wait for next request from client
    data = req_sock.recv()
    message = pmt.to_python(pmt.deserialize_str(data))
    print("Received request: %s" % message)

    output = message.upper()

    #  Send reply back to client
    rep_sock.send (pmt.serialize_str(pmt.to_pmt(output)))