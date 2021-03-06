# Custom Latex Math Unicode Input using m17n

In the ibus-m17n package is an input method file that translates "latex"-math
commands to unicode symbols. Sadly it doesn't strictly follow the rules of latex and
I wanna fix that. 

Luckily for me somebody already wrote a quite complete Latex-Math to Unicode map (in
python). The project behind it is called unicodeit and I'll just take that file and
create a script in it that creates a valid m17n input file.

## How to get the latex unicode map

The file `math_map` can be found here:
https://github.com/svenkreiss/unicodeit/blob/master/unicodeit/data.py

Thank you unicodeit for your contribution.

## Setup

1. Make sure that you're using the ibus input system. The easiest way is to check `ps aux | grep ibus` for any processes running.
    - an alternative in Gnome is "Settings →  Region & Language →  Gear next to "Input Sources"
2. Install the m17n ibus package, it currently is in the aptitude under `ibus-m17n` ([launchpad](https://launchpad.net/ubuntu/+source/ibus-m17n))
3. adapt and execute the `keyboard-generator` script
    - as of right now only the `REPLACEMENT` variable was mapped
4. move the generated file into the `/usr/share/m17n/` or `~/.m17n.d/` directory
5. restart ibus (`ibus restart`)
6. insert the new input method under Gnome's "Input Sources"
    - you probably need to select "Others" at the bottom of the list


## How to use?

After the keyboard input appears in your language list you can simply select it and start typing out your commands. For easier use I've removed the leading `\` from all commands. The ibus input also has the limitation that you cannot remove a character when you hit the wrong key. You would need to start from the beginning then.

Example
- `n in mathbb{N} Rightarrow n in mathbb{Q}`: n ∈ ℕ ⇒ n ∈ ℚ
- `n nsubseteq emptyset`: n ⊈ ∅


## Issues 

Entering `{` on a German keyboard doesn't work as `{` requires <kbd>AltGr</kbd>, which interrupts the current input.
