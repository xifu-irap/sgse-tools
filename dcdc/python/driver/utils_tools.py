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

# standard library
import math

class Display:
    """
       Provide low level functions for the display
    """

    def __init__(self):
        """init the variable
        """
        # separator for the title/sub-title
        self.char_section = "*"
        # number of separator char
        self.nb_char_section = 70
        # separator for the indentation
        self.char_indent = " "
        # number of character for the indentation
        self.nb_char_indent = 4

        # level of indentation
        self.level = 0



    def _compute_indent(self):
        """compute the string for the indentation

        Returns:
            str: string for the indentation
        """
        return self.char_indent * self.nb_char_indent * self.level

    def _compute_section(self):
        """Compute the string for the section (separator)

        Returns:
            str: string for the section
        """
        return self.char_section * self.nb_char_section * self.level

    def display_title(self,msg_p):
        """print a title to the console

        Args:
            msg_p (str or list of str): message to print
        """

        msg_list = convert_str_to_str_list(msg_p=msg_p)
        str_indent = self._compute_indent()
        str_section = self._compute_section()

        str_sep = str_indent + str_section

        print("")
        print(str_sep)
        for msg in msg_list:
            str0 = str_indent + " " + msg
            print(str0)
        print(str_sep)

    def display_subtitle(self,msg_p):
        """print a subtitle to the console

        Args:
            msg_p (str or list of str): message to print
        """

        msg_list = convert_str_to_str_list(msg_p=msg_p)
        str_indent = self._compute_indent()
        str_section = self._compute_section()

        str_sep = str_indent + str_section

        print("")
        for msg in msg_list:
            str0 = str_indent + " " + msg
            print(str0)
        print(str_sep)

    def display(self,msg_p):
        """print a subtitle to the console

        Args:
            msg_p (str or list of str): message to print
        """

        msg_list = convert_str_to_str_list(msg_p=msg_p)
        str_indent = self._compute_indent()

        for msg in msg_list:
            str0 = str_indent + " " + msg
            print(str0)

    def display_register(self,addr_p, addr_width_p, data_p, data_width_p):
        """print the register (addr, data)

        Args:
            addr_p (uint): address value
            addr_width_p (uint): address width (expressed in bits: start@1)
            data_p (uint): data value
            data_width_p (uint): data width (expressed in bits: start@1)
        """

        msg = "addr: 0x" + convert_uint_to_str_hex(addr_p,addr_width_p)
        self.display(msg)
        msg = "data: 0x" + convert_uint_to_str_hex(data_p,data_width_p)
        self.display(msg)

    def display_bit_from_data(self,bit_name_p, bit_pos_p, bit_width_p, data_p):
        """print the bit field value

        Args:
            bit_name_p (str): bit field name
            bit_pos_p (uint): index low of the position of the bit field (start from @0)
            bit_width_p (uint): bit width (expressed in bits: start@1)
            data_p (int): data where to extract the bit field
        """

        #  build mask for the data bit field
        mask = 2**(bit_width_p) - 1
        # keep the bit field value
        value = (data_p >> bit_pos_p) & mask

        self.display_bit(bit_name_p,value, bit_width_p)

    def display_bit(self,bit_name_p, bit_value_p, bit_width_p):
        """print the bit field value

        Args:
            bit_name_p (str): bit field name
            bit_value_p (int): bit field value
            bit_width_p (uint): bit field width (expressed in bits: start@1)
        """
        # convert int to uint
        if bit_value_p < 0:
            bit_value = convert_int_to_uint(bit_value_p, bit_width_p)
        else:
            bit_value = bit_value_p

        msg = bit_name_p + ": 0x" + convert_uint_to_str_hex(bit_value,bit_width_p)
        self.display(msg)

def check_equal(display_p,value0_p, value1_p, msg_p):
    """check if 2 values are equal

    Args:
        display_p (Display class): instance of the Display class
        value0_p (int): first value to compare
        value1_p (int): second value to compare
        msg_p (str): message to print

    Returns:
        int: error status
    """

    disp = display_p
    str_data0 = convert_uint_to_str_hex(value0_p,32)
    str_data1 = convert_uint_to_str_hex(value1_p,32)

    if value0_p != value1_p:
        msg = "[KO]: " + msg_p
        disp.display(msg)
        msg = "[check_equal]: value0_p: 0x" + str_data0 + " !=  value_1_p: 0x" + str_data1;
        disp.display(msg)
        return -1
    else:
        msg = "[OK]: " + msg_p
        disp.display(msg)
        msg = "[check_equal]: value0_p: 0x" + str_data0 + " !=  value_1_p: 0x" + str_data1;
        disp.display(msg)
        return 0


def convert_str_to_str_list(msg_p):
    """convert the input msg into a list if it's not.

    Args:
        msg_p (str): message (list or not)

    Returns:
        list of str: return a list of string
    """

    if isinstance(msg_p, list):
        return msg_p
    else:
        return [msg_p]

def convert_uint_to_str_hex(value_p, width_p):
    """Convert an integer into a hexadecimal string

    Args:
        value_p (uint): unsigned integer value to convert
        width_p (uint): value width (expressed in bits: start@1)

    Returns:
        str: hexadecimal string
    """
    # compute the number of hex characters
    nb_hex_char = math.ceil(width_p/4)
    # compute the formatting string
    str_format = '{0:0' + nb_hex_char + 'x}'
    # convert value to hexadecimal string
    str_hex = str_format.format(value_p)

    return str_hex

def convert_uint_to_ascii(value_p, width_p):
    """Convert a value to a ASCII string

    Args:
        value_p (uint): unsigned integer value to convert
        width_p (uint): value width (expressed in bits: start@1)

    Returns:
        str: ASCII string
    """

    # compute the number of bytes
    nb_bytes = math.ceil(width_p/8)

    str0 = ''
    for i in range(nb_bytes):
        # scan each bytes
        value = (value_p >> (8*i) ) & 0xFF
        # convert each byte into ASCII character
        ascii_str = chr(value)
        # build ascii string
        str0 = ascii_str + str0

    return str0

def convert_uint_to_int(data_p,width_p):
    """convert an unsigned integer value to a signed integer value

    Args:
        data_p (uint): unsigned integer value to convert
        width_p (uint): value width (expressed in bits: start@1)

    Returns:
        int: converted value
    """
    if data_p >= 2**(width_p - 1):
        val = data_p - 2**width_p
    else:
        val = data_p
    return val

def convert_int_to_uint(data_p,width_p):
    """Convert a signed integer value into a unsigned integer value

    Args:
        data_p (int): signed integer value to convert
        width_p (uint): value width (expressed in bits: start@1)

    Returns:
        uint: converted value
    """
    if data_p < 0:
        val = 2**width_p + data_p
    else:
        val = data_p
    return val


