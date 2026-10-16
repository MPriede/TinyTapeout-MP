# Checks the hex decoder for all 256 input values.
# ui[3:0] = hex digit, ui[7:4] = parity inputs.
# uo[6:0] = segments A-G, uo[7] = dot (odd parity of ui[7:4]).
import cocotb
from cocotb.triggers import Timer

SEGMENTS = ["abcdef", "bc", "abdeg", "abcdg", "bcfg", "acdfg", "acdefg", "abc",
            "abcdefg", "abcdfg", "abcefg", "cdefg", "adef", "bcdeg", "adefg", "aefg"]

def expected(value):
    out = 0
    for bit, seg in enumerate("abcdefg"):
        if seg in SEGMENTS[value & 0xF]:
            out |= 1 << bit
    if bin(value >> 4).count("1") % 2:
        out |= 0x80
    return out

@cocotb.test()
async def test_hex_decoder(dut):
    dut.ena.value = 1
    dut.clk.value = 0
    dut.rst_n.value = 1
    dut.uio_in.value = 0
    for value in range(256):
        dut.ui_in.value = value
        await Timer(10, units="ns")
        got = int(dut.uo_out.value)
        assert got == expected(value), \
            f"ui_in={value:#04x}: uo_out={got:#04x}, expected {expected(value):#04x}"
    dut._log.info("All 256 input values passed")
