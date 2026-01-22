# sgse-tools

---

JavaScript scripts to manage the tests of the DRE and WFEE.

The analysis of the performance tests is done automatically after the data acquisition.
The analysis-tools shall be installed in C:/

---

### Directories and files description

  - (dir.) **configurations**: xml DRE configuration files
  - (dir.) **includes**: low-level tools to be included in high-level scripts
    - (dir.) **dcdc**: tools for the management of the DRE DCDC converter
      + (dir.) **python**: Pythons scripts for the test of the DCDC driver
    - (dir.) **equipments**: JavaScripts to drive test equipements (oscilooscopes, ...)
    - (dir.) **fpasim**: JavaScripts to drive the FPAsim EGSE
      + (dir.) **fpasim**: contains JavaScripts dedicated to the testing of the fpasim firmware
      + (dir.) **fpasim_default_ram**: contains the default mem files of the fpasim (i.e. transfer functions)
      + (dir.) **fpasim_specific_ram**: contains specific mem files that can be used to replace the default ones
    - (dir.) **ras-a75-fw**: JavaScripts to drive the DRE RAS PROTOTYPE module
    - (dir.) **tmtc**: JavaScripts to drive the CDIF firmware
    - (file) **common_constants.dscript**: Javascripts defining constants 
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
      + (file) **ampSquidDacTest.dscript**: Javascript to test the OFCO output chain 
      + (file) **muxSquidDacTest.dscript**: Javascript to test the FDBK output chain (+ ERROR chain)
    - (dir.) **dmxFunc**: JavaScripts for the functional tests of the DRE DEMUX module
      + (file) **dmxCheckDefaults.dscript**: JavaScripts to test default values of the TDM firmware registers
      + (file) **dmxCheckReadWrite.dscript**: JavaScripts to test read/write of the TDM firmware registers
      + (file) **dmxCheckTC**: Javascript to test the error handling on the SPI link
      + (file) **dmxCheckTM**: Javascript to test the different DEMUX TM modes
      + (file) **dmxDelockCounters**: Javascript to test DEMUX delock flags and counters
      + (file) **dmxFdbkDelay**: Javascript to characterize the feedback delay
      + (file) **dmxSamplingDelay.dscript**: Javascript to characterize the sampling delay
    - (dir.) **dmxPerf**: JavaScripts for the performance tests of the DRE DEMUX module
      + (file) **bandShape_error**: Javascript to characterize the bandshape of the ERROR input
      + (file) **bandShape_fdbk**: Javascript to characterize the bandshape of the FEEDBACK output
      + (file) **linearity_fdbkAndError.dscript**: Javascript to characterize the NL of feedback + Error signals
      + (file) **linearity_ofcoAndError.dscript**: Javascript to characterize the NL of ofco + Error signals
      + (file) **noise.dscript**: Javascript to characterize DEMUX noise
      + (file) **XTalk**: Javascript to characterize the crosstalk of the DEMUX module
    - (dir.) **dmxWithEP**: JavaScripts to test the coupling of the DEMUX and EP modules
    - (dir.) **dreTutorials**: JavaScripts to demonstrate some DRE functionalities
    - (dir.) **operational**: JavaScripts to operate the DRE in a representative environment
      + (file) **carac_knorm.dscript**: 
      + (file) **FPSsim_startup.dscript**: 
      + (file) **lockAmpSquid.dscript**: 
      + (file) **lockMuxSquid.dscript**: 
      + (file) **scanAmpSquid.dscript**: 
      + (file) **scanSquids.dscript**: 
      + (file) **timingsSettings.dscript**:
      + (file) **tstSquidSim**: Javascript to use the DEMUX module with the SQUIDsim EGSE
    - (dir.) **ras**: Javascript for the testing of the ras module
      + (file) **rasCheckReadWrite.dscript**: JavaScripts to test the low level commands defined in rasTools.dscript
  - (dir.) **tools**: Tools to help in the preparation of the JavaScripts
    - (file) **SQA_offset_settings.xlsx**: Excel file to compute the settings of the DEMUX offset compensation signal
  - (file) **LICENCE**: Licence file
  - (file) **README.md**: this file

---
