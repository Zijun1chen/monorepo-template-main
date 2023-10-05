**TODO for your task:** Edit the Text in italics with your text.

<hr>

# Use Case 4

<hr>

**Use Case**:  Mouse Drawing on Canvas

**Primary Actor**: User

**Goal in Context**: To draw on the canvas in a manner similar to using a pencil on paper by pressing and dragging the mouse.

**Preconditions**: 
The application is open and active.
The canvas is accessible and responsive.
A color has been selected for drawing.

**Trigger**: User presses the left mouse button while moving the mouse over the canvas.
  
**Scenario**: 
User positions the mouse cursor over the canvas area where they want to begin drawing.
User presses the left mouse button and starts dragging the mouse.
System continuously changes the color of pixels under the mouse cursor to the currently selected color as the user drags the mouse.
The user releases the mouse button to stop drawing.
 
**Exceptions**: 
If the system fails to detect mouse movements or presses, it might not draw on the canvas.
If the application becomes unresponsive, the user might need to restart or wait.

**Priority**: High
**When available**: Version 1.0

**Channel to actor**: Through the mouse input and the graphical user interface (GUI) of the application.

**Secondary Actor**: None

**Channels to Secondary Actors**: None

**Open Issues**: 
How does the system handle different shapes?
Should there be an option to change the drawing's opacity?

<hr>



(adapted by Pressman and Maxim, Software Engineering: A Practitioner’s Approach, pp. 151-152, from Cockburn,
A., Writing Effective Use-Cases, Addison-Wesley, 2001)
