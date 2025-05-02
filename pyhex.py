#!/usr/bin/env python3.8
"""
PyHex is a simple python Hex editor
"""
#https://github.com/Builditluc/PyHex















 
class HexFile:
   

    def decode_hex(self):
        """
        This function decodes the hex content of the file to ascii

        :return: The decoded text, already formatted
        """
        decoded_array = []

        for line in self.hex_array:
            line_array = []
            for hex_object in line:
                # Convert the hex byte into a normal byte
                byte_object = bytes.fromhex(hex_object)

                # Convert the byte into ascii
                try:
                    ascii_object = byte_object.decode("ascii")
                except UnicodeDecodeError:
                    ascii_object = "."

                # Replace the char with a dot if it's a special character
                if ascii_object in self.special_characters:
                    ascii_object = "."

                # Add the ascii char to the line array
                line_array.append(ascii_object)

            # add the line to the decoded array
            decoded_array.append(line_array)

        return decoded_array

   

    def _format_content(self):
        # Formats the Hex Array
        i = 0
        line = []
        new_array = []
        for byte in self.hex_array:
            if i == self.columns:
                new_array.append(line)
                line = []
                i = 0

            line.append(byte)
            i += 1

        if line:
            new_array.append(line)

        self.hex_array = new_array

  


if __name__ == '__main__':
    file_to_hex("debug.txt")
                

