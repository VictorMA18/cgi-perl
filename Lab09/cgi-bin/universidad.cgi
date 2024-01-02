#!/usr/bin/perl
use strict;
use warnings;

open(IN, "ProgramasdeUniversidades.csv") or die("Error al abrir el archivo");
my $line = <IN>;
print $line;
close(IN);

