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
#   Test: check the ADCs' reading
#
# ------------------------------------------------------------------------------------------------------------

# Standard library
import sys
from pathlib import Path
import time
import argparse
import os

# get the script base path
script_base_path = str(Path(__file__).parents[0])
script_name      = str(Path(__file__).stem)

# custom library
from driver import DCDC,Display,check_equal


def test_adc(device_p):
    device = device_p

    test = 1
    cnt = 0
    while test:
        device.display_title("test_adc "+'{0:02d}'.format(cnt))
        cnt += 1
        str_value = input("Get ADCs value, press: -1 (to stop), 0 (default: to continue): ")
        print("str_value ", str_value)
        if str_value.isnumeric():
            # all numeric
            pass
        else:
            if str_value == "-1":
                # stop the test
                break;
            else:
                # string: not numeric, not "-1"
                pass



        msg = "DCDC: Start the ADCs acquisition"
        device.display(msg)
        device.set_adc()

        device.display("")

        # tempo to be sure to be able to retrieve adc values
        time.sleep(1)

        # get the adc value
        msg = "DCDC: Get the register: ADC0"
        device.display(msg)
        adc0 = device.get_adc0()
        device.display("")

        msg = "DCDC: Get the register: ADC1"
        device.display(msg)
        adc1 = device.get_adc1()
        device.display("")

        msg = "DCDC: Get the register: ADC2"
        device.display(msg)
        adc2 = device.get_adc2()
        device.display("")

        msg = "DCDC: Get the register: ADC3"
        device.display(msg)
        adc3 = device.get_adc3()
        device.display("")

        msg = "DCDC: Get the register: ADC4"
        device.display(msg)
        adc4 = device.get_adc4()
        device.display("")

        msg = "DCDC: Get the register: ADC5"
        device.display(msg)
        adc5 = device.get_adc5()
        device.display("")

        msg = "DCDC: Get the register: ADC6"
        device.display(msg)
        adc6 = device.get_adc6()
        device.display("")

        msg = "DCDC: Get the register: ADC7"
        device.display(msg)
        adc7 = device.get_adc7()
        device.display("")


    return 0




if __name__ == '__main__':

    ###########################################
    # parse command line
    ###########################################
    # user-defined: default firmware filepath (relative to this script path)
    default_firmware_filpath = "..\\..\\dcdc-fw_002.bit"

    parser = argparse.ArgumentParser(description='Define command line arguments')
    # add an optional argument with limited choices
    parser.add_argument('--firmware_filepath', '-f', default=default_firmware_filpath,
                        help='The firmware filepath can be absolute or relative to this script path.')

    args_known = parser. parse_known_args()
    # get arguments defined in this file.
    args = args_known[0]
    # get arguments not defined in this file in order to pass them to the called script.
    args_unknown = args_known[1]

    ###########################################
    # User-defined parameters
    ###########################################
    # path to the firmware
    firmware_filepath = args.firmware_filepath

    if os.path.isabs(firmware_filepath):
        # absolute path
        # print("absolute path: ",firmware_filepath)
        firmware_filepath = firmware_filepath
    else:
        # compute the absolute path relative to this script path
        # print("relative_path: ",firmware_filepath)
        firmware_filepath = str(Path(script_base_path,firmware_filepath).resolve())

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
    "The test purpose is to check the ADCs' reading."
    ]
    board.display(msg_list)

    msg = 'Test progress.'
    board.display_subtitle(msg)
    msg_list = [
    "Test the ADCs' reading",
    "    . loop on user demand",
    "  IMPORTANT:",
    "    . The test is not full automatized => visually check the ADC voltage"
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
    error_adc_cnt = test_adc(board)


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

    # summary of the test_adc.
    # if (error_adc_cnt == 0):
    #     msg_tmp = "[OK]: Test: ADC reading has " + str(error_adc_cnt) + " error.";
    #     board.display(msg_tmp)
    # else:
    #     msg_tmp = "[KO]: Test: ADC reading has " + str(error_adc_cnt) + " errors.";
    #     board.display(msg_tmp)

    # summary of the internal errors.
    if (error_internal_cnt == 0):
        msg_tmp = "[OK]: Internal errors has " + str(error_internal_cnt) + " error.";
        board.display(msg_tmp)
    else:
        msg_tmp = "[KO]: Internal errors has " + str(error_internal_cnt) + " errors.";
        board.display(msg_tmp)

