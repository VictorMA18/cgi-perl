#!/usr/bin/perl
use strict;
use warnings;

open(IN, "ProgramasdeUniversidades.csv") or die("Error al abrir el archivo");
my @line = <IN>;
close(IN);
my $count = 0;
my $etiquetas = cabecera(@line);
my $datos = cabecerasclasificadas();
if($line[1] =~ /$datos/){
   print $1."\n";
   print $22."\n";
   print $3."\n";
}else{
   print "error";
}
sub cabecera{
   while($_[0] =~ /^([^\|]+)\|(.+)/){
      print "$count:"."$1\n";
      $count++;
      $_[0] = $2;
   }
   print "$count:$_[0]\n";
   return $count;
}
sub cabecerasclasificadas{
   my $agrupaciones = "^";
   for(my $i = 0; $i < 22; $i++){
      $agrupaciones .= '([^\|]+)\|';
   }
   $agrupaciones .= '([^\|]+)';
   return $agrupaciones;
}


