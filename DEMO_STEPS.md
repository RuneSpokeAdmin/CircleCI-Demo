# Live Demo , exact steps

## Before the call (setup, done in advance)
- Repo pushed to GitHub, connected to CircleCI, at least one GREEN build showing.
- Terminal open in the repo. CircleCI pipeline page open in a browser tab.

## The break (do this live)
Open app/__init__.py and change this line:

    widgets = ["sprocket", "gadget", "cog"]

to:

    widgets = ["sprocket", "gadget", "cog", "bolt"]

Then:

    git commit -am "Add bolt widget"
    git push

Switch to the CircleCI tab. The build runs and goes RED on test_widget_count
(assert 4 == 3). Narrate: "A normal-looking change. Tests caught it. This never
reaches production."

## The fix (do this live)
Change the line back to three widgets:

    widgets = ["sprocket", "gadget", "cog"]

Then:

    git commit -am "Revert: keep count in sync with tests"
    git push

Build goes GREEN. Narrate: "Fixed, validated, and now it ships. That's the
guardrail , every change, automatically, every time."
