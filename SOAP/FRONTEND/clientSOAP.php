<?php

$wsdl = "http://localhost:8000/?wsdl";

try {
    $client = new SoapClient($wsdl, [
    'trace' => 1,
    'exceptions' => true
    ]);

    echo "Connexion réussie au service SOAP\n";
} catch (SoapFault $e) {
    echo "Erreur SOAP : " . $e->getMessage() . "\n";
}