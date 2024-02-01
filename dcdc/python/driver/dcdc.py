import sys
from pathlib import Path

script_base_path = str(Path(__file__).parents[0])
sys.path.append(script_base_path)

from driver import Driver

class DCDC(Driver):
    """
    """

    def __init__(self):
        super().__init__()
        # list all wire_in addresses
        self.addr_wire_in = {}
        self.addr_wire_in['CTRL'] = 0x00
        self.addr_wire_in['POWER_CTRL'] = 0x01
        #self.addr_wire_in['RFU'] = 0x02
        #self.addr_wire_in['RFU'] = 0x03
        self.addr_wire_in['ADC_CTRL'] = 0x04
        # self.addr_wire_in['ADC_STATUS'] = 0x05
        #self.addr_wire_in['RFU'] = 0x06
        #self.addr_wire_in['RFU'] = 0x07
        #self.addr_wire_in['RFU'] = 0x08
        #self.addr_wire_in['RFU'] = 0x09
        #self.addr_wire_in['RFU'] = 0x0A
        #self.addr_wire_in['RFU'] = 0x0B
        #self.addr_wire_in['RFU'] = 0x0C
        #self.addr_wire_in['RFU'] = 0x0D
        #self.addr_wire_in['RFU'] = 0x0E
        #self.addr_wire_in['RFU'] = 0x0F
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
        self.addr_wire_in['ERRORS'] = 0x1A
        self.addr_wire_in['STATUS'] = 0x1B
        #self.addr_wire_in['RFU'] = 0x1C
        # self.addr_wire_in['HARDWARE_ID'] = 0x1D
        # self.addr_wire_in['FIRMWARE_NAME'] = 0x1E
        # self.addr_wire_in['FIRMWARE_ID'] = 0x1F

        # list all wire_out addresses
        self.addr_wire_out = {}
        self.addr_wire_out['CTRL'] = 0x20
        self.addr_wire_out['POWER_CTRL'] = 0x21
        #self.addr_wire_out['RFU'] = 0x22
        #self.addr_wire_out['RFU'] = 0x23
        self.addr_wire_out['ADC_CTRL'] = 0x24
        self.addr_wire_out['ADC_STATUS'] = 0x25
        #self.addr_wire_out['RFU'] = 0x26
        #self.addr_wire_out['RFU'] = 0x27
        #self.addr_wire_out['RFU'] = 0x28
        #self.addr_wire_out['RFU'] = 0x29
        #self.addr_wire_out['RFU'] = 0x2A
        #self.addr_wire_out['RFU'] = 0x2B
        #self.addr_wire_out['RFU'] = 0x2C
        #self.addr_wire_out['RFU'] = 0x2D
        #self.addr_wire_out['RFU'] = 0x2E
        #self.addr_wire_out['RFU'] = 0x2F
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
        #self.addr_wire_out['RFU'] = 0x3C
        self.addr_wire_out['HARDWARE_ID'] = 0x3D
        self.addr_wire_out['FIRMWARE_NAME'] = 0x3E
        self.addr_wire_out['FIRMWARE_ID'] = 0x3F

    def get_ctrl(self):
        addr = self.addr_wire_out['CTRL']
        res = self.get_wire_out(addr_p=addr)
        return res

    def get_power_ctrl(self):
        addr = self.addr_wire_out['POWER_CTRL']
        res = self.get_wire_out(addr_p=addr)
        return res

    def get_adc_ctrl(self):
        addr = self.addr_wire_out['ADC_CTRL']
        res = self.get_wire_out(addr_p=addr)
        return res

    def get_adc_status(self):
        addr = self.addr_wire_out['ADC_STATUS']
        res = self.get_wire_out(addr_p=addr)
        return res

    def get_adc0(self):
        addr = self.addr_wire_out['ADC0']
        res = self.get_wire_out(addr_p=addr)
        return res

    def get_adc1(self):
        addr = self.addr_wire_out['ADC1']
        res = self.get_wire_out(addr_p=addr)
        return res

    def get_adc2(self):
        addr = self.addr_wire_out['ADC2']
        res = self.get_wire_out(addr_p=addr)
        return res

    def get_adc3(self):
        addr = self.addr_wire_out['ADC3']
        res = self.get_wire_out(addr_p=addr)
        return res

    def get_adc4(self):
        addr = self.addr_wire_out['ADC4']
        res = self.get_wire_out(addr_p=addr)
        return res

    def get_adc5(self):
        addr = self.addr_wire_out['ADC5']
        res = self.get_wire_out(addr_p=addr)
        return res

    def get_adc6(self):
        addr = self.addr_wire_out['ADC6']
        res = self.get_wire_out(addr_p=addr)
        return res

    def get_adc7(self):
        addr = self.addr_wire_out['ADC7']
        res = self.get_wire_out(addr_p=addr)
        return res

    def get_debug_ctrl(self):
        addr = self.addr_wire_out['DEBUG_CTRL']
        res = self.get_wire_out(addr_p=addr)
        return res

    def get_error_sel(self):
        addr = self.addr_wire_out['ERROR_SEL']
        res = self.get_wire_out(addr_p=addr)
        return res

    def get_errors(self):
        addr = self.addr_wire_out['ERRORS']
        res = self.get_wire_out(addr_p=addr)
        return res

    def get_status(self):
        addr = self.addr_wire_out['STATUS']
        res = self.get_wire_out(addr_p=addr)
        return res

    def get_hardware_id(self):
        addr = self.addr_wire_out['HARDWARE_ID']
        res = self.get_wire_out(addr_p=addr)
        return res

    def get_firmware_name(self):
        addr = self.addr_wire_out['FIRMWARE_NAME']
        res = self.get_wire_out(addr_p=addr)
        return res

    def get_firmware_id(self):
        addr = self.addr_wire_out['FIRMWARE_ID']
        res = self.get_wire_out(addr_p=addr)
        return res
