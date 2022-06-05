# HalloWorld-OS
--- 
## Console
### Commands

> ### cls  
>     
> **Funcs:**  
> - This command can be used to clear console 

> ### cwd 
>     
> **Funcs:**  
> - This command prints current working directory 

> ### cd *{ path }*  
> **Params:**  
> - **path** - you can specify full path or just one dir
>     
> **Funcs:**  
> - This command can be used to change directory  

> ### md *{ path }*  
> **Params:**  
> - **path** - you can specify full path or just one dir  
> 
> **Funcs:**  
> - This command can be used to crete directory

> ### mf *{ path /content }*  
> **Params:**  
> - **path** - you can specify full path or just one file
> - **content** - you can specify content of file (text)  
> 
> **Funcs:**  
> - This command can be used to crete any file

> ### ld *{ path }*  
> **Params:**  
> - **path** - you can specify full path or just one dir or nothing
> 
> **Funcs:**  
> - This command can be used to list out files/dirs

> ### contentof *{ path }*
> **Params:**  
> - **path** - you can specify full path or just one file 
> 
> **Funcs:**  
> - This command can be used to see what is inside file

> ### rd *{ path param1 }*
> **Params:**  
> - **path** - you can specify full path or just one file
> - **param1**
>   - *r* - remove dir with all its content 
>   - *none(default)* - remove only empty dir
> 
> **Funcs:**  
> - This command can be used to delete dir

> ### rf *{ path }*
> **Params:**  
> - **path** - you can specify full path or just one file
> 
> **Funcs:**  
> - This command can be used to delete file

> ### rn *{ path new_path}*
> **Params:**  
> - **path** - you can specify full path or just one file that you want to rename or move
> - **new_path** - you can specify full path or just one file that you want to be renamed to or moved to
> 
> **Funcs:**  
> - This command can be used to rename dir/file

> ### open *{ path }*
> **Params:**  
> - **path** - you can specify full path or just one file
> 
> **Funcs:**  
> - This command can be used to open file in gui text editor

> ### openapp *{ app }*
> **Params:**  
> - **app** - you can specify what app do you want to open
>   - texteditor - gui text editor
> 
> **Funcs:**  
> - This command can be used to open any app

> ### help
> 
> **Funcs:**  
> - This command can be used to see all commands

> ### exit
> 
> **Funcs:**  
> - This command can be used to exit program

## Apps
### TextEditor
> **Funcs:**
> - **File**
>   - *save* - save file content
>   - *save as* - save file content to any directory
>   - *new* - open new untitled file
> - **Edit**
>   - *undo* - undo changes
>   - *redo* - redo changes

### Time
> **Funcs:**
> - **Time**
>   - just show current time and date
> - **Stopwatch**
>   - every time you click on menu ti resets
> **Timer**
>   - you can set time for timer
>   - !!for now it make no sound!!
