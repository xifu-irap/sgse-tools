# sgse-tools

---

JavaScript scripts to manage the tests of the DRE DEMUX.

## 1. Directories and files description

---

  - (dir.) **common**: contains general purpose JavaScripts
    + (file) **utilTools.dscript**: JavaScript with various utilities
  - (dir.) **dcdc**: contains tools dedicated to the management of the DRE DCDC converter
    + (dir.) **python**: contains Pythons scripts dedicated to the test of the DCDC driver
  - (dir.) **demux**: contains JavaScripts dedicated to the management of the DRE DEMUX
    + (file) **dmx_check_commands.dscript**: JavaScripts to test the low level commands defined in dmxTools.dscript
    + (file) **dmxFake.dscript**: JavaScripts faking the DEMUX registers (can be used with dmx_check_commands.dscript)
    + (file) **dmxHk.dscript**: JavaScripts dedicated to read and convert DMX housekeepings
    + (file) **dmx_listOfFunctions.md**: list of low level functions available to manage the DEMUX
    + (file) **dmxRegAddresses.dscript**: definition of the DEMUX register addresses
    + (file) **dmxTools.dscript**: JavaScripts with low level commands for the DRE DEMUX
    + (file) **SQA_offset_settings.xlsx**: Excel file to compute the settings of the DEMUX offset compensation signal
  - (dir.) **dmxTestPlanXX**: contain JavaScripts dedicated to test plan-XX
  - (dir.) **fpasim**: contains JavaScripts dedicated to the management of the FPAsim EGSE
    + (dir.) **fpasim**: contains JavaScripts dedicated to the testing of the fpasim firmware
    + (dir.) **fpasim_default_ram**: contains the default mem files of the fpasim (i.e. transfer functions)
    + (dir.) **fpasim_specific_ram**: contains some specific mem files that can be used to replace the default ones
  - (dir.) **main**: high level JavaScripts dedicated to the management of the tests
    + (file) **launcher.dscript**: main JavaScript which starts the test
  - (dir.) **ras**: contains JavaScripts dedicated to the management of the DRE RAS
    + (file) **rasCheckReadWrite.dscript**: JavaScripts to test the low level commands defined in rasTools.dscript
    + (file) **rasFake.dscript**: JavaScripts faking the RAS registers (can be used with rasCheckReadWrite.dscript)
    + (file) **rasRegAddresses.dscript**: definition of the RAS register addresses
    + (file) **rasTools.dscript**: JavaScripts with low commands for the DRE RAS
  - (dir.) **ras-a75-fw**: JavaScripts dedicated to the management of the RAS proto firmware
  - (dir.) **tmtc**: JavaScripts dedicated to the management of the tmtc EGSE firmware
  - (dir.) **wfee**: contains JavaScripts dedicated to the management of the WFEE
    + (file) **wfeeTools.dscript**: JavaScripts with low commands for the WFEE

---
