""""""""""""""""""""""common settings under both windows and linux"""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
set nobackup
set softtabstop=4
set expandtab
set shiftwidth=4 
set hlsearch

let g:shiftTab = 1
function! ShiftTab()
    if g:shiftTab == 1
        set softtabstop&vim
        set noexpandtab
        set shiftwidth&vim 
        let g:shiftTab = 0
    else
        set softtabstop=4
        set expandtab
        set shiftwidth=4 
        let g:shiftTab = 1
    endif
endfunction
map <S-TAB> :call ShiftTab()<cr>

map ,qa :qall!<cr>
map ,d :%s/^\(.*\)\n\1$/\1/g<CR>
map ,j :%s/\n//g<CR>
map ,c :g/^\s*$/d<CR>

function! RangeFill(start,stop)
    let l:num = a:start
    while l:num <= a:stop
        call append(line('$'), l:num)
        let l:num = l:num+1
    endwhile
endfunction

let s:cscope_index = findfile("cscope.out", ".;")
if s:cscope_index != ""
    :exe ":cs add ".s:cscope_index
endif

map ,tc :call CreateCscopeDB()<CR>
map ,fs :cs f s <cword><CR>
map ,fg :cs f g <cword><CR>
map ,fd :cs f d <cword><CR>
map ,fc :cs f c <cword><CR>
map ,ft :cs f t <cword><CR>
map ,fe :cs f e <cword><CR>
map ,ff :cs f f <cword><CR>
map ,fi :cs f i <cword><CR>

map ,l :<UP><CR>

" …Ë÷√––º‰æ‡
set lsp=5
map <M-d> <C-d>
map <M-u> <C-u>

if has("unix")
    map ,e :execute ":!"."./".expand("%")<CR>
else
    map ,e :execute ":!".expand("%")<CR>
endif
let g:netrw_preview   = 1
let g:netrw_liststyle = 3
let g:netrw_winsize   = 10
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""windows settings"""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" color murphy
vmap ,g "zy<Esc>:exec ':silent ! start http://www.google.com/search?q='.@z<CR>
vmap ,b "zy<Esc>:exec ':silent ! start http://www.baidu.com/s?wd='.@z<CR>

function! BrowseWord()
    let l:word = expand("<cword>")
    let l:explanation = split(system("d:/tools/sdcv/sdcv.exe -n --data-dir d:/tools/sdcv " . l:word),"\\n")
    call append(line('.'), ["*#################################################*"])
    call append(line('.'), l:explanation)
    call append(line('.'), "*##############". l:word . " from SDCV##############*")
endfunction
map ,, :call BrowseWord()<CR> 

"map ,a :redir! >>D:/tools/vocabulary.knl\|echo expand('<cword>') \| redir END<CR><CR> 

" let $HOME="C:\\Documents and Settings\\brookhong\\"

" set directory=C:\\temp\\


function! DigitAlign(d,w)
    let l:ret = a:d
    while len(l:ret) < a:w
        let l:ret = "a".l:ret
    endwhile
    let l:ret = substitute(l:ret,"a","0","g")
    return l:ret
endfunction

function! LRCFix(step,flag)
    " put current lrc file forward/backward step*10 ms
    :g/^\[\d\+:\d\+.\d\+\]/s/^\[\(\d\+\):\(\d\+\).\(\d\+\)\(.*\)$/\="[".((submatch(1)*60+submatch(2))*1000+submatch(3)*10).submatch(4)/
    if a:flag > 0
        :g/^\[\d\+\]/s/^\[\(\d\+\)\(.*\)$/\="[".(submatch(1)+a:step*10).submatch(2)/
    else
        :g/^\[\d\+\]/s/^\[\(\d\+\)\(.*\)$/\="[".(submatch(1)-a:step*10).submatch(2)/
    endif
    :g/^\[\d\+\]/s@^\[\(\d\+\)\(.*\)$@\="[".DigitAlign(submatch(1)/60000,2).":".DigitAlign((submatch(1)%60000)/1000,2).".".DigitAlign(((submatch(1)%60000)%1000)/10,2).submatch(2)@
    :g/^\[-\d\+\]/s@^\[-\d\+\(.*\)$@[00:00.00\1@
endfunction

function! NextFilePWD()
    let l:curFile = expand("%:p:t")
    exe "normal ggdG" 
    exe ":r !dir /B"
    exe ":g/" .l:curFile."/normal jyy"
    let l:nextFile = substitute(getreg(0),"\\n","","")
    if findfile(l:nextFile) != ""
        if isdirectory(l:nextFile) != 1 
            exe ":e! " .l:nextFile
            exe "normal gg" 
        endif
    endif
endfunction
map ,f :call NextFilePWD()<CR>

"map ,r :silent !echo "<cword>"\|d:\\tools\\festival\\festival --libdir d:\\tools\\festival\\lib --tts<CR><CR>
"map ,r :silent !d:\\tools\\ReadPlease2003\\ReadPleasePlus2003.exe /state=1 /text="<cword>" <CR><CR>
map ,r :silent !d:\\tools\\tts\\tts.exe -v 3 "<cword>" <CR>
"map <C-i> :exe "!d:\\tools\\tts\\tts.exe -v 3 \"" . substitute(getreg(), "\[\n\|\"\]", " ", "g") . "\""<CR>
"set encoding=utf-8
"set fileencoding=utf-16le

":map ,s :!clear & grep --exclude %:. -rn "<cword>" %:p:h<cr>
map ,s :execute "vimgrep /\\<" . expand("<cword>") . "\\>/j **/*.h **/*.c **/*.cc **/*.cpp" <Bar> cw<CR>
:map <C-L> :source D:/tools/_vimrc<CR>

function! TidyPath(path)
    if match(a:path,":") == -1
        let l:path = expand("%:p:h")."/".a:path
    else
        let l:path = a:path
    endif
    let l:path = substitute(l:path, "\\", "/", "g")
    while match(l:path,"/\\.\\./") >= 0
        let l:path = substitute(l:path, "[^/]\\+/\\.\\./", "", "g")
    endwhile
    while match(l:path,"/\\./") >= 0
        let l:path = substitute(l:path, "/\\./", "/", "g")
    endwhile
    let l:path = substitute(l:path, "/", "\\", "g")
    return l:path
endfunction

function! CreateBrookTags()
    call inputsave()
    let l:ctags_dir = input("dir to ctags: ")
    call inputrestore()
    if(len(l:ctags_dir)>0)
        let l:ctags_dir = TidyPath(l:ctags_dir)
        :exe ":!ctags -f " . l:ctags_dir . "/brook_tags -R " . l:ctags_dir . "/*"
    endif
    let l:ctags_dir = ""
endfunction
map ,ct :call CreateBrookTags()<CR>
map ,tj <C-]>
set tags=brook_tags;
set autochdir

function! CreateCscopeDB()
    call inputsave()
    let l:cscope_dir = input("dir to cscope: ")
    call inputrestore()
    if(len(l:cscope_dir)>0)
        let l:cscope_dir = TidyPath(l:cscope_dir)
        :exe "!\"cd ".l:cscope_dir." & dir /s /b *.c *.h *.cpp *.hpp *.cc *.hh > cscope.files & cscope -b & del cscope.files\""
        :exe ":cs add ".l:cscope_dir."\\cscope.out"
    endif
endfunction
