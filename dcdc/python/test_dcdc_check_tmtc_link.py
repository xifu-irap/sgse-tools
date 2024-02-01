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
#    @file                   test_dcdc_check_tmtc_link.py
# -------------------------------------------------------------------------------------------------------------
#    Automatic Generation    No
#    Code Rules Reference    N/A
# -------------------------------------------------------------------------------------------------------------
#   @details
#
#   Provide functions (write/read) in order to access to all DCDC registers.
#
# ------------------------------------------------------------------------------------------------------------

# Standard library
import sys
from pathlib import Path
import time

# get the script base path
script_base_path = str(Path(__file__).parents[0])
script_name      = str(Path(__file__).stem)


# custom library
from driver import DCDC,Display,check_equal


def test_wire(device_p):
    device = device_p

    # count error
    cnt_error_wire = 0

    ############################################
    # check the CTRL register
    ############################################
    mask  = 0xFFFF_FFFE # don't touch the rst bit
    data0 = 0x09AB_CEF0 & mask

    msg = "DCDC: Set the register: CTRL"
    device.display(msg)
    # set register
    device.set_debug_wirein_by_name("CTRL",data0)
    # read register
    data1 = device.get_debug_wireout_by_name("CTRL")

    # check the read data Vs the written data
    msg = "DCDC: Check register: CTRL.";
    error = check_equal(device,data0, data1, msg)
    if error == -1:
        cnt_error_wire += 1


    ############################################
    # check the POWER_CTRL register
    ############################################
    mask  = 0xFFFF_FFF0; # don't touch the rst bit
    data0 = 0xBCDE_FEAB & mask

    msg = "DCDC: Set the register: POWER_CTRL"
    device.display(msg)
    # set register
    device.set_debug_wirein_by_name("POWER_CTRL",data0)
    # read register
    data1 = device.get_debug_wireout_by_name("POWER_CTRL")

    # check the read data Vs the written data
    msg = "DCDC: Check register: POWER_CTRL"
    error = check_equal(device,data0, data1, msg)
    if error == -1:
        cnt_error_wire += 1


    ############################################
    # check the DEBUG_CTRL register
    ############################################
    # don't touch the rst_status and debug_pulse bit
    mask  = 0xFFFF_FFFC
    data0 = 0xAAAA_BBBB & mask

    msg = "DCDC: Set the register: DEBUG_CTRL"
    device.display(msg)
    # set register
    device.set_debug_wirein_by_name("DEBUG_CTRL",data0)
    # read register
    data1 = device.get_debug_wireout_by_name("DEBUG_CTRL")

    # check the read data Vs the written data
    msg = "DCDC: Check register: DEBUG_CTRL";
    error = check_equal(device,data0, data1, msg)
    if error == -1:
        cnt_error_wire += 1

    ############################################
    # check the ERROR_SEL register
    ############################################
    data0 = 0xCCCC_DDDD

    msg = "DCDC: Set the register: ERROR_SEL"
    device.display(msg)
    # set register
    device.set_debug_wirein_by_name("ERROR_SEL",data0)
    # read register
    data1 = device.get_debug_wireout_by_name("ERROR_SEL")

    # check the read data Vs the written data
    msg = "DCDC: Check register: ERROR_SEL"
    error = check_equal(device,data0, data1, msg)
    if error == -1:
        cnt_error_wire += 1

    return cnt_error_wire



if __name__ == '__main__':

    # path to the firmware
    firmware_filepath =  str(Path(script_base_path,"..\\..\\dcdc-fw_001.bit").resolve())

    # Program the FPGA
    board = DCDC()
    board.open(firmware_filepath_p=firmware_filepath)

    ###########################################
    # display the test description
    ###########################################
    msg = "tmtc Test Description: " + script_name
    board.display_title(msg)

    msg = 'Context and purpose of the test.'
    board.display_subtitle(msg)

    msg_list = [
    'The test purpose is to check the communication between the DCDC firmware and XIFU Studio application by writting and reading the DCDC registers.'
    ]
    board.display(msg_list)

    msg = 'Test progress.'
    board.display_subtitle(msg)
    msg_list = [
    "Read constant register values (example: FIRMWARE_ID, FIRMWARE_NAME, etc.)",
    "Test the DCDC register configuration.",
    "    . For each main register, do the following steps:",
    "      . write -> read back -> check (written value = reading value?)"
    ]
    board.display(msg_list)

    msg = ""
    board.display(msg)
    ###########################################
    # Test to execute
    ###########################################
    msg = "Tests to execute:"
    board.display_title(msg)

    ###########################################
    # test wire access
    ###########################################
    error_wire_cnt = test_wire(board)


    ###########################################
    # check internal error
    ###########################################
    cnt_error = board.check_internal_errors()

    ###########################################
    # summary
    ###########################################
    # get HARDWARE_ID
    reg_name = 'HARDWARE_ID'
    msg = "DCDC: Get " + reg_name + ": "
    board.display(msg)
    data = board.get_wireout_by_name(reg_name)

    msg = ""
    board.display(msg)

    # get the FIRMWARE_NAME
    reg_name = 'FIRMWARE_NAME'
    msg = "TMTC: Get " + reg_name + ": "
    board.display(msg)
    data = board.get_wireout_by_name(reg_name)


    msg = " "
    board.display(msg)

    # get FIRMWARE_ID
    reg_name = 'FIRMWARE_ID'
    msg = "TMTC: Get " + reg_name + ": "
    board.display(msg)
    data = board.get_wireout_by_name(reg_name)

    msg = " "
    board.display(msg)

    # summary of the test_wire errors.
    if (error_wire_cnt == 0):
        msg_tmp = "[OK]: test_wire has " + str(error_wire_cnt) + " error.";
        board.display(msg_tmp)
    else:
        msg_tmp = "[KO]: test_wire has " + str(error_wire_cnt) + " errors.";
        board.display(msg_tmp)

    # summary of the internal errors.
    if (error_wire_cnt == 0):
        msg_tmp = "[OK]: Internal errors has " + str(error_wire_cnt) + " error.";
        board.display(msg_tmp)
    else:
        msg_tmp = "[KO]: Internal errors has " + str(error_wire_cnt) + " errors.";
        board.display(msg_tmp)

