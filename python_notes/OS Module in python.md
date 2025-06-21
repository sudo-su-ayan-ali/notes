

##  1. File And Dicrectory Management

| Function               | Description                                      |
| ---------------------- | ------------------------------------------------ |
| `os.getcwd()`          | Get the current working directory                |
| `os.chdir(path)`       | Change the current working directory             |
| `os.listdir(path='.')` | List files and directories in the specified path |
| `os.mkdir(path)`       | Create a new directory                           |
| `os.makedirs(path)`    | Create intermediate-level directories            |
| `os.rmdir(path)`       | Remove a directory (only if empty)               |
| `os.removedirs(path)`  | Remove directories recursively                   |
| `os.rename(src, dst)`  | Rename a file or directory                       |
| `os.replace(src, dst)` | Replace the destination file if it exists        |
| `os.stat(path)`        | Get the status of a file or directory            |
| `os.scandir(path)`     | Return an iterator of `os.DirEntry` objects      |
## 2. File Operations
| Function               | Description               |
| ---------------------- | ------------------------- |
| `os.remove(path)`      | Remove (delete) a file    |
| `os.unlink(path)`      | Same as `remove()`        |
| `os.path.exists(path)` | Check if a path exists    |
| `os.path.isfile(path)` | Check if it's a file      |
| `os.path.isdir(path)`  | Check if it's a directory |
## 3. Path Manipulation (via ```os.path``` )
|Function|Description|
|---|---|
|`os.path.join(path, *paths)`|Join multiple paths|
|`os.path.basename(path)`|Get the last component of the path|
|`os.path.dirname(path)`|Get the directory name|
|`os.path.abspath(path)`|Get the absolute path|
|`os.path.split(path)`|Split into (head, tail)|
|`os.path.splitext(path)`|Split into (filename, extension)|
## 4. Enivronment Variables
|Function|Description|
|---|---|
|`os.environ`|Access environment variables|
|`os.environ.get('VAR')`|Get a specific environment variable|
|`os.putenv(key, value)`|Set an environment variable _(not recommended; use `os.environ`)_|
|`os.getenv(key, default=None)`|Get an environment variable with default fallback|
## 5. Process Management
| Function               | Description                                             |
| ---------------------- | ------------------------------------------------------- |
| `os.system(command)`   | Run a shell command                                     |
| `os.startfile(path)`   | Open a file with its default application (Windows only) |
| `os.execv(path, args)` | Replace the current process with a new one              |
| `os.getpid()`          | Get the current process ID                              |
| `os.getppid()`         | Get the parent process ID                               |
## 6. Permissions and Modes
|Function|Description|
|---|---|
|`os.chmod(path, mode)`|Change the mode (permissions) of a file|
|`os.chown(path, uid, gid)`|Change owner and group (Unix only)|
|`os.umask(mask)`|Set the default permission mask|
## 7. Cross Platform Constants
|Constant|Description|
|---|---|
|`os.name`|OS name (e.g., `'posix'`, `'nt'`)|
|`os.sep`|Path separator (`'/'` or `'\\'`)|
|`os.linesep`|Line separator (`'\n'` or `'\r\n'`)|
|`os.pathsep`|Separator for PATH-like variables|
