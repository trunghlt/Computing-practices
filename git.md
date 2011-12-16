Git practices:
==============

## Use vimdiff for git diff
    git config --global diff.tool vimdiff
    git config --global difftool.prompt false
    git config --global alias.d difftool
    
  Typing "git d" yields the expected behavior, type :wq or :qa in vim cycles to the next file in the changeset.    