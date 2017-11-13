"my configure


set nocompatible
syn on
set nu
set ai
set bs=2
set showmatch
set expandtab
set shiftwidth=4
set cursorline
set autoread
set hls
set fileencodings=utf-8,gbk,gb18030,gk2312
set encoding=utf-8 
"控制台编码
language messages zh_CN.utf-8
"菜单编码
source $VIMRUNTIME/delmenu.vim
source $VIMRUNTIME/menu.vim

colo torte 
"设置字体
set guifont=Consolas:h12

"Toggle Menu and Toolbar"隐藏菜单工具栏
set guioptions-=m
set guioptions-=T

map <silent> <F2> :if &guioptions =~# 'T'<Bar>
\set guioptions-=T<Bar>
\set guioptions-=m<bar>
\else<Bar>
\set guioptions+=T<Bar>
\set guioptions+=m<Bar>
\endif<CR>

"Alpha Window  "装载vimtweak插件,设置工具透明度  vimtweak插件
call libcallnr("vimtweak.dll","SetAlpha",180)
au GUIEnter * call libcallnr("vimtweak.dll", "SetAlpha", 200) "Alpha

map M-2 <Esc>:call libcallnr("vimtweak.dll", "SetAlpha", 200)
map M-3 <Esc>:call libcallnr("vimtweak.dll", "SetAlpha", 230)
map M-5 <Esc>:call libcallnr("vimtweak.dll", "SetAlpha", 255)
map M-8 <Esc>:call libcallnr("vimtweak.dll", "SetAlpha", 180)

"-Maximized Windows: 
map M-1 <Esc>:call libcallnr("vimtweak.dll", "EnableMaximize", 1)
map M-0 <Esc>:call libcallnr("vimtweak.dll", "EnableMaximize", 0)


"TagList 源代码函数,模型定位 ctags,taglist 插件
let Tlist_Show_One_File=1
let Tlist_Exit_OnlyWindow=1

"Pydiction plugin 代码补全,用TAB键 Pydiction插件
filetype plugin on
let g:pydiction_location = 'D:/Program Files/Vim/vimfiles/ftplugin/pydiction/complete-dict'
let g:pydiciton_menu_height = 20


"auto compile 运行,编译
autocmd BufRead *.py set makeprg=python\ -c\ \"import\ py_compile,sys;\ sys.stderr=sys.stdout;\ py_compile.compile(r'%')\"
autocmd BufRead *.py set efm=%C\ %.%#,%A\ \ File\ \"%f\"\\,\ line\ %l%.%#,%Z%[%^\ ]%\\@=%m
autocmd BufRead *.py nmap <F5> :!python %<CR>
autocmd BufRead *.py nmap <F6> :make<CR>
autocmd BufRead *.py copen "如果是py文件，则同时打开编译信息窗口  

"代码检查插件 pyflakes 插件
filetype on
filetype plugin on

"共享剪贴板
set clipboard=unnamed


"indentLines 插件  缩进对齐功能
let g:indentLine_color_gui = '#A4E57E'
let g:indentLine_char = ':'
"let g:indentLine_enabled = 0

" none X terminal
let g:indentLine_color_tty_light = 7 " (default: 4)
let g:indentLine_color_dark = 1 " (default: 2)

"其他设置
set tabstop=4 "让一个tab等于4个空格
set wrapscan "搜索在文件的两端绕回
set incsearch "在输入要搜索的文字时，vim会实时匹配 
"set backspace=indent,eol,start whichwrap+=<,>,[,] "允许退格键的def使用  
"  
if(has("win32") || has("win95") || has("win64") || has("win16")) "判定当前操作系统类型  
    let g:iswindows=1  
else  
    let g:iswindows=0  
endif  

if(g:iswindows==1) "允许鼠标的使用  
    "防止linux终端下无法拷贝  
    if has('mouse')  
        set mouse=a  
    endif  
    au GUIEnter * simalt ~x  
endif  


"进行Tlist的设置  
filetype on  
let Tlist_Show_Menu = 1  
"TlistUpdate可以更新tags  
map <F3> :silent! Tlist<CR>  "按下F3就可以呼出Taglist  
let Tlist_Ctags_Cmd='ctags' "因为我们放在环境变量里，所以可以直接执行  
let Tlist_Use_Right_Window=0 "让窗口显示在右边，0的话就是显示在左边  
let Tlist_Show_One_File=1 "让taglist可以同时展示多个文件的函数列表，如果想只有1个，设置为1  
let Tlist_File_Fold_Auto_Close=1 "非当前文件，函数列表折叠隐藏  
let Tlist_Exit_OnlyWindow=1 "当taglist是最后一个分割窗口时，自动退出vim  
let Tlist_Process_File_Always=0 "是否一直处理tags.1:处理;0:不处理  
let Tlist_Inc_Winwidth=0   

"colorscheme desert  
set diffexpr=MyDiff()  
function MyDiff()  
  let opt = '-a --binary '  
  if &diffopt =~ 'icase' | let opt = opt . '-i ' | endif  
  if &diffopt =~ 'iwhite' | let opt = opt . '-b ' | endif  
  let arg1 = v:fname_in  
  if arg1 =~ ' ' | let arg1 = '"' . arg1 . '"' | endif  
  let arg2 = v:fname_new  
  if arg2 =~ ' ' | let arg2 = '"' . arg2 . '"' | endif  
  let arg3 = v:fname_out  
  if arg3 =~ ' ' | let arg3 = '"' . arg3 . '"' | endif  
  let eq = ''  
  if $VIMRUNTIME =~ ' '  
    if &sh =~ '\<cmd'  
      let cmd = '""' . $VIMRUNTIME . '\diff"'  
      let eq = '"'  
    else  
      let cmd = substitute($VIMRUNTIME, ' ', '" ', '') . '\diff"'  
    endif  
  else  
    let cmd = $VIMRUNTIME . '\diff'  
  endif  
  silent execute '!' . cmd . ' ' . opt . arg1 . ' ' . arg2 . ' > ' . arg3 . eq  
endfunction  


set tags=tags;
set autochdir
