# Ook- (Ook Minus)

***It's [ook](https://esolangs.org/wiki/Ook!), but without the ook!***

So instead of `Ook. Ook?`, you would use `.?`  
Still confused? Great!

**NOTE: Some code is still untested as of this moment**

## Valid Operations
Ook- | Ook | Description
--- | --- | ---
.? | Ook. Ook? | Increment Pointer
?. | Ook? Ook. | Decrement Pointer
.. | Ook. Ook. | Increment value at pointer
!! | Ook! Ook! | Decrement value at pointer
!. | Ook! Ook. | Write value indicated by pointer to output
.! | Ook. Ook! | Read from standard input to store to value indicated by the pointer
!? | Ook! Ook? | Begin a loop
?! | Ook? Ook! | Jump to start of the loop if the pointed-to memory value is zero

***ALL OPERATIONS MUST BE SEPERATED BY A SPACE***

## Usage
`python.exe .\ookMinus.py .\my-ook-file.ook-`
