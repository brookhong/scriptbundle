# coding=utf-8

  #$_SERVER['HTTP_HOST'] = (string) 'zhong.www5.dev.omniture.com';
  #$_SERVER['HTTPS']    = (string) 'on';
  #$_SERVER['REQUEST_URI'] = (string) '/login/';
  #$_SERVER['HTTP_CONNECTION'] = (string) 'keep-alive';

  #$_SERVER['HTTP_CACHE_CONTROL'] = (string) 'max-age=0';
  #$_SERVER['HTTP_USER_AGENT'] = (string) 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_1) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.79 Safari/537.4';
  #$_SERVER['HTTP_ACCEPT'] = (string) 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8';
  #$_SERVER['HTTP_ACCEPT_ENCODING'] = (string) 'gzip,deflate,sdch';
  #$_SERVER['HTTP_ACCEPT_LANGUAGE'] = (string) 'en-US,en;q=0.8';
  #$_SERVER['HTTP_ACCEPT_CHARSET'] = (string) 'GBK,utf-8;q=0.7,*;q=0.3';
  #$_SERVER['HTTP_COOKIE'] = (string) 'ADMS_ID=39354612669174432882239944680924783447; FLASH_ENABLED=yes; s_sv_p1=1@16@d/9906/9866&e/88; sc_user_settings=sparkl%3D0%2Aflsh_en%3D0%2Aapic%3D1%2Awkend%3D1%2Aforce_width%3D1%2Aqhlp%3D1%2Adet%3D1%2Aiav%3D1%2Afcst%3D1%2Adflt%3D0%2Amnu%3D0%2Amtrc%3D1%2Afrmt%3D1%2Aexcel_intro%3D0%2Ac_hierarchy%3D0%2Aallother%3D0%2Aecnone%3D0; cookies_enabled=1; mc_company=Brook+Corp; sc_def_dir=sc15; sc_ident=Brook+Corp%7C%7Czhong%7E%7EASCQE%7C%7Czhong%7E%7EAdobe+China%7C%7Cxingliwu%7E%7EASC+Genesis+SJO%7C%7Czhong%7E%7EAdobe+China%7C%7Czhong; sc_sl=9dbf6e66a26b6fa6741c49d76be8ce27%2C9dbf6e66a26b6fa6741c49d76be8ce27%2C9dbf6e66a26b6fa6741c49d76be8ce27%2C9dbf6e66a26b6fa6741c49d76be8ce27%2C9dbf6e66a26b6fa6741c49d76be8ce27%2C9dbf6e66a26b6fa6741c49d76be8ce27%2C9dbf6e66a26b6fa6741c49d76be8ce27%2C9dbf6e66a26b6fa6741c49d76be8ce27%2C9dbf6e66a26b6fa6741c49d76be8ce27%2C9dbf6e66a26b6fa6741c49d76be8ce27%2C9dbf6e66a26b6fa6741c49d76be8ce27%2C9dbf6e66a26b6fa6741c49d76be8ce27%2C9dbf6e66a26b6fa6741c49d76be8ce27%2C9dbf6e66a26b6fa6741c49d76be8';
import httplib
#import pdb
#pdb.set_trace()
headers = {
"Connection"      : "keep-alive",
"Cache-Control"   : "max-age=0",
"User-Agent"      : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_1) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.79 Safari/537.4",
"Accept"          : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
"Accept-Encoding" : "gzip,deflate,sdch",
"Accept-Language" : "en-US,en;q=0.8",
"Accept-Charset"  : "GBK,utf-8;q=0.7,*;q=0.3",
"Cookie"          : "ADMS_ID=39354612669174432882239944680924783447; FLASH_ENABLED=yes; s_sv_p1=1@16@d/9906/9866&e/88; sc_user_settings=sparkl%3D0%2Aflsh_en%3D0%2Aapic%3D1%2Awkend%3D1%2Aforce_width%3D1%2Aqhlp%3D1%2Adet%3D1%2Aiav%3D1%2Afcst%3D1%2Adflt%3D0%2Amnu%3D0%2Amtrc%3D1%2Afrmt%3D1%2Aexcel_intro%3D0%2Ac_hierarchy%3D0%2Aallother%3D0%2Aecnone%3D0; cookies_enabled=1; mc_company=Brook+Corp; sc_def_dir=sc15; sc_ident=Brook+Corp%7C%7Czhong%7E%7EASCQE%7C%7Czhong%7E%7EAdobe+China%7C%7Cxingliwu%7E%7EASC+Genesis+SJO%7C%7Czhong%7E%7EAdobe+China%7C%7Czhong; sc_sl=9dbf6e66a26b6fa6741c49d76be8ce27%2C9dbf6e66a26b6fa6741c49d76be8ce27%2C9dbf6e66a26b6fa6741c49d76be8ce27%2C9dbf6e66a26b6fa6741c49d76be8ce27%2C9dbf6e66a26b6fa6741c49d76be8ce27%2C9dbf6e66a26b6fa6741c49d76be8ce27%2C9dbf6e66a26b6fa6741c49d76be8ce27%2C9dbf6e66a26b6fa6741c49d76be8ce27%2C9dbf6e66a26b6fa6741c49d76be8ce27%2C9dbf6e66a26b6fa6741c49d76be8ce27%2C9dbf6e66a26b6fa6741c49d76be8ce27%2C9dbf6e66a26b6fa6741c49d76be8ce27%2C9dbf6e66a26b6fa6741c49d76be8ce27%2C9dbf6e66a26b6fa6741c49d76be8"
}

#conn = httplib.HTTPConnection("zhong.www5.dev.omniture.com")
conn = httplib.HTTPSConnection("zhong.www5.dev.omniture.com")
conn.request("GET", "/login/", None, headers)
r1 = conn.getresponse()
print r1.status, r1.reason
data1 = r1.read()
print data1
conn.close()
