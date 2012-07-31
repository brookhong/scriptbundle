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
$b = array();
$b[0] = 33;
echo "a:".reset($a);
$a['d'] = 33;
print $a['d'];
print_r(array_keys($a));
print $b[0];
print_r(array_keys($b));
echo htmlspecialchars("<");

list ($ymd, $num_m) = explode ('D', "1120328D66");
echo $ymd." ".$num_m;

$subject = "abc=def,abdd=1,ddfd=33";
$a = explode(',', $subject);
print_r($a);
foreach ($a as $k) {
	echo $k;
}
$a = implode(':', $a);
print_r($a);
preg_match('/([^=]*)=([^=]*)/', $subject, $matches);
print_r($matches);

$xmlObj = simplexml_load_string("<ReportSuite.SaveClassifications> <c_options/> <c_view>{{Campaign|classification}}</c_view> <camp_view>0</camp_view> <name>Delivery Tool</name> <rsid_list> <item>{{RSID}}</item> </rsid_list> </ReportSuite.SaveClassifications>");
echo $xmlObj->name;

$b['bac']++;
$b['bac']++;
if(array_key_exists('bac',$b)) {
  print_r($b);
}
?>
