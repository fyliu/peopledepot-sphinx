# Notes for working on models

## Working without proper use cases

### Defensive coding practices

AKA: a passive-aggressive way to tease out the requirements.

#### Model definitions

- Set fields to required until the client tells you how they're using it that needs the fields to be optional. Django already does this by default. You'd have to set `blank=True` to make a text field optional.
  - This is good design to make sure all declared fields are being used. If all fields were declared optional by default, a lot of them could be sitting there unused and the developer won't know to remove them.
