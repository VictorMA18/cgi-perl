#!/usr/bin/perl
use strict;
use warnings;

open(IN, "ProgramasdeUniversidades.csv") or die("Error al abrir el archivo");
my $line = <IN>;
my $count = 0;
while($line =~ /^([^\|]+)\|(.+)/){
   print "$count:"."$1\n";
   $count++;
   $line = $2;
}
print "$count:$line\n";
close(IN);


