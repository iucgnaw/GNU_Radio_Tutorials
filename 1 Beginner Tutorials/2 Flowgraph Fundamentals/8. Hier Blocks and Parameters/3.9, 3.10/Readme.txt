A Python .py file and YAML .yml file will be created. For GNU Radio v3.8 the files will be created in your home directory:
/home/$USER/.grc_gnuradio/


For GNU Radio v3.10, the files will be created in directory where the .grc file is saved. Please create the .grc_gnuradio directory and copy the .py and .yml files there:
$ mkdir /home/$USER/.grc_gnuradio
$ cp FrequencyShifter.block.yml /home/$USER/.grc_gnuradio/
$ cp FrequencyShifter.py /home/$USER/.grc_gnuradio/ 