#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias pia='sh ~/pia/pia-linux-3.1-06756.run'
PS1='[\u@\h \W]\$ '

export PATH=$PATH:~/.emacs.d/bin
