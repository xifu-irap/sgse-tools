# ------------------------------------------------------------------------------------------------------------
#                            Copyright (C) 2023-2030 Ken-ji de la ROSA, IRAP Toulouse.
# ------------------------------------------------------------------------------------------------------------
#                            This file is part of the ATHENA X-IFU DRE Telemetry and Telecommand Firmware.
#
#                            dcdc-hk-fw is free software: you can redistribute it and/or modify
#                            it under the terms of the GNU General Public License as published by
#                            the Free Software Foundation, either version 3 of the License, or
#                            (at your option) any later version.
#
#                            This program is distributed in the hope that it will be useful,
#                            but WITHOUT ANY WARRANTY; without even the implied warranty of
#                            MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#                            GNU General Public License for more details.
#
#                            You should have received a copy of the GNU General Public License
#                            along with this program.  If not, see <https://www.gnu.org/licenses/>.
# ------------------------------------------------------------------------------------------------------------
#    email                   kenji.delarosa@alten.com
#    @file                   driver.py
# -------------------------------------------------------------------------------------------------------------
#    Automatic Generation    No
#    Code Rules Reference    N/A
# -------------------------------------------------------------------------------------------------------------
#   @details
#
#   Programm the FPGA and provide low level functions for the read/write register access
#
# ------------------------------------------------------------------------------------------------------------


import sys
from pathlib import Path

#script_base_path = str(Path(__file__).parents[0])
#sys.path.append(script_base_path)

from .ok import *

class Driver:
    """ 
       Programm the FPGA and provide low level functions for the read/write register access
    """

    def __init__(self):
        """init the variable
        """

        self.dev = None

    def open(self,firmware_filepath_p):
        """Load the firmware in the FPGA

        Args:
            firmware_filepath_p (file): path to the FPGA bitstream (firmware file)
        """
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
        """configure a USB wire (register)

        Args:
            addr_p (uint8_t): address of the wire_in
            value_p (uint32_t): value to write
        """

        self.dev.setWireInValue(addr_p,value_p)
        self.dev.UpdateWireIns()

    def get_wire_out(self,addr_p):
        """ Retreive a USB wire value (register)

        Args:
            addr_p (uint8_t): address of the wire_out

        Returns:
            uint32_t: read register value.
        """
        self.dev.UpdateWireOuts()
        result = self.dev.GetWireOutValue(addr_p)
        return result
