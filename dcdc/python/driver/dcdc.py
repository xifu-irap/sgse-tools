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
#    @file                   dcdc.py
# -------------------------------------------------------------------------------------------------------------
#    Automatic Generation    No
#    Code Rules Reference    N/A
# -------------------------------------------------------------------------------------------------------------
#   @details
#
#   Provide functions (write/read) in order to access to all DCDC registers.
#
# ------------------------------------------------------------------------------------------------------------

# standard library
import sys
from pathlib import Path

# compute the script path
script_base_path = str(Path(__file__).parents[0])
sys.path.append(script_base_path)

from driver import Driver

class DCDC(Driver):
    """Provide functions (write/read) in order to access to all DCDC registers.

    Args:
        Driver (class): provide low level function to access to the register (write/read).
    """

    def __init__(self):
        """Define the available register addresses for:
                . wire_in
                . wire_out
        """
        # init the parent class
        super().__init__()

        # list all wire_in addresses
        #################################################
        self.addr_wire_in = {}
        self.addr_wire_in['CTRL'] = 0x00
        self.addr_wire_in['POWER_CTRL'] = 0x01
        # self.addr_wire_in['RFU'] = 0x02
        # self.addr_wire_in['RFU'] = 0x03
        self.addr_wire_in['ADC_CTRL'] = 0x04
        # self.addr_wire_in['ADC_STATUS'] = 0x05
        # self.addr_wire_in['RFU'] = 0x06
        # self.addr_wire_in['RFU'] = 0x07
        # self.addr_wire_in['RFU'] = 0x08
        # self.addr_wire_in['RFU'] = 0x09
        # self.addr_wire_in['RFU'] = 0x0A
        # self.addr_wire_in['RFU'] = 0x0B
        # self.addr_wire_in['RFU'] = 0x0C
        # self.addr_wire_in['RFU'] = 0x0D
        # self.addr_wire_in['RFU'] = 0x0E
        # self.addr_wire_in['RFU'] = 0x0F
        # self.addr_wire_in['ADC0'] = 0x10
        # self.addr_wire_in['ADC1'] = 0x11
        # self.addr_wire_in['ADC2'] = 0x12
        # self.addr_wire_in['ADC3'] = 0x13
        # self.addr_wire_in['ADC4'] = 0x14
        # self.addr_wire_in['ADC5'] = 0x15
        # self.addr_wire_in['ADC6'] = 0x16
        # self.addr_wire_in['ADC7'] = 0x17
        self.addr_wire_in['DEBUG_CTRL'] = 0x18
        self.addr_wire_in['ERROR_SEL'] = 0x19
        # self.addr_wire_in['ERRORS'] = 0x1A
        # self.addr_wire_in['STATUS'] = 0x1B
        # self.addr_wire_in['RFU'] = 0x1C
        # self.addr_wire_in['HARDWARE_ID'] = 0x1D
        # self.addr_wire_in['FIRMWARE_NAME'] = 0x1E
        # self.addr_wire_in['FIRMWARE_ID'] = 0x1F

        # list all wire_out addresses
        #################################################
        self.addr_wire_out = {}
        self.addr_wire_out['CTRL'] = 0x20
        self.addr_wire_out['POWER_CTRL'] = 0x21
        # self.addr_wire_out['RFU'] = 0x22
        # self.addr_wire_out['RFU'] = 0x23
        self.addr_wire_out['ADC_CTRL'] = 0x24
        self.addr_wire_out['ADC_STATUS'] = 0x25
        # self.addr_wire_out['RFU'] = 0x26
        # self.addr_wire_out['RFU'] = 0x27
        # self.addr_wire_out['RFU'] = 0x28
        # self.addr_wire_out['RFU'] = 0x29
        # self.addr_wire_out['RFU'] = 0x2A
        # self.addr_wire_out['RFU'] = 0x2B
        # self.addr_wire_out['RFU'] = 0x2C
        # self.addr_wire_out['RFU'] = 0x2D
        # self.addr_wire_out['RFU'] = 0x2E
        # self.addr_wire_out['RFU'] = 0x2F
        self.addr_wire_out['ADC0'] = 0x30
        self.addr_wire_out['ADC1'] = 0x31
        self.addr_wire_out['ADC2'] = 0x32
        self.addr_wire_out['ADC3'] = 0x33
        self.addr_wire_out['ADC4'] = 0x34
        self.addr_wire_out['ADC5'] = 0x35
        self.addr_wire_out['ADC6'] = 0x36
        self.addr_wire_out['ADC7'] = 0x37
        self.addr_wire_out['DEBUG_CTRL'] = 0x38
        self.addr_wire_out['ERROR_SEL'] = 0x39
        self.addr_wire_out['ERRORS'] = 0x3A
        self.addr_wire_out['STATUS'] = 0x3B
        # self.addr_wire_out['RFU'] = 0x3C
        self.addr_wire_out['HARDWARE_ID'] = 0x3D
        self.addr_wire_out['FIRMWARE_NAME'] = 0x3E
        self.addr_wire_out['FIRMWARE_ID'] = 0x3F

    def set_ctrl(self,rst_p):
        """Configure the CTRL register

        Args:
            rst_p (uint1_t): software reset
        """

        data = rst_p & 0x1
        addr = self.addr_wire_out['CTRL']
        self.set_wire_in(addr_p=addr,data_p=data)

    def set_power_ctrl(self,dmx0_power_on_off_p,dmx1_power_on_off_p,ras_power_on_off_p,wfee_power_on_off_p):
        """Configure the POWER_CTRL register

        Args:
            dmx0_power_on_off_p (uint1_t): DMX0- 1: power up, 0: power down
            dmx1_power_on_off_p (uint1_t): DMX1- 1: power up, 0: power down
            ras_power_on_off_p (uint1_t): RAS- 1: power up, 0: power down
            wfee_power_on_off_p (uint1_t): WFEE- 1: power up, 0: power down
        """
        data1 = (wfee_power_on_off_p << 3) + (ras_power_on_off_p << 2 )
        data0 = (dmx1_power_on_off_p << 1) + dmx0_power_on_off_p
        data = data1 + data0
        addr = self.addr_wire_out['POWER_CTRL']
        self.set_wire_in(addr_p=addr,data_p=data)

    def set_adc_ctrl(self,adc_start_p):
        """Configure the ADC_CTRL register

        Args:
            adc_start_p (uint1_t): software reset
        """

        data = adc_start_p & 0x1
        addr = self.addr_wire_out['ADC_CTRL']
        self.set_wire_in(addr_p=addr,data_p=data)

    def set_debug_ctrl(self,rst_status_p,debug_pulse_p):
        """Configure the DEBUG_CTRL register

        Args:
            rst_status_p (uint1_t): 1: reset the internal errors, 0: do nothing
            debug_pulse_p (uint1_t): 1: delay error, 0: latch error
        """

        data = ( rst_status_p << 1) + debug_pulse_p
        addr = self.addr_wire_out['DEBUG_CTRL']
        self.set_wire_in(addr_p=addr,data_p=data)

    def set_error_sel(self,sel_error_p):
        """Configure the ERROR_SEL register

        Args:
            sel_error_p (uint1_t): select the internal status/error.
        """

        data = sel_error_p
        addr = self.addr_wire_out['ERROR_SEL']
        self.set_wire_in(addr_p=addr,data_p=data)


    def get_ctrl(self):
        """Retrieve the value from the CTRL register (wire_out)

        Returns:
            uint32_t: read value
        """
        addr = self.addr_wire_out['CTRL']
        res = self.get_wire_out(addr_p=addr)
        return res

    def get_power_ctrl(self):
        """Retrieve the value from the POWER_CTRL register (wire_out)

        Returns:
            uint32_t: read value
        """
        addr = self.addr_wire_out['POWER_CTRL']
        res = self.get_wire_out(addr_p=addr)
        return res

    def get_adc_ctrl(self):
        """Retrieve the value from the ADC_CTRL register (wire_out)

        Returns:
            uint32_t: read value
        """
        addr = self.addr_wire_out['ADC_CTRL']
        res = self.get_wire_out(addr_p=addr)
        return res

    def get_adc_status(self):
        """Retrieve the value from the ADC_STATUS register (wire_out)

        Returns:
            uint32_t: read value
        """
        addr = self.addr_wire_out['ADC_STATUS']
        res = self.get_wire_out(addr_p=addr)
        return res

    def get_adc0(self):
        """Retrieve the read ADC0 value from the ADC device.
        Note:
          . The reading should be done after calling the set_adc_ctrl function

        Returns:
            uint32_t: read value
        """
        addr = self.addr_wire_out['ADC0']
        res = self.get_wire_out(addr_p=addr)
        return res

    def get_adc1(self):
        """Retrieve the read ADC1 value from the ADC device.
        Note:
          . The reading should be done after calling the set_adc_ctrl function

        Returns:
            uint32_t: read value
        """
        addr = self.addr_wire_out['ADC1']
        res = self.get_wire_out(addr_p=addr)
        return res

    def get_adc2(self):
        """Retrieve the read ADC2 value from the ADC device.
        Note:
          . The reading should be done after calling the set_adc_ctrl function

        Returns:
            uint32_t: read value
        """
        addr = self.addr_wire_out['ADC2']
        res = self.get_wire_out(addr_p=addr)
        return res

    def get_adc3(self):
        """Retrieve the read ADC3 value from the ADC device.
        Note:
          . The reading should be done after calling the set_adc_ctrl function

        Returns:
            uint32_t: read value
        """
        addr = self.addr_wire_out['ADC3']
        res = self.get_wire_out(addr_p=addr)
        return res

    def get_adc4(self):
        """Retrieve the read ADC4 value from the ADC device.
        Note:
          . The reading should be done after calling the set_adc_ctrl function

        Returns:
            uint32_t: read value
        """
        addr = self.addr_wire_out['ADC4']
        res = self.get_wire_out(addr_p=addr)
        return res

    def get_adc5(self):
        """Retrieve the read ADC5 value from the ADC device.
        Note:
          . The reading should be done after calling the set_adc_ctrl function

        Returns:
            uint32_t: read value
        """
        addr = self.addr_wire_out['ADC5']
        res = self.get_wire_out(addr_p=addr)
        return res

    def get_adc6(self):
        """Retrieve the read ADC6 value from the ADC device.
        Note:
          . The reading should be done after calling the set_adc_ctrl function

        Returns:
            uint32_t: read value
        """
        addr = self.addr_wire_out['ADC6']
        res = self.get_wire_out(addr_p=addr)
        return res

    def get_adc7(self):
        """Retrieve the read ADC7 value from the ADC device.
        Note:
          . The reading should be done after calling the set_adc_ctrl function

        Returns:
            uint32_t: read value
        """
        addr = self.addr_wire_out['ADC7']
        res = self.get_wire_out(addr_p=addr)
        return res

    def get_debug_ctrl(self):
        """Retrieve the value from the DEBUG_CTRL register (wire_out)

        Returns:
            uint32_t: read value
        """
        addr = self.addr_wire_out['DEBUG_CTRL']
        res = self.get_wire_out(addr_p=addr)
        return res

    def get_error_sel(self):
        """Retrieve the value from the ERROR_SEL register (wire_out)

        Returns:
            uint32_t: read value
        """
        addr = self.addr_wire_out['ERROR_SEL']
        res = self.get_wire_out(addr_p=addr)
        return res

    def get_errors(self):
        """Retrieve the value from the selected internal error register (wire_out)
        Note:
          . before calling this function, select the internal register by calling the set_error_sel function
        Returns:
            uint32_t: read value
        """
        addr = self.addr_wire_out['ERRORS']
        res = self.get_wire_out(addr_p=addr)
        return res

    def get_status(self):
        """Retrieve the value from the selected internal status register (wire_out)
        Note:
          . before calling this function, select the internal register by calling the set_error_sel function
        Returns:
            uint32_t: read value
        """
        addr = self.addr_wire_out['STATUS']
        res = self.get_wire_out(addr_p=addr)
        return res

    def get_hardware_id(self):
        """Retrieve the value from HARDWARE_ID register (wire_out)
        Returns:
            uint32_t: read value
        """
        addr = self.addr_wire_out['HARDWARE_ID']
        res = self.get_wire_out(addr_p=addr)
        return res

    def get_firmware_name(self):
        """Retrieve the value from FIRMWARE_NAME register (wire_out)
        Returns:
            uint32_t: read value
        """
        addr = self.addr_wire_out['FIRMWARE_NAME']
        res = self.get_wire_out(addr_p=addr)
        return res

    def get_firmware_id(self):
        """Retrieve the value from FIRMWARE_ID register (wire_out)
        Returns:
            uint32_t: read value
        """
        addr = self.addr_wire_out['FIRMWARE_ID']
        res = self.get_wire_out(addr_p=addr)
        return res

    ###########################################
    # debugging
    def set_debug_wirein_by_name(self,reg_name_p,data_p):
        """By register name, set the wire_in register value

        Args:
            reg_name_p (str): register name (wire_in)
            data_p (uint32_t): value to write
        """

        addr = self.addr_wire_in.get(reg_name_p)
        if addr is None:
            print("[KO]: " + reg_name_p + "register doesn't exist")
        else:
            self.set_wire_in(addr_p=addr,data_p=data_p)

    def get_debug_wireout_by_name(self,reg_name_p):
        """By register name, get the wire_out register value.

        Args:
            reg_name_p (str): register name (wire_out)
        """
        addr = self.addr_wire_out.get(reg_name_p)
        if addr is None:
            print("[KO]: " + reg_name_p + "register doesn't exist")
            return -1

        if reg_name_p == 'CTRL':
            value = self.get_ctrl()
        elif reg_name_p == "POWER_CTRL":
            value = self.get_power_ctrl()
        elif reg_name_p == "ADC_CTRL":
            value = self.get_adc_ctrl()
        elif reg_name_p == "ADC_STATUS":
            value = self.get_adc_status()
        elif reg_name_p == "ADC0":
            value = self.get_adc0()
        elif reg_name_p == "ADC1":
            value = self.get_adc1()
        elif reg_name_p == "ADC2":
            value = self.get_adc2()
        elif reg_name_p == "ADC3":
            value = self.get_adc3()
        elif reg_name_p == "ADC4":
            value = self.get_adc4()
        elif reg_name_p == "ADC5":
            value = self.get_adc5()
        elif reg_name_p == "ADC6":
            value = self.get_adc6()
        elif reg_name_p == "ADC7":
            value = self.get_adc7()
        elif reg_name_p == "DEBUG_CTRL":
            value = self.get_debug_ctrl()
        elif reg_name_p == "ERROR_SEL":
            value = self.get_error_sel()
        elif reg_name_p == "ERRORS":
            value = self.get_errors()
        elif reg_name_p == "STATUS":
            value = self.get_status()
        elif reg_name_p == "HARDWARE_ID":
            value = self.get_hardware_id()
        elif reg_name_p == "FIRMWARE_NAME":
            value = self.get_firmware_name()
        elif reg_name_p == "FIRMWARE_ID":
            value = self.get_firmware_id()

        return value