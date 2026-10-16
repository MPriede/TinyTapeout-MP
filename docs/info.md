## How it works

The design is a hexadecimal decoder for a 7-segment display, made from logic gates in Wokwi.

- Inputs `ui[0]` to `ui[3]` make a 4-bit number. `ui[3]` is the most significant bit.
- NOT gates make the inverted version of each input bit.
- Each display segment (`uo[0]` to `uo[6]`, segments A to G) has its own group of AND gates and OR gates. The AND gates find the numbers that turn the segment on. The OR gates combine them.
- The display shows the number as a hexadecimal digit from 0 to F.
- Inputs `ui[4]` to `ui[7]` go into 3 XOR gates. Output `uo[7]` (the dot) is 1 when an odd number of these inputs are 1.

## How to test

1. Connect a common-cathode 7-segment display to `uo[0]` to `uo[7]` (A, B, C, D, E, F, G, DP).
2. Set `ui[0]` to `ui[3]` to a binary number. Make sure that the display shows the correct hexadecimal digit (for example, 0000 = 0, 1010 = A, 1111 = F).
3. Set `ui[4]` to `ui[7]`. Make sure that the dot comes on only when an odd number of these inputs are 1.

## External hardware

A common-cathode 7-segment display (the display on the Tiny Tapeout demo board is sufficient) and 8 switches.
