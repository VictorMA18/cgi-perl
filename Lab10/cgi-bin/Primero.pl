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
my $sth = $dbh->prepare("INSERT INTO Actor (ActorId, Name) Values(?,?)");
$sth->execute($idactor, "Pancho");
$sth = $dbh->prepare("DESC Actor");
$sth->execute();
while(my @rowcabe = $sth->fetchrow_array){
   print "$rowcabe[0] ";
}
$sth = $dbh -> prepare("SELECT * FROM Actor WHERE ActorId=?");
$sth->execute($idactor);
while(my @row = $sth->fetchrow_array){
  print "\n";
  foreach my $data(@row){
    print "$data ";
  }
  print "\n";
}
$sth->finish;
$dbh->disconnect;
