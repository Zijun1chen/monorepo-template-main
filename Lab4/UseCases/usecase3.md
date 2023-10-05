**TODO for your task:** Edit the Text in italics with your text.

<hr>

# Use Case 3

<hr>

**Use Case**:  Canvas Clearing with Space Key

**Primary Actor**: User

**Goal in Context**: To clear the drawing canvas, filling it entirely with the last selected color.

**Preconditions**: 
The application is open and active.
The canvas area is accessible.
A color has been previously selected.

**Trigger**: User presses the space key.
  
**Scenario**: 
User has completed some drawing on the canvas.
User decides to clear the canvas.
User presses the space key.
System recognizes the key press event.
System clears all the pixels on the canvas.
System fills the entire canvas with the last selected color.
 
**Exceptions**: 
If the application fails to recognize the space key press, a  notification may guide the user to try again.
If no color has been previously selected, the canvas might default to a pre-defined color.

**Priority**: Medium

**When available**: Version 1.3

**Channel to actor**:  Through the keyboard input and the graphical user interface (GUI) of the application.

**Secondary Actor**: None

**Channels to Secondary Actors**: None

**Open Issues**: 
Should there be a confirmation prompt before clearing the canvas?
Is there a need for an undo feature after the canvas is cleared?

<hr>



(adapted by Pressman and Maxim, Software Engineering: A Practitioner’s Approach, pp. 151-152, from Cockburn,
A., Writing Effective Use-Cases, Addison-Wesley, 2001)
