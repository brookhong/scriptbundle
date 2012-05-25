<?php

//$client = new SoapClient('http://soap.amazon.com/schemas3/AmazonWebServices.wsdl');
//var_dump($client->__getFunctions());


class Foo {
    //function __construct() {
        //echo 'hi!';
    //}

    static public function test($name) {
        print '[['. $name ."]]\n";
    }
}

//spl_autoload_register(__NAMESPACE__ .'\Foo::test'); // As of PHP 5.3.0

//new Bar;
//echo rawurlencode("/Users/zhong/DSC01 369.jpg ")."\n";
$a = new Foo();
$a->test("afdfd");
if(property_exists($a, 'name'))
    print "name none\n";
$a->name = "brook";
if(property_exists($a, 'name'))
    print "name ".$a->name;

$a = array();
$a['d'] = 33;
print $a['d'];
echo htmlspecialchars("<");
?>
