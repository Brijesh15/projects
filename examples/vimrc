set nocompatible              " required
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')
"
" let Vundle manage Vundle, required
Plugin 'gmarik/Vundle.vim'

" add all your plugins here (note older versions of Vundle
" used Bundle instead of Plugin)

" ...

" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required

set splitbelow
set splitright

"split navigations
nnoremap <C-J> <C-W><C-J>
nnoremap <C-K> <C-W><C-K>
nnoremap <C-L> <C-W><C-L>
nnoremap <C-H> <C-W><C-H>

" Enable folding
set foldmethod=indent
set foldlevel=99

" Enable folding with the spacebar
nnoremap <space> za

Plugin 'tmhedberg/SimpylFold'

let g:SimpylFold_docstring_preview=1

"au BufNewFile *.py
au BufNewFile, BufRead *.py
    \ set textwidth=79 |
    \ set tabstop=4 |
    \ set softtabstop=4 |
    \ set shiftwidth=4 |
    \ set expandtab |
    \ set autoindent |
    \ set fileformat=unix

au BufNewFile,BufRead *.lua, *.html, *.css, *.xml
    set tabstop=2 softtabstop=2 shiftwidth=2
		
Plugin 'vim-scripts/indentpython.vim'

au BufRead, BufNewFile *.py,*.pyw,*.c,*.h match BadWhitespace /\s\+$/

set encoding=utf-8

Bundle 'Valloric/YouCompleteMe'
let g:ycm_autoclose_preview_window_after_completion=1
map <leader>g  :YcmCompleter GoToDefinitionElseDeclaration<CR>
"python with virtualenv support
"py << EOF
"import os
"import sys
"if 'VIRTUAL_ENV' in os.environ:
"  project_base_dir = os.environ['VIRTUAL_ENV']
"  activate_this = os.path.join(project_base_dir, 'bin/activate_this.py')
"  execfile(activate_this, dict(__file__=activate_this))
"EOF

Plugin 'vim-syntastic/syntastic'
Plugin 'nvie/vim-flake8'
let g:flake8_max_line_length=120
let python_highlight_all=1
syntax on
let g:pymode_options_max_line_length=120
autocmd FileType python set colorcolumn=120
" Support virtualenv
let g:pymode_virtualenv = 1
set number
set tags=tags

Bundle 'scrooloose/nerdtree'
map <F2> :NERDTreeToggle<CR>
map <S-Right> :tabn<CR>
map <S-Left>  :tabp<CR>
"map  <C-l> :tabn<CR>
"map  <C-h> :tabp<CR>
"map  <C-n> :tabnew<CR>
