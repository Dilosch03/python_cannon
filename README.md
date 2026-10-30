# Python Cannon

A modified version of the **Cannon** game from
[Free Python Games](https://grantjenks.com/docs/freegames/).
Click to fire a cannonball and pop the balloons before they cross the screen.

## How to run
```bash
pip install -r requirements.txt
python cannon.py
```

## Changes from the original

| Feature | Original | This version |
|---|---|---|
| Shot strength | Fixed offset of `200` hard-coded in `tap()` | Pulled out into a global constant `ball_speed_base = 250`, so shots are faster and easier to tune |
| Balloon speed | Every balloon moves at `0.5` px per frame | Each balloon gets a random speed when it spawns |
| Balloon color | Always blue | Color shows speed: yellow (slowest) → green → blue → purple (fastest) |
| Game over | The game stops as soon as one balloon leaves the screen | The game never ends: a balloon that leaves the screen comes back on the right side at a random height |

### Technical details
- Targets are now stored as `(position, speed)` tuples instead of plain vectors,
  so each balloon keeps its own speed.
- `balloon_colors` maps each speed level to a color.
- The `return` that ended the game loop in `move()` now moves the balloon back to the
  right side of the screen instead.

## Contributors
- [Dilosch03](https://github.com/Dilosch03): shot speed constant, random balloon speeds and colors
- [Josemaría Contreras](https://github.com/jcontreras13): endless mode (balloons come back on screen)

## Credits
Base game: *Cannon* from Free Python Games by Grant Jenks.
