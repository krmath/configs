#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

# set prompt
export PS1="\[\e[34m\]\W\[\e[m\]\[\e[32m\]>\[\e[m\] "

alias ls='ls --color=auto'
alias pia='sh ~/pia/pia-linux-3.1-06756.run'
alias goodbye='shutdown 0'
alias lmon=~/.scripts/leftmonitor.sh
alias rmon=~/.scripts/rightmonitor.sh
alias onemon=~/.scripts/onemonitor.sh
alias volume='alsamixer'

export PATH=$PATH:~/.emacs.d/bin
