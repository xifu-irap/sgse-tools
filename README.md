# sgse-tools

---

JavaScript scripts to manage the tests of the DRE and WFEE.

## Directories and files description

---

  - (dir.) **configurations**: xml DRE configuration files
  - (dir.) **dmxAndFPAsim**: Javascripts for coupling tests DEMUX / FPAsim
    + (file) **carac_knorm.dscript**: 
    + (file) **compteursRelock.dscript**: 
    + (file) **errorStatus.dscript**: 
    + (file) **FPSsim_startup.dscript**: 
    + (file) **lockAmpSquid.dscript**: 
    + (file) **lockMuxSquid.dscript**: 
    + (file) **scanAmpSquid.dscript**: 
    + (file) **scanSquids.dscript**: 
    + (file) **timingsSettings.dscript**:
  - (dir.) **dmxElec**: Javascripts for electrical tests of the DEMUX
    + (file) **ampSquidDacTest.dscript**: Javascript to test the OFCO output chain 
    + (file) **muxSquidDacTest.dscript**: Javascript to test the FDBK output chain (+ ERROR chain)
  - (dir.) **dmxFuncAndPerf**: JavaScripts for the functional and performance tests of the DRE DEMUX module
    + (file) **bandShape_error**: Javascript to characterize the bandshape of the ERROR input
    + (file) **bandShape_fdbk**: Javascript to characterize the bandshape of the FEEDBACK output
    + (file) **dmxCheckDefaultRegValues.dscript**: JavaScripts to test default values of the TDM firmware registers
    + (file) **dmxCheckReadWriteRegValues.dscript**: JavaScripts to test read/write of the TDM firmware registers
    + (file) **dmxCheckTC**: Javascript to test the error handling on the SPI link
    + (file) **dmxCheckTM**: Javascript to test the different DEMUX TM modes
    + (file) **fdbkDelayAnalysis**: Javascript to characterize the feedback delay
    + (file) **linearity_fdbkAndError.dscript**: Javascript to characterize the NL of feedback + Error signals
    + (file) **linearity_ofcoAndError.dscript**: Javascript to characterize the NL of ofco + Error signals
    + (file) **noiseAnalysis.dscript**: Javascript to characterize DEMUX noise
    + (file) **samplingDelayAnalysis.dscript**: Javascript to characterize the sampling delay
    + (file) **testTstPatternAcqMode.dscript**: Javascript to check the behaviour of the test pattern acquisition mode
    + (file) **tstSquidSim**: Javascript to use the DEMUX module with the SQUIDsim EGSE
    + (file) **XTalkAnalysis**: Javascript to characterize the crosstalk of the DEMUX module
  - (dir.) **includes**: low-level tools to be included in high-level scripts
    - (dir.) **common**: general purpose JavaScripts
      + (file) **constants.dscript**: Javascripts defining constants 
      + (file) **utilTools.dscript**: JavaScript with various utilities
    - (dir.) **dcdc**: tools for the management of the DRE DCDC converter
      + (dir.) **python**: Pythons scripts for the test of the DCDC driver
    - (dir.) **demux**: JavaScripts to drive the DRE DEMUX module
      + (file) **dmxCheckDefaults.dscript**: JavaScripts to test default values of the TDM firmware registers
      + (file) **dmxCheckReadWrite.dscript**: JavaScripts to test read/write of the TDM firmware registers
      + (file) **dmxHk.dscript**: JavaScripts to read and convert DMX housekeepings
      + (file) **dmx_listOfFunctions.md**: list of low level functions available to manage the DEMUX
      + (file) **dmxRegAddresses.dscript**: definition of the DEMUX register addresses
      + (file) **dmxStart.dscript**: JavaScripts to start the DEMUX
      + (file) **dmxTools.dscript**: JavaScripts with low level commands for the DRE DEMUX
      + (file) **SQA_offset_settings.xlsx**: Excel file to compute the settings of the DEMUX offset compensation signal
    - (dir.) **equipments**: JavaScripts to drive test equipements (oscilooscopes, ...)
    - (dir.) **fpasim**: JavaScripts to drive the FPAsim EGSE
      + (dir.) **fpasim**: contains JavaScripts dedicated to the testing of the fpasim firmware
      + (dir.) **fpasim_default_ram**: contains the default mem files of the fpasim (i.e. transfer functions)
      + (dir.) **fpasim_specific_ram**: contains some specific mem files that can be used to replace the default ones
    - (dir.) **ras**: JavaScripts to drive the DRE RAS module
      + (file) **rasCheckReadWrite.dscript**: JavaScripts to test the low level commands defined in rasTools.dscript
      + (file) **rasRegAddresses.dscript**: definition of the RAS register addresses
      + (file) **rasSequences.dscript**: JavaScripts to define some row address sequences
      + (file) **rasTools.dscript**: JavaScripts with low commands for the DRE RAS
    - (dir.) **ras-a75-fw**: JavaScripts to drive the DRE RAS PROTOTYPE module
    - (dir.) **tmtc**: JavaScripts to drive the CDIF firmware
    - (dir.) **wfee**: JavaScripts to drive the WFEE through the DRE RAS module
      + (file) **wfeeTools.dscript**: JavaScripts with low commands for the WFEE
  - (dir.) **rasFuncAndPerf**: JavaScripts for the functional and performance tests of the DRE RAS module
  - (file) **README.md**: this file

---
