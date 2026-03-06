#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Rx Fm Host Udp
# Generated: Thu Jun 26 14:44:45 2025
##################################################

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt5 import Qt
from PyQt5 import Qt, QtCore
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import zeromq
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import pmt
import sip
import sys
from gnuradio import qtgui


class RX_FM_Host_UDP(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Rx Fm Host Udp")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Rx Fm Host Udp")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "RX_FM_Host_UDP")

        if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
            self.restoreGeometry(self.settings.value("geometry").toByteArray())
        else:
            self.restoreGeometry(self.settings.value("geometry", type=QtCore.QByteArray))

        ##################################################
        # Variables
        ##################################################
        self.var_freq = var_freq = 102.2
        self.var_freq_MHz = var_freq_MHz = var_freq*1e6
        self.var_amp = var_amp = 0.5
        self.samp_rate = samp_rate = 2e6
        self.bw = bw = 300e3

        ##################################################
        # Blocks
        ##################################################
        self._var_amp_range = Range(0, 1, 0.01, 0.5, 200)
        self._var_amp_win = RangeWidget(self._var_amp_range, self.set_var_amp, "var_amp", "counter_slider", float)
        self.top_layout.addWidget(self._var_amp_win)
        self.zeromq_push_msg_sink_0 = zeromq.push_msg_sink('tcp://10.67.44.132:9996', 100)
        self._var_freq_range = Range(88.4, 107.6, 0.01, 102.2, 200)
        self._var_freq_win = RangeWidget(self._var_freq_range, self.set_var_freq, "var_freq", "counter_slider", float)
        self.top_layout.addWidget(self._var_freq_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_f(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	var_freq_MHz, #fc
        	bw, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(True)
        self.qtgui_freq_sink_x_0.enable_grid(True)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()

        if "float" == "float" or "float" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.blocks_udp_source_0 = blocks.udp_source(gr.sizeof_gr_complex*1, '10.67.44.132', 9997, 1472, True)
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vff((var_amp, ))
        self.blocks_message_strobe_0 = blocks.message_strobe(pmt.from_double(((var_freq_MHz)+300e3)), 1000)
        self.blocks_complex_to_mag_0 = blocks.complex_to_mag(1)
        self.audio_sink_0_0 = audio.sink(16000, '', True)
        self.analog_wfm_rcv_0 = analog.wfm_rcv(
        	quad_rate=int(samp_rate/150*12),
        	audio_decimation=10,
        )

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_message_strobe_0, 'strobe'), (self.zeromq_push_msg_sink_0, 'in'))
        self.connect((self.analog_wfm_rcv_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.blocks_complex_to_mag_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.audio_sink_0_0, 0))
        self.connect((self.blocks_udp_source_0, 0), (self.analog_wfm_rcv_0, 0))
        self.connect((self.blocks_udp_source_0, 0), (self.blocks_complex_to_mag_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "RX_FM_Host_UDP")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_var_freq(self):
        return self.var_freq

    def set_var_freq(self, var_freq):
        self.var_freq = var_freq
        self.set_var_freq_MHz(self.var_freq*1e6)

    def get_var_freq_MHz(self):
        return self.var_freq_MHz

    def set_var_freq_MHz(self, var_freq_MHz):
        self.var_freq_MHz = var_freq_MHz
        self.qtgui_freq_sink_x_0.set_frequency_range(self.var_freq_MHz, self.bw)
        self.blocks_message_strobe_0.set_msg(pmt.from_double(((self.var_freq_MHz)+300e3)))

    def get_var_amp(self):
        return self.var_amp

    def set_var_amp(self, var_amp):
        self.var_amp = var_amp
        self.blocks_multiply_const_vxx_0_0.set_k((self.var_amp, ))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

    def get_bw(self):
        return self.bw

    def set_bw(self, bw):
        self.bw = bw
        self.qtgui_freq_sink_x_0.set_frequency_range(self.var_freq_MHz, self.bw)


def main(top_block_cls=RX_FM_Host_UDP, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
