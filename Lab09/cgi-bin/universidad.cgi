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
sub universidadResol{
   my $count = 0;
   my $name = $_[0];
   for(my $i= 0; $i <= $longitud; $i++){
      if($line[$i + 1] =~ /$datos/){
         if($2 eq $name){
            $universi[$count] = $line[$i + 1];
            $count++;
         } 
      }
   }
   if($count > 0){
      return @universi;
   }else{
      return @line;
   }
}
my @licencia;
sub licenciamientoResol{
   my $count = 0;
   my $name = $_[0];
   for(my $i= 0; $i <= $longitud; $i++){
      if($line[$i + 1] =~ /$datos/){
         if($5 == $name){
            $licencia[$count] = $line[$i + 1];
            $count++;
         } 
      }
   }
   if($count > 0){
      return @licencia;
   }else{
      return @line
   } 
}
my @departamento;
sub departamentoResol{
   my $count = 0;
   my $name = $_[0];
   for(my $i= 0; $i <= $longitud; $i++){
      if($line[$i + 1] =~ /$datos/){
         if($11 eq $name){
            $departamento[$count] = $line[$i + 1];
            $count++;
         } 
      }
   }
   if($count > 0){
      return @departamento;
   }else{   
      return @line;
   }
}
my @programa;
sub programaResol{
   my $count = 0;
   my $name = $_[0];
   for(my $i= 0; $i <= $longitud; $i++){
      if($line[$i + 1] =~ /$datos/){
         if($17 eq $name){
            $programa[$count] = $line[$i + 1];
            $count++;
         } 
      }
   }
   if($count > 0){
      return @programa;
   }else{
      return @line;
   }
}
sub diferencia_de_arrays{
    my @arrays = @_;
    my %hash;
    my @diferencia;
    # Convertir cada array en un hash
    foreach my $array (@arrays) {
        foreach my $element (@$array) {
            $hash{$element}++;
        }
    }
    # Encontrar los elementos que aparecen solo en uno de los arrays
    foreach my $element (keys %hash) {
        if ($hash{$element} == 4) {
            push @diferencia, $element;
        }
    }
    return @diferencia;
}
#if($line[1] =~ /$datos/){
   #print $1."\n";
   #print $22."\n";
   #print $3."\n";
#}else{
   #print "error";
#}
sub cabecera{
   my $count = 0;
   while($_[0] =~ /^([^\|]+)\|(.+)/){
      print "$count:"."$1\n";
      $count++;
      $_[0] = $2;
   }
   print "$count:$_[0]\n";
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
my @hola = universidadResol($universidad);
my @hola2 = licenciamientoResol($perlicenciamiento);
my @hola3 = departamentoResol($departalocal);
my @hola4 = programaResol($denomprograma);

my @union = map { $_ } @hola, @hola2, @hola3, @hola4;
my @interseccion = diferencia_de_arrays(\@hola, \@hola2, \@hola3, \@hola4);
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
print("<p> EL resultado de universidades es: ".@hola." </p>\n");
print("<p> EL resultado de licencias es: ".scalar(@hola2)." </p>\n");
print("<p> EL resultado de licencias es: ".scalar(@hola3)." </p>\n");
print("<p> EL resultado de licencias es: ".scalar(@hola4)." </p>\n");
print("<p> EL resultado de licencias es: ".scalar(@interseccion)." </p>\n");
print("<p> EL resultado de licencias es: $interseccion[1] </p>\n");
print<<HTML;
   </main>
</body>
</html>
HTML
