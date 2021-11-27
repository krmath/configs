#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

# Powerline
#powerline-daemon -q
#POWERLINE_BASH_CONTINUATION=1
#POWERLINE_BASH_SELECT=1
#. /usr/share/powerline/bindings/bash/powerline.sh

# set prompt
export PS1="\[\e[34m\]\W\[\e[m\]\[\e[32m\] ❭\[\e[m\] "

alias ls='ls --color=auto'
alias pia='sh ~/pia/pia-linux-3.1.2-06767.run'
alias goodbye='shutdown 0'
alias lmon=~/.scripts/leftmonitor.sh
alias rmon=~/.scripts/rightmonitor.sh
alias onemon=~/.scripts/onemonitor.sh
alias volume='alsamixer'

# interactive safety nets
alias rm='rm -i'
alias mv='mv -i'
alias cp='cp -i'

# make it easier to sync and update doom emacs
export PATH=$PATH:~/.emacs.d/bin

