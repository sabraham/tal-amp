# TAL-AMP
A terminal TAL player

Made at the [2015 This American Life Audio Hackathon] (http://audiohackathon.com/).

## Features

* `Episode` - Jump to your favorite episode
* `Random` - Who knows which episode you'll get next??
* `Gray Hair` - Because Death comes to all, even Ira Glass.

Initial episodes feature full black hair,
![Episode 1](/screenshots/1.png)
and as episodes become more recent,
![Episode 222](/screenshots/222.png)
Ira's hair grays appropriately.
![Episode 500](/screenshots/500.png)

## Install

There are 2 steps to install `tal-amp`.

1. `tal-amp` is a `curses`  wrapper around `mpg123`, so let's get that first
  * MAC OS X: `brew install mpg123`
  * Linux: `apt-get install mpg123`
2. Install `tal-amp`
  * `python setup.py install`

## Running

Now that you've installed `tal-amp`, all you need to do is enter

`tal-amp`

on your command line and it should start. To interact with the player, type one
of the following characters:

* `e` - Then enter which episode you want to tune into followed by `ENTER`.
* `p` - Play or Pause the current episode.
* `n` - Move on to the next episode; if `random` is `on`, then this will be a
surprise.
* `r` - Flip `random` episode selection on and off.
* `q` - Quit `tal-amp`

## Rationale

* Terminal Apps are FUN
* iTunes and Flash are TERRIBLE
* The ~new web~ often leaves many behind (e.g., the visually-impaired)

## License

This is free software under the MIT license; see the LICENSE file for full
details. Source code lives at [https://github.com/sabraham/tal-amp](https://github.com/sabraham/tal-amp).
