import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout, QSlider, QLabel
from PyQt5.QtCore import Qt

# Import your flowgraph
from fm_receiver import fm_receiver
from gnuradio import audio, blocks


class FM(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 FM Receiver with Recording")

        # Instantiate FM Receiver App
        self.tb = fm_receiver()
        self.setMinimumSize(700, 500)

        # State variables
        self.listening = False
        self.recording = False

        # Initialize recording block (not yet connected)
        self.recorder = blocks.wavfile_sink(
            'recording.wav',
            1,
            int(48e3),
            blocks.FORMAT_WAV,
            blocks.FORMAT_PCM_16,
            False
        )

        # Layout
        layout = QVBoxLayout()

        # Listening Button
        self.listen_button = QPushButton("Start Listening")
        self.listen_button.clicked.connect(self.toggle_listening)
        layout.addWidget(self.listen_button)

        # Recording Button
        self.record_button = QPushButton("Start Recording")
        self.record_button.clicked.connect(self.toggle_recording)
        layout.addWidget(self.record_button)

        # Frequency Label
        self.freq_label = QLabel("Frequency: 100 MHz")
        layout.addWidget(self.freq_label)

        # Frequency Slider
        self.freq_slider = QSlider(Qt.Horizontal)
        self.freq_slider.setMinimum(88000000)   # 88 MHz
        self.freq_slider.setMaximum(108000000)  # 108 MHz
        self.freq_slider.setValue(int(self.tb.get_freq()))  
        self.freq_slider.setTickInterval(int(1e6))  # 1 MHz step
        self.freq_slider.setSingleStep(100000)
        self.freq_slider.valueChanged.connect(self.change_frequency)
        layout.addWidget(self.freq_slider)

        # Add the Frequency Sink widget from GNU Radio (Qt GUI block)
        layout.addWidget(self.tb._qtgui_freq_sink_x_0_win)

        self.setLayout(layout)

    def toggle_listening(self):
        """Toggle listening state and update button text."""
        self.listening = not self.listening

        if self.listening:
            self.listen_button.setText("Stop Listening")
            print("Listening started...")
            self.tb.start()
        else:
            self.listen_button.setText("Start Listening")
            print("Listening stopped.")
            self.tb.stop()
            self.tb.wait()

    def toggle_recording(self):
        """Toggle audio recording by connecting/disconnecting wavfile_sink."""
        self.recording = not self.recording

        if self.recording:
            self.record_button.setText("Stop Recording")
            print("Recording started...")

            # Dynamically connect FM decoder to wavfile sink
            self.tb.stop()
            self.tb.wait()
            self.tb.connect((self.tb.analog_wfm_rcv_0, 0), (self.recorder, 0))
            self.tb.start()
        else:
            self.record_button.setText("Start Recording")
            print("Recording stopped.")

            # Disconnect wavfile sink
            self.tb.stop()
            self.tb.wait()
            try:
                self.tb.disconnect((self.tb.analog_wfm_rcv_0, 0), (self.recorder, 0))
            except Exception as e:
                print("Already disconnected:", e)
            self.tb.start()

    def change_frequency(self, freq):
        """Update FM receiver frequency from slider."""
        self.tb.set_freq(freq)
        self.freq_label.setText(f"Frequency: {freq/1e6:.1f} MHz")
        print(f"Frequency set to {freq/1e6:.1f} MHz")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FM()
    window.show()
    sys.exit(app.exec_())
