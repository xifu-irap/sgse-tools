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
import time

# compute the script path
script_base_path = str(Path(__file__).parents[0])
sys.path.append(script_base_path)

from driver import Driver, convert_uint_to_ascii, convert_uint_to_str_hex

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
        self._addr_wire_in = {}
        self._addr_wire_in['CTRL'] = 0x00
        self._addr_wire_in['POWER_CONF'] = 0x01
        # self._addr_wire_in['RFU'] = 0x02
        # self._addr_wire_in['RFU'] = 0x03
        # self._addr_wire_in['RFU'] = 0x04
        # self._addr_wire_in['ADC_STATUS'] = 0x05
        # self._addr_wire_in['RFU'] = 0x06
        # self._addr_wire_in['RFU'] = 0x07
        # self._addr_wire_in['RFU'] = 0x08
        # self._addr_wire_in['RFU'] = 0x09
        # self._addr_wire_in['RFU'] = 0x0A
        # self._addr_wire_in['RFU'] = 0x0B
        # self._addr_wire_in['RFU'] = 0x0C
        # self._addr_wire_in['RFU'] = 0x0D
        # self._addr_wire_in['RFU'] = 0x0E
        # self._addr_wire_in['RFU'] = 0x0F
        # self._addr_wire_in['ADC0'] = 0x10
        # self._addr_wire_in['ADC1'] = 0x11
        # self._addr_wire_in['ADC2'] = 0x12
        # self._addr_wire_in['ADC3'] = 0x13
        # self._addr_wire_in['ADC4'] = 0x14
        # self._addr_wire_in['ADC5'] = 0x15
        # self._addr_wire_in['ADC6'] = 0x16
        # self._addr_wire_in['ADC7'] = 0x17
        self._addr_wire_in['DEBUG_CTRL'] = 0x18
        self._addr_wire_in['ERROR_SEL'] = 0x19
        # self._addr_wire_in['ERRORS'] = 0x1A
        # self._addr_wire_in['STATUS'] = 0x1B
        # self._addr_wire_in['RFU'] = 0x1C
        # self._addr_wire_in['HARDWARE_ID'] = 0x1D
        # self._addr_wire_in['FIRMWARE_NAME'] = 0x1E
        # self._addr_wire_in['FIRMWARE_ID'] = 0x1F

        # list all wire_out addresses
        #################################################
        self._addr_wire_out = {}
        self._addr_wire_out['CTRL'] = 0x20
        self._addr_wire_out['POWER_CONF'] = 0x21
        # self._addr_wire_out['RFU'] = 0x22
        # self._addr_wire_out['RFU'] = 0x23
        # self._addr_wire_out['RFU'] = 0x24
        self._addr_wire_out['ADC_STATUS'] = 0x25
        # self._addr_wire_out['RFU'] = 0x26
        # self._addr_wire_out['RFU'] = 0x27
        # self._addr_wire_out['RFU'] = 0x28
        # self._addr_wire_out['RFU'] = 0x29
        # self._addr_wire_out['RFU'] = 0x2A
        # self._addr_wire_out['RFU'] = 0x2B
        # self._addr_wire_out['RFU'] = 0x2C
        # self._addr_wire_out['RFU'] = 0x2D
        # self._addr_wire_out['RFU'] = 0x2E
        # self._addr_wire_out['RFU'] = 0x2F
        self._addr_wire_out['ADC0'] = 0x30
        self._addr_wire_out['ADC1'] = 0x31
        self._addr_wire_out['ADC2'] = 0x32
        self._addr_wire_out['ADC3'] = 0x33
        self._addr_wire_out['ADC4'] = 0x34
        self._addr_wire_out['ADC5'] = 0x35
        self._addr_wire_out['ADC6'] = 0x36
        self._addr_wire_out['ADC7'] = 0x37
        self._addr_wire_out['DEBUG_CTRL'] = 0x38
        self._addr_wire_out['ERROR_SEL'] = 0x39
        self._addr_wire_out['ERRORS'] = 0x3A
        self._addr_wire_out['STATUS'] = 0x3B
        # self._addr_wire_out['RFU'] = 0x3C
        self._addr_wire_out['HARDWARE_ID'] = 0x3D
        self._addr_wire_out['FIRMWARE_NAME'] = 0x3E
        self._addr_wire_out['FIRMWARE_ID'] = 0x3F

        # Trig in: index of the bit
        #######################################
        self._addr_trigin = {}
        self._addr_trigin['TRIG_CTRL']  = 0x40;

        self._pos_trigin = {}
        self._pos_trigin['power_valid'] = 0;
        self._pos_trigin['adc_valid']   = 4;

        # ADC
        #######################################
        # ADC analog voltage
        self._c_ADC_VA = 5

        # ADC resolution (expressed in bits)
        self._c_ADC_res = 12

        # register
        #######################################
        # data width of the register
        self._c_REG_DATA_WIDTH = 32
        # address width of the register
        self._c_REG_ADDR_WIDTH = 32

        # print
        #######################################
        # level of _verbosity
        self._verbosity = 0

        # level of _verbosity to print the function name
        self._c_VERBOSITY_REG = 0
        # level of _verbosity to print the data/address
        self._c_VERBOSITY_ADDR = 1
        # level of _verbosity to print the bit values
        self._c_VERBOSITY_BIT = 2

    def set_verbosity(self,value_p):
        """Set the level of verbosity

        Args:
            value_p (uint_t): level of verbosity (-1: no verbosity, level of verbosity: 1 to 2)
        """
        self._verbosity =  value_p

    def set_ctrl(self,rst_p):
        """Configure the CTRL register

        Args:
            rst_p (uint1_t): software reset
        """

        data = rst_p & 0x1
        addr = self._addr_wire_in['CTRL']
        self.set_wire_in(addr,data)

        # print
        ####################################
        level0 = self.level
        level1 = self.level + 1
        level2 = self.level + 2

        if self._verbosity < 0:
            # no print
            pass
        else:
            if self._verbosity >= self._c_VERBOSITY_REG:
                msg = "[dcdc.set_ctrl]: Set the register value ";
                self.display(msg,level0)
            if self._verbosity >= self._c_VERBOSITY_ADDR:
                self.display_register(addr, self._c_REG_ADDR_WIDTH, data, self._c_REG_DATA_WIDTH, level1)
            if self._verbosity >= self._c_VERBOSITY_BIT:
                self.display_bit("rst_p", rst_p, 0, level2)

    def set_power(self,dmx0_power_on_off_p,dmx1_power_on_off_p,ras_power_on_off_p,wfee_power_on_off_p):
        """ Start the power_top function

        Args:
            dmx0_power_on_off_p (uint1_t): DMX0- 1: power up, 0: power down
            dmx1_power_on_off_p (uint1_t): DMX1- 1: power up, 0: power down
            ras_power_on_off_p (uint1_t): RAS- 1: power up, 0: power down
            wfee_power_on_off_p (uint1_t): WFEE- 1: power up, 0: power down
        """
        # print
        ####################################
        level0 = self.level
        if self._verbosity >= self._c_VERBOSITY_REG:
            msg = "[dcdc.set_power]: Set the register value ";
            self.display(msg,level0)

        self.set_power_trig()
        self.set_power_conf(dmx0_power_on_off_p,dmx1_power_on_off_p,ras_power_on_off_p,wfee_power_on_off_p)

    def set_power_trig(self):
        """
         Activate the power_valid trig

        """

        addr = self._addr_trigin['TRIG_CTRL']
        data = self._pos_trigin['power_valid']

        # print
        ####################################
        level0 = self.level
        level1 = self.level + 1
        level2 = self.level + 2

        if self._verbosity < 0:
            # no print
            pass
        else:
            if self._verbosity >= self._c_VERBOSITY_REG:
                msg = "[dcdc.set_power_trig]: Set the register value ";
                self.display(msg,level0)
            if self._verbosity >= self._c_VERBOSITY_ADDR:
                self.display_register(addr, self._c_REG_ADDR_WIDTH, data, self._c_REG_DATA_WIDTH, level1)
            if self._verbosity >= self._c_VERBOSITY_BIT:
                self.display_bit("power_valid index", data, 0, level2)

    def set_power_conf(self,dmx0_power_on_off_p,dmx1_power_on_off_p,ras_power_on_off_p,wfee_power_on_off_p):
        """
        Configure the POWER_CONF register

        Args:
            dmx0_power_on_off_p (uint1_t): DMX0- 1: power up, 0: power down
            dmx1_power_on_off_p (uint1_t): DMX1- 1: power up, 0: power down
            ras_power_on_off_p (uint1_t): RAS- 1: power up, 0: power down
            wfee_power_on_off_p (uint1_t): WFEE- 1: power up, 0: power down
        """
        data1 = (wfee_power_on_off_p << 3) + (ras_power_on_off_p << 2)
        data0 = (dmx1_power_on_off_p << 1 ) + (dmx0_power_on_off_p << 0)

        data = data1 + data0
        addr = self._addr_wire_in['POWER_CONF']
        self.set_wire_in(addr,data)

        # print
        ####################################
        level0 = self.level
        level1 = self.level + 1
        level2 = self.level + 2

        if self._verbosity < 0:
            # no print
            pass
        else:
            if self._verbosity >= self._c_VERBOSITY_REG:
                msg = "[dcdc.set_power_conf]: Set the register value ";
                self.display(msg,level0)
            if self._verbosity >= self._c_VERBOSITY_ADDR:
                self.display_register(addr, self._c_REG_ADDR_WIDTH, data, self._c_REG_DATA_WIDTH, level1)
            if self._verbosity >= self._c_VERBOSITY_BIT:
                self.display_bit("dmx0_power_on_off_p", dmx0_power_on_off_p, 0, level2)
                self.display_bit("dmx1_power_on_off_p", dmx1_power_on_off_p, 1, level2)
                self.display_bit("ras_power_on_off_p", ras_power_on_off_p, 2, level2)
                self.display_bit("wfee_power_on_off_p", wfee_power_on_off_p, 3, level2)

    def set_adc(self):
        """
            Start the dcdc_top function

        """
        # print
        ####################################
        level0 = self.level
        if self._verbosity >= self._c_VERBOSITY_REG:
            msg = "[dcdc.set_adc]: Set the register value ";
            self.display(msg,level0)

        self.set_adc_trig()

    def set_adc_trig(self):
        """
           Activate the adc_valid trig

        """

        addr = self._addr_trigin['TRIG_CTRL']
        data = self._pos_trigin['adc_valid']

        # print
        ####################################
        level0 = self.level
        level1 = self.level + 1
        level2 = self.level + 2

        if self._verbosity < 0:
            # no print
            pass
        else:
            if self._verbosity >= self._c_VERBOSITY_REG:
                msg = "[dcdc.set_adc_trig]: Set the register value ";
                self.display(msg,level0)
            if self._verbosity >= self._c_VERBOSITY_ADDR:
                self.display_register(addr, self._c_REG_ADDR_WIDTH, data, self._c_REG_DATA_WIDTH, level1)
            if self._verbosity >= self._c_VERBOSITY_BIT:
                self.display_bit("adc_valid index", data, 0, level2)

    def set_debug_ctrl(self,rst_status_p,debug_pulse_p):
        """Configure the DEBUG_CTRL register

        Args:
            rst_status_p (uint1_t): 1: reset the internal errors, 0: do nothing
            debug_pulse_p (uint1_t): 1: delay error, 0: latch error
        """

        data = ( rst_status_p << 1) + debug_pulse_p
        addr = self._addr_wire_in['DEBUG_CTRL']
        self.set_wire_in(addr,data)

        # print
        ####################################
        level0 = self.level
        level1 = self.level + 1
        level2 = self.level + 2

        if self._verbosity < 0:
            # no print
            pass
        else:
            if self._verbosity >= self._c_VERBOSITY_REG:
                msg = "[dcdc.set_debug_ctrl]: Set the register value ";
                self.display(msg,level0)
            if self._verbosity >= self._c_VERBOSITY_ADDR:
                self.display_register(addr, self._c_REG_ADDR_WIDTH, data, self._c_REG_DATA_WIDTH, level1)
            if self._verbosity >= self._c_VERBOSITY_BIT:
                self.display_bit("debug_pulse_p", debug_pulse_p, 0, level2)
                self.display_bit("rst_status_p", rst_status_p, 1, level2)

    def set_error_sel(self,sel_error_p):
        """Configure the ERROR_SEL register

        Args:
            sel_error_p (uint1_t): select the internal status/error.
        """

        data = sel_error_p
        addr = self._addr_wire_in['ERROR_SEL']
        self.set_wire_in(addr,data)

        # print
        ####################################
        level0 = self.level
        level1 = self.level + 1
        level2 = self.level + 2

        if self._verbosity < 0:
            # no print
            pass
        else:
            if self._verbosity >= self._c_VERBOSITY_REG:
                msg = "[dcdc.set_error_sel]: Set the register value ";
                self.display(msg,level0)
            if self._verbosity >= self._c_VERBOSITY_ADDR:
                self.display_register(addr, self._c_REG_ADDR_WIDTH, data, self._c_REG_DATA_WIDTH, level1)
            if self._verbosity >= self._c_VERBOSITY_BIT:
                self.display_bit("sel_error_p", sel_error_p, 0, level2)

    def get_ctrl(self):
        """Retrieve the value from the CTRL register (wire_out)

        Returns:
            uint32_t: read value
        """
        addr = self._addr_wire_out['CTRL']
        data = self.get_wire_out(addr_p=addr)

        # print
        ####################################
        level0 = self.level
        level1 = self.level + 1
        level2 = self.level + 2

        if self._verbosity < 0:
            # no print
            pass
        else:
            if self._verbosity >= self._c_VERBOSITY_REG:
                msg = "[dcdc.get_ctrl]: Set the register value ";
                self.display(msg,level0)
            if self._verbosity >= self._c_VERBOSITY_ADDR:
                self.display_register(addr, self._c_REG_ADDR_WIDTH, data, self._c_REG_DATA_WIDTH, level1)
            if self._verbosity >= self._c_VERBOSITY_BIT:
                self.display_bit_from_data("rst", 0, 1, data, level2)

        return data

    def get_power_conf(self):
        """Retrieve the value from the POWER_CONF register (wire_out)

        Returns:
            uint32_t: read value
        """
        addr = self._addr_wire_out['POWER_CONF']
        data = self.get_wire_out(addr_p=addr)

        # print
        ####################################
        level0 = self.level
        level1 = self.level + 1
        level2 = self.level + 2

        if self._verbosity < 0:
            # no print
            pass
        else:
            if self._verbosity >= self._c_VERBOSITY_REG:
                msg = "[dcdc.get_power_conf]: Set the register value ";
                self.display(msg,level0)
            if self._verbosity >= self._c_VERBOSITY_ADDR:
                self.display_register(addr, self._c_REG_ADDR_WIDTH, data, self._c_REG_DATA_WIDTH, level1)
            if self._verbosity >= self._c_VERBOSITY_BIT:
                self.display_bit_from_data("dmx0_power_on_off", 0, 1, data, level2)
                self.display_bit_from_data("dmx1_power_on_off", 1, 1, data, level2)
                self.display_bit_from_data("ras_power_on_off", 2, 1, data, level2)
                self.display_bit_from_data("wfee_power_on_off", 3, 1, data, level2)

        return data

    def get_adc_status(self):
        """Retrieve the value from the ADC_STATUS register (wire_out)

        Returns:
            uint32_t: read value
        """
        addr = self._addr_wire_out['ADC_STATUS']
        data = self.get_wire_out(addr_p=addr)

        # print
        ####################################
        level0 = self.level
        level1 = self.level + 1
        level2 = self.level + 2

        if self._verbosity < 0:
            # no print
            pass
        else:
            if self._verbosity >= self._c_VERBOSITY_REG:
                msg = "[dcdc.get_adc_status]: Set the register value ";
                self.display(msg,level0)
            if self._verbosity >= self._c_VERBOSITY_ADDR:
                self.display_register(addr, self._c_REG_ADDR_WIDTH, data, self._c_REG_DATA_WIDTH, level1)
            if self._verbosity >= self._c_VERBOSITY_BIT:
                self.display_bit_from_data("adc_ready", 0, 1, data, level2)

        return data

    def _compute_adc_voltage(self,data_p):
        """ Convert an ADC numerical value into the corresponding ADC voltage

        Args:
            data_p (uint): ADC numerical value
        """

        voltage = data_p * self._c_ADC_VA/(2**self._c_ADC_res)
        return voltage

    def get_adc0(self):
        """Retrieve the read ADC0 value from the ADC device.
        Note:
          . The reading should be done after calling the set_adc_ctrl function

        Returns:
            uint32_t: read value
        """
        addr = self._addr_wire_out['ADC0']
        data = self.get_wire_out(addr_p=addr)

        # print
        ####################################
        level0 = self.level
        level1 = self.level + 1
        level2 = self.level + 2

        if self._verbosity < 0:
            # no print
            pass
        else:
            if self._verbosity >= self._c_VERBOSITY_REG:
                msg = "[dcdc.get_adc0]: Set the register value ";
                self.display(msg,level0)
            if self._verbosity >= self._c_VERBOSITY_ADDR:
                self.display_register(addr, self._c_REG_ADDR_WIDTH, data, self._c_REG_DATA_WIDTH, level1)
            if self._verbosity >= self._c_VERBOSITY_BIT:
                self.display_bit_from_data("adc0", 0, 16, data, level2)
                voltage = self._compute_adc_voltage(data)
                msg = "ADC (Volt): "+ str(voltage)
                self.display(msg,level2 + 1)

        return data

    def get_adc1(self):
        """Retrieve the read ADC1 value from the ADC device.
        Note:
          . The reading should be done after calling the set_adc_ctrl function

        Returns:
            uint32_t: read value
        """
        addr = self._addr_wire_out['ADC1']
        data = self.get_wire_out(addr_p=addr)

        # print
        ####################################
        level0 = self.level
        level1 = self.level + 1
        level2 = self.level + 2

        if self._verbosity < 0:
            # no print
            pass
        else:
            if self._verbosity >= self._c_VERBOSITY_REG:
                msg = "[dcdc.get_adc1]: Set the register value ";
                self.display(msg,level0)
            if self._verbosity >= self._c_VERBOSITY_ADDR:
                self.display_register(addr, self._c_REG_ADDR_WIDTH, data, self._c_REG_DATA_WIDTH, level1)
            if self._verbosity >= self._c_VERBOSITY_BIT:
                self.display_bit_from_data("adc1", 0, 16, data, level2)
                voltage = self._compute_adc_voltage(data)
                msg = "ADC (Volt): "+ str(voltage)
                self.display(msg,level2 + 1)

        return data

    def get_adc2(self):
        """Retrieve the read ADC2 value from the ADC device.
        Note:
          . The reading should be done after calling the set_adc_ctrl function

        Returns:
            uint32_t: read value
        """
        addr = self._addr_wire_out['ADC2']
        data = self.get_wire_out(addr_p=addr)

        # print
        ####################################
        level0 = self.level
        level1 = self.level + 1
        level2 = self.level + 2

        if self._verbosity < 0:
            # no print
            pass
        else:
            if self._verbosity >= self._c_VERBOSITY_REG:
                msg = "[dcdc.get_adc2]: Set the register value ";
                self.display(msg,level0)
            if self._verbosity >= self._c_VERBOSITY_ADDR:
                self.display_register(addr, self._c_REG_ADDR_WIDTH, data, self._c_REG_DATA_WIDTH, level1)
            if self._verbosity >= self._c_VERBOSITY_BIT:
                self.display_bit_from_data("adc2", 0, 16, data, level2)
                voltage = self._compute_adc_voltage(data)
                msg = "ADC (Volt): "+ str(voltage)
                self.display(msg,level2 + 1)

        return data

    def get_adc3(self):
        """Retrieve the read ADC3 value from the ADC device.
        Note:
          . The reading should be done after calling the set_adc_ctrl function

        Returns:
            uint32_t: read value
        """
        addr = self._addr_wire_out['ADC3']
        data = self.get_wire_out(addr_p=addr)

        # print
        ####################################
        level0 = self.level
        level1 = self.level + 1
        level2 = self.level + 2

        if self._verbosity < 0:
            # no print
            pass
        else:
            if self._verbosity >= self._c_VERBOSITY_REG:
                msg = "[dcdc.get_adc3]: Set the register value ";
                self.display(msg,level0)
            if self._verbosity >= self._c_VERBOSITY_ADDR:
                self.display_register(addr, self._c_REG_ADDR_WIDTH, data, self._c_REG_DATA_WIDTH, level1)
            if self._verbosity >= self._c_VERBOSITY_BIT:
                self.display_bit_from_data("adc3", 0, 16, data, level2)
                voltage = self._compute_adc_voltage(data)
                msg = "ADC (Volt): "+ str(voltage)
                self.display(msg,level2 + 1)

        return data

    def get_adc4(self):
        """Retrieve the read ADC4 value from the ADC device.
        Note:
          . The reading should be done after calling the set_adc_ctrl function

        Returns:
            uint32_t: read value
        """
        addr = self._addr_wire_out['ADC4']
        data = self.get_wire_out(addr_p=addr)

        # print
        ####################################
        level0 = self.level
        level1 = self.level + 1
        level2 = self.level + 2

        if self._verbosity < 0:
            # no print
            pass
        else:
            if self._verbosity >= self._c_VERBOSITY_REG:
                msg = "[dcdc.get_adc4]: Set the register value ";
                self.display(msg,level0)
            if self._verbosity >= self._c_VERBOSITY_ADDR:
                self.display_register(addr, self._c_REG_ADDR_WIDTH, data, self._c_REG_DATA_WIDTH, level1)
            if self._verbosity >= self._c_VERBOSITY_BIT:
                self.display_bit_from_data("adc4", 0, 16, data, level2)
                voltage = self._compute_adc_voltage(data)
                msg = "ADC (Volt): "+ str(voltage)
                self.display(msg,level2 + 1)

        return data

    def get_adc5(self):
        """Retrieve the read ADC5 value from the ADC device.
        Note:
          . The reading should be done after calling the set_adc_ctrl function

        Returns:
            uint32_t: read value
        """
        addr = self._addr_wire_out['ADC5']
        data = self.get_wire_out(addr_p=addr)

        # print
        ####################################
        level0 = self.level
        level1 = self.level + 1
        level2 = self.level + 2

        if self._verbosity < 0:
            # no print
            pass
        else:
            if self._verbosity >= self._c_VERBOSITY_REG:
                msg = "[dcdc.get_adc5]: Set the register value ";
                self.display(msg,level0)
            if self._verbosity >= self._c_VERBOSITY_ADDR:
                self.display_register(addr, self._c_REG_ADDR_WIDTH, data, self._c_REG_DATA_WIDTH, level1)
            if self._verbosity >= self._c_VERBOSITY_BIT:
                self.display_bit_from_data("adc5", 0, 16, data, level2)
                voltage = self._compute_adc_voltage(data)
                msg = "ADC (Volt): "+ str(voltage)
                self.display(msg,level2 + 1)

        return data

    def get_adc6(self):
        """Retrieve the read ADC6 value from the ADC device.
        Note:
          . The reading should be done after calling the set_adc_ctrl function

        Returns:
            uint32_t: read value
        """
        addr = self._addr_wire_out['ADC6']
        data = self.get_wire_out(addr_p=addr)

        # print
        ####################################
        level0 = self.level
        level1 = self.level + 1
        level2 = self.level + 2

        if self._verbosity < 0:
            # no print
            pass
        else:
            if self._verbosity >= self._c_VERBOSITY_REG:
                msg = "[dcdc.get_adc6]: Set the register value ";
                self.display(msg,level0)
            if self._verbosity >= self._c_VERBOSITY_ADDR:
                self.display_register(addr, self._c_REG_ADDR_WIDTH, data, self._c_REG_DATA_WIDTH, level1)
            if self._verbosity >= self._c_VERBOSITY_BIT:
                self.display_bit_from_data("adc6", 0, 16, data, level2)
                voltage = self._compute_adc_voltage(data)
                msg = "ADC (Volt): "+ str(voltage)
                self.display(msg,level2 + 1)

        return data

    def get_adc7(self):
        """Retrieve the read ADC7 value from the ADC device.
        Note:
          . The reading should be done after calling the set_adc_ctrl function

        Returns:
            uint32_t: read value
        """
        addr = self._addr_wire_out['ADC7']
        data = self.get_wire_out(addr_p=addr)

        # print
        ####################################
        level0 = self.level
        level1 = self.level + 1
        level2 = self.level + 2

        if self._verbosity < 0:
            # no print
            pass
        else:
            if self._verbosity >= self._c_VERBOSITY_REG:
                msg = "[dcdc.get_adc7]: Set the register value ";
                self.display(msg,level0)
            if self._verbosity >= self._c_VERBOSITY_ADDR:
                self.display_register(addr, self._c_REG_ADDR_WIDTH, data, self._c_REG_DATA_WIDTH, level1)
            if self._verbosity >= self._c_VERBOSITY_BIT:
                self.display_bit_from_data("adc7", 0, 16, data, level2)
                voltage = self._compute_adc_voltage(data)
                msg = "ADC (Volt): "+ str(voltage)
                self.display(msg,level2 + 1)

        return data

    def get_debug_ctrl(self):
        """Retrieve the value from the DEBUG_CTRL register (wire_out)

        Returns:
            uint32_t: read value
        """
        addr = self._addr_wire_out['DEBUG_CTRL']
        data = self.get_wire_out(addr_p=addr)

        # print
        ####################################
        level0 = self.level
        level1 = self.level + 1
        level2 = self.level + 2

        if self._verbosity < 0:
            # no print
            pass
        else:
            if self._verbosity >= self._c_VERBOSITY_REG:
                msg = "[dcdc.get_debug_ctrl]: Set the register value ";
                self.display(msg,level0)
            if self._verbosity >= self._c_VERBOSITY_ADDR:
                self.display_register(addr, self._c_REG_ADDR_WIDTH, data, self._c_REG_DATA_WIDTH, level1)
            if self._verbosity >= self._c_VERBOSITY_BIT:
                self.display_bit_from_data("debug_pulse", 0, 1, data, level2)
                self.display_bit_from_data("rst_status", 1, 1, data, level2)

        return data

    def get_error_sel(self):
        """Retrieve the value from the ERROR_SEL register (wire_out)

        Returns:
            uint32_t: read value
        """
        addr = self._addr_wire_out['ERROR_SEL']
        data = self.get_wire_out(addr_p=addr)

        # print
        ####################################
        level0 = self.level
        level1 = self.level + 1
        level2 = self.level + 2

        if self._verbosity < 0:
            # no print
            pass
        else:
            if self._verbosity >= self._c_VERBOSITY_REG:
                msg = "[dcdc.get_error_sel]: Set the register value ";
                self.display(msg,level0)
            if self._verbosity >= self._c_VERBOSITY_ADDR:
                self.display_register(addr, self._c_REG_ADDR_WIDTH, data, self._c_REG_DATA_WIDTH, level1)
            if self._verbosity >= self._c_VERBOSITY_BIT:
                self.display_bit_from_data("error_sel", 0, 1, data, level2)


        return data

    def get_errors(self):
        """Retrieve the value from the selected internal error register (wire_out)
        Note:
          . before calling this function, select the internal register by calling the set_error_sel function
        Returns:
            uint32_t: read value
        """
        addr = self._addr_wire_out['ERRORS']
        data = self.get_wire_out(addr_p=addr)

        # print
        ####################################
        level0 = self.level
        level1 = self.level + 1
        level2 = self.level + 2

        if self._verbosity < 0:
            # no print
            pass
        else:
            if self._verbosity >= self._c_VERBOSITY_REG:
                msg = "[dcdc.get_errors]: Set the register value ";
                self.display(msg,level0)
            if self._verbosity >= self._c_VERBOSITY_ADDR:
                self.display_register(addr, self._c_REG_ADDR_WIDTH, data, self._c_REG_DATA_WIDTH, level1)
            if self._verbosity >= self._c_VERBOSITY_BIT:
                self.display_bit_from_data("errors", 0, 32, data, level2)

        return data

    def get_status(self):
        """Retrieve the value from the selected internal status register (wire_out)
        Note:
          . before calling this function, select the internal register by calling the set_error_sel function
        Returns:
            uint32_t: read value
        """
        addr = self._addr_wire_out['STATUS']
        data = self.get_wire_out(addr_p=addr)

        # print
        ####################################
        level0 = self.level
        level1 = self.level + 1
        level2 = self.level + 2

        if self._verbosity < 0:
            # no print
            pass
        else:
            if self._verbosity >= self._c_VERBOSITY_REG:
                msg = "[dcdc.get_status]: Set the register value ";
                self.display(msg,level0)
            if self._verbosity >= self._c_VERBOSITY_ADDR:
                self.display_register(addr, self._c_REG_ADDR_WIDTH, data, self._c_REG_DATA_WIDTH, level1)
            if self._verbosity >= self._c_VERBOSITY_BIT:
                self.display_bit_from_data("status", 0, 32, data, level2)
        return data

    def get_hardware_id(self):
        """Retrieve the value from HARDWARE_ID register (wire_out)
        Returns:
            uint32_t: read value
        """
        addr = self._addr_wire_out['HARDWARE_ID']
        data = self.get_wire_out(addr_p=addr)

        # print
        ####################################
        level0 = self.level
        level1 = self.level + 1
        level2 = self.level + 2

        if self._verbosity < 0:
            # no print
            pass
        else:
            if self._verbosity >= self._c_VERBOSITY_REG:
                msg = "[dcdc.get_hardware_id]: Set the register value ";
                self.display(msg,level0)
            if self._verbosity >= self._c_VERBOSITY_ADDR:
                self.display_register(addr, self._c_REG_ADDR_WIDTH, data, self._c_REG_DATA_WIDTH, level1)
            if self._verbosity >= self._c_VERBOSITY_BIT:
                self.display_bit_from_data("HARDWARE_ID", 0, 32, data, level2)

        return data

    def get_firmware_name(self):
        """Retrieve the value from FIRMWARE_NAME register (wire_out)
        Returns:
            uint32_t: read value
        """
        addr = self._addr_wire_out['FIRMWARE_NAME']
        data = self.get_wire_out(addr_p=addr)

        # print
        ####################################
        level0 = self.level
        level1 = self.level + 1
        level2 = self.level + 2

        if self._verbosity < 0:
            # no print
            pass
        else:
            if self._verbosity >= self._c_VERBOSITY_REG:
                msg = "[dcdc.get_firmware_name]: Set the register value ";
                self.display(msg,level0)
            if self._verbosity >= self._c_VERBOSITY_ADDR:
                self.display_register(addr, self._c_REG_ADDR_WIDTH, data, self._c_REG_DATA_WIDTH, level1)
            if self._verbosity >= self._c_VERBOSITY_BIT:
                self.display_bit_from_data("FIRMWARE_NAME", 0, 32, data, level2)
                msg = "(ASCII): " + convert_uint_to_ascii(data, self._c_REG_DATA_WIDTH)
                self.display(msg, level2 + 1)

        return data

    def get_firmware_id(self):
        """Retrieve the value from FIRMWARE_ID register (wire_out)
        Returns:
            uint32_t: read value
        """
        addr = self._addr_wire_out['FIRMWARE_ID']
        data = self.get_wire_out(addr_p=addr)

        # print
        ####################################
        level0 = self.level
        level1 = self.level + 1
        level2 = self.level + 2

        if self._verbosity < 0:
            # no print
            pass
        else:
            if self._verbosity >= self._c_VERBOSITY_REG:
                msg = "[dcdc.get_firmware_id]: Set the register value ";
                self.display(msg,level0)
            if self._verbosity >= self._c_VERBOSITY_ADDR:
                self.display_register(addr, self._c_REG_ADDR_WIDTH, data, self._c_REG_DATA_WIDTH, level1)
            if self._verbosity >= self._c_VERBOSITY_BIT:
                self.display_bit_from_data("FIRMWARE_ID", 0, 32, data, level2)

        return data

    ###########################################
    # debugging
    def set_debug_wirein_by_name(self,reg_name_p,data_p):
        """By register name, set the wire_in register value

        Args:
            reg_name_p (str): register name (wire_in)
            data_p (uint32_t): value to write
        """
        data = data_p
        addr = self._addr_wire_in.get(reg_name_p)
        if addr is None:
            print("[KO]: " + reg_name_p + "register doesn't exist")
        else:
            self.set_wire_in(addr,data)


        # print
        ####################################
        level0 = self.level
        level1 = self.level + 1

        if self._verbosity < 0:
            # no print
            pass
        else:
            if self._verbosity >= self._c_VERBOSITY_REG:
                msg = "[dcdc.set_debug_wirein_by_name]: Set the register value of "+ reg_name_p;
                self.display(msg,level0)
            if self._verbosity >= self._c_VERBOSITY_ADDR:
                self.display_register(addr, self._c_REG_ADDR_WIDTH, data, self._c_REG_DATA_WIDTH, level1)


    def get_debug_wireout_by_name(self,reg_name_p):
        """By register name, get the wire_out register value.

        Args:
            reg_name_p (str): register name (wire_out)
        """
        if self._verbosity < 0:
            # no print
            pass
        else:
            if self._verbosity >= self._c_VERBOSITY_REG:
                msg = "[dcdc.set_debug_wirein_by_name]: Set the register value of "+ reg_name_p;
        addr = self._addr_wire_out.get(reg_name_p)
        if addr is None:
            print("[KO]: " + reg_name_p + "register doesn't exist")
            return -1

        if reg_name_p == 'CTRL':
            value = self.get_ctrl()
        elif reg_name_p == "POWER_CONF":
            value = self.get_power_conf()
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

    def check_internal_errors(self):
        """ Check and count the number of internal errors.

        Note:
          . All internal errors should be set to 0
        """
        # number of internal error/status
        nb_errors = 1

        cnt = 0
        for i in range(nb_errors):
            self.set_debug_wirein_by_name("ERROR_SEL",i)
            # sleep (in s)
            time.sleep(0.2)
            value = self.get_errors()
            if value != 0:
                msg = "[KO]: errors" + str(i)
                cnt += 1
        return cnt

