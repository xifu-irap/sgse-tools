# sgse-tools

---

JavaScript scripts to manage the tests of the DRE DEMUX.

## 1. Directories and files description

---

  - (dir.) **common**: contains general purpose JavaScripts
    + (file) **util_tools.dscript**: JavaScript with various utilities
  - (dir.) **dcdc**: contains tools dedicated to the management of the DRE DCDC converter
    + (dir.) **python**: contains Pythons scripts dedicated to the test of the DCDC driver
  - (dir.) **demux**: contains JavaScripts dedicated to the management of the DRE DEMUX
    + (file) **dmx_check_commands.dscript**: JavaScripts to test the low level commands defined in dmx_tools.dscript
    + (file) **dmx_fake.dscript**: JavaScripts faking the DEMUX registers (can be used with dmx_check_commands.dscript)
    + (file) **dmx_listOfFunctions.md**: list of low level functions available to manage the DEMUX
    + (file) **dmx_reg_addresses.dscript**: definition of the DEMUX register addresses
    + (file) **dmx_tools.dscript**: JavaScripts with low level commands for the DRE DEMUX
    + (file) **SQA_offset_settings.xlsx**: Excel file to compute the settings of the DEMUX offset compensation signal
  - (dir.) **fpasim**: contains JavaScripts dedicated to the management of the FPAsim EGSE
    + (dir.) **fpasim**: contains JavaScripts dedicated to the testing of the fpasim firmware
    + (dir.) **fpasim_default_ram**: contains the default mem files of the fpasim (i.e. transfer functions)
    + (dir.) **fpasim_specific_ram**: contains some specific mem files that can be used to replace the default ones
  - (dir.) **main**: high level JavaScripts dedicated to the management of the tests
    + (file) **launcher.dscript**: main JavaScript which starts the test
    + (file) **testSequence.dscript**: JavaScript which manages the test session
  - (dir.) **ras**: contains JavaScripts dedicated to the management of the DRE RAS
    + (file) **ras_check_commands.dscript**: JavaScripts to test the low level commands defined in ras_tools.dscript
    + (file) **ras_fake.dscript**: JavaScripts faking the RAS registers (can be used with ras_check_commands.dscript)
    + (file) **ras_reg_addresses.dscript**: definition of the RAS register addresses
    + (file) **ras_tools.dscript**: JavaScripts with low commands for the DRE RAS
  - (dir.) **ras-a75-fw**: JavaScripts dedicated to the management of the RAS proto firmware
  - (dir.) **tmtc**: JavaScripts dedicated to the management of the tmtc EGSE firmware