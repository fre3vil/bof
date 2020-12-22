## This is vulnserver exploit workthrought


### Step one. fuzz the vulnserver


### Tools

generic_send_tcp

```

# Strings
s_string("string")	 	// simply prints the string string as part of your SPIKE
s_string_repeat(string,200);	// repeats the string string 200 times
s_string_variable("string");    // inserts a fuzzed string into your SPIKE.

# Binary Data
s_binary(x41); 			// inserts binary representation of hex 0x41 = ASCII "A"
s_binary_repeat(x41, 200); 	// inserts binary representation of 0x41 200 times

# Defining Blocks
s_block_start(block1); // defines the start of block block1
s_block_end(block1); // defines the end of block block1


# Block Sizes
s_blocksize_string(block1, 2);	// adds a string 2 characters long to the SPIKE that represents the size of block block1
s_binary_block_size_byte(block1);	// adds a 1 byte value to the SPIKE that represents the size of block block1

# Other Useful Commands

s_read_packet(); // Reads and prints to screen data received from the server
s_readline(); // Reads a single line of input from the server

# An Example SPIKE Script

s_string("POST /testme.php HTTP/1.1\r\n");
s_string("Host: testserver.example.com\r\n");
s_string("Content-Length: ");
s_blocksize_string("block1", 5);
s_string("Connection: close\r\n\r\n");
s_block_start("block1");
s_string("inputvar=");
s_string_variable("inputval");
s_block_end("block1");



```

execute the follow perl code.
exp_control_eip.pl
exp_fill_ebp.pl
exp_badchars.pl
exp_full_pattern.pl







