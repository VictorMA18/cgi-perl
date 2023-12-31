#!/usr/bin/perl
use strict;
use CGI;


my $cgi = new CGI;
my $numero1 = $cgi->param('numero1');
my $numero2 = $cgi->param('numero2');
my $operacion = $cgi->param('operacion');
my $resultado;

if ($numero1 !~ /^[0-9]+$/ or $numero2 !~ /^[0-9]+$/) {
    print $cgi->header("text/html");
    print "Solo se aceptan números \n\n";
} else {
    print $cgi->header("text/html");

    if ($operacion eq 'sumar') {
        $resultado = $numero1 + $numero2;
        print 'El resultado de la suma es: ' . $resultado;
    }elsif ($operacion eq 'restar') {
        $resultado = $numero1 - $numero2;
        print 'El resultado de la resta es: ' . $resultado;
    }
    
}
