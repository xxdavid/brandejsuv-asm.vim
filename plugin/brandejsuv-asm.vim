let s:path = expand('<sfile>:p:h')
let s:lastTask = 0

function! s:loadTask(n)
    if winnr('$') == 2
        wincmd k
        :bdelete!
    endif

    execute 'new | 0read !' . s:path . '/../scripts/task.py ' . a:n . ' ' . g:is_muni_issession . ' ' .  g:is_muni_iscreds
    normal! gg
    wincmd j

    let s:lastTask = a:n
endfunction

command -nargs=1 BrandejsAsmUpload execute 'w | !' .  s:path . '/../scripts/upload.py ' . <args> . ' %:p ' . g:is_muni_issession . ' ' .  g:is_muni_iscreds
command BrandejsAsmUploadCurrent execute 'w | !' .  s:path . '/../scripts/upload.py ' . s:lastTask . ' %:p ' . g:is_muni_issession . ' ' .  g:is_muni_iscreds
command -nargs=1 BrandejsAsmTask call <SID>loadTask(<args>)
