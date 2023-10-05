**TODO for your task:** Edit the Text in italics with your text.

<hr>

# Use Case 2

<hr>

**Use Case**: Color Selection via Number Keys

**Primary Actor**: User

**Goal in Context**: To change the drawing color by pressing one of the number keys from 1 through 8.

**Preconditions**: 
The application is open and active.
The canvas is accessible.

**Trigger**: User presses a number key between 1 and 8.
  
**Scenario**: 
User decides to change the drawing color.
User presses one of the number keys (1-8).
System recognizes the key press event.
System changes the drawing color based on the pressed number:
1 = Black
2 = White
3 = Red
4 = Green
5 = Blue
6 = Yellow
7 = Magenta
8 = Cyan
User starts drawing, and the drawing color corresponds to the selected color.
 
**Exceptions**: 
If a number key outside of the 1-8 range is pressed, no change in color occurs.
If the application fails to recognize the key press, a tooltip or notification may inform the user of the valid number keys to use.

**Priority**: Medium

**When available**: Version 1.2 

**Channel to actor**: Through the keyboard input and the graphical user interface (GUI) of the application.

**Secondary Actor**:  None

**Channels to Secondary Actors**:  None

**Open Issues**: 
Should there be a visual indication showing the active or selected color?

<hr>



(adapted by Pressman and Maxim, Software Engineering: A Practitioner’s Approach, pp. 151-152, from Cockburn,
A., Writing Effective Use-Cases, Addison-Wesley, 2001)
