# generic
> ## git
> > > ---
    * Global setup:
    git config --global user.name "Your Name"
    git config --global user.email aaaaaaaaaa@hotmail.com
    * Next steps:
    mkdir scriptbundle
    cd scriptbundle
    git init
    touch README
    git add README
    git commit -m 'first commit'
    git remote add origin git@github.com:brookhong/scriptbundle.git
    git push -u origin master
    * Existing Git Repo?
    cd existing_git_repo
    git remote add origin git@github.com:brookhong/scriptbundle.git
    git push -u origin master
    * Useful config
    git config --global alias.s status
    git config --global alias.d difftool
    git config --global alias.co checkout
    git config --global diff.external /d/works/scriptbundle/gitdiff.sh
    git config core.filemode false
    git config --global alias.sc "show --pretty=\"format:\" --name-only"
    git config --global alias.sma "submodule add"
    git config --global core.gitproxy /usr/local/bin/gitproxy
    * cmds
    git show --pretty="format:" --name-only bd61ad98
    git sma git://github.com/vim-scripts/mru.vim.git bundle/mru
    * /usr/local/bin/gitproxy
    #!/bin/bash
    corkscrew <proxy_host> <proxy_port> $1 $2
    * ~/.ssh/config on client
    Host github.com
        Hostname github.com
        #ProxyCommand corkscrew <proxy_host> <proxy_port> %h %p
        IdentityFile ~/.ssh/id_rsa.git
    * ~/.ssh on server
        chmod 700 ~/.ssh
        chmod 600 ~/.ssh/authorized_keys
    * /etc/ssh/sshd_config on server
        RSAAuthentication yes
        PubkeyAuthentication yes
        AuthorizedKeysFile    .ssh/authorized_keys        
    * sudo /usr/sbin/sshd -d
   
> ## vim
> > > ---
    * :0put = range(1,100) 纵插入1，100数字 :for i in range(1,10)|put ='192.168.0.1'.i|endfor
    * !! 在 noraml 模式里直接插入外部程序输出
    * 查询某个模式在整个文件中出现的次数： :%s/pattern//n n 标志表示只显示次数但不进行替换 另见 :help count-items
    * gF 打开光标下的文件名，能识别文件名后的行号（如 abc:80 等）。
    * g; 按照最近修改的顺序进行光标的跳转，g, 与 g; 类似但方向相反
    * :scriptnames 列出全部已加载的插件和 vimrc 文件

> ## english
> > > ---
    * weigh in (with sth) (infml 口) join in a discussion, an argument, etc by saying sth important or convincing; contribute confidently （在讨论、辩论等时）提出重要的或令人信服的意见; 自信地提出看法

> ## perl
> > > ---
    * http://search.cpan.org/CPAN/authors/id/J/JO/JONATHAN/Math-Calculus-Expression-0.2.2.tar.gz
    cpan[2]> i /Math/
    cpan[1]> install JONATHAN/Math-Calculus-Expression-0.2.2.tar.gz

> ## apache
> > ### httpd.conf@windows
> > > ---
    LoadModule php5_module "D:/tools/php-5.3.10-Win32-VC9-x86/php5apache2_2.dll"
    AddType application/x-httpd-php .php
    Alias /scriptbundle D:/works/scriptbundle/php/
    <Directory "D:/works/scriptbundle/php/">
        Options Indexes FollowSymLinks
        AllowOverride None
        Order allow,deny
        Allow from all
    </Directory>

    Alias /phpmyadmin d:/install_pkgs/phpMyAdmin-3.4.10.1-english/
    <Directory "d:/install_pkgs/phpMyAdmin-3.4.10.1-english/">
        DirectoryIndex main.php
        AllowOverride None
        Order allow,deny
        Allow from all
    </Directory>

> > > ---
    * Starting httpd: Warning: DocumentRoot [/home/mysite] does not exist.
    Edit /etc/sysconfig/selinux and change it to disabled then reboot.

> > ### php
> > > ---
    * http://downloads.zend.com/studio_debugger/20100729/ZendDebugger-20100729-darwin9.5-x86_64.tar.gz
    * allphpfiles.sh
      find . -iname "*.php" -or -iname "*.tpl" -or -iname "*.html" -or -iname "*.inc" -or -iname "*.yml" -or -iname "*.tmpl" -or -iname "*.template" -or -iname "*.class" > cscope.files
      cscope -bq
    * in apache.conf --
      PHPINIDir /home/brookhong/php

> > ### php
> > > ---
    Get real height of a div --
    jQuery(jQuery("div.failure.message")[1]).outerHeight()
    jQuery("div.failure.message")[1].offsetHeight

> > ### php.ini@windows
> > > ---
    extension_dir=d:/tools/php-5.3.10-Win32-VC9-x86/ext/
    extension=php_mysql.dll
    extension=php_mysqli.dll

> ## linux
> > > ---
    export HISTCONTROL=ignoredups
    export HISTFILE=~/.bash_history
    history -cr $HISTFILE
    rpm -q --info php-aws
    grep -o "^#[0-9]\+[^(]*\|called at .*$" debug_print_backtrace_of_gigya_settings.log
    find . -type f -newer ./sql/3.0/product_countries.sql -exec ls -l {} \;
    find /home/ -maxdepth 2 -iname ".bashrc" -exec echo "###"{} \; -exec echo "=========" \; -exec cat {} \; -exec echo "==========" \;
    find broken links: find / -type l ! -exec test -r {} \; -print
    -T filename In x or t mode, tar will read the list of names to be extracted from filename.  In c mode, tar will read names to be archived from filename.
    tar czvf a.tgz -T a
    iptables -L
    iptables -D INPUT 6
    iptables -I INPUT -p tcp --dport 8080 -j ACCEPT
    iptables -I INPUT 1  -p tcp --dport 8080 -j ACCEPT
    iptables -I RH-Firewall-1-INPUT -s 172.28.153.0/24  -p tcp -j ACCEPT
    iptables -I RH-Firewall-1-INPUT -d 172.28.153.84  -p tcp -j ACCEPT
    iptables -I RH-Firewall-1-INPUT -s 172.28.153.84  -p tcp --dport 37786 -j ACCEPT
    ll /etc/sysconfig/iptables
    /sbin/service iptables save
    iptables -A Linox-INTRANET-INPUT-HOOK  -p tcp --dport 8080 -j ACCEPT
    extract rpm package: rpm2cpio php-5.1.4-1.esp1.x86_64.rpm | cpio -idmv
    jobeet: svn co http://svn.jobeet.org/doctrine/trunk/

    build tmux
    cd libevent-2.0.19-stable
    ./configure --prefix=/home/httpd/copper/usr/
    make
    make install
    cd tmux-1.6
    LDFLAGS="-L/home/httpd/copper/usr/lib" CPPFLAGS="-I/home/httpd/copper/usr/include" LIBS="-lresolv" ./configure --prefix=/home/httpd/copper/usr/
    make
    make install
    patchelf --set-rpath /home/httpd/copper/usr/lib/ ~/copper/usr/bin/tmux

  
> > > ---
    build openssl
    ./config --prefix=/opt/openssl-0.9.8e/
    make
    make test
    make install
    sudo make install
# windows
> ## cmd
> > > ---
    icacls ftdetect /t /grant:r everyone:f

> ## install win7
> > > ---
    * http://zhidao.baidu.com/question/126555341.html

    一、Windows 7 下硬盘全新安装更高版本Windows7

    1、下载Windows7 7600 ISO镜像，用虚拟光驱拷贝至非C盘(如D:7600) 
    2、开机按F8 -> 修复系统 -> 选择最后一项命令修复  -> 在命令框输入“D:7600sourcessetup.exe“(不带引号) 
    3、进入安装界面、选择Custom Install (自定义安装)
    4、选择安装语言、格式化C盘 
    5、安装完成后将是纯净系统(非双系统)

    二、硬盘有Windows 7镜像，同时有Vista安装盘
    1、下载Windows7 7600 ISO镜像，用虚拟光驱拷贝至非C盘(如D:7600) 
    2、BIOS中选择光驱启动，进入Vista安装界面 
    3、选择左下角修复计算机(自动搜索系统，提示加载驱动或关闭，选择关闭进入修复选项) 
    4、选择最后一项命令修复，在命令框输入“D:7600sourcessetup.exe“(不带引号)，开始安装 
    5、选择安装语言、格式化C盘 (即使C盘原本没有系统此法也可行)

    三、XP系统下硬盘全新安装Windows 7

    1、下载Windows7 7600 ISO镜像，用虚拟光驱拷贝至非C盘(如D:7600) 
    2、把D:7600目录下的bootmgr和boot目录，并在C盘根目录下建个sources文件夹
    3、把D:7600sources下的boot.win复制到C盘刚建的sources文件夹 
    4、用管理员身份运行cmd，然后输入c:bootbootsect.exe/nt60 c: 提示successful(即成功了!) 
    5、关闭cmd窗口重启计算机，自动进入安装界面，选择安装语言
    6、出现“开始安装界面”，(要注意了，不点击“现在安装”)点左下角“修复计算机”(repair mycomputer)，进入"系统恢复选择"，选择最后一项"命令提示符"(commandprompt)，进入DOS窗口 
    7、输入“D:7600sourcessetup.exe“(不带引号)，开始安装 
    8、选择安装语言、格式化C盘，就OK了 

    四、Vista系统下全新安装Windows7(实践证明XP用此种方法也更加方便)

    1、下载Windows7 7600 ISO镜像，用虚拟光驱拷贝至非C盘(如D:7600) 
    2、复制D:7600文件夹中的Boot、EFI、sources文件夹和bootmgr至C盘根目录下 
    3、复制D:7600boot下Bootsect.exe至C盘根目录下 
    4、管理员身份运行cmd，输入c:bootsect.exe/nt60 c:并回车(最好复制，中间有空格) 
    5、重启系统自动进入安装界面，点左下角的修复计算机repair my computer) 
    6、选择最后一项命令提示符，进入DOS窗口，输入D:7600sourcessetup.exe进入安装界面 
    7、选择安装语言、格式化C盘，就OK了

# mac
> > > ---
    * hdiutil mount a.dmg 

# n97mini
  * N97mini硬格方法

> > > ---
    手机连接电脑，删除E盘和内存卡上 
    private  sys  system  resource  patches几个文件夹  这样其他文件不丢失
    然后再硬格C盘比较彻底
    硬格C盘 关机  按住shift(左下角) + 删除键(右上角←键) + 空格，不要松手
    按开机键，直到出现地区选项，格式化完成 此格式化比较彻底.

# reading
《一百个人的十年》，《定西孤儿院纪事》，《夹边沟记事》，《墓碑》
