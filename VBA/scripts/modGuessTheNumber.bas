Attribute VB_Name = "modGuessTheNumber"
Sub GuessTheNumber()
Attribute GuessTheNumber.VB_ProcData.VB_Invoke_Func = "g\n14"
    Dim targetNumber As Integer
    Dim userGuess As Integer
    Dim attemptCount As Integer
    Dim targetCell As Range
    
    Dim table As ListObject
    Dim newTableRow As ListRow
    
    Dim attemptCol As ListColumn
    Dim guessCol As ListColumn
    Dim resultCol As ListColumn
    
    ' Specify the table where the guesses will be stored
    Set table = ThisWorkbook.Worksheets("Guess the Number!").ListObjects("Num")
    
    Set targetCell = ThisWorkbook.Worksheets("Answer").Range("B1")
    
    ' Get the reference to the columns by their names
    Set attemptCol = table.ListColumns("Attempt")
    Set guessCol = table.ListColumns("Users Guess")
    Set resultCol = table.ListColumns("Result")
    
    ' Generate a random number between 1 and 100
    
    Randomize
    targetNumber = Int((100 * Rnd) + 1)
    
    targetCell.Value = targetNumber
    
    attemptCount = 0
    
    Do
        ' Prompt the user to enter a guess
        userGuess = InputBox("Guess the number (1-100):")
        
        ' Add a new row to the table for the current guess
            Set newTableRow = table.ListRows.Add
            attemptCount = attemptCount + 1
            
            newTableRow.Range(attemptCol.Index) = attemptCount
            newTableRow.Range(guessCol.Index) = userGuess
        
        ' Validate the user's guess
        If IsNumeric(userGuess) Then
            
            ' Compare the user's guess with the target number
            If userGuess < targetNumber Then
                MsgBox "Too low! Try again."
                newTableRow.Range(resultCol.Index) = "Too low"
                
            ElseIf userGuess > targetNumber Then
                MsgBox "Too high! Try again."
                newTableRow.Range(resultCol.Index) = "Too high"
                
            Else
                MsgBox "Congratulations! You guessed the number in " & attemptCount & " attemptCount."
                newTableRow.Range(resultCol.Index) = "Correct!"
                
            End If
            
        Else
            MsgBox "Invalid input. Please enter a numeric value."
            newTableRow.Range(resultCol.Index) = "Invalid"
            
        End If
        
    Loop Until userGuess = targetNumber
    
End Sub

Sub ResetTable()
    Dim table As ListObject
    Dim tableRange As Range
    Dim ws As Worksheet
    
    ' Specify the sheet name where the table is located
    Set ws = ThisWorkbook.Worksheets("Guess the Number!")
    
    ' Specify the table name
    Set table = ws.ListObjects("Num")
    
    ' Clear the table data and formatting
    Set tableRange = table.DataBodyRange
    
    If table.ListRows.Count > 0 Then
    tableRange.Rows.Delete
    tableRange.Interior.Color = xlNone
    
    Else
    MsgBox "Table already cleared!"
    End If
    
End Sub



