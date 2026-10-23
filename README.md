# sgse-tools

---

JavaScript scripts to manage the tests of the DRE and WFEE.

The analysis of the performance tests is done automatically after the data acquisition.
The analysis-tools shall be installed in C:/

---

### Directories and files description

  - (dir.) **add-ons**: Additional tools not required for the nominal operation
    - (file) **dmxSQA_offset_settings.xlsx**: Excel file to compute the settings of the DEMUX offset compensation signal
  - (dir.) **configurations**: xml DRE configuration files
    - (file) **whole_default_conf.xml**: default DRE configuration
  - (dir.) **includes**: low-level tools to be included in high-level scripts
    - (dir.) **dcdc**: tools for the management of the DRE DCDC converter
      + (dir.) **python**: Python scripts for the test of the DCDC driver
        - (dir.) **driver**: DCDC driver source code
          + (file) **dcdc.py**: low-level driver for the DCDC converter
          + (file) **driver.py**: high-level driver
          + (file) **utils_tools.py**: helper utilities
          + (file) **README.md**: driver documentation
        - (file) **test_dcdc.py**: generic DCDC test
        - (file) **test_dcdc_adc.py**: test of the DCDC ADC
        - (file) **test_dcdc_check_tmtc_link.py**: test of the TMTC link
        - (file) **test_dcdc_power.py**: power test of the DCDC
    - (dir.) **equipments**: JavaScripts to drive test equipements (oscilooscopes, ...)
      + (file) **MSO64_LIB.dscript**: library to drive the MSO64 oscilloscope
      + (file) **test_mesure_oscillo.dscript**: oscilloscope measurement test
    - (dir.) **fpasim**: JavaScripts to drive the FPAsim EGSE
      + (file) **fpasim_config.dscript**: FPAsim configuration
      + (file) **fpasim_includes.dscript**: inclusion helpers for the FPAsim scripts
      + (file) **fpasim_load_tables_amp_squid.dscript**: loading of the amp squid tables
      + (file) **fpasim_load_tables_mux_squid.dscript**: loading of the mux squid tables
      + (file) **fpasim_load_tables_tes_pulse_shape.dscript**: loading of the TES pulse shape table
      + (file) **fpasim_load_tables_template.dscript**: template for the loading of tables
      + (file) **fpasim_startup.dscript**: FPAsim startup sequence
      + (file) **fpasim_test_check_tmtc_link.dscript**: test of the FPAsim TMTC link
      + (file) **fpasim_test_make_pulse_generation.dscript**: test of the pulse generation
      + (dir.) **fpasim**: contains JavaScripts dedicated to the testing of the fpasim firmware
        - (file) **fpasim.dscript**: main FPAsim driver
        - (file) **fpasim_tools.dscript**: FPAsim low-level commands
        - (file) **utils_tools.dscript**: helper utilities
        - (file) **ads62p49.dscript**: driver for the ADS62P49 ADC
        - (file) **amc7823.dscript**: driver for the AMC7823
        - (file) **cdce72010.dscript**: driver for the CDCE72010
        - (file) **dac3283.dscript**: driver for the DAC3283
      + (dir.) **fpasim_default_ram**: contains the default mem files of the fpasim (i.e. transfer functions)
        - (file) **amp_squid_tf.mem**: amp squid transfer function
        - (file) **mux_squid_tf.mem**: mux squid transfer function
        - (file) **mux_squid_offset.mem**: mux squid offset
        - (file) **tes_pulse_shape.mem**: TES pulse shape
        - (file) **tes_std_state.mem**: TES standard state
      + (dir.) **fpasim_specific_ram**: contains specific mem files that can be used to replace the default ones
        - (file) **amp_squid_linear_tf.mem**: linear amp squid transfer function
        - (file) **mux_squid_linear_tf.mem**: linear mux squid transfer function
        - (file) **tes_linear_shape.mem**: linear TES shape
        - (file) **tes_std_state_FSR.mem**: TES full-scale standard state
    - (dir.) **ras-a75-fw**: JavaScripts to drive the DRE RAS PROTOTYPE module
      + (file) **ras_tools.dscript**: low-level RAS tools
      + (file) **configure_ras.dscript**: RAS configuration
      + (file) **check_ps_gs_levels.dscript**: check of the PS/GS levels
      + (file) **default_configurations.dscript**: default RAS configurations
      + (file) **default_config.txt**: default configuration file
      + (file) **scan_FAS_level.dscript**: scan of the FAS level
      + (file) **scan_delay.dscript**: scan of the delay
      + (file) **scan_nbrows.dscript**: scan of the number of rows
      + (file) **scan_overlap.dscript**: scan of the overlap
      + (file) **scan_rowperiod.dscript**: scan of the row period
    - (dir.) **tmtc**: JavaScripts to drive the CDIF firmware
      + (file) **Test_SPI_read.dscript**: SPI read test
      + (file) **Test_SPI_write.dscript**: SPI write test
      + (file) **Test_SPI_read_DEMUX_RAS.dscript**: SPI read test on DEMUX and RAS
      + (file) **Test_SPI_write_DEMUX_RAS.dscript**: SPI write test on DEMUX and RAS
      + (file) **Test_DRE_science_debug_full_speed.dscript**: DRE science debug at full speed
      + (file) **Test_tmtc_check_link.dscript**: check of the TMTC link
      + (file) **test_DRE_science.dscript**: DRE science test
      + (file) **test_SPI_on_CDIF.dscript**: SPI test on CDIF
      + (dir.) **tmtc**: TMTC driver
        - (file) **tmtc.dscript**: main TMTC driver
        - (file) **tmtc_tools.dscript**: TMTC low-level commands
        - (file) **utils_tools.dscript**: helper utilities
    - (file) **common_constants.dscript**: Javascripts defining constants 
    - (file) **dmxConfigurations.dscript**: DEMUX configuration helpers
    - (file) **dmxHk.dscript**: JavaScripts to read and convert DMX housekeepings
    - (file) **dmxRegAddresses.dscript**: definition of the DEMUX register addresses
    - (file) **dmxStart.dscript**: JavaScripts to start the DEMUX
    - (file) **dmxTools.dscript**: JavaScripts with low level commands for the DRE DEMUX
    - (file) **rasRegAddresses.dscript**: definition of the RAS register addresses
    - (file) **rasSequences.dscript**: JavaScripts to define some row address sequences
    - (file) **rasTools.dscript**: JavaScripts with low commands for the DRE RAS
    - (file) **utilTools.dscript**: JavaScript with various utilities
    - (file) **wfeeTools.dscript**: JavaScripts with low commands for the WFEE
  - (dir.) **scripts**: Javascripts to handle the tests of the DRE
    - (dir.) **dmxElec**: Javascripts for electrical tests of the DEMUX
      + (file) **calibHkTemp.dscript**: calibration of the housekeeping temperature
      + (file) **dmxAdcInrush.dscript**: inrush test of the DEMUX ADC
      + (file) **dmxDacInrush.dscript**: inrush test of the DEMUX DAC
      + (file) **fdbk.dscript**: test of the feedback chain
      + (file) **ofco_dac_spi.dscript**: test of the OFCO DAC SPI link
      + (file) **ofco_mux.dscript**: test of the OFCO multiplexer
    - (dir.) **dmxFunc**: JavaScripts for the functional tests of the DRE DEMUX module
      + (file) **bandShape_error.dscript**: characterization of the ERROR bandshape
      + (file) **dmxCheckDefaults.dscript**: JavaScripts to test default values of the TDM firmware registers
      + (file) **dmxCheckReadWrite.dscript**: JavaScripts to test read/write of the TDM firmware registers
      + (file) **dmxCheckTC.dscript**: Javascript to test the error handling on the SPI link
      + (file) **dmxCheckTM.dscript**: Javascript to test the different DEMUX TM modes
      + (file) **dmxDelockCounters.dscript**: Javascript to test DEMUX delock flags and counters
      + (file) **dmxFdbkDelay.dscript**: Javascript to characterize the feedback delay
      + (file) **dmxFdbkEdges.dscript**: characterization of the feedback edges
      + (file) **dmxOfcoCoarse.dscript**: characterization of the OFCO coarse delay
      + (file) **dmxOfcoDelay.dscript**: characterization of the OFCO delay
      + (file) **dmxOfcoEdges.dscript**: characterization of the OFCO edges
      + (file) **dmxOfcoFine.dscript**: characterization of the OFCO fine delay
      + (file) **dmxPulseShaping.dscript**: test of the pulse shaping
      + (file) **dmxSamplingDelay.dscript**: Javascript to characterize the sampling delay
    - (dir.) **dmxPerf**: JavaScripts for the performance tests of the DRE DEMUX module
      + (file) **bandShape_fdbk.dscript**: Javascript to characterize the bandshape of the FEEDBACK output
      + (file) **linearity_fdbkAndError.dscript**: Javascript to characterize the NL of feedback + Error signals
      + (file) **linearity_ofcoAndError.dscript**: Javascript to characterize the NL of ofco + Error signals
      + (file) **noise.dscript**: Javascript to characterize DEMUX noise
      + (file) **x-talk.dscript**: Javascript to characterize the crosstalk of the DEMUX module
    - (dir.) **dmxWithEP**: JavaScripts to test the coupling of the DEMUX and EP modules
      + (file) **pseudo_pulses_full_scale.dscript**: pseudo-pulses at full scale
      + (file) **pseudo_pulses_only_positive.dscript**: pseudo-pulses positive only
      + (file) **simple_test.dscript**: simple coupling test
      + (file) **test_pattern.dscript**: test pattern test
    - (dir.) **dreTutorials**: JavaScripts to demonstrate some DRE functionalities
      + (file) **EPsimTest.dscript**: test with the EP simulator
      + (file) **dmxFdbkTest.dscript**: feedback test
      + (file) **dmxOfcoTest.dscript**: OFCO test
      + (file) **dmxStartStopDacs.dscript**: start/stop of the DACs
      + (file) **dmx_checkDefaults.dscript**: check of the default values
      + (file) **dmx_ofcoTest.dscript**: OFCO test (variant)
      + (file) **dmx_testPatternAcqMode.dscript**: test pattern in acquisition mode
      + (file) **ras_address_overlap.dscript**: RAS address overlap
      + (file) **ras_address_sequence.dscript**: RAS address sequence
      + (file) **ras_dmx_delay.dscript**: RAS-DEMUX delay
      + (file) **ras_ps_gs_levels.dscript**: RAS PS/GS levels
      + (file) **ras_test_pattern.dscript**: RAS test pattern
    - (dir.) **operational**: JavaScripts to operate the DRE in a representative environment
      + (file) **carac_knorm.dscript**: characterization of the knorm
      + (file) **carac_ofco_fll_filter.dscript**: characterization of the OFCO FLL filter
      + (file) **carac_wfeesim.dscript**: characterization with the WFEE simulator
      + (file) **FPAsim_startup.dscript**: startup of the FPAsim
      + (file) **measurePulses.dscript**: pulse measurement
      + (file) **measurePulsesWithDelocks.dscript**: pulse measurement with delocks
      + (file) **measurePulsesWithFLL.dscript**: pulse measurement with FLL
      + (file) **scanAmpSquid.dscript**: scan of the amp squid
      + (file) **scanMuxSquid.dscript**: scan of the mux squid
      + (file) **scanSquids.dscript**: scan of the squids
      + (file) **set_a.dscript**: set of parameter A
      + (file) **testAutoRelocks.dscript**: test of the auto-relocks
      + (file) **timingsSettings.dscript**: timings settings
      + (file) **tstSquidSim.dscript**: Javascript to use the DEMUX module with the SQUIDsim EGSE
    - (dir.) **ras**: Javascript for the testing of the ras module
      + (file) **rasCheckReadWrite.dscript**: JavaScripts to test the low level commands defined in rasTools.dscript
      + (file) **tc1_icu_selection.dscript**: test case 1 - ICU selection
      + (file) **tc2_firmware_and_board_ids.dscript**: test case 2 - firmware and board IDs
      + (file) **tc3_4_ps_gs_levels.dscript**: test cases 3 & 4 - PS/GS levels
      + (file) **tc5_address_sequence.dscript**: test case 5 - address sequence
      + (file) **tc6_7_sequence_delay.dscript**: test cases 6 & 7 - sequence delay
      + (file) **tc8_address_overlap.dscript**: test case 8 - address overlap
      + (file) **tc9_test_pattern.dscript**: test case 9 - test pattern
      + (file) **tc9b_test_pattern.dscript**: test case 9b - test pattern
      + (file) **tc10_test_HK.dscript**: test case 10 - housekeeping
      + (file) **tc11_test_I2C_WFEE.dscript**: test case 11 - I2C on WFEE
      + (file) **tc12_test_pattern_on_WFEE.dscript**: test case 12 - test pattern on WFEE
  - (file) **LICENSE**: Licence file
  - (file) **README.md**: this file

---
