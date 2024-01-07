#!/usr/bin/perl
use strict;
use warnings;
use CGI;
use DBI;
 
my $cgi = CGI->new;
$cgi->charset('UTF-8');
my $user = "alumno";
my $password = "pweb1";
my $dsn = "DBI:MariaDB:database=pweb1;host=192.168.0.10";
my $dbh = DBI->connect($dsn, $user, $password) or die("No se conecto");
my $idactor = "5";
my $sth = $dbh -> prepare("SELECT * FROM Actor WHERE ActorId<100");
$sth->execute();
while(my @rowcabe = $sth->fetchrow_array){
   print "@rowcabe\n";
}
$sth -> finish;
$dbh->disconnect;
