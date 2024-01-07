#!/usr/bin/perl
use strict;
use warnings;
use CGI;
use DBI;

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
HTML
my $cgi = CGI->new;
$cgi->charset('UTF-8');
my $user = "alumno";
my $password = "pweb1";
my $dsn = "DBI:MariaDB:database=pweb1;host=192.168.0.10";
my $dbh = DBI->connect($dsn, $user, $password) or die("No se conecto");
my $puntos = "7";
my $votos = "5000";
my $sth = $dbh->prepare("DESC Movie");
$sth->execute();
   while(my @rowcabe = $sth->fetchrow_array){
      print "<th>$rowcabe[0]</th>\n";
   }
   print "</tr>\n";
$sth = $dbh -> prepare("SELECT * FROM Movie WHERE Score > ? && Votes > ?");
$sth->execute($puntos, $votos);
   while(my @row = $sth->fetchrow_array){
      print "<tr>\n";
      foreach my $data(@row){
          print "<td>$data</td>\n";
      }
      print "</tr>\n";
   }
print<<HTML;
    </table>

  </body>
</html>
HTML
$sth->finish;
$dbh->disconnect;
