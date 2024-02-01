import sys
from pathlib import Path

#script_base_path = str(Path(__file__).parents[0])
#sys.path.append(script_base_path)

from .ok import *
#import ok

class Driver:
    """
    """

    def __init__(self):

        self.dev = None

    def open(self,firmware_filepath_p):
        # Open the first device we find.
        dev = ok.FrontPanelDevices().Open()
        if not dev:
            print ("A device could not be opened.  Is one connected?")

        devInfo = ok.okTDeviceInfo()
        if (dev.NoError != dev.GetDeviceInfo(devInfo)):
            print ("Unable to retrieve device information.")

        print("********************************************************")
        print("** Opal Kelly Board Info:")
        print("********************************************************")
        print("         Product: " + devInfo.productName)
        print("Firmware version: %d.%d" % (devInfo.deviceMajorVersion, devInfo.deviceMinorVersion))
        print("   Serial Number: %s" % devInfo.serialNumber)
        print("       Device ID: %s" % devInfo.deviceID)

        # Configures the PLL with settings stored in EEPROM.
        dev.LoadDefaultPLLConfiguration()

        # Download the configuration file.
        if (dev.NoError != dev.ConfigureFPGA(firmware_filepath_p)):
            print ("FPGA configuration failed.")

        # Check for FrontPanel support in the FPGA configuration.
        if (False == dev.IsFrontPanelEnabled()):
            print ("FrontPanel support is not available.")


        self.dev = dev

    def set_wire_in(self,addr_p,value_p):

        self.dev.setWireInValue(addr_p,value_p)
        self.dev.UpdateWireIns()

    def get_wire_out(self,addr_p):
        self.dev.UpdateWireOuts()
        result = self.dev.GetWireOutValue(addr_p)
        return result
