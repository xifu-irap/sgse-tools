# ------------------------------------------------------------------------------------------------------------
#                            Copyright (C) 2024-2030 Ken-ji de la ROSA, IRAP Toulouse.
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
from utils_tools import Display

class Driver(Display):
    """
       Programm the FPGA and provide low level functions for the read/write register access
    """

    def __init__(self):
        """init the variable
        """
        # init the parent class
        super().__init__()
        self.dev = None

    def open(self,firmware_filepath_p):
        """Load the firmware in the FPGA

        Args:
            firmware_filepath_p (file): path to the FPGA bitstream (firmware file)
        """
        # print("********************************************************")
        # print("** Opal Kelly Board Info:")
        # print("********************************************************")
        msg = "Opal Kelly Board Info:"
        self.display_title(msg)


        # Open the first device we find.
        dev = ok.FrontPanelDevices().Open()
        if not dev:
            # print ("A device could not be opened.  Is one connected?")
            msg = "[KO]: A device could not be opened.  Is one connected?"
            self.display(msg)

        devInfo = ok.okTDeviceInfo()
        if (dev.NoError != dev.GetDeviceInfo(devInfo)):
            # print ("Unable to retrieve device information.")
            msg = "[KO]: Unable to retrieve device information."
            self.display(msg)

        # print("         Product: " + devInfo.productName)
        # print("Firmware version: %d.%d" % (devInfo.deviceMajorVersion, devInfo.deviceMinorVersion))
        # print("   Serial Number: %s" % devInfo.serialNumber)
        # print("       Device ID: %s" % devInfo.deviceID)
        msg_list = []
        msg_list.append("         Product: " + devInfo.productName)
        msg_list.append("Firmware version: %d.%d" % (devInfo.deviceMajorVersion, devInfo.deviceMinorVersion))
        msg_list.append("   Serial Number: %s" % devInfo.serialNumber)
        msg_list.append("       Device ID: %s" % devInfo.deviceID)
        self.display(msg_list)

        # Configures the PLL with settings stored in EEPROM.
        dev.LoadDefaultPLLConfiguration()

        # Download the configuration file.
        if (dev.NoError != dev.ConfigureFPGA(firmware_filepath_p)):
            # print ("FPGA configuration failed.")
            msg = "[KO]: Load FPGA firmware: "+ firmware_filepath_p
            self.display(msg)
        else:
            msg = "[OK]: Load FPGA firmware: "+ firmware_filepath_p
            self.display(msg)

        # Check for FrontPanel support in the FPGA configuration.
        if (False == dev.IsFrontPanelEnabled()):
            # print ("FrontPanel support is not available.")
            msg = "[KO]: FrontPanel support is not available."
            self.display(msg)


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
