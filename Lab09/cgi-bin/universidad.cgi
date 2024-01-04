#!/usr/bin/perl
use strict;
use Encode;
use warnings;
use CGI;

my $cgi = new CGI;
$cgi->charset("UTF-8");
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
my @licencia;
#print("LOngitud: ".$longitud."\n");
sub universidadResol{
   my $count = 0;
   my $name = $_[0];
   for(my $i= 0; $i <= $longitud; $i++){
      if($line[$i + 1] =~ /$datos/){
         if($2 =~ /$name/){
            $licencia[$count] = $line[$i + 1];
            $count++;
         } 
      }
   }
   return @licencia;
}
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
   return @licencia;
}
sub departamentoResol{
   my $count = 0;
   my $name = $_[0];
   for(my $i= 0; $i <= $longitud; $i++){
      if($line[$i + 1] =~ /$datos/){
         if($11 eq $name){
            $licencia[$count] = $line[$i + 1];
            $count++;
         } 
      }
   }
   return @licencia;
}
sub programaResol{
   my $count = 0;
   my $name = $_[0];
   for(my $i= 0; $i <= $longitud; $i++){
      if($line[$i + 1] =~ /$datos/){
         if($17 =~ /$name/){
            $licencia[$count] = $line[$i + 1];
            $count++;
         } 
      }
   }
   return @licencia;
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
universidadResol($universidad);
licenciamientoResol($perlicenciamiento);
departamentoResol($departalocal);
programaResol($denomprograma);

sub matcher {
  my $results = "";
  foreach my $line (@_) {
    chomp($line);
    my @params = split(/\|/, $line);
    $results .= makeRow(@params); 
  }
  return $results;
}
sub makeRow {
  my $row = "<tr>\n";
  foreach my $data (@_) { $row .= "<td>$data</td>\n"; }
  $row .= "</tr>\n";
  return $row;
}
my $rows = matcher(@licencia);
$rows = encode('utf-8', $rows);
print "Content-type: text/html\n\n";
print <<HTML;
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Buscador</title>
    <link rel="stylesheet" type="text/css" href="../style.css">
</head>
<body>
   <div class="opciones">
      <button class="buscar" onclick="window.history.back()">Volver a la sección anterior</button> 
   </div>
   <table class="resultados">
      <tr>
        <th>CODIGO ENTIDAD</th>
        <th>NOMBRE</th>
        <th>TIPO GESTION</th>
        <th>ESTADO LICENCIAMIENTO</th>
        <th>PERIODO LICENCIAMIENTO</th>
        <th>CODIGO FILIAL</th>
        <th>NOMBRE FILIAL</th>
        <th>DEPARTAMENTO FILIAL</th>
        <th>PROVINCIA FILIAL</th>
        <th>CODIGO LOCAL</th>
        <th>DEPARTAMENTO LOCAL</th>
        <th>PROVINCIA LOCAL</th>
        <th>DISTRITO LOCAL</th>
        <th>LATITUD UBICACION</th>
        <th>LONGITUD UBICACION</th>
        <th>TIPO AUTORIZACION LOCAL</th>
        <th>DENOMINACION PROGRAMA</th>
        <th>TIPO NIVEL ACADEMICO</th>
        <th>NIVEL ACADEMICO</th>
        <th>CODIGO CLASE PROGRAMA N2</th>
        <th>NOMBRE CLASE PROGRAMA N2</th>
        <th>TIPO AUTORIZACION PROGRAMA</th>
        <th>TIPO AUTORIZACION PROGRAMA LOCAL</th>
      </tr>
      <tr>
HTML
print($rows);
print<<HTML;
      </tr>
    </table>

  </body>
</html>
HTML
