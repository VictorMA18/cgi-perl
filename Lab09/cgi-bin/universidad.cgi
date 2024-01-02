#!/usr/bin/perl
use strict;
use warnings;

open(IN, "ProgramasdeUniversidades.csv") or die("Error al abrir el archivo");
my @line = <IN>;
close(IN);
my $count = 0;
while($line[0] =~ /^([^\|]+)\|(.+)/){
   print "$count:"."$1\n";
   $count++;
   $line[0] = $2;
}
print "$count:$line[0]\n";


