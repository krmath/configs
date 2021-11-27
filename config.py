# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Shift focus between monitors
    Key([mod], "m", lazy.next_screen(),
        desc="Move focus to next screen"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod, "shift"], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),

    # Custom launcher keybinds
    Key([mod], "b", lazy.spawn("librewolf"), desc="Launch browser"),
    Key([mod], "e", lazy.spawn("emacsclient -c -a 'emacs' "), desc="Launch emacs"),
    Key([mod], "d", lazy.spawn("discord"), desc="Launch discord"),
    Key([mod], "f", lazy.spawn("pcmanfm"), desc="Launch files"),
    Key([mod], "r", lazy.spawn("dmenu_run"), desc="Launch dmenu"),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])

layouts = [
    # layout.Columns(border_focus='#8FBCBB', border_normal='#4C566A', border_focus_stack=['#d75f5f', '#8f3d3d'], border_width=5, insert_position=1),
    layout.Bsp(border_focus='#8FBCBB', border_normal='#4C566A', border_width=5, fair=False),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]


# Bar colors

def init_colors():
    return[["#2F343F", "#363F53"], # color 0
           ["#2F343F", "#2F343F"]], # color 1



widget_defaults = dict(
    font='meslo',
    fontsize=16,
    padding=3,
)
extension_defaults = widget_defaults.copy()

def sep():
    return widget.Sep(linewidth=0, padding=4, background="#2E3440")

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Memory(
                    background="#8FBCBB",
                    foreground="#2E3440"
                ),

                sep(),

                widget.CPU(
                    background="#5E81AC",
                    foreground="#2E3440",
                    format='CPU {load_percent}%'
                ),

                sep(),

                widget.Net(background="#88C0D0", foreground="#2E3440"),

                widget.Spacer(
                    length = bar.STRETCH,
                    background="2E3440"
                ),


                widget.GroupBox(
                    background="2E3440",
                    block_highlight_text_color="#A3BE8C",
                    active="#ECEFF4",
                    inactive="#4C566A",
                    this_current_screen_border="5E81AC",
                    highlight_method="block",
                    other_current_screen_border="#4C566A"
                ),

                widget.CurrentLayout(background="#2E3440", foreground="#ECEFF4"),

                widget.Prompt(background="8FBCBB", foreground="#2E3440"),
                #widget.WindowName(background="#2E3440", foreground="#ECEFF4"),

                widget.Spacer(
                    length = bar.STRETCH,
                    background="2E3440"
                ),

                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                # widget.TextBox("default config", name="default"),
                #widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                widget.Systray(background="#ECEFF4"),


                sep(),

                widget.Clock(background="#5E81AC", foreground="2E3440", format='%a %d-%m-%Y'),

                sep(),

                widget.Clock(background="#88C0D0", foreground="2E3440", format='%H:%M'),

                sep(),

                widget.Battery(background="#5E81AC", foreground="#2E3440", battery=0, format='{percent:2.0%} {char}'),

                widget.Battery(background="#5E81AC", foreground="#2E3440", battery=1, format='{percent:2.0%} {char}'),

                sep(),

                widget.PulseVolume(background="#88C0D0", foreground="2E3440", limit_max_volume='True'),

                sep(),
                # widget.QuickExit(),
            ],
            24,
        ),
    ),

    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayout(background="#2E3440", foreground="#ECEFF4"),

                widget.GroupBox(
                    background="2E3440",
                    block_highlight_text_color="#A3BE8C",
                    active="#ECEFF4",
                    inactive="#4C566A",
                    this_current_screen_border="5E81AC",
                    highlight_method="block",
                    other_current_screen_border="#4C566A"
                ),

                widget.Prompt(background="8FBCBB", foreground="#2E3440"),
                widget.WindowName(background="#2E3440", foreground="#ECEFF4"),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                # widget.TextBox("default config", name="default"),
                #widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                widget.Systray(background="#ECEFF4"),

                widget.Memory(
                    background="#8FBCBB",
                    foreground="#2E3440"
                ),

                sep(),

                widget.CPU(
                    background="#5E81AC",
                    foreground="#2E3440",
                    format='CPU {load_percent}%'
                ),

                sep(),

                widget.Net(background="#88C0D0", foreground="#2E3440"),

                sep(),

                widget.Clock(background="#5E81AC", foreground="2E3440", format='%a %d-%m-%Y'),

                sep(),

                widget.Clock(background="#88C0D0", foreground="2E3440", format='%H:%M'),

                sep(),

                widget.Battery(background="#5E81AC", foreground="#2E3440", format='{percent:2.0%}'),

                sep(),

                # widget.QuickExit(),
            ],
            24,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
