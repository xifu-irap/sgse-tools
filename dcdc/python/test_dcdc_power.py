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
#    @file                   test_dcdc_power.py
# -------------------------------------------------------------------------------------------------------------
#    Automatic Generation    No
#    Code Rules Reference    N/A
# -------------------------------------------------------------------------------------------------------------
#   @details
#
#   Test: check the power control
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


def test_power(device_p):
    device = device_p

    test = 1
    cnt = 0
    while test:
        device.display_title("test_power "+'{0:02d}'.format(cnt))
        cnt += 1
        str_value = input("Set the power: value (bit3:wfee,bit2:ras,bit1:dmx1,bit0:dwx0), -1: to stop: ")
        if str_value.isnumeric():
            # get the value
            value = int(str_value)
        else:
            if str_value == "-1":
                # stop the test
                break;
            else:
                # string: not a numeric, not "-1" => re-ask because we must have a numeric input value
                continue

            # not numeric => re-ask the value

        dmx0_power_on_off = (value >> 0) & 0x1
        dmx1_power_on_off = (value >> 1) & 0x1
        ras_power_on_off  = (value >> 2) & 0x1
        wfee_power_on_off = (value >> 3) & 0x1

        msg = "DCDC: Set the register: POWER_CTRL"
        device.display(msg)
        device.set_power(dmx0_power_on_off,dmx1_power_on_off,ras_power_on_off,wfee_power_on_off)
        device.display("")




if __name__ == '__main__':

    ###########################################
    # User-defined parameters
    ###########################################
    # path to the firmware
    firmware_filepath =  str(Path(script_base_path,"..\\..\\dcdc-fw_002.bit").resolve())
    # level of verbosity
    verbosity = 2


    ###########################################
    # Start script
    ###########################################

    # Program the FPGA
    board = DCDC()
    board.open(firmware_filepath_p=firmware_filepath)

    board.set_verbosity(verbosity)

    # display the test description
    ###########################################
    msg = "tmtc Test Description: " + script_name
    board.display_title(msg)

    msg = 'Context and purpose of the test.'
    board.display_subtitle(msg)

    msg_list = [
    'The test purpose is to check the power control.'
    ]
    board.display(msg_list)

    msg = 'Test progress.'
    board.display_subtitle(msg)
    msg_list = [
    "Test the power configuration",
    "    . loop on user demand",
    ]
    board.display(msg_list)

    msg = ""
    board.display(msg)

    # Test to execute
    ###########################################
    msg = "Tests to execute:"
    board.display_title(msg)

    # test wire access
    ###########################################
    error_power_cnt = test_power(board)


    # check internal error
    ###########################################
    board.display_subtitle("Check internal errors")
    error_internal_cnt = board.check_internal_errors()
    board.display("")
    ###########################################
    # summary
    ###########################################
    board.display_title("SUMMARY")

    # get HARDWARE_ID
    reg_name = 'HARDWARE_ID'
    msg = "DCDC: Get " + reg_name + ": "
    board.display(msg)
    data = board.get_hardware_id()

    msg = ""
    board.display(msg)

    # get the FIRMWARE_NAME
    reg_name = 'FIRMWARE_NAME'
    msg = "TMTC: Get " + reg_name + ": "
    board.display(msg)
    data = board.get_firmware_name()


    msg = " "
    board.display(msg)

    # get FIRMWARE_ID
    reg_name = 'FIRMWARE_ID'
    msg = "TMTC: Get " + reg_name + ": "
    board.display(msg)
    data = board.get_firmware_id()

    msg = " "
    board.display(msg)

    # summary of the test_power.
    if (error_power_cnt == 0):
        msg_tmp = "[OK]: test_power has " + str(error_power_cnt) + " error.";
        board.display(msg_tmp)
    else:
        msg_tmp = "[KO]: test_power has " + str(error_power_cnt) + " errors.";
        board.display(msg_tmp)

    # summary of the internal errors.
    if (error_internal_cnt == 0):
        msg_tmp = "[OK]: Internal errors has " + str(error_internal_cnt) + " error.";
        board.display(msg_tmp)
    else:
        msg_tmp = "[KO]: Internal errors has " + str(error_internal_cnt) + " errors.";
        board.display(msg_tmp)

