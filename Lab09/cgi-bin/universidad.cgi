#!/usr/bin/perl
use strict;
use warnings;
use CGI;

my $cgi = new CGI;
my $universidad = $cgi->param('universidad');
my $perlicenciamiento = $cgi->param('licenciamiento');
my $departalocal = $cgi->param('local');
my $denomprograma = $cgi->param('programa');

open(IN, "ProgramasdeUniversidades.csv") or die("Error al abrir el archivo");
my @line = <IN>;
close(IN);


my $etiquetas = cabecera(@line);
my $datos = cabecerasclasificadas($etiquetas);
my $longitud = @line;
my @universi;
#print("LOngitud: ".$longitud."\n");
my $count = 0;
sub univer(){
   for(my $i= 0; $i < $longitud; $i++){
      if($line[$i] =~ /$datos/){
         if($2 eq $universidad){
            $universi[$count] = $2."\n";
            $count++;
         } 
      }
   }
   return @universi;
}

#if($line[1] =~ /$datos/){
   #print $1."\n";
   #print $22."\n";
   #print $3."\n";
#}else{
   #print "error";
#}
sub cabecera{
   while($_[0] =~ /^([^\|]+)\|(.+)/){
      #print "$count:"."$1\n";
      $count++;
      $_[0] = $2;
   }
   #print "$count:$_[0]\n";
   return $count;
}
sub cabecerasclasificadas{
   my $length = $_[0];
   my $agrupaciones = "^";
   for(my $i = 0; $i < $_[0]; $i++){
      $agrupaciones .= '([^\|]+)\|';
   }
   $agrupaciones .= '([^\|]+)';
   return $agrupaciones;
}
my @hola = univer();
print "Content-type: text/html\n\n";
print <<HTML;
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Buscador</title>
    <link rel="stylesheet" type="text/css" href="Style.css">
</head>
<body>
    <div class="nombre">
        <h4>Lab09 - Ejemplo Unificado y Archivo de Universidades Licenciadas - Mamani Anahua Victor</h4>
    </div>
    <main>
HTML
print("<p> EL resultado es: ".@hola." </p>\n");
print<<HTML;
   </main>
</body>
</html>
HTML
