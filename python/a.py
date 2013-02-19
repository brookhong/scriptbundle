import xml.etree.ElementTree as ET
import sys,base64
country_data_as_string="""<?xml version="1.0"?>
<data>
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank>4</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
    <country name="Panama">
        <rank>68</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W"/>
        <neighbor name="Colombia" direction="E"/>
    </country>
</data>
"""
#country_data_as_string="""<?xml version="1.0" encoding="iso-8859-1"?><response xmlns="urn:debugger_protocol_v1" xmlns:xdebug="http://xdebug.org/dbgp/xdebug" command="property_get" transaction_id="5" status="break" reason="ok"><error code="300"><message></message></error></response> """
country_data_as_string="""
		<property name="name" fullname="$a-&gt;name" facet="public" address="4332667704" type="string" size="5" encoding="base64">
			<![CDATA[YnJvb2s=]]>
		</property>
		"""

root = ET.fromstring(country_data_as_string)
a = root.find("{urn:debugger_protocol_v1}")
print len(list(root))
print base64.decodestring(root.text)
