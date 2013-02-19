
<?php 
$xml_data = "<soapenv:Envelope xmlns:omn=\"http://www.omniture.com/\" xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"> <soapenv:Header><wsse:Security soapenv:mustUnderstand=\"1\" xmlns:wsse=\"http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd\" xmlns:wsu=\"http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd\"><wsse:UsernameToken wsu:Id=\"UsernameToken-4\"><wsse:Username>adobe_zhong</wsse:Username><wsse:Password Type=\"http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-username-token-profile-1.0#PasswordDigest\">9Jvxkc67TNzyowJQINh0Dx+U9S0=</wsse:Password><wsse:Nonce EncodingType=\"http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-soap-message-security-1.0#Base64Binary\">gN9qgaNWACfU+1p1FcWvZw==</wsse:Nonce><wsu:Created>2012-10-22T12:22:21.315Z</wsu:Created></wsse:UsernameToken></wsse:Security></soapenv:Header> <soapenv:Body> <omn:Product.Get soapenv:encodingStyle=\"http://schemas.xmlsoap.org/soap/encoding/\"> <productCode xsi:type=\"xsd:string\">b7f66202e12c06e8</productCode> </omn:Product.Get> </soapenv:Body> </soapenv:Envelope>";


$URL = "https://zhong-acc.www5.dev.omniture.com:443/p/sn/3.1/csoap.html";

$ch = curl_init($URL);
//curl_setopt($ch, CURLOPT_MUTE, 1);
curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 0);
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type: text/xml'));
curl_setopt($ch, CURLOPT_POSTFIELDS, "$xml_data");
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
$output = curl_exec($ch);
print $output;
curl_close($ch);

?>
